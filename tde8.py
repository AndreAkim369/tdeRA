altura = float(input("qual a altura do cilindro? "))
raio = float(input("qual o raio do cilindro? "))

areaL = 2*3.14*raio*altura
areaB = 3.14*raio**2

areaT = 2*areaB + areaL

latas = areaT/15

custo = latas*50

print("custo é de: ", custo)
print("quantidade de latas: ", latas)