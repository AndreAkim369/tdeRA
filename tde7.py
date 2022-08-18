hora = float(input("que horas sao? "))
minutos = float(input("quantos minutos? "))
segundos = float(input("quantos segundos? "))

minutosTotal = hora*60 + minutos
segundosTotal = hora*3600 + segundos
print("minutos: ", minutosTotal)
print("segundos: ", segundosTotal)