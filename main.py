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


i1=ImportCsv()
i2=XmlGpx()
i1.reseta_atributos()
i1.inicia_rotina_csv()

# print(i1.names_csv)
# print(i1.categorys_csv)
# print(i1.lats_csv)
# print(i1.lons_csv)
ET.dump(i2.tree)
print(i2.get_wpt_atributos())
