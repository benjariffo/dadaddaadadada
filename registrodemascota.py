mascotasactivas = []
mascotadormilona = []
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de mascotas a registrar: "))

        if cantidad > 0:
            break
        else:
            raise ValueError;
    except ValueError:
        print("Error: Debe ingresar un número válido.")

#crear la estructura for para registrar las mascotas
for i in range(cantidad):
   #pedir el nombre de la mascota
   while True: 
       try:
           nombremascota = input(f"Ingrese el nombre de la mascota {i+1}: ")
           if(len(nombremascota) >= 4):
               break
           else:
               raise ValueError;
       except ValueError:
               print("Error: El nombre de la mascota debe tener al menos 4 caracteres.")
    #pedir nivel de la energia que tiene que ser un numero entero positivio
   while True:
       try:
            energia = int(input(f"Ingrese el nivel de la energia {i+1}:"))
            if energia > 0:
                break
            else:
                raise ValueError;
       except ValueError:
            print("Error: el nivel de energia tiene que ser positivo")
   while True:
       try:
            edad = int(input(f"Ingrese la edad de la mascota {i+1}:"))
            if edad > 0:
                break
            else:
                raise ValueError;
       except ValueError:
            print("Error: la edad de la mascota tiene que ser positiva")
   if energia >= 80:
       print("tu mascota es activa")
       mascotasactivas += 1;
   elif energia >= 50:
         print("tu mascota es dormilona")
         mascotadormilona += 1;
#mostrar el resultado
print(f"cantidad de mascotas activas: {mascotasactivas}")
print(f"cantidad de mascotas dormilonas: {mascotadormilona}")
print(f"cantidad de mascotas reguistreadas: {cantidad}")

             