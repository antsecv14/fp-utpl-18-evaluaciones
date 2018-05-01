c1=int(input("Ingrese la calificacion 1: "))
c2=int(input("Ingrese la calificacion 2: "))
c3=int(input("Ingrese la calificacion 3: "))
c4=int(input("Ingrese la calificacion 4: "))
med=int
med=c1+c2+c3+c4
if med>=90 :
	print("El estudiante con el promedio de calificacion {0} tiene una puntiacion de A".format(med))
else:
	if med>=80 and med<=89 :
		print("El estudiante con el promedio de calificacion {0} tiene una puntuacion de B".format(med))
	else:
		if med>=70 and med<=79 :
			print("El estudiante con el promedio de califiacion {0} tiene una puntuacion de C".format(med))
		else:
			if med<70 :
				print("El estuadiante con el promedio de califiacion {0} tiene una puntuacion de D".format(med))
