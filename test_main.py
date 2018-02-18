# coding: utf-8
# version:1.0
# Copyright © 2001-2018 Python Software Foundation https://docs.python.org/3/license.html
#author: José Ivan Silva Vegiani

"""
ConvertGpx:
version:1.0
Copyright © 2001-2018 Python Software Foundation https://docs.python.org/3/license.html
author: José Ivan Silva Vegiani
Aplicação para conversão de arquivos csv para gpx.
Código aberto e livre, cedido gratuitamente e voluntáriamente pelo autor.
Destinado a todos interessados a utilizar a aplicação, em forma live e gratuita.
"""
import xml.etree.ElementTree as ET
from import_csv import ImportCsv
from xml_gpx import XmlGpx
import pytest




i1=ImportCsv()
i2=XmlGpx()
i1.reseta_atributos()

#----------------------testes unitários ----------------------
i2.set_wpt_atributos('-260000','-266655',0)
i2.set_name_texto('texto2',0)
i2.set_category_texto('vamos la',0)
i1.set_lats_lons_csv('-260000','-225555',0)
print(i2.get_wpt_atributos(0))
print(i2.get_name_texto(0))
print(i2.get_category_texto(0))
print(i1.get_lats_lons_csv(0))
ET.dump(i2.tree)

#-------------------pytest ---------------

def test_get_wpt_atributos():
    assert i2.get_wpt_atributos(0)=={'lat': '-260000', 'lon': '-266655'}
