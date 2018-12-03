import json, re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from time import gmtime, strftime
from urllib.request import urlopen

# chilean_pesos
# ------------------------------------------------------------------------------
now = datetime.now()
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre',]
translation = {'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}
url = 'https://si3.bcentral.cl/Indicadoressiete/secure/Serie.aspx?gcode=PRE_EUR&param=cgBnAE8AOQBlAGcAIwBiAFUALQBsAEcAYgBOAEkASQBCAEcAegBFAFkAeABkADgASAA2AG8AdgB2AFMAUgBYADIAQwBzAEEARQBMAG8ASgBWADQATABrAGQAZAB1ADIAeQBBAFAAZwBhADIAbABWAHcAXwBXAGgATAAkAFIAVAB1AEIAbAB3AFoAdQBRAFgAZwA5AHgAdgAwACQATwBZADcAMwAuAGIARwBFAFIASwAuAHQA'
soup = BeautifulSoup(urlopen(url), "html.parser") #Get the HTML
year = soup.find("label", { "id" : "lblAnioValor" }).getText()
clp = {}
for month in months:
    for day in range(31):
        search = ('gr_ctl%s_%s' % ("%02d" % (day + 1),month))
        item = soup.find("span", { "id" : search })
        if item != None:
            item = item.getText()
            if item != '':
                date = '%s-%s-%s' % (year, translation[month], "%02d" % (day))
                date = datetime.strptime(date, "%Y-%m-%d")
                date = date.strftime('%d.%m.%Y')
                clp[date] = item

for i in clp:
    print(i, clp[i])
