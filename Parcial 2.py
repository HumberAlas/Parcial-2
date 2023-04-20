# Mensaje de bienvenida.
print("\033[1m"+"\n Bienvenid@ al programa. "+"\033[0m")

# Variable que permita ejecutar el primer bucle.
VarDef = -1

# Bucle para que el usuraio ingrese un numero valido
while VarDef <= 0:

    # Funcion que permita que el bulce continue si el usuario ingresa un dato invalido  
    try:
        # Solicitar al usuario cuántos números desea ingresar
        VarDef = int(input("\nDefina un número para realizar la serie de datos. -> "))

        # Estructura condicional que haga que el bucle se detenga si el usuario ingresa un numero valido.
        if VarDef > 0:
            break
        
        print("\033[1m"+"\nNo es posible ingresar el datos escrito, por favor vuelva a intentarlo."+"\033[0m")

    # Mensaje que le indique al usuario que ha ingresado un dato invaido
    except ValueError:
        print("\033[1m"+"\nUsted ingresó un valor que no es un número entero. Por favor ingrese un valor valido."+"\033[0m")

#Variables para la suma de la serie de datos
totalSuma = 1
evalaur = 1

#Blucle de la suma de la serie de datos 
while evalaur < VarDef:
    totalSuma += 1/(1+evalaur)
    evalaur +=1

print("\nEl resultado de la suma es ", totalSuma)

print("\nFIN")