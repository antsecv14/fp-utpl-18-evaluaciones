vent=int(input("Ingrese las ventas del empleado: "))
sb=float
por=float
sf=float
sb=360.40
if vent>5000:
	por=vent*0.15
	sf=por+sb;
	print("El sueldo final sera de: {0}".format(sf))
else:
	if vent>1000 and vent<=5000:
		por=vent*0.10
		sf=por+sb
		print("El sueldo final sera de: {0}".format(sf))
	else:
		if vent>500 and vent<=1000:
			por=vent*0.08
			sf=por+sb
			print("El sueldo final sera de: {0}".format(sf))
		else:
			if vent<=500:
				por=vent*0.05
				sf=por+sb
				print("El sueldo final sera de: {0} $".format(sf))