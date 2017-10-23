#!/usr/bin/env python
#-*- coding: utf-8 -*-

import m_IO as io
import m_conf as conf

def weapon_menu():
    io.cls()
    print '***************************'
    print '*         Weapons         *'
    print '***************************'
    print '1   : Check weapon list'
    print '2   : Check one weapon'
    print '3   : Add a new weapon'
    print 'OUT : Back to the main menu'
    print '***************************'
    return raw_input('What is your choice : ')

# Print item
def print_weapon(weapon):
    sep = ' | '
    w = '* '
    for field in conf.get_conf('weapon.conf')['fields_size'].split(','):
	w = w + io.add_space(weapon[int(field.split(':')[2])], int(field.split(':')[1])) + sep
    print w[:-3:] + '*'

# Print list of items
def print_weapons(weapons):
    sep = ' | '
    sep_line = io.add_space('', 104).replace(' ', '*')
    header = '* '
    for field in conf.get_conf('weapon.conf')['fields_size'].split(','):
        header = header + io.add_space(field.split(':')[0], int(field.split(':')[1])) + sep
    header = header[:-2:] + '*'
    print sep_line
    print header
    print sep_line
    for weapon in weapons:
        print_weapon(weapon)
    print sep_line
# Add weapon
def add_weapon():
        w_data={}
        for field in conf.get_conf('weapon.conf')['get_fields'].split(','):
	    w_data[field.split(':')[0]] = raw_input(field.split(':')[1].replace("'",'') + ' : ')
        return io.set_weapon(w_data)
# Return weapon full list 
def weapon():
    return print_weapons(io.get_weapon_full())

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
    else:
        raw_input('Action not allowed :(')
        return True

# Menu loop
def weapon_main():
    while weapon_action():
        True
