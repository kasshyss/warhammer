#!/usr/bin/env python

# regroup main programme fonctions

import m_IO as io
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def index():
    print '** Warhammer 40k Army list manager **'
    print '   Options : '
    print '    * 1 : Add or Update units and weapon definition'
    print '    * 2 : Army list management'
    print '    * 3 : Display data'
    print '    * 4 : Codex'
    print '   Other : '
    print '    * OUT : program end'
    return raw_input('')


def library_change():
    print '\n** Add or remove item or unit **'
    print '   Options :'
    print '    * 1 : Unit'
    print '    * 2 : Weapon'
    print '    * 3 : Link weapon and units'
    print '    * 4 : Special rules'
    print '    * 5 : Link unit and special rules'
    print '   Other : '
    print '    * OUT : Menu out'
    return raw_input('')

def add_units():
    print 'What do you want to do ?'
    print '1 : Check units'
    print '2 : Add new unit'
    print '3 : Update a unit'
    return raw_input('')

def codex():
    print 'What do you want to do ?'
    print '1 : Check Codex'
    print '2 : Add codex'
    print '3 : Update a codex'
    return raw_input('')

def print_codex(row):
    print str(row[0]) + ' | ' + str(row[1])

run_status = True

while run_status:
    loop_option_status = True
    option_index = index()
    if option_index == '1':
        while loop_option_status:
            option = library_change()
            if option == 'OUT':
                loop_option_status = False
            elif option == '1':
                add = add_units()
                if add == '1':
                    print 'TBD display unit (LIKE)'
                elif add == '2':
                    print 'TBD Create unit'
                elif add == '3':
                    print 'TBD change an input'
                else:
                    print 'Bad option'

            elif option == '2':
                print 'TBD weapon option'
            elif option == '3':
                print 'TBD link unit weapon'
            elif option == '4':
                print 'TBD Special rules'
            elif option == '5':
                print 'TBD Linl rules and unit'
            else:
                print 'Bad option !'

    elif option_index == '2':
        print 'TBD : list management'
    elif option_index == 'OUT':
        print 'Bye bye !'
        run_status = False
    elif option_index == '3':
        print 'TBD display'
    elif option_index == '4':
        c = codex()
        if c == '1':
            print 'Codex full list'
            for code in io.get_codex_full():
                print_codex(code)
        elif c == '2':
            print 'Add a codex'
            for code in io.set_codex(raw_input('Codex name : ')):
                print_codex(code)
        elif c == '3':
            print 'Update a codex'
            print_codex(io.update_codex(raw_input('What is the codex id ? '),raw_input('What is the new name ? '))[0])
        else:
            print 'Bad codex option !!'
    else:
        print 'Bad option'

