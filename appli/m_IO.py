#!/usr/bin/env python

import m_log as log
import psycopg2 as pg
import m_conf as conf
import os

# Clean console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_space(item, size):
    item_len = len(str(item))
    item = str(item)
    if item_len >= size:
        return item
    for i in range(size - i_len):
        item = ' ' + item
    return item

#run a sql query in postgres
#return the result
#use config to connect to the rigth DB
def __pg_request(query):

    db_conf = conf.get_conf('db.conf')
    try:
        conn = pg.connect("dbname='" + str(db_conf['DB']) + "' user='" + str(db_conf['USER']) + "' host='" + str(db_conf['IP']) + "' password='" + str(db_conf['PWD']) +"'")
        cursor =  conn.cursor()
        cursor.execute(query)
        conn.commit()
        if query[:6:] == 'SELECT':
            data = cursor.fetchall()
        else:
            data='Query done : ' + query
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_IO.__pg_request | Unable to manage the database link' + str(ValueError))
        return False
    return data

# Codex fonc
def get_codex_full():
    return __pg_request(conf.get_conf('queries.conf')['get_codex_full'])
def get_codex_spe(name):
    return __pg_request(conf.get_conf('queries.conf')['get_codex_spe'].replace('$like$', name))
def set_codex(name):
    __pg_request(conf.get_conf('queries.conf')['set_codex'].replace('$name$', name))
    return __pg_request(conf.get_conf('queries.conf')['get_codex_spe'].replace('$like$', name))
def update_codex(codex_id, name):
    __pg_request(conf.get_conf('queries.conf')['update_codex'].replace('$name$', name).replace('$id$', codex_id))
    return __pg_request(conf.get_conf('queries.conf')['get_codex_id'].replace('$id$', codex_id))

# Weapon fonct
def get_weapon_full():
    return __pg_request(conf.get_conf('queries.conf')['get_weapon_full'])
def get_weapon_ids(ids): #ids = id1,id2,id3
    return __pg_request(conf.get_conf('queries.conf')['get_weapon_ids'].replace('$id$', ids))
def get_weapon_spe(name): #name is a string
    return __pg_request(conf.get_conf('queries.conf')['get_weapon_like'].replace('$name$', name))
def set_weapon(data): # data is a dico
    __pg_request(conf.get_conf('queries.conf')['set_weapon'].replace('$name$', data['name']).replace('$range$', data['range']).replace('$type$',data['type']).replace('$S$', data['S']).replace('$AP$', data['AP']).replace('$D$',data['D']).replace('$abilities$', data['abilities']).replace('$cost$', data['cost']) )
    return __pg_request(conf.get_conf('queries.conf')['get_weapon_like'].replace('$name$', data['name']))

# Unit fonction
def get_unit_full():
    return __pg_request(conf.get_conf('queries.conf')['get_unit_full'])
def get_unit_ids(ids): #ids = id1,id2,id3 etc....
    return __pg_request(conf.get_conf('queries.conf')['get_unit_ids'].replace('$ids$',ids))
def get_unit_weapon(unit_id):
    return __pg_request(conf.get_conf('queries.conf')['get_unit_weapon'].replace('$uid$',unit_id))

# capacity
def get_capacities():
    return __pg_request(conf.get_conf('queries.conf')['get_abilities'])
def get_capacity_name(name):
    return __pg_request(conf.get_conf('queries.conf')['get_ability_spe'].replace('$name$', name))
def set_capacity(c_data):
    __pg_request(conf.get_conf('queries.conf')['set_ability'].replace('$name$', c_data['name']).replace('$description$', c_data['desc']))
    return __pg_request(conf.get_conf('queries.conf')['get_ability_spe'].replace('$name$',c_date['name']))
    
