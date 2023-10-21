import csv

global archivo
archivo=input("Ingrese el nombre del archivo: ")

global dni 
dni = input("Ingrese su DNI: ")

global salida 
salida = input("Ingrese (en letras mayusculas) de que manera quiere ver los datos PANTALLA o CSV: ")

global estado 
estado = input("Ingrese (en letras mayusculas) si el cheque es EMITIDO o DEPOSITADO: ")
  

def lectura_archivo():
    filtered_rows = []
    cheque_dict = {}  # Un diccionario para llevar un registro de los números de cheque por cuenta
    with open(archivo, 'r') as entrada:
        reader = csv.reader(entrada)
        header = next(reader)  # Leer la primera fila (encabezado)
        for row in reader:
            row_dni = row[8]  # Obtener el valor del DNI en la fila
            if row_dni == dni:
                nro_cheque = row[0]
                cuenta = row[3]
                if cuenta in cheque_dict and nro_cheque in cheque_dict[cuenta]:
                    print(f"Error: El número de cheque {nro_cheque} está repetido en la cuenta {cuenta}")
                else:
                    if cuenta not in cheque_dict:
                        cheque_dict[cuenta] = set()
                    cheque_dict[cuenta].add(nro_cheque)
                filtered_rows.append(row)
    
    return header, filtered_rows



def guardar_en_pantalla(header, rows):
    print(header)
    for row in rows:
        print(row)

def guardar_en_csv(header, rows):
    with open('resultados_filtrados.csv', 'w', newline='') as salida:
        writer = csv.writer(salida)
        writer.writerow(header)
        writer.writerows(rows)

if salida == "PANTALLA":
    header, filtered_rows = lectura_archivo()
    guardar_en_pantalla(header, filtered_rows)
elif salida == "CSV":
    header, filtered_rows = lectura_archivo()
    guardar_en_csv(header, filtered_rows)
else:
    print("La opción de salida no es válida. Debe ser 'PANTALLA' o 'CSV'.")