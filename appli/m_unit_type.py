#!/usr/bin/env python

import m_IO as io
import m_conf as conf

# unit type fonctions

# Main menu
def u_type_menu():
    io.cls()
    print '******************************'
    print '**   Unit Type Management   **'
    print '*******************$$$$*******'
    print 'What do you want to do ?'
    print '1   : Check unit type list'
    print '2   : Add a new unit type'
    print 'OUT : Back to main menu'
    print '******************************'
    return raw_input('Enter your choice : ')

# How print a unit type item
def print_u_type(row):
    print '* ' + io.add_space(str(row[0]), 3) + ' | ' + io.add_space(str(row[1]), 30) + ' *'

# Print a unit type list
def print_u_types(u_types):
    sep_line = io.add_space('',40).replace(' ', '*')
    io.cls()
    print sep_line
    print '* '+ io.add_space('Types',17) + ' list' + io.add_space('',14) + ' *'
    print '* ' + ' ID | ' + io.add_space('Unit type', 30) + ' *'
    print sep_line
    for ut in u_types:
        print_u_type(ut)
    print sep_line
    return True


def add_u_type():
    io.cls()
    print_u_types(io.get_unit_type())
    print '***********************'
    print '*   Add a unit type   *'
    print '***********************'
    print_u_types(io.set_unit_type(raw_input('What is the unit type name ? :\n')))
    raw_input('Unit type added ...')

def unit_type():
    return print_u_types(io.get_unit_type())

def u_type_action():
    c = u_type_menu()
    if c == '1':
        unit_type()
	raw_input('Ok, done !!')
        return True
    elif c == '2':
        add_u_type()
        return True
    elif c.upper() == 'OUT':
        return False
    else:
        raw_input('Bad unit type option !!')
        return True

def u_type_main():
    while u_type_action():
        True
