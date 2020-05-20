
from binary_tree import *
from stack import *

def build_parsetree(exp_string):
    elist = exp_string.split()
    s = Stack()
    etree = BinaryTree("@")
    s.push(etree)

    curr = etree
    print(elist)
    for token in elist:
        print("--------")
        print("token = " + token)
        if token == '(':
            print("Rule 1")
            curr.insert_left('@')
            s.push(curr)
            curr = curr.get_left()

            
        elif token not in '+-*/)': # token is an operand
            print("Rule 3")
            curr.set_root(int(token))
            parent = s.pop()
            curr = parent
            
        elif token in '+-*/':      # token is an operator
            print("Rule 2")
            #set root of current to operatot
            curr.set_root(token)
            #add new node to right child
            curr.insert_right('@')
            #descend to right child
            s.push(curr)
            curr = curr.get_right()

        elif token == ')':
            print("Rule 4")
            
  
            
        else:
            print("Error: token not recognized")
            exit()
            
        print(etree)
        
    return etree

