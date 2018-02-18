# coding: utf-8
import csv

path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'

class ImportCsv():

    """
    único modelo csv aceito:
    datum wgs84 formato graus decimais
    nome|categoria|latitude|longitude
    """

    global names_csv
    names_csv=[]
    global categorys_csv
    categorys_csv=[]
    global lats_lons_csv
    global lat2_csv
    global lon2_csv
    lat2_csv=''
    lon2_csv=''
    lats_lons_csv=[]


    def __init__(self):

        self.names_csv=names_csv
        self.categorys_csv=categorys_csv
        self.delimitador='|'
        self.delimitador_texto='"'
        self.spamreader=[[]]
        self.linha=[]
        self.lats_lons_csv=[{'lat':lat2_csv,'lon':lon2_csv}]
        self.names_csv=['']
        csvfile=open(path_input)
        spamreader = csv.reader(csvfile, delimiter=self.delimitador, quotechar=self.delimitador_texto)

    def reseta_atributos(self):
        del names_csv[:]
        del categorys_csv[:]
        del lats_lons_csv[:]

    def set_lats_lons_csv(self,lat2_csv,lon2_csv,i):
        self.lats_lons_csv[i]={'lat':lat2_csv,'lon':lon2_csv}

    def get_lats_lons_csv(self,i):
        return self.lats_lons_csv[i]

    def set_names_csv(self,names,i):
        self.names_csv[i]=names

    def get_names_csv(self,i):
        return self.names_csv[i]




#parei aqui
