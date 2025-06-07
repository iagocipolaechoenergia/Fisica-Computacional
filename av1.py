ra = int(input("DIGITE SEU RA: "))

# pegando a soma dos digitos do ra
soma = 0
for i in str(ra):
    soma += int(i)

print("SOMA DOS DIGITOS DO RA: ", soma)

G = 9.8
v = soma
hmax = soma**2 / (2 * G)
# imprimindo hmax com 2 casas decimais
print("ALTURA MAXIMA ATINGIDA: {:.2f} m".format(hmax))