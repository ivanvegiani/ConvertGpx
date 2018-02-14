# coding: utf-8
import csv
path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'

class ImportCsv():

    """
    modelo csv:
    datum wgs84 formato graus decimais
    nome|categoria|latitude|longitude
    """

    global names_csv
    names_csv=[]
    global categorys_csv
    categorys_csv=[]
    global lats_csv
    lats_csv=[]
    global lons_csv
    lons_csv=[]

    def __init__(self):

        self.names_csv=names_csv
        self.categorys_csv=categorys_csv
        self.lats_csv=lats_csv
        self.lons_csv=lons_csv
        self.delimitador='|'
        self.delimitador_texto='"'
        self.spamreader=[[]]
        self.linha=[]



    def inicia_rotina_csv(self):
        csvfile=open(path_input)
        spamreader = csv.reader(csvfile, delimiter=self.delimitador, quotechar=self.delimitador_texto)
        for linha in spamreader:
            name_csv=linha[0]
            category_csv=linha[1]
            lat_csv=linha[2]
            lon_csv=linha[3]
            names_csv.append(name_csv)
            categorys_csv.append(category_csv)
            lats_csv.append(lat_csv)
            lons_csv.append(lon_csv)
        return lons_csv and lats_csv and categorys_csv and names_csv




    def reseta_atributos(self):
        del names_csv[:]
        del categorys_csv[:]
        del lats_csv[:]
        del lons_csv[:]
