#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Unit management use case
# Check
# Add
# Remove

import m_IO as io
import m_weapon as weapon

def unit_menu():
    io.cls()
    print '***************************'
    print '*          Units          *'
    print '***************************'
    print '1   : Check unit list'
    print '2   : Check one unit'
    print '3   : Add a new unit'
    print '4   : Add a new capacity'
    print '5   : Link capacity and unit'
    print '6   : Link weapon and unit'
    print '7   : Update an unit'
    print 'OUT : Back to the main menu'
    print '***************************'
    return raw_input('What is your choice : ')


# Actions
def unit_action():
    action = unit_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        raw_input('TBD  all units...')
        return True
    elif action == '2':
        raw_input('TBD  one unit with detail...')
        return True
    elif action == '3':
        raw_input('TBD  add unit ...')
        return True
    elif action == '4':
        raw_input('TBD  capacity...')
        return True
    elif action == '5':
        raw_input('TBD  capacity => unit...')
        return True
    elif action == '6':
        raw_input('TBD  weapon  => unit...')
        return True
    elif action == '7':
        raw_input('TBD  updates...')
        return True
    else:
        raw_input('Action not allowed :(')
        return True

# Menu loop
def unit_main():
    while unit_action():
        True
