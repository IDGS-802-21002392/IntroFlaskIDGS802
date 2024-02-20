from io import open

archivo_texto = open('anombres.txt', 'r')
#archivo_texto.write('\n datos en el archivo')
#print(archivo_texto.readlines())

for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

archivo_texto.close()