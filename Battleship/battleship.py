'''
File: battleship.py
Author: Kyle Strokes
Purpose: Simulates the board game Battleship, user enters coordinates of
            ship positions and user enters coordinates of the guesses
Course: CS 120, Section 1F, Spring 2018.

--------------

Inputs:

'game board' file: This file is a text file representing the placements of
your ships. An example of the file:

A 0 7 4 7
P 4 2 5 2
D 7 5 7 3
B 2 2 2 5
S 9 9 9 7

Each line is formatted as:
<ship letter> <starting x coordinate> <starting y coordinate> <ending x coordinate> <ending y coordinate>

ship letter:
    A: Aircraft carrier takes up 5 spaces
    P: Patrol boat takes 2 spaces
    D: Destroyer takes 3 spaces
    B: Battleship takes 4 spaces
    S: Submarine takes 3 spaces

starting coordinates:
    x: the first number after the ship letter is the starting x coordinate
        this number needs to be between 0 and 10 exclusive
    y: second number after starting x coordinate, same rules apply

    These two numbers combine to make a starting coordinate for example:

    A 0 7 4 7

    The starting coordinate for Aircraft A would be (0,7)

ending coordinates:
    x: the third number in a line is the ending x coordinate, same rules apply
    y: last number is the ending y coordinate, same rules apply

    A 0 7 4 7

    The ending coordinates for Aircraft A would be (4,7)

The coordinates must align in such a way that the distance between the two
coordinates corresponds to the length (number of spaces) of the ship they represent

Coordinates can only differ in x coordinate or y coordinate, but NOT both (diagonal)


'''

import sys

def main():
    pfile = input("Enter your 'game board' file's name: ")
    file_error(pfile)
    gfile = input("Enter your 'guessing' file's name: ")
    file_error(gfile)
    pfile = open(pfile)
    gfile = open(gfile)
    input_check = []
    ship_pts = []
    '''for ship objects'''
    ship_list = []
    '''grid of GridPos objects'''
    grid = []
    grid = make_grid(grid)
    '''board object'''
    board = Board(grid, ship_list)
    for line in pfile:
        ship_data, coords = parse_pfile(line, input_check, ship_pts)
        '''Ship object'''
        new_ship = Ship(ship_data, coords)
        ship_list.append(new_ship)
    '''Checks that there are 5 ships in fleet'''
    try:
        for letter in input_check:
            assert(len(input_check) == 5 and input_check.count(letter)\
                   == 1)
    except AssertionError:
        print("ERROR: fleet composition incorrect")
        sys.exit(1)
    '''Tells GridPos that theres an ship in it'''    
    board.ship_in_grid()
    for line in gfile:
        guess_pt = parse_gfile(line)
        '''prints illegal points'''
        if type(guess_pt) != tuple and guess_pt != None:
            print(guess_pt)
        elif guess_pt == None:
            pass
        else:
            '''GridPos object of guessed point'''
            guess_pt = find_pt_object(guess_pt, grid)
            if guess_pt.get_ship_in() != None:
                '''Ship object that is hit'''
                ship_hit = guess_pt.get_ship_in()
                '''Targets left to hit is subtracted -1'''
                ship_hit.hit()
                if ship_hit.get_targets() == 0:
                    print("{} sunk".format(ship_hit.get_name()))
                    ship_list.remove(ship_hit)
                else:
                    if guess_pt.get_guessed():
                        print('hit (again)')
                    else:
                        guess_pt.set_guessed(True)
                        print('hit')              
            else:
                if guess_pt.get_guessed() == False:
                    print('miss')
                    guess_pt.set_guessed(True)

                else:
                    print('miss (again)')                    
    print('all ships sunk: game over')
 

'''This function gets the point in the guess file
    and returns the corresponding GridPos object in grid

    Parameters: The guess point from the line after it
                is parsed, the grid full of GridPos objects

    Returns: A GridPos object at the corresponding indice
            of grid

    Pre-Conditions: The guess point must be a tuple for it
                    to find correctly and guess pt must be
                    legal

    Post-Conditions: guess_pt is a legal pt GridPos object
            that corresponds to the guess pt tuple parameter''' 
