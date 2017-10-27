#!/usr/bin/env python
#-*- coding: utf-8 -*-

import m_unit as unit
import m_conf as conf
import m_IO as io

# Squad menu option
# Create a squad
# print a squad
def squad_menu():
    print '***********************************'
    print '*         Squad management        *'
    print '***********************************'
    print '* 1   : Create a new squad        *'
    print '* 2   : Add missing units         *'
    print '* 3   : Print squads list         *'
    print '* 4   : Print a squad             *'
    print '* 5   : Units management          *'
    print '* OUT : Back to the previous menu *'
    print '***********************************'
    return raw_input('What is your choice BUDDY ? ')

# Print squads list
def print_squad(squad):
    d_squad = '* '
    sep = ' | '
    for field in conf.get_conf('squad.conf')['display'].split(','):
        d_squad = d_squad + io.add_space(squad[int(field.split(':')[2])],int(field.split(':')[1]))  + sep
    print d_squad[:-2:] + '*'
def print_squads(squads):
    sep = ' | '
    header = '* '
    line_sep = io.add_space('', 53).replace(' ', '*')
    for field in conf.get_conf('squad.conf')['display'].split(','):
        header = header + io.add_space(field.split(':')[0], int(field.split(':')[1])) + sep
    header = header[:-2:] + '*'
    print line_sep
    print header
    print line_sep
    for squad in squads:
        print_squad(squad)
    print line_sep

# Add a new squad
def squad_add():
    s_data={}
    for field in conf.get_conf('squad.conf')['fields'].split(','):
        s_data[field.split(':')[1]] = raw_input(field.split(':')[0])
    squad_id = io.set_squad(s_data)[0][0]
    while raw_input('Add a new unit to the squad (Y/N) ? ') <> 'N':
        unit.add_unit(squad_id)

def squad_display(name):
    tmp = io.get_squad_spe(name)
    squad_id = tmp[0]
    print_squads(tmp)
    tmp = io.get_unit_by_squad(squad_id)
    unit_id = tmp[0]
    unit.print_units(tmp)

# display the squad lull list
def squad_display_full():
    print_squads(io.get_squads())

# Action in squad menu
def squad_action():
    io.cls()
    action = squad_menu()
    if action.upper() == 'OUT':
        return False
    elif action == '1':
        io.cls()
        squad_add()
        return True
    elif action == '2':
        io.cls()
        squad_display_full()
        unit.add_unit(raw_input('What is the squad id to update ? '))
        return True
    elif action == '3':
        squad_display_full()
        raw_input('I want them all !! ')
        return True
    elif action == '4':
        squad_display(raw_input('What is the squad name ?\n'))
    elif action == '5':
        unit.unit_main()
    else:
        raw_input('Read option, well, try to chose one which in the list next time NOOB ')
        return True

# Main squad
def squad_main():
    while squad_action():
        True
