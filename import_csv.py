# coding: utf-8
import csv
path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'



class ImportCsv():

    def inicia_rotina_csv(self):
        csvfile=open(path_input)
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            print(row)
