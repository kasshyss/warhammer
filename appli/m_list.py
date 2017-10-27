#!/usr/bin/env python
#-*- coding: utf-8 -*-

import m_IO as io
import m_conf as conf

# Menu (action display)
# Return the action
def list_menu():
    print '**********************************'
    print '*      List management menu      *'
    print '**********************************'
    print '* 1   : Create a new list        *'
    print '* 2   : Update a list            *'
    print '* 3   : Display a list           *'
    print '* OUT : Return ton tne main menu *'
    print '**********************************'
    return raw_input('What is your choice ? ')

# Display a item list
def print_list(li):
    sep = ' | '
    p_li = '* '
    for field in conf.get_conf('list.conf')['display'].split(','):
        p_li =  + io.add_space(li[int(field.split(':')[2])], int(field.split(':')[1]))  + sep
    print p_li[:-2:] + '*'

# Display tuples of list
def print_lists(lists):
    sep = ' | '
    sep_line = io.add_space('', 77).replace(' ','*')
    header = '* '
    for field in conf.get_conf('list.conf')['display'].split(','):
        header = header + io.add_space(field.split(':')[0], int(field.split(':')[1]))  + sep
    header = header[:-2:] + '*'
    print sep_line
    print header
    print sep_line
    for i_list in lists:
        print_list()
    print sep_line


# Display all the available list
def list_display_all():
    return 'Display all the list'

# Update a list by adding
def list_update():
    print 'Update list'

# Create a new list and chain on list update
def list_create():
    print 'Create a new list'

# Action list available in list
def list_action():
    io.cls()
    action = list_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        list_create()
    elif action == '2':
        list_update()
    else:
        raw_input('Wrong choice baby !!! ')
        return True

def list_main():
    while list_action():
        True
