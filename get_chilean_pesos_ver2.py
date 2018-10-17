#!/usr/bin/python
## -*- coding: utf-8 -*-
import os, re,random, string, sys,  os.path
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from func.func import *
from db.db import *


url = 'https://si3.bcentral.cl/Indicadoressiete/secure/Serie.aspx?gcode=PRE_EUR&param=cgBnAE8AOQBlAGcAIwBiAFUALQBsAEcAYgBOAEkASQBCAEcAegBFAFkAeABkADgASAA2AG8AdgB2AFMAUgBYADIAQwBzAEEARQBMAG8ASgBWADQATABrAGQAZAB1ADIAeQBBAFAAZwBhADIAbABWAHcAXwBXAGgATAAkAFIAVAB1AEIAbAB3AFoAdQBRAFgAZwA5AHgAdgAwACQATwBZADcAMwAuAGIARwBFAFIASwAuAHQA'
html = urlopen(url) #Open the website
soup = BeautifulSoup(html, "html.parser") #Get the HTML
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre',]
months_dictionary = {
                     'Enero'        :'01'
                    ,'Febrero'      :'02'
                    ,'Marzo'        :'03'
                    ,'Abril'        :'04'
                    ,'Mayo'         :'05'
                    ,'Junio'        :'06'
                    ,'Julio'        :'07'
                    ,'Agosto'       :'08'
                    ,'Septiembre'   :'09'
                    ,'Octubre'      :'10'
                    ,'Noviembre'    :'11'
                    ,'Diciembre'    :'12'
                    }

year = soup.find("label", { "id" : "lblAnioValor" }).getText()
for i in range(31):
    _date = str(i)
    _date = '0' + _date if len(_date) < 2 else _date

    pull_date = str(i+1)
    pull_date = '0' + pull_date if len(pull_date) < 2 else pull_date

    for month in months:
        item = soup.find("span", { "id" : "gr_ctl"+pull_date+"_"+month+"" })
        if item == None or item == '':
            pass
        else:
            item = item.getText()
            if item =='':
                pass
            else:
                data = symbol = rate = ''
                date    = year+'-'+str(months_dictionary[month])+'-'+str(_date)
                symbol  = 'CLP'
                rate    = item.replace(',','.')
                print (date, symbol, rate)
