# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.parse.generate import generate

def tokenize(text):
    return list(text)

def parse(s):
    grammarString = """
    Q0 -> 'A' Q2 | 'B' Q2 | 'C' Q1 | 'A' | 'B'
    Q1 -> 'A' Q3 | 'B' Q3 | 'C' Q4 | 'A' | 'B' | 'C'
    Q2 -> 'A' Q1 | 'B' Q1 | 'C' Q5 
    Q3 -> 'A' Q4 | 'B' Q4 | 'C' Q2 | 'A' | 'B' | 'C'
    Q4 -> 'A' Q2 | 'B' Q2 | 'C' Q1 | 'A' | 'B' 
    Q5 -> 'A' Q4 | 'B' Q4 | 'C' Q2 | 'A' | 'B' | 'C'
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
        tree = parse(s)

        if tree:
            salida = "PERTENECE"
        else:
            salida = "NO PERTENECE"
    except ValueError:
        salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
