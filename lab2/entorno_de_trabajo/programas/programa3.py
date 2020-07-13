# -*- coding: utf-8 -*-

import sys
import io
import nltk
import re
from nltk.tree import Tree

def tokenize(text):
    return list(text)

def parse(s):
    grammarString = """
    E -> A | E '*' A '*' E | E '_' A '_' E | '*' A '*' | '_' A '_' 
    A -> A B | A C | A D | B | C | D
    B -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    C -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
    D -> ' ' | '.' | ',' | '(' | ')'
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree

def imprimirrecursivo(t):
    salida = ""
    primerasterisco = True
    primerbarra = True
    for node in t:
        if type(node) is Tree:
            salida = salida + imprimirrecursivo(node)
        else:
            if node == '*':
                if primerasterisco:
                    salida = salida + "\\textbf{"
                else:
                    salida = salida + "}"    
                primerasterisco = not primerasterisco
            elif node == '_':
                if primerbarra:
                    salida = salida + "\emph{"
                else:
                    salida = salida + "}"
                primerbarra = not primerbarra
            elif node == "(":
                salida = salida + "\("
            elif node == ")":
                salida = salida + "\)"
            else:
                salida += node
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
            # cambiamos . por | y viceversa

            salida = imprimirrecursivo(tree)
        else:
            salida = "NO PERTENECE"
    except ValueError:
        salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





