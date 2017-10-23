#!/usr/bin/env python

import m_IO as io
import m_conf as conf

# Codex fonctions

# Main menu
def codex_menu():
    io.cls()
    print '**************************'
    print '**   Codex Management   **'
    print '**************************'
    print 'What do you want to do ?'
    print '1   : Check Codex list'
    print '2   : Add a new codex'
    print '3   : Get a codex id'
    print 'OUT : Back to main menu'
    print '**************************'
    return raw_input('Enter your choice : ')

# How print a codex item
def print_codex_item(row):
    print '* ' + io.add_space(str(row[0]), 3) + ' | ' + io.add_space(str(row[1]), 30) + ' *'

# Print a codex list
def print_codex(codex):
    sep_line = io.add_space('',40).replace(' ', '*')
    io.cls()
    print sep_line
    print '* '+ io.add_space('Codex',17) + ' list' + io.add_space('',14) + ' *'
    print '* ' + ' ID | ' + io.add_space('Codex name', 30) + ' *'
    print sep_line
    print ''
    for c in codex:
        print_codex_item(c)
    print sep_line
    return True


def add_codex():
    io.cls()
    print '****************************'
    print '*    Current codex list    *'
    print '****************************'
    print_codex(io.get_codex_full())
    print '***********************'
    print '*    Add a codex      *'
    print '***********************'
    print_codex(io.set_codex(raw_input(conf.get_conf('codex.conf')['get_codex_label'].split(':')[1] + ' : ')))
    raw_input('Codex added ...')

def codex():
    return print_codex(io.get_codex_full())


def get_codex_name(c_id):
    print_codex(io.get_codex_id(c_id))

def codex_action():
    c = codex_menu()
    if c == '1':
        print_codex(io.get_codex_full())
	raw_input('Ok, done !!')
        return True
    elif c == '2':
        add_codex()
        return True
    elif c == '3':
        get_codex_name(raw_input('Enter the codex id : \n'))
        raw_input('Continue ...')
        return True
    elif c.upper() == 'OUT':
        return False
    else:
        raw_input('Bad codex option !!')
        return True

def codex_main():
    while codex_action():
        True
