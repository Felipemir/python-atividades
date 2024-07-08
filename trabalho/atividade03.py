print("Bem vindos a Fábrica de Camisetas do Robson Felipe Da Silva Miranda")

print("""Olá, entre com o modelo desejado:
    • Camiseta Manga Curta Simples (MCS)
    • Camiseta Manga Longa Simples (MLS)
    • Camiseta Manga Curta Com Estampa (MCE)
    • Camiseta Manga Longa Com Estampa (MLE)
    """)

def escolha_modelo():
    modelos_camisetas = ['MCS', 'MLS', 'MCE', 'MLE']
    while True:
        modelo = input("Digite o modelo desejado (MCS, MLS, MCE, MLE): ").upper()
        if modelo not in modelos_camisetas:
            print("Modelo inválido, digite novamente")
        else:
            return modelo

def num_camisetas():
    while True:
        try:
            numero = int(input("Digite a quantidade de camisetas: "))
            if numero > 20000:
                print("Por favor, digite um número menor que 20 mil.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
# definindo a função frete
def frete():
    while True:
        print("Modelo de frete:")
        print("1 - Frete por transportadora - R$ 100,00")
        print("2 - Frete por sedex - R$ 200,00")
        print("3 - Retirar pedido na fábrica - R$ 0,00")
        try:
            frete = int(input("Digite o modelo de frete desejado: "))
            if frete == 1:
                return 100.00
            elif frete == 2:
                return 200.00
            elif frete == 3:
                return 0.00
            else:
                print("Opção inválida, por favor escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


# Definindo os valores para cada modelo de camiseta
valores_camisetas = {
    'MCS': 1.80,
    'MLS': 2.10,
    'MCE': 2.90,
    'MLE': 3.25,
}

modelo_escolhido = escolha_modelo()
quantidade_camisetas = num_camisetas()
preco_unitario = valores_camisetas[modelo_escolhido]

if quantidade_camisetas < 20:
    desconto = 0
elif quantidade_camisetas >= 20 and quantidade_camisetas < 200:
    desconto = 0.05
elif quantidade_camisetas >= 200 and quantidade_camisetas < 2000:
    desconto = 0.07
elif quantidade_camisetas >= 2000 and quantidade_camisetas < 20000:
    desconto = 0.12

valor_total = quantidade_camisetas * preco_unitario * (1 - desconto)
valor_frete = frete()

if valor_frete > 0:
    valor_total_com_frete = valor_total + valor_freted
else:
    valor_total_com_frete = valor_total

print(f"Modelo escolhido: {modelo_escolhido}")
print(f"Quantidade de camisetas: {quantidade_camisetas}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Desconto aplicado: {desconto * 100}%")
print(f"Valor total: R${valor_total:.2f}")
print(f"Valor do frete: R${valor_frete:.2f}")
print(f"Valor total com frete: R${valor_total_com_frete:.2f}")