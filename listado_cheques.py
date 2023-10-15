import csv

archivo=input("Ingrese el nombre del archivo: ")

with open(archivo, 'r') as entrada:
    reader= csv.reader(entrada)
    for row in reader:
        print(row)
  