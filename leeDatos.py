# leeDatos.py
# Leer CSV y construir una matriz (lista de listas)

def leer_csv_a_matriz(ruta):
    matriz = []
    f = open(ruta, "r", encoding="utf-8")
    lineas = f.readlines()
    for linea in lineas:
        cols = linea.rstrip("\n").split(",")
        matriz.append(cols)
    f.close()
    return matriz

def main():
    datos = leer_csv_a_matriz("titanic.csv")
    
    # Imprimir encabezado
    print("Encabezado:", datos[0])
    
    # Número de objetos (filas sin encabezado)
    num_objetos = len(datos) - 1
    print("Número de objetos:", num_objetos)
    
    # Valor de la columna 2 del objeto 4
    print("Columna 2 del objeto 4:", datos[4][1])
    
    # Mínimo y máximo de la columna 3 (numérica)
    valores_col3 = [float(x[2]) for x in datos[1:] if x[2]]
    print("Mínimo de columna 3:", min(valores_col3))
    print("Máximo de columna 3:", max(valores_col3))

main()

