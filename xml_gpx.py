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



    def __init__(self):

        ET.register_namespace('','http://www.topografix.com/GPX/1/1')
        ET.register_namespace("xsi",'http://www.w3.org/2001/XMLSchema-instance')
        tree = ET.parse('input_model.xml') #importa o xml e atribiu na árvore
        root = tree.getroot() # captura a tag gpx como o root
        lat='lat'
        lon='lon'
        name_texto='texto name'
        category_texto='texto category'
        wpt_atributos={'lat':lat,'lon':lon}
        wpt=ET.Element('wpt',wpt_atributos)
        name=ET.SubElement(wpt, 'name')
        category=ET.SubElement(wpt, 'category')
        root.append(wpt)
        self.tree=tree
        self.root=root
        self.wpt_atributos=wpt_atributos
        self.lat=lat
        self.lon=lon
        self.name_texto=name_texto
        self.category_texto=category_texto
















#for elemento in tree.iter():
#    print(elemento.tag)
#    print(elemento.attrib)
#print(ET.iselement(wpt))



#tree.write('favourites.gpx', encoding='UTF-8')
