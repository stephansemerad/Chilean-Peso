#!/usr/bin/python
## -*- coding: utf-8 -*-
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)

#Note Only works on 2.7
#unfortunately mechanize only works with Python 2.4, Python 2.5, Python 2.6, and Python 2.7.



from bs4 import BeautifulSoup
import re
from time import gmtime, strftime
from datetime import datetime, timedelta

_browser = mechanize.Browser()
_browser.open("https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx")
_browser.select_form(name='form1')
_browser.set_all_readonly(False) # allow changing the .value of all controls
_browser['txtDate'] = '%s %s %s' % (day,month,year)
_browser.submit()
content = _browser.response().read()
soup = BeautifulSoup(content, "html.parser")
'label', {'id': 'lblValor1_5'}
rate =  re.findall('<label id="lblValor1_5">?.*</label>', str(soup))[0]
rate = rate.replace('<label id="lblValor1_5">','').replace('</label>','').replace(' ','').replace(',','.')
rate = float(rate)
print (rate)
