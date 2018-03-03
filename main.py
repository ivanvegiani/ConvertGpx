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
import os
from import_csv import ImportCsv
# from xml_gpx import XmlGpx
# xml_gps é um módulo utilizado para testes


# para linux
# path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'
#path_input='../input/input.csv'
# path_output='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/output/favourites.gpx'
#path_output='../output/favourites.gpx'


# para windows
path_output='..\output\\favourites.gpx'
path_input='..\input\input.csv'
# path_output='G:\Projetos\ConvertGpx\output\gavourites.gpx'
#----------------------testes unitários ----------------------

# instancias de testes t1 e t2
# t1=ImportCsv(path_input)
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
i1=ImportCsv(path_input)
names_csv=[]
categorys_csv=[]
lats_lons_csv=[]
names_csv=i1.get_names_csv()
categorys_csv=i1.get_categorys_csv()
lats_lons_csv=i1.get_lats_lons_csv()


# conversão de sexagesimal para decimal:
# graus decimais = graus + minutos/60 +segundos

# print(i1.head[0])
# print(len(i1.head[0]))
# print(len(lats_lons_csv))
# print(len(names_csv))

# print(names_csv)
# print(categorys_csv)
# print(lats_lons_csv)
# adicionando os atributos no elemento wpt

ET.register_namespace('','http://www.topografix.com/GPX/1/1')
ET.register_namespace("xsi",'http://www.w3.org/2001/XMLSchema-instance')
tree = ET.parse('input_model.xml') #importa o xml e atribiu na árvore
root = tree.getroot()
# wpt_atributos={}
# wpt=ET.Element('wpt')
# name=ET.SubElement(wpt, 'name')
# category=ET.SubElement(wpt, 'category')
# wpt.attrib={'lat':'-fdfdf','lon':'fodkofdk'}  <== exemplo para atributos lat lon
# name.text='nome' <== exemplo para texto
# category.text='categoria'<== exemplo para texto
# root.append(wpt)  <== adiciona o elemento wpt para árvore
# print(lats_lons_csv[5])
i=0
name=['']
for rows in lats_lons_csv:
    wpt=ET.Element('wpt',lats_lons_csv[i])
    name=ET.SubElement(wpt, 'name')
    name.text=names_csv[i]
    category=ET.SubElement(wpt, 'category')
    category.text=categorys_csv[i]
    root.append(wpt)
    i=i+1
ET.dump(tree)
print(os.name)
#print(len(i1.head[0]))
tree.write(path_output,encoding='UTF-8')
