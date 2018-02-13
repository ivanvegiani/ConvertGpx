# coding: utf-8
import csv
path_input='/media/ivanvegiani/repositorios/Projetos/ConvertGpx/input/modelo.csv'
with open(path_input) as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')
    for row in spamreader:
        print(row)
