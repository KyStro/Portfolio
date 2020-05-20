"""
Kyle Strokes
SL: Sean Current
2/3/2020
ISTA 331 HW1

@@@ADD SUMMARY@@@@@@@@@@


Some code that you can mess with as you implement your functions to see
what is going on.  Once your code works, you can switch to main1 and
get a better view of your work in action.
"""

import pandas as pd, numpy as np, random, sqlite3

def isbn_to_title(conn):
    c = conn.cursor()
    query = 'SELECT isbn, book_title FROM Books;'
    return {row['isbn']: row['book_title'] for row in c.execute(query).fetchall()}

def select_book(itt):
    isbns = sorted(itt)
    print('All books:')
    print('----------')
    for i, isbn in enumerate(isbns):
        print(' ', i, '-->', isbn, itt[isbn][:60])
    print('-' * 40)
    selection = input('Enter book number or return to quit: ')
    return isbns[int(selection)] if selection else None
    
def similar_books(key, cm, pm, itt, spm): # an isbn, count_matrix, p_matrix, isbn_to_title
    bk_lst = []
    for isbn in cm.columns:
        if key != isbn:
            bk_lst.append((cm.loc[key, isbn], isbn))
    bk_lst.sort(reverse=True)
    print('Books similar to', itt[key] + ':')
    print('-----------------' + '-' * (len(itt[key]) + 1))
    for i in range(5):
        print(str(i) + ':')
        print(' ', bk_lst[i][0], '--', itt[bk_lst[i][1]][:80])
        print('  spm:', itt[spm[key][i]][:80])
        print('  p_matrix:', pm.loc[key, bk_lst[i][1]])
        
  
    
  
    
    
def get_purchase_matrix(conn):
    cur = conn.cursor()
    q = 'select * from orderitems natural join orders;'
    dic = {}
    for row in cur.execute(q).fetchall():
        #if customer isnt in dic add them if they are then
        #add the book in the row
        if row[-1] not in dic:
            dic[row[-1]] = []
            dic[row[-1]].append(row[1])
        elif row[1] not in dic[row[-1]]:
            dic[row[-1]].append(row[1])
            dic[row[-1]].sort()
    return dic
        



    
def main1():
    conn = sqlite3.connect('small.db')
    conn.row_factory = sqlite3.Row
    purchase_matrix = get_purchase_matrix(conn)
    count_matrix = get_empty_count_matrix(conn)
    fill_count_matrix(count_matrix, purchase_matrix)
    p_matrix = make_probability_matrix(count_matrix)
    spm = sparse_p_matrix(p_matrix)
    ######
    itt = isbn_to_title(conn)
    selection = select_book(itt)
    while selection:
        similar_books(selection, count_matrix, p_matrix, itt, spm)
        input('Enter to continue:')
        selection = select_book(itt)
    ######
    cid = get_cust_id(conn)
    while cid:
        print()
        titles = purchase_history(cid, purchase_matrix[cid], conn)
        print(titles)
        print(get_recommendation(cid, spm, purchase_matrix[cid], conn))
        input('Enter to continue:')
        cid = get_cust_id(conn)
    
def main2():
    conn = sqlite3.connect('bookstore.db')
    conn.row_factory = sqlite3.Row
    
    purchase_matrix = get_purchase_matrix(conn)
    print('*' * 20, 'Purchase Matrix', '*' * 20)
    print(purchase_matrix)
    print()
    
    count_matrix = get_empty_count_matrix(conn)
    print('*' * 20, 'Empty Count Matrix', '*' * 20)
    print(count_matrix)
    print()
    
    fill_count_matrix(count_matrix, purchase_matrix)
    print('*' * 20, 'Full Count Matrix', '*' * 20)
    print(count_matrix)
    print()
    
    p_matrix = make_probability_matrix(count_matrix)
    print('*' * 20, 'Probability Matrix', '*' * 20)
    print(p_matrix)
    print()
    
    spm = sparse_p_matrix(p_matrix)
    print('*' * 20, 'Sparse Probability Matrix', '*' * 20)
    print(spm)
    print()
    
    ######
    itt = isbn_to_title(conn)
    print('*' * 20, 'itt dict', '*' * 20)
    print(itt)
    print()
    
    """
    selection = select_book(itt)
    while selection:
        similar_books(selection, count_matrix, p_matrix, itt, spm)
        input('Enter to continue:')
        selection = select_book(itt)
    ######
    cid = get_cust_id(conn)
    while cid:
        print()
        titles = purchase_history(cid, purchase_matrix[cid], conn)
        print(titles)
        print(get_recommendation(cid, spm, purchase_matrix[cid], conn))
        input('Enter to continue:')
        cid = get_cust_id(conn)
    """
if __name__ == "__main__":
    main1()
    
    
    
    
    
    
    
    
