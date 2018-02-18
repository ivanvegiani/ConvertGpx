#coding: utf-8
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from import_csv import ImportCsv
import xml.etree.ElementTree as ET



'''
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?> # declaração XMl
<gpx version="1.1" creator="COPEL" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"> #root e seus atributos
  <wpt lat="-26.1860003" lon="-50.9284544"> elemento  tag "wpt" atributos lat="-26.1860003" lon="-50.9284544"
    <name>876759780</name> tag nane e text 876759780
    <category>Geral</category>tag category e text Geral
  </wpt>
</gpx>
'''

class XmlGpx(ElementTree):

    global tree
    global root
    global name_texto
    global wpt_atributos
    global category_texto
    global lat
    global lon
    global lat1
    global lon1
    global name_texto1
    global category_texto1

    lat1='lat'
    lon1='lon'
    lat=['lat']
    lon=['lon']
    name_texto1=''
    name_texto=[name_texto1]
    category_texto1=''
    category_texto=[category_texto1]
    wpt_atributos=[{}]

    # tree.write('favourites.gpx',encoding='UTF-8')

    def __init__(self):

        ET.register_namespace('','http://www.topografix.com/GPX/1/1')
        ET.register_namespace("xsi",'http://www.w3.org/2001/XMLSchema-instance')
        tree = ET.parse('input_model.xml') #importa o xml e atribiu na árvore
        root = tree.getroot() # captura a tag gpx como o root
        #wpt=ET.Element('wpt',wpt_atributos[0])S
        wpt=ET.Element('wpt')
        name=ET.SubElement(wpt, 'name')
        category=ET.SubElement(wpt, 'category')
        root.append(wpt)
        self.wpt=wpt
        self.tree=tree
        self.root=root
        self.wpt_atributos=wpt_atributos
        self.name_texto=name_texto
        self.category_texto=category_texto

    def __str__(self):
        return "%s" % (self.wpt_atributos[0])

    def get_wpt(self):
        pass

    def get_tree(self):
        pass

    def set_wpt_atributos(self,lat,lon,i):
        self.wpt_atributos[i]={lat1:lat,lon1:lon}

    def get_wpt_atributos(self,i):
        return wpt_atributos[i]

    def set_name_texto(self,name_texto1,i):
        self.name_texto[i]=name_texto1

    def get_name_texto(self,i):
        return name_texto[i]

    def set_category_texto(self,category_texto1,i):
        self.category_texto[i]=category_texto1


    def get_category_texto(self,i):
        return self.category_texto[i]