def find_pt_object(guess_pt, grid):
    if type(guess_pt[0]) == int:
        i = guess_pt[0]
        j = guess_pt[1]
        guess_pt = grid[i][j]
    return guess_pt

    '''This function make the grid that will hold GridPos
        objects

    Parameters: an empty list grid

    Returns: 10x10 grid with each element being GridPos
                objects

    Pre-Conditions: grid must be empty

    Posr-Conditions: grid is a 10x10 grid of GridPos objects'''
def make_grid(grid):
    for i in range(10):
        row = []
        x = i
        for j in range(10):
            y = j
            '''GridPos object'''
            new_pt = GridPos(x,y)
            row.append(new_pt)
        grid.append(row)
    return grid

'''This class represents the board that the ships and points
    will be on it initializes the grid of GridPos objects and
    the list of Ship objects'''
class Board:
    def __init__(self, grid, ship_list):
        self.grid = grid
        self.ship_list = ship_list
        
    '''This method parses the grid and calls a method in a
        GridPos class to say there's a ship at said point

        Parameters/Returns: None

        Pre-Conditions: grid must be 10x10 and have GridPos
            objects, ship_list must be a list of Ship objects

        Post-Conditions: Calls function to say whether ship
            is at a given point'''
    def ship_in_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pt = self.grid[i][j]
                for ship in self.ship_list:
                    if pt.__str__() in ship.get_coords():
                        pt.found_ship(ship)

    def get_grid(self):
        return self.grid           

    def __str__(self):
        return self.grid

   
'''This class represents a grid point on the board. Takes in
    a x and y coordinate and if the point has and ship and
    if it has been previously guessed'''    
class GridPos:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ship_in = None
        self.guessed = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    '''This method indicates a ship is at a point'''
    def found_ship(self, ship):
        self.ship_in = ship
           
    def get_ship_in(self):
        return self.ship_in
    '''This method indicates when a point has been
        guessed'''
    def set_guessed(self, true):
        self.guessed = true

    def get_guessed(self):
        return self.guessed

    def __str__(self):
        return (self.x,self.y)
    


'''This class represents each of the 5 ships on the board.
    Takes in the name letter of ship and its length also its
    coordinates it takes up and how many targets are left to
    hit'''
class Ship:
    def __init__(self, ship_data, coords):
        self.name = ship_data[0]
        self.length = ship_data[1]
        self.coords = coords
        self.targets = ship_data[1]

    '''This method decreases the number of targets the ship
    can take after being hit'''
    def hit(self):
        self.targets -= 1
                
    def get_name(self):
        return self.name

    def get_length(self):
        return self.length

    def get_coords(self):
        return self.coords

    def get_targets(self):
        return self.targets

    def __str__(self):
        return self.name

'''This function tests for errors in the files that the
    user inputs

    Parameters: a file to be tested

    Returns: None

    Pre-Conditions: file must be found, reable and correct
            format

    Post-Conditions: If no errors the file is legal'''
def file_error(file):
    try:
        open(file)
    except FileNotFoundError:
        print("ERROR: Could not open file:", file)
        sys.exit(1)
    except IOError:
        print("ERROR: Cannot read file:", file)
        sys.exit(1)

'''This function checks for errors in the format of placement
    file

    Parameters: parsed data from input line, the length of a
        ship, and the raw (unparsed) line for error message

    Returns: None

    Pre-Conditions: pt_data must correspond to the ship and
        must be intergers, also length must correspond to the
        ship

    Post-Conditions: All ships are vertical or horitzontal and
        correct size'''
def format_check(pt_data, length, raw_line):
    try:
        assert(pt_data[0][0] == pt_data[1][0] or pt_data[0][1]\
               == pt_data[1][1])
    except AssertionError:
        print("ERROR: ship not horizontal or vertical:", raw_line)
        sys.exit(1)
    try:
        distancex = abs(pt_data[0][0] - pt_data[1][0]) + 1
        distancey = abs(pt_data[0][1] - pt_data[1][1]) + 1
        assert(length == distancex or length == distancey)
    except AssertionError:
        print("ERROR: incorrect ship size:", raw_line)
        sys.exit(1)
       
