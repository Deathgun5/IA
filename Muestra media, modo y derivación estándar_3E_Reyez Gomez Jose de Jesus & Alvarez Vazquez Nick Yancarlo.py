import math
import statistics as stats

#Integrantes: Alvarez Vazquez Nick Yancarlo
#             Jose de Jesus Reyes Gomez

def menu():
 print ()
 print ("1) Ingresar datos")
 print ("2) Calcular media")
 print ("3) Calcular varianza")
 print ("4) Calcular desviación")
 print ("5) Calcular la moda")
 print ("6) Salir")

def obtenerDatos():
 print ("Cuantos datos desea ingresar?")
 numeroDatos = int(input())
 datos = []
 for i in range(0, numeroDatos):
  print ("Ingresar datos ", i + 1)
  dato = input()
  datos.append(int(dato))
 return datos

def obtenerPromedio(datos):
 suma = 0
 for dato in datos:
  suma += dato
 return suma / len(datos)

def obtenerVarianza(datos):
 n = len(datos)
 promedio = obtenerPromedio(datos)
 varianza = 0
 for dato in datos:
  varianza += math.pow((dato - promedio), 2)
 return varianza / (n - 1)

def obtenerDesviacion(varianza, datos):
 if(varianza == 0):
  varianza = obtenerVarianza(datos)
  return math.sqrt(varianza)
 elif(varianza > 0):
  return math.sqrt(varianza)

def obtenerModa(datos):
    datos.sort()
    n=len(datos)
    i=0
    b=0
    c=0
    while(i<n):
        a=datos.count(i)
        if(a>b):
            b=a
            c=datos[i]
        i=i+1
    return c
print("La moda es: ", obtenerModa)

def main():
 salir = False
 datos = []
 varianza = 0
 while not salir:
  opcion = -1
  menu()
  opcion = input()
  if(opcion == '1'):
   datos = obtenerDatos()
  elif(opcion == '2'):
   promedio =  sum (datos) / len (datos)
   print ("Valor de la media es: ", promedio)
   input("Enter para continuar...")
  elif(opcion == '3'):
   varianza = obtenerVarianza(datos)
   print ("Valor de varianza: ", varianza)
   input("Enter para continuar...")
  elif(opcion == '4'):
   desviasion = obtenerDesviacion(varianza, datos)
   print ("Valor de Desviacion estandar: ", desviasion)
   input("Enter para continuar...")
  elif(opcion == '5'):
   obtenerModa=len(datos)
   print("La moda es: ", obtenerModa)
   input("Enter para continuar...")
  elif(opcion == '6'):
   salir = True
  else:
   print ("No existe opción")

if __name__ == "__main__":
 main()