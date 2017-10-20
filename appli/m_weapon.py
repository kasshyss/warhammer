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

# Add space before a string
def add_space(item, size):
    i_len = len(str(item))
    item = str(item)
    if i_len >= size:
        return item
    for i in range(size - i_len):
        item = ' ' + item
    return item

# Print item
def print_weapon(weapon):
    print '* ' + add_space(weapon[0], 3) + ' | ' + add_space(weapon[1], 20) + ' | ' + add_space(weapon[3], 15) + ' | ' + add_space(str(weapon[2]), 5) + ' | ' + add_space(str(weapon[4]), 3) + ' | ' + add_space(weapon[5], 3) + ' | ' + add_space(weapon[6], 3) +' | '+ add_space(weapon[8], 4) + ' | ' + add_space(weapon[7], 20) + ' *'
# Print list
def print_weapons(weapons):
    print '********************************************************************************************************'
    print '* '+add_space('ID', 3)+' | '+add_space('Weapon name',20)+' | '+add_space('Type', 15)+' | '+add_space('Range',4)+' | '+'  S |  AP |   D | Cost | '+add_space('Comment', 20)+' *'
    print '* ____________________________________________________________________________________________________ *'
    for weapon in weapons:
        print_weapon(weapon)
    print '********************************************************************************************************\n'
# Add weapon
def add_weapon():
        weapon_fields =[['name','Weapon name (30) : '], ['range','Weapon range (int) '], ['type','Weapon type (15) : '], ['S', 'Weapon Strength (int) : '], ['AP', 'Armor pen (3) : '], ['D','Damage (4) : '], ['abilities','Comment (75) : '], ['cost', 'Cost in point (int) : ']]
        w_data={}
        for field in weapon_fields:
            w_data[field[0]] = raw_input(field[1])
        return io.set_weapon(w_data)

# Actions
def weapon_action():
    action = weapon_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        print_weapons(io.get_weapon_full())
        raw_input('Continue ...')
        return True
    elif action == '2':
        print_weapons(io.get_weapon_spe(raw_input('What is the weapon name ?\n')))
        raw_input('Continue ...')
        return True
    elif action == '3':
        print_weapons(add_weapon())
        raw_input('Continue ...')
        return True
    elif action == '4':
        raw_input('TBD update weapon')
        return True
    else:
        raw_input('Action not allowed :(')
        return True

# Menu loop
def weapon_main():
    while weapon_action():
        True
