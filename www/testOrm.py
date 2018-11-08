# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:41:18 2018

@author: zhujihang
"""

import orm,asyncio
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop,user='www-data',password='www-data',db='awesome')
    
    u=User(name='Michael', email='michael@example.com',passwd='123456',image='about:blank')
    
    await u.save()
    
    a= await u.findAll()
    print(a)
    
    await orm.destroy_pool()
    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

