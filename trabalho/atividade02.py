print("Bem vindos a loja do Robson Felipe Da Silva Miranda")

print("""A Loja possui a seguinte relação:
    • Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
    • Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
    • Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais""")

def escolha_prato():
    acumulador = 0
    
    tamanho_BA_P = 16
    tamanho_BA_M = 18
    tamanho_BA_G = 22
    
    tamanho_FF_P = 15
    tamanho_FF_M = 17
    tamanho_FF_G = 21
    
    while True:
        prato = input("Digite o sabor do prato (BA/FF): ").upper()
        tamanho = input("Digite o tamanho (P, M ou G): ").upper()
        
        if prato == "BA" and (tamanho == "P" or tamanho == "M" or tamanho == "G"):
            if tamanho == "P":
                acumulador += tamanho_BA_P
            elif tamanho == "M":
                acumulador += tamanho_BA_M
            elif tamanho == "G":
                acumulador += tamanho_BA_G
            print(f"Você pediu um Bife Acebolado no tamanho: {tamanho}. O preço dele é: R${acumulador}")
        
        elif prato == "FF" and (tamanho == "P" or tamanho == "M" or tamanho == "G"):
            if tamanho == "P":
                acumulador += tamanho_FF_P
            elif tamanho == "M":
                acumulador += tamanho_FF_M
            elif tamanho == "G":
                acumulador += tamanho_FF_G
            print(f"Você pediu um Filé de Frango no tamanho: {tamanho}. O preço dele é: R${acumulador}")
        
        else:
            if prato != "BA" and prato != "FF":
                print("Sabor inválido, tente novamente")
            if tamanho != "P" and tamanho != "M" and tamanho != "G":
                print("Tamanho inválido, tente novamente")
            continue
        
        mais_alguma_coisa = input("Deseja pedir mais alguma coisa? (S/N): ")
        if mais_alguma_coisa.upper() != "S":
            break

    print(f"O total do seu pedido é: R${acumulador}")

escolha_prato()