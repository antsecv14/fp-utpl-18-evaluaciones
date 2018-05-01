t=int(input("Ingrese el valor en segundos que desea transformar: "))
m=int
s=int
m=0
if t>=60 :
	m=m+1;
	s=t-(m*60);
	print("El valor en segundos {0} es {1} minutos y {2} segundos".format(t,m,s))