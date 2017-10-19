#!/usr/bin/env python

import m_log as log
import psycopg2 as pg
import m_conf as conf
import os

# Clean console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

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
