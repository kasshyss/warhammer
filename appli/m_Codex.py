#!/usr/bin/env python

import m_IO as io

# Codex fonctions

# Main menu
def codex():
    io.cls()
    print '**************************'
    print '**   Codex Management   **'
    print '**************************'
    print 'What do you want to do ?'
    print '1   : Check Codex'
    print '2   : Add codex'
    print '3   : Update a codex'
    print 'OUT : Back to main menu'
    print '**************************'
    return raw_input('')

# How print a codex
def print_codex(row):
    print str(row[0]) + ' | ' + str(row[1])

def print_codex_tuple(tuples_codex):
    io.cls()
    print '**************************'
    print '*      Codex list        *'
    print '**************************'
    for codex in tuples_codex:
        print_codex(codex)
    print '**************************'
    raw_input('Continue ...')
    return True

def codex_main():
    c = codex()
    if c == '1':
        print_codex_tuple(io.get_codex_full())
        return True
    elif c == '2':
        print '**************************'
        print '*      Add a codex       *'
        print '**************************'
        print_codex_tuple(io.set_codex(raw_input('Codex name : ')))
        return True
    elif c == '3':
        print_codex_tuple(io.get_codex_full())
        print '**************************'
        print '*    Update a codex      *'
        print '**************************'
        print_codex(io.update_codex(raw_input('What is the codex id ? '),raw_input('What is the new name ? '))[0])
        print '**************************'
        raw_input('Continue ...')
        return True
    elif c.upper() == 'OUT':
        return False
    else:
        print 'Bad codex option !!'
        return True

def codex_loop():
    while codex_main():
        True
