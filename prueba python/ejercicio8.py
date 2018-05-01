l1=input("Ingrese la letra 1 : ")
l2=input("Ingrese la letra 2 : ")
l3=input("Ingrese la letra 3 : ")
if l1<l2 and l1<l3:
	print("La primera letra es: \n {0}".format(l1))
else:
	if l2<l1 and l2<l3:
		print("La primera letra es: \n {0}".format(l2))
	else:
		if l3<l1 and l3<l2:
			print("La primera letra es: \n {0}".format(l3))