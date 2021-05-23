Lpropiedades = ["cochera","departamento","casa"]
casacomprap=4500000
casaalquilerp=11500
habitaciones=0
List=[casaalquilerp, habitaciones]
def calcular(List):
	if aoc=="alquilo" and prop=="casa":	
		if habitaciones==1: 
			calculo=casaalquilerp
			total=calculo
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==2: 
			calculo=casaalquilerp*0.17
			total=calculo+casaalquilerp
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==3: 
			calculo=casaalquilerp*0.37
			total=calculo+casaalquilerp
			print("El valor del alquiler es: $ "+nombre)
			print(total)
	if aoc=="alquilo" and prop=="departamento":
		if habitaciones==1: 
			calculo=casaalquilerp
			total=calculo+casaalquilerp*0.11
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==2: 
			calculo=casaalquilerp*0.28
			total=calculo+casaalquilerp
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==3: 
			calculo=casaalquilerp*0.48
			total=calculo+casaalquilerp
			print("El valor del alquiler es: $ "+nombre)
			print(total)
	if aoc=="compro" and prop=="casa":
		if habitaciones==1: 
			calculo=casacomprap
			total=calculo
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==2: 
			calculo=casacomprap*0.18
			total=calculo+casacomprap
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==3: 
			calculo=casacomprap*0.33
			total=calculo+casacomprap
			print("El valor del alquiler es: $ "+nombre)
			print(total)
	if aoc=="compro" and prop=="departamento":
		if habitaciones==1: 
			calculo=casacomprap
			total=calculo+casacomprap*0.11
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==2: 
			calculo=casacomprap*0.29
			total=calculo+casacomprap
			print("El valor del alquiler es: $ "+nombre)
			print(total)
		if habitaciones==3: 
			calculo=casacomprap*0.44
			total=calculo+casacomprap
			print("El valor del alquiler es: $ "+nombre)
			print(total)

print("Ingrese su nombre")
nombre=input()
print("¿Que propiedad desea averiguar? cochera,departamento o casa "+nombre)
prop=input()
Lpropiedades=prop
print("¿Alquila o compra? si alquilas escribe alquilo y si compras escribe compro "+nombre)
aoc=input()
if aoc=="alquilo":
	if prop=="casa":
		print("¿Con cuantas habitaciones? con un maximo de 3+ habitaciones "+nombre)
		habitaciones=int(input())	
		calcular(habitaciones)
	if prop=="departamento":
		print("¿Con cuantas habitaciones? con un maximo de 3+ habitaciones "+nombre)
		habitaciones=int(input())
		calcular(habitaciones)
	if prop=="cochera":
			print("Precio del alquiler $2780$ "+nombre)
if aoc=="compro":
	if prop=="casa":
		print("¿Con cuantas habitaciones? con un maximo de 3+ habitaciones "+nombre)
		habitaciones=int(input())
		calcular(habitaciones)
	if prop=="departamento":
		print("¿Con cuantas habitaciones? con un maximo de 3+ habitaciones "+nombre)
		habitaciones=int(input())
		calcular(habitaciones)
	if prop=="cochera":
		print("No vendemos las cocheras que poseemos, solo las alquilamos señor "+nombre)
for i in prop:
	if prop=="casa" or "cochera" or "departamento":
		prop=""
		aoc=""
		habitaciones=0
		print("-Variables reseteadas-")

