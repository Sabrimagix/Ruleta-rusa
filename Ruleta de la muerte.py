# IMPORTAR LIBRERIAS
import random

# CAPTURAR JUGADORES
jugador=[]

nombre = input("Agregar nombre de jugador: ")
nombre=nombre.upper()
jugador.append(nombre)

x=True
while x:
  respuesta = input("Deseas agregar jugador S/N: ")
  if respuesta == "S" or respuesta =="s":
    nombre=input("Agregar nombre de jugador: ")
    # pone los nombres en mayusculas
    nombre=nombre.upper()
    jugador.append(nombre)
  elif respuesta == "N" or respuesta =="n":
    x = False
  else:
    print("Error al elegir")
    
####### DE AQUI EN ADELANTE SE REPETE ESTE CODIGO HASTA QUE QUEDE UN JUGADOR #########

# PREPARAR PISTOLA
# Turnos

while len(jugador)>1:
  turno=[]
  totalTurno = len(jugador)*3
  for t in range(totalTurno):
    turno.append(False)

    
  # cantidad de balas (1 por cada 6 turnos)
  totalBalas = totalTurno//6
  
  # poner balas al azar en los turnos
  for b in range(totalBalas):
    bala = random.randint(0,totalTurno-1)
    if turno[bala] == True:
      bala = random.randint(0,totalTurno-1)
      turno[bala] = True
    turno[bala] = True
  
  # cantidad Turnos/cantidad balas
  print("-----------------------------")
  print("Turnos: ",len(turno),"- Balas: ",totalBalas)  


  # JALAR EL GATILLO
  t=0
  contarBalas = 0
  while t < len(turno):
    nombre=input("Nombre de persona al turno: ")
    nombre=nombre.upper()
    if nombre in jugador:
      if turno[t]==True:
        if nombre in jugador:
          jugador.remove(nombre)
          print("-----------------------------")
          print("Jugador: ",nombre," eliminado")
          contarBalas += 1
      else:
        print(nombre," Aún no te tocaba")
      # si lla se acabaron las bals y solo hay un jugador se sale
      if contarBalas == totalBalas:
        break
      t += 1

    else:
      print("Escribe el nombre correctamente")

# Nombre del primer elemento de la lista (el que quedo)
print("---------------------------")
print("El ganador es: " + jugador[0])
