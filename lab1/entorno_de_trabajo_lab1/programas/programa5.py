# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    texto = re.sub(r".*//.*\n","",texto)
    texto = re.sub(r".*\*\*\*[^\*\*\*]*\*\*\*.*\n","",texto)
    texto = re.sub(r"funcion.*{", "", texto)

    # Usamos la expresion regular [\w|(|)|\/|\+|\-|\*|\&|\=|\<|\>| ]* para que el programa no
    # detecte los saltos de linea como parte de la string 
    declaraciones = re.findall(r"\w+\s*:.*=\s*[\w|(|)|\/|\+|\-|\*|\&|\=|\<|\>| ]*", texto)

    for i in range(0, len(declaraciones)):
        nohayflecha = re.search(r"->", declaraciones[i])
        if nohayflecha != None:
            declaraciones[i] = re.sub(r"\s*->.*", "", declaraciones[i])
        declaraciones[i] = re.sub(r"\s*:.*\s*=\s*", ",", declaraciones[i])
        declaraciones[i] = re.sub(r"\n", "", declaraciones[i])

    output = ""
    for i in range(0, len(declaraciones)):
        output += "(" + declaraciones[i] + ")"
        if i != len(declaraciones) - 1:
            output += "\n"
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