#!/usr/bin/env python

# regroup main programme fonctions

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import m_IO as io
import m_codex as codex
import m_weapon as weapon
import m_unit as unit
import m_unit_type as u_type
import m_capacity as capacity

def index():
    io.cls()
    print '***********************************************************'
    print '**           Warhammer 40k Army list manager             **'
    print '***********************************************************'
    print '   Options : '
    print '    * 1 : Data management'
    print '    * 2 : Army list management'
    print '   Other : '
    print '    * OUT : program end'
    print '***********************************************************'
    return raw_input('Enter your choice : ')

def data_management():
    print ('\n')
    print '***********************************************************'
    print '**             Add or remove item or unit                **'
    print '***********************************************************'
    print '   Options :'
    print '    * 1 : Squad and unit'
    print '    * 2 : Weapon'
    print '    * 3 : Codex'
    print '    * 4 : Abilities'
    print '    * 5 : Unit types'
    print '   Other : '
    print '    * OUT : Menu out'
    print '***********************************************************'
    return raw_input('Enter your choice : ')

run_status = True

while run_status:
    option_index = index()
    if option_index == '1':
        l_unit_weapon = data_management()
	if l_unit_weapon.upper() == 'OUT':
	    raw_input('Back to main menu ...')        
	elif l_unit_weapon == '1':
            unit.unit_main()
        elif l_unit_weapon == '2':
            weapon.weapon_main()
	elif l_unit_weapon == '3':
	     codex.codex_main()
	elif l_unit_weapon == '4':
	     capacity.capacity_main()
	elif l_unit_weapon == '5':
	     print u_type.u_type_main()
        else:
            raw_input('Wrong option ...')

    elif option_index == '2':
        print 'TBD : list management'
    elif option_index.upper() == 'OUT':
        print 'Bye bye !'
        run_status = False
    else:
        raw_input('Bad option ... 1 OR 2 noob.')

