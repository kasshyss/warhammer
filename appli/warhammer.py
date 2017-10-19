#!/usr/bin/env python

# regroup main programme fonctions

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import m_IO as io
import m_Codex as codex
import m_weapon as weapon
import m_unit as unit

def index():
    io.cls()
    print '***********************************************************'
    print '**           Warhammer 40k Army list manager             **'
    print '***********************************************************'
    print '   Options : '
    print '    * 1 : Add or Update units and weapon definition'
    print '    * 2 : Army list management'
    print '    * 3 : Display data'
    print '    * 4 : Codex'
    print '   Other : '
    print '    * OUT : program end'
    print '***********************************************************'
    return raw_input('')

def library_change():
    print ('\n')
    print '***********************************************************'
    print '**             Add or remove item or unit                **'
    print '***********************************************************'
    print '   Options :'
    print '    * 1 : Unit'
    print '    * 2 : Weapon'
    print '   Other : '
    print '    * OUT : Menu out'
    print '***********************************************************'
    return raw_input('')

run_status = True

while run_status:
    loop_option_status = True
    option_index = index()
    if option_index == '1':
        l_unit_weapon = library_change()
        
        if l_unit_weapon == '1':
            unit.unit_main()
        elif l_unit_weapon == '2':
            weapon.weapon_main()
        else:
            raw_input('Wrong option ...')

    elif option_index == '2':
        print 'TBD : list management'
    elif option_index.upper() == 'OUT':
        print 'Bye bye !'
        run_status = False
    elif option_index == '3':
        print 'TBD display'
    # Codex use case
    elif option_index == '4':
	codex.codex_loop()
        
    else:
        print 'Bad option'

