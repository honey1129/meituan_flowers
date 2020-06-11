#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
@version: python 3.7.0
@author: liuxuchao
@contact: liuxuchao1129@foxmail.com
@software: PyCharm
@file: run.py
@time: 2020-05-07 23:35
"""

from scrapy import cmdline


name = 'mt'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())