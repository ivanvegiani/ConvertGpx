# coding: utf-8
import csv



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
    lat2_csv=""
    lon2_csv=""
    lats_lons_csv=[]
    global spamreader


    def __init__(self,path_input):

        self.names_csv=names_csv
        self.categorys_csv=categorys_csv
        self.delimitador='|'
        self.delimitador_texto='"'
        self.spamreader=[[]]
        self.linha=[]
        self.lats_lons_csv=lats_lons_csv
        #self.names_csv=['']
        csvfile=open(path_input)
        spamreader = csv.reader(csvfile, delimiter=self.delimitador, quotechar=self.delimitador_texto)

        for rows in spamreader:
                self.names_csv.append(rows[0])
                self.categorys_csv.append(rows[1])
                self.lats_lons_csv.append({'lat':rows[2],'lon':rows[3]})

    def __repr__ (self):
        return "%s" (self.lats_lons_csv)

    def __str__ (self):
        return "%s" (self.lats_lons_csv)

    def reseta_atributos(self):
        del names_csv[:]
        del categorys_csv[:]
        del lats_lons_csv[:]

    # def set_lats_lons_csv(self,lat2_csv,lon2_csv,i):
    #     for i in spamreader:
    #         self.lats_lons_csv[i]={'lat':lat2_csv,'lon':lon2_csv}

    def get_lats_lons_csv(self):
        return self.lats_lons_csv

    # def set_names_csv(self,names,i):
    #     self.names_csv[i]=names

    def get_names_csv(self):
        return self.names_csv

    # def set_categorys_csv(self,i):
    #     self.categorys_csv

    def get_categorys_csv(self):
        return self.categorys_csv
