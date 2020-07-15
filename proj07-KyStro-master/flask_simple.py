from flask import Flask, request, render_template, url_for, redirect, make_response
import MySQLdb
import passwords
import cgi  
import cgitb
import random
import string
cgitb.enable()

app = Flask(__name__)



@app.route("/<username>/profolio/<name>", methods=['POST'])
def add_stock(username, name):
    conn = make_conn()
    cursor = conn.cursor()
    ticker = request.form['stock']
    cursor.execute('insert into pro_stock (id, ticker) values ({}, "{}");'.format(
        get_prof_id(name,username),ticker))
    records = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return redirect(url_for('profolio_name', username=username, name=name))

def get_prof_id(name, username):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('select id from profolios where name="{}" and\
            username="{}";'.format(name,username))
    records = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    return records[0]

@app.route("/<username>/profolio/<name>")
def profolio_name(username, name):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('select ticker, price from stocks;')
    records = cursor.fetchall()
    cursor.close()
    cursor = conn.cursor()
    cursor.execute('select stocks.ticker, stocks.price from stocks\
            inner join pro_stock on stocks.ticker = pro_stock.ticker\
            inner join profolios on profolios.id = pro_stock.id where\
            profolios.id = {};'.format(get_prof_id(name,username)))
    own = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('stocks.html', username=username, name=name,
            records=records, own=own)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_username():
    username = request.form['username']
    cookie = create_cookie()
    if not user_exists(username):
        insert_user(username, cookie)
        add_dummy_stocks()
        redir = redirect(url_for('login', username=username))
        redir.set_cookie("cookie_name", cookie)
        return redir
    else:

        redir = redirect(url_for('login', username=username))
        redir.set_cookie("cookie_name", cookie)
        return redir

@app.route('/login/<username>')
def login(username):
    cookie = request.cookies.get('cookie_name')
    there = has_profolios(username)
    redir = render_template('login.html', username=username, there=there)
    #redir.set_cookie('cookie_name',cookie)
    return redir

def user_exists(user):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('select count(*) from sessions where username="{}";'.format(user))
    records = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    if records[0] == 0:
        return False
    else:
        return True

def is_session(cookie):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM sessions WHERE NOW() < expires and\
           id="{}";')
    records = cursor.fetchall()[0]
    cursor.close()
    conn.commit()
    conn.close()
    if records == 0:
        return False
    else:
        return True


@app.route("/login/<username>", methods=['POST'])
def get_profolio(username):
    cookie = request.cookies.get('cookie_name')
    profolio = request.form['profolio']
    insert_profolio(profolio, username)
    there = has_profolios(username)
    redir = redirect(url_for('login', username=username, there=there))
    redir.set_cookie('cookie_name',cookie)
    return redir

def get_stock():
    letters = string.ascii_uppercase
    ticker = ''.join(random.choice(letters) for i in range(4))
    return ticker

def get_price():
    d = random.random()
    return round(d * 100,4)


def add_dummy_stocks():
    conn = make_conn()
    for i in range(20):
        stock = get_stock()
        price = get_price()
        cursor = conn.cursor()
        cursor.execute('insert into stocks (ticker, price) values ("{}",{});'.format(stock,price))
        cursor.close()
    conn.commit()
    conn.close()

def has_profolios(username):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('select name from profolios where username="{}";'.format(username))
    records = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return records

def insert_profolio(name, username):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('insert into profolios (name, username) values ("'+name+'", "'+username+'");')
    cursor.close()
    conn.commit()
    conn.close()

def insert_stock(ticker, price):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('insert into stocks (ticker, price) values ("'+ticker+'", '+str(price)+');')
    cursor.close() 
    conn.commit()
    conn.close()

def insert_user(username, cookie):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute('''insert into sessions (id, username, expires) values
    ("'''+cookie+'''", "'''+username+'''", ADDTIME(NOW(), 100) );''')
    cursor.close()
    conn.commit()
    conn.close()

def create_cookie():
    ID_as_int = random.randint(0, 16**64) # 4 bits per hex, times 64 hex chars
    ID_as_str = "%064x" % ID_as_int
    return ID_as_str

def make_conn():
    conn = MySQLdb.connect(host = passwords.SQL_HOST,
    user = passwords.SQL_USER,
    passwd = passwords.SQL_PASSWD,
    db = "cookies")
    return conn
