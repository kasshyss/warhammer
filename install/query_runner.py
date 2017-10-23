#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import psycopg2 as pg

print sys.argv[1]
conn = pg.connect(dbname='warhammer', user='meriadoc', host='127.0.0.1', password='aradave')
cursor = conn.cursor()
cursor.execute(sys.argv[1])
conn.commit()
if sys.argv[1][:6:] == 'SELECT':
    for data in cursor.fetchall():
        print data
else:
    print 'Query OK'
cursor.close()
