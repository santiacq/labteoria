# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto = re.sub(r".*//.*\n","",texto)
    texto = re.sub(r".*\*\*\*[^\*\*\*]*\*\*\*.*\n","",texto)
    texto = re.search(r"funcion.*\{", texto)
    texto = texto.group()
    
    nombrefuncion = re.sub(r"funcion ", "", texto)
    nombrefuncion = re.sub(r"\(.*\{", "", nombrefuncion)
    
    variables = re.search(r"\(.*\)", texto)
    variables = variables.group()
    variables = re.sub(r"\(", "", variables)
    variables = re.sub(r"\)", "", variables)
    
    retorno = re.search(r"\-\>.*\{",texto)
    if retorno != None:
        retorno = retorno.group()
        retorno = re.sub(r"\-\> ","",retorno)
        retorno = re.sub(r" \{", "", retorno)    
    output = nombrefuncion
    if variables != "":
        output = output + "\n" + variables
    if retorno !=None :
        output = output + "\n" + retorno  
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