'''This function takes the coords from input file and places
    then in tuples in a list which it returns

    Parameters: pt_data is parsed data from the line of ship

    Returns: a list of tuples of coords for ship

    Pre-Conditions: pt_data is a parsed line of start and end
        points

    Post-Conditions: coords a list of tuples of all points
        covered by ship'''
def ship_coords(pt_data):
    coords = []
    num_xs = abs(pt_data[0][0] - pt_data[1][0])
    num_ys = abs(pt_data[0][1] - pt_data[1][1])
    if num_xs == 0:
        start_y = min(pt_data[0][1],pt_data[1][1])
        end_y = max(pt_data[0][1],pt_data[1][1])
        '''appends all vertical coords'''
        for i in range(num_ys + 1):
            coords.append((pt_data[0][0],start_y + i))
    else:
        start_x = min(pt_data[0][0],pt_data[1][0])
        end_x = max(pt_data[0][0],pt_data[1][0])
        for i in range(num_xs + 1):
            '''appends all horitzontal coords'''
            coords.append((start_x + i,pt_data[0][1]))
    return coords
    
'''This function sees if any ships overlap

    Parameters: a list of ship points from previous
        ships, the coords from one ship, and an unparsed
        line for error output

    Returns: Returns ship points of current and prev
        ships in question

    Pre-Conditions: ship_pts contain all pts from previously
        checked points, coords are the coords for a ship in
        question, raw_line is the line ship is on

    Post-Conditions: ship_pts returns ship points of current
    and prev ships in question'''
def test_overlap(ship_pts, coords, raw_line):
    try:
        for pt in coords:
            test_pt = pt
            assert(test_pt not in ship_pts)
            ship_pts.append(test_pt)
    except AssertionError:
        print("ERROR: overlapping ship: " + raw_line)
        sys.exit(1)
    return ship_pts

'''This function parses each line in the placement file and
    gives the data for each ship while also checking if
    the coords are legal and format

    Parameters: raw line from input, a list to see if fleet
        compostion is correct, and list to append ship points
        for ship overlap test

    Returns: ship data: name, length, and list of coords of
        ship

    Pre-Conditions: line is formatted correctly, input_check
        contains ships previously parsed and the coords of
        them are in ship_pts

    Post-Conditions: ship data contains: the name, length
        and the coords are the ship coords it is present'''
def parse_pfile(line, input_check, ship_pts):
    ships = [['A','Aircraft carrier','5'],['B','Battleship','4'],['S','Submarine','3'],\
             ['D','Destroyer','3'],['P','Patrol boat','2']]
    for i in range(len(ships)):
        if line[0] == ships[i][0]:
            input_check.append(line[0])
            raw_line = line
            line = raw_line.split()
            name = ships[i][0]
            length = int(ships[i][2])
            pt1 = (int(line[1]),int(line[2]))
            pt2 = (int(line[3]),int(line[4]))
            '''tests if ship placement is legal'''
            try:
                assert(0 <= int(line[1]) <= 9)
                assert(0 <= int(line[2]) <= 9)
                assert(0 <= int(line[3]) <= 9)
                assert(0 <= int(line[4]) <= 9)
            except AssertionError:
                print("ERROR: ship out-of-bounds:", raw_line)
                sys.exit(1)
            ship_data = (name, length) 
            pt_data = (pt1, pt2)
            format_check(pt_data, length, raw_line)
            coords = ship_coords(pt_data)
            s = test_overlap(ship_pts, coords, raw_line)
            return ship_data, coords

'''This function parses the guess file into a tuple of guess
    points

    Parameters: a raw line from file

    Returns: a tuple with the x and y coords

    Pre-conditions: line is formatted correctly

    Post-conditions: guess_pt is a tuple in the form (x, y)'''
def parse_gfile(line):
    line = line.split()
    if line != []:
        guess_x = int(line[0])
        guess_y = int(line[1])
        guess_pt = (guess_x, guess_y)
        '''checks to see if point is a legal guess'''
        try:
            assert(0 <= int(line[0]) <= 9)
            assert(0 <= int(line[1]) <= 9)
        except AssertionError:
            return "illegal guess"
        return guess_pt


main()
