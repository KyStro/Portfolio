'''
File: dates.py
Author: Kyle Strokes
Purpose: This program reads in a file of dates and events with I or R in
    front, I enters date and event into a dictionary and R prints out events
    for that date.
Course: CS 120, Section 1F, Spring 2018.
'''

'''To stop program w/ errors found'''
import sys

def main():
    file = input()
    '''If error found with input file the except prints its message'''
    try:
        file = open(file)
    except FileNotFoundError:
        print('ERROR: Could not open file ' + file)
        sys.exit(1)
    date_dict = {}
    for line in file:
        '''Checks to see if we add to event to given date'''
        if line.startswith('I'):
            date, event = parse(line)
            new_date = Date(date, event)
            new_date.add_event()
            '''Needed to init these values before passings'''
            key, value = '', ''
            new_date_set = DateSet(new_date, date_dict, key, value)
            new_date_set.add_date()
            '''Checks to see if we want to read the events for a date'''
        elif line.startswith('R'):
            date, event = parse(line)
            new_date = Date(date, event)
            for key in date_dict.keys():
                if key == date:
                    events = date_dict[key]
                    for event in sorted(events):
                        event_in_list = event
                        for event in event_in_list:
                            value = event[:-1]
                            new_date_set = DateSet(new_date, date_dict, key, value)
                            print(new_date_set)
        else:
            '''Asserts that line begins w/ I or R if not assertion error
                follows with the exception print statment'''
            try:
                assert(line[0] == 'I' or line[0] == 'R')
            except AssertionError:
                print('ERROR: Illegal operation on line "' + str(line.strip()) + '"')
                sys.exit(1)

def parse(line):
    '''This function puts the line no matter what format into date = yyyy-mm-dd
        and event is a string of the event with said date

    Parameters: a raw line from input file

    Returns: the cannonical date yyyy-mm-dd and a string of the event that
            happened on the date

    Pre-conditons: Line must begin with I or R, of course file has to be
                    found and readable

    Post-conditons: Date is in cannonical order with ':' removed and the
        event is a string for date'''
    raw_line = line
    line = raw_line[1:].strip().split()
    '''Each if statment takes each possible format of the date and put it into
        a day, month, and year'''
    if ':' in line:
        line.remove(':')           
    date = line[0].split()
    if '/' in date[0]:
        date = date[0].split('/')
        month, day, year = date[0].strip(':'), date[1].strip(':'), date[2].strip(':')
        event_list = line[1:]
    if '-' in date[0]:
        date = date[0].split('-')
        year, month, day = date[0].strip(':'), date[1].strip(':'), date[2].strip(':')
        event_list = line[1:]
    m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if date[0] in m:
        date = line[:3]
        day, year = date[1].strip(':'), date[2].strip(':')
        month = str(m.index(date[0]) + 1).strip(':')
        event_list = line[3:]
        '''Finally all the pieces of the date come together here'''
    date = "{:d}-{:d}-{:d}".format( int(year), int(month), int(day))
    '''If date has more than 31 days, or date has more than 12 months assertion
            error and exception print statment follows'''
    try:
        assert(int(day) < 31 and int(month) < 12)
    except AssertionError:
        print('ERROR: Illegal date on line "'  + str(raw_line.strip()) + '"')
        sys.exit(1)
    event = ''
    for word in event_list:
        '''This makes all words in the event_list into a single string'''
        event += word + ' '    
    return date, event

class Date:
    '''This a Date class and it makes each canoncial date its own
        object you can get the event with this date, the events and
        the date itself also adds events to event list

        Parameters: date which is the canonical date and the string
            event

        Returns: the date, the events list on that date

        Pre-conditions: date is the cancical date in string form and event
            is a string of event of that date

        Post - conditions: event list is a list of all events that happened
                on date'''
    def __init__(self, date, event):
        self._date = date
        self._event = event
        self._event_list = []

    def add_event(self):
        self._event_list.append(self._event)

    def get_event_list(self):
        return self._event_list
       
    def __str__(self):
        return self._date    

class DateSet:
    '''This is the DateSet class it adds the dates to a dictionary and prints
        out the output in str

    Parameters: new_date is a Date object, date_dict is the dictionary with
        cancial dates, key empty at first but used to get the key which is the
        date in the dictionary and the value is the list of events.

    Returns: the value of the date key which is a list of events and
        the formatted out put of the date: event. in str'''
    def __init__(self, new_date, date_dict, key, value):
        self._date_dict = date_dict
        self._date_name = new_date.__str__()
        self._events = new_date.get_event_list()
        self._key = key
        self._value = value

    def add_date(self):
        if self._date_name not in self._date_dict:
            self._date_dict[self._date_name] = [self._events]
        else:
            self._date_dict[self._date_name].append(self._events)
        return self._date_dict[self._date_name]

    def __str__(self):
        return "{}: {}".format(self._key, self._value)


main()
