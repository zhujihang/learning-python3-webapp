# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:57:04 2018

@author: zhujihang
"""

__author__ ='zhujihang'

import asyncio,logging
import aiomysql

def log(sql, args=()):
    logging.info('SQL:%s' %sql)
    
#创建数据库的全局连接池
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
    
    async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs
            

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)