#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Weapon managment use case
# Check full list
# Check like list
# Add new weapon
# Update a weapon

import m_IO as io

def weapon_menu():
    io.cls()
    print '***************************'
    print '*         Weapons         *'
    print '***************************'
    print '1   : Check weapon list'
    print '2   : Check one weapon'
    print '3   : Add a new weapon'
    print '4   : Update a weapon'
    print 'OUT : Back to the main menu'
    print '***************************'
    return raw_input('What is your choice : ')

# Actions
def weapon_action():
    action = weapon_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        print 'TBD print all weapons'
    elif action == '2':
        print 'TBD weapon like input'
    elif action == '3':
        print 'TBD add weapon'
    elif action == '4':
        print 'TBD update weapon'
    else:
        raw_input('Action not allowed :(')
        return True

# Menu loop
def weapon_main():
    while weapon_action():
        True
