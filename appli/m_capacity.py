#!/usr/bin/env pyhon
#-*- coding: utf-8 -*-

import m_IO as io

def capacity_menu():
    io.cls()
    print '*******************************'
    print '* Special unit abilities menu *'
    print '*******************************'
    print '1   : Add a new capacity'
    print '2   : Check a capacity'
    print '3   : Check all the capacities'
    print 'OUT : back to the previous menu'
    print '*******************************'
    return raw_input('Enter your choice : ')

def print_capacity(capacity):
    sep = ' | '
    print '* ' + io.add_space(capacity[0], 3) + sep + io.add_space(capacity[1], 20) + sep + io.add_space(capacity[2], 80) + ' *'

def print_capacities(caps):
    sep = ' | '
    sep_line = io.add_space('',113).replace(' ', '*')
    print sep_line
    print '* ' + io.add_space('ID', 3) + sep + io.add_space('Name',20) + sep + io.add_space('Description', 80) + ' *'
    print sep_line
    for c in caps:
        print_capacity(c)
    print sep_line

def add_capacity():
    c_fields = [['name','What is the ability name ? '],['desc','Please enter a full description : ']]
    c_data = {}
    for field in c_fields:
        c_data[field[0]] = raw_input(field[1])
    return io.set_capacity(c_data)
    

def action_capacity():
    action = capacity_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        print_capacities(add_capacity())
        raw_input('Abilities added ....')
        return True
    elif action == '2':
        print_capacities(io.get_capacity_name(raw_input('Please enter the capacity name : ')))
        raw_input('To continue, insert a coin ... killing press enter')
        return True
    elif action == '3':
        print_capacities(io.get_capacities())
        raw_input('Not to long ?')
        return True
    else:
        raw_input('Bad entry noob')
        return True

def capacity_main():
    while action_capacity():
        True
