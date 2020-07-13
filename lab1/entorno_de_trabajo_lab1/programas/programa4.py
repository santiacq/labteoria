# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto = re.sub(r".*//.*\n","",texto)
    texto = re.sub(r".*\*\*\*[^\*\*\*]*\*\*\*.*\n","",texto)
    texto = re.sub(r"funcion.*{", "", texto)

    cantbool = len(re.findall(r">=", texto))
    cantbool += len(re.findall(r"<=", texto))
    cantbool += len(re.findall(r">", texto)) - len(re.findall(r">=", texto)) - len(re.findall(r"->", texto))
    cantbool += len(re.findall(r"<", texto)) - len(re.findall(r"<=", texto))
    cantbool += len(re.findall(r"==", texto))
    cantbool += len(re.findall(r"&&", texto))
              
    cantnobool = len(re.findall(r"\+", texto))
    cantnobool += len(re.findall(r"-", texto)) - len(re.findall(r"->", texto))
    cantnobool += len(re.findall(r"\*", texto))
    cantnobool += len(re.findall(r"/", texto))

    output = "booleanas: " + str(cantbool) + "\n" + "no booleanas: " + str(cantnobool)
    return output

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
