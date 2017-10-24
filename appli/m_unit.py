#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Unit management use case
# Check
# Add
# Remove

import m_IO as io
import m_weapon as weapon
import m_capacity as capa
import m_codex as codex
import m_squad as squad
import m_conf as conf
import m_unit_type as ut

def unit_menu():
    io.cls()
    print '***************************'
    print '*          Units          *'
    print '***************************'
    print '1   : Check unit list'
    print '2   : Check one unit'
    print '3   : Add a new unit'
    print '4   : Capacity menu'
    print '5   : Link capacity and unit'
    print '6   : Link weapon and unit'
    print 'OUT : Back to the main menu'
    print '***************************'
    return raw_input('What is your choice : ')

def print_unit(unit):
    sep = ' | '
    u = '* '
    for field in conf.get_conf('unit.conf')['unit_display'].split(','):
	u = u + io.add_space(unit[int(field.split(':')[2])], int(field.split(':')[1])) + sep
    print u[:-2:] + '*'

def print_units(units):
    sep = ' | '
    star = io.add_space('',139).replace(' ', '*')
    header =  '* '
    for field in conf.get_conf('unit.conf')['unit_display'].split(','):
	header = header + io.add_space(field.split(':')[0], int(field.split(':')[1])) + sep
    header = header[:-2:] + '*'
    print star
    print header
    print star
    for unit in units:
        print_unit(unit)
    print star

def unit_weapon_menu(unit_id):
    io.cls()
    print '***************'
    print '* unit/weapon *'
    print '***************'
    print '1   : link     '
    print '2 : : add&link'
    print 'OUT : next step'
    print '***************\n'
    print_units(io.get_unit_ids(str(unit_id)))
    print '\n'
    weapon.print_weapons(io.get_unit_weapon(str(unit_id)))
    return raw_input('\nWhat do you do Sir ? ')

def unit_capacity_menu(unit_id):
    io.cls()
    print '***************'
    print '* unit/ability *'
    print '***************'
    print '1   : link     '
    print '2 : : add&link'
    print 'OUT : next step'
    print '***************\n'
    print_units(io.get_unit_ids(str(unit_id)))
    print '\n'
    capa.print_capacities(io.get_unit_capacities(str(unit_id)))
    return raw_input('\nWhat do you do Sir ? ')

def unit_weapon_action(unit_id):
    action = unit_weapon_menu(unit_id)
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        io.set_unit_weapon(str(unit_id), raw_input('Weapon ID : '))
        return True
    elif action == '2':
        weapon.print_weapons(weapon.add_weapon())
        io.set_unit_weapon(str(unit_id), raw_input('Weapon ID : '))
        return True
    else:
        raw_input('Wrong input noob ...')
        return True

def unit_capacity_action(unit_id):
    action = unit_capacity_menu(unit_id)
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        io.set_unit_capacity(unit_id, raw_input('Ability ID : '))
        return True
    elif action == '2':
        capa.print_capacities(capa.add_capacity())
        io.set_unit_capacity(unit_id, raw_input('Ability ID : '))
        return True
    else:
        raw_input('Wrong input noob ...')
        return True

def unit_weapon(unit_id):
    while unit_weapon_action(unit_id):
        True

def unit_capacity(unit_id):
    while unit_capacity_action(str(unit_id)):
        True

# step 1 creat unit
# 2 add abilities
# 3 add weapons
def add_unit():
    u_data={}
    for field in conf.get_conf('unit.conf')['unit_fields'].split(','):
	if field.split(':')[0] == 'codex':
	    codex.codex()
	if field.split(':')[0] == 'type':
	    ut.unit_type()
        u_data[field.split(':')[0]] = raw_input(field.split(':')[1] + ' ')
    unit_id = io.set_unit(u_data)[0][0]
    raw_input('\nUnit add, now link unit and weapon   ' + str(unit_id))
    io.cls()
    unit_weapon(unit_id)
    raw_input('all weapons added, now add abilities')
    unit_capacity(unit_id)

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
    else:
        raw_input('Action not allowed :(')
        return True

# Menu loop
def unit_main():
    while unit_action():
        True
