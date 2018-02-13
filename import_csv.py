# coding: utf-8
import csv
path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'

class ImportCsv():

    """
    modelo csv:
    datum wgs84 formato graus decimais
    nome|categoria|latitude|longitude
    """

    def __init__(self):

        self.delimitador='|'
        self.delimitador_texto='"'



    def inicia_rotina_csv(self):
        csvfile=open(path_input)
        spamreader = csv.reader(csvfile, delimiter=self.delimitador, quotechar=self.delimitador_texto)
        for row in spamreader:
            print(row)
