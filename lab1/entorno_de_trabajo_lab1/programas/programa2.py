# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto = re.sub(r".*//.*\n","",texto)
    texto = re.sub(r".*\*\*\*[^\*\*\*]*\*\*\*.*\n","",texto)
    si = len(re.findall(r" +si +", texto))
    paracada = len(re.findall(r" +para cada +", texto)) 
    para = len(re.findall(r" +para +", texto)) - paracada
    mientras = len(re.findall(r" +mientras +", texto))
    
    output = "si: " + str(si) + "\n" + "para: " + str(para) + "\n" + "para-cada: " + str(paracada) + "\n" + "mientras: " + str(mientras)
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
    
