preco = float(input("qual o preco do produto? "))
juros = preco * 0.05
preco1 = (preco + juros)/3
preco2 = preco/2
preco3 = preco - juros

print("Parcelado em 3 vezes com 5% de juros: ", preco1, "por mes")
print("Parcelado em 2 vezes sem juros: ", preco2)
print("a vista com 5% de desconto: ", preco3)