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
# from xml_gpx import XmlGpx
# xml_gps é um módulo utilizado para testes

path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'

#----------------------testes unitários ----------------------

# instancias de testes t1 e t2
t1=ImportCsv(path_input)
# t2=XmlGpx()
# t1.reseta_atributos()
# t2.set_wpt_atributos('-260000','-266655',0)
# t2.set_name_texto('texto2',0)
# t2.set_category_texto('vamos la',0)
#
# t1.set_lats_lons_csv('-260000','-225555',0)
# t1.set_names_csv('ivan jose',0)
# t1.set_categorys_csv('categoria do ivan',0)


# print(t2.get_wpt_atributos(0))
# print(t2.get_name_texto(0))
# print(t2.get_category_texto())
#
#

# print(t1.get_names_csv())
# print(t1.get_categorys_csv())
# print(t1.get_lats_lons_csv())
# ET.dump(t2.tree)

# ------------------ main---------------------------------------
# importando o CSV e atrinbuindo os atributos lat, lon, name e category
#intancia 1 ImportCsv
#intancia 2 xml_gpx
i11=ImportCsv(path_input)
names_csv=[]
categorys_csv=[]
lats_lons_csv=[]
names_csv=i11.get_names_csv()
categorys_csv=i11.get_categorys_csv()
lats_lons_csv=i11.get_lats_lons_csv()
# print(names_csv)
# print(categorys_csv)
# print(lats_lons_csv)
# adicionando os atributos no elemento wpt

ET.register_namespace('','http://www.topografix.com/GPX/1/1')
ET.register_namespace("xsi",'http://www.w3.org/2001/XMLSchema-instance')
tree = ET.parse('input_model.xml') #importa o xml e atribiu na árvore
root = tree.getroot() # captura a tag gpx como o root
# for rows in categorys_csv:
#     wpt



ET.dump(tree)
