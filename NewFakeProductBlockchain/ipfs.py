# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:15:03 2022

@author: Studio Pc-1
"""
import urllib3
url = 'https://ipfs.io/ipfs/'+"QmZBUoczcWyVjEzRiPbUfDkdBXuv37nqLMDy9xdcjedFYm"
connection_pool = urllib3.PoolManager()
resp = connection_pool.request('GET',url )
f = open("QmZBUoczcWyVjEzRiPbUfDkdBXuv37nqLMDy9xdcjedFYm", 'wb')
f.write(resp.data)
f.close()
resp.release_conn()