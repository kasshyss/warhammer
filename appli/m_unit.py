#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Unit management use case
# Check
# Add
# Remove

import m_IO as io
import m_weapon as weapon
import m_capacity as capa

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

def print_unit(unit):
    sep = ' | '
    print '* ' + io.add_space(unit[0],3) +sep+ io.add_space(unit[1], 30) +sep+ io.add_space(unit[2], 12) +sep+ io.add_space(unit[3], 20) +sep+ io.add_space(unit[4],2) +sep+ io.add_space(unit[5], 2) +sep+ io.add_space(unit[6], 2) +sep+ io.add_space(unit[7], 2) +sep+ io.add_space(unit[8], 2) +sep+ io.add_space(unit[9],2) +sep+ io.add_space(unit[10], 2) +sep+ io.add_space(unit[11],2) +sep+ io.add_space(unit[12], 5) +sep+ io.add_space(unit[13], 4)  +' *'

def print_units(units):
    sep = ' | '
    star = io.add_space('',134).replace(' ', '*')
    print star
    print '* ' + ' ID' +sep+ io.add_space('Unit name', 30) +sep+ io.add_space('Type', 12) +sep+ io.add_space('Codex',20) +sep+ ' M' +sep+ 'WS' +sep+ 'BS' +sep+ ' S' +sep+ ' T' +sep+ ' A' +sep+ 'Ld' +sep+ 'Sg' +sep+ 'Point' +sep+ 'Power'  + ' *'
    print star
    for unit in units:
        print_unit(unit)
    print star

# step 1 creat unit
# 2 add abilities
# 3 add weapons
def add_unit():
    # TODO conf file
    unit_field = [['name','What is the unit name (str 30) ? '],['type','What is the unit category (str 12) ? '],['codex','What is the codex id (int) ? '],['m','What is the unit mouvement (int) ? '],['ws','What is the unit weapon skill WS (int) ? '],['bs','What is the unit battel skill BS (int) ? '],['s','What is the unit strength ? '],['t','What is the unit toughness ? '],['a','How many attacks ? '],['ld ','What is the unit leadership ? '],['sg','What is the unit base savgarde ? '],['point','How many cost this unit in point ? '], ['power','How many cost this unit in point']]
    # TODO Query insert

# Actions
def unit_action():
    action = unit_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        print_units(io.get_unit_full())
        raw_input('I cannot find ... JOKE')
        return True
    elif action == '2':
        unit_id = raw_input('What is the unit id to display ? ')
        io.cls()
        print_units(io.get_unit_ids(unit_id))
        weapon.print_weapons(io.get_unit_weapon(unit_id))
        capa.print_capacities(io.get_unit_capacities(unit_id))
        raw_input('See what I see ...')
        return True
    elif action == '3':
        add_unit()
        raw_input('Unit added mother fucker')
        return True
    elif action == '4':
        capa.capacity_main()
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
