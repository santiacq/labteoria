# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.tree import Tree

def tokenize(text):
    return list(text)

def parse(s):
    grammarString = """
    S -> 'a' | 'b' | '(' S ')' | '(' S ')' '*' | S '.' S | S '|' S 
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree

def imprimirrecursivo(t):
    salida = ""
    for node in t:
        if type(node) is Tree:
            salida = salida + imprimirrecursivo(node)
        else:
            if node == '.':
                salida = salida + "|"
            elif node == '|':
                salida = salida + "."
            else:
                salida = salida + node
    return salida



if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
        tree = parse(s)
        if tree:

            salida = imprimirrecursivo(tree)
        else:
            salida = "NO PERTENECE"
    except ValueError:
        salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





