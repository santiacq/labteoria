# -*- coding: utf-8 -*-
import re
import sys
import os
import glob


if __name__ == '__main__':

	# CHEQUEAR VERSION DE PYTHON
	if (sys.version_info.major != 3 ) or (sys.version_info.minor != 8):
		print("Está usando la versión de Python: "+str(sys.version))
		sys.exit("Pero debe usar la versión de Python 3.8.X")
	
	# VEFIFICAR QUE EXISTA EL DIRECTORIO SALIDAS
	try:
		os.stat("salidas")
	except:
		os.mkdir("salidas")
	
	# ITERAR SOBRE TODOS LOS PROGRAMAS Y ENTRADAS
	errores = 0;
	for archPrograma in sorted(glob.glob('programas'+os.sep+'programa*.py')):

		for archEntrada in sorted(glob.glob('entradas'+os.sep+'entrada*.txt')):

			# OBTENER LOS NOMBRES DE ARCHIVOS
			s = re.search(r"(programa\d)", archPrograma, flags=0)
			programa = s.group(1)
			s = re.search(r"(entrada\d+)", archEntrada, flags=0)
			entrada = s.group(1)
			archSalida = "salidas" + os.sep + programa + "_" + entrada + ".txt"
			archSalidaOficial = "salidas_oficiales" + os.sep + programa + "_" + entrada + ".txt"

			# EJECUTAR EL PROGRAMA
			print("\n\nPrograma: "+programa+" - Entrada: "+entrada+"\n")
			ejecutar = "python " + archPrograma + " " + archEntrada + " " + archSalida
			print(ejecutar)
			x = os.system(ejecutar)
			if x != 0:
			   print ("ERROR: al ejecutar "+programa+" para la entrada "+entrada)
			   errores = errores + 1

			else:
			    # COMPARAR LAS SALIDAS
				diferencias = "diff --strip-trailing-cr " + archSalida + " " + archSalidaOficial 
				print(diferencias)
				x = os.system(diferencias)		
				if x != 0:
					print("ERROR: los archivos de salida: "+archSalida+" y "+archSalidaOficial+" no son iguales")
					errores = errores + 1
				else:
					print("OK")
	
	# MOSTRAR RESULTADO
	if errores == 0:
		print("\nResultado: todos los test OK!!")
	else:
		print("\nResultado: "+str(errores)+" error/es.")
