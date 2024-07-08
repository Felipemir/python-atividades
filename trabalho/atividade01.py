print("bem vindo a loja de Robson Felipe Da Silva Miranda")

valorDoPedido = float(input("Digite o valor do pedido: R$ "))
valorQuantidadeParcelas = int(input("Digite a quantidade de parcelas: "))
valorTotalParcelado = 0
valorParcelas = 0

if(valorQuantidadeParcelas < 4 ):
    valorParcelas = valorDoPedido / valorQuantidadeParcelas
    valorTotalParcelado = valorDoPedido
    print(f"O valor das parcelas é de: R$ {valorParcelas:.2f} e o valor total do pedido é de: R$ {valorTotalParcelado:.2f}")
    
elif(valorQuantidadeParcelas >= 4  and valorQuantidadeParcelas < 6 ) :
    valorParcelas = valorDoPedido * (1 + 0.4) / valorQuantidadeParcelas
    valorTotalParcelado = valorDoPedido * (1 + 0.4)
    print(f"O valor das parcelas é de: R$ {valorParcelas:.2f} e o valor total do pedido é de: R$ {valorTotalParcelado:.2f}")
    
elif(valorQuantidadeParcelas >= 6 and valorQuantidadeParcelas < 9):
    valorParcelas = valorDoPedido * (1 + 0.8) / valorQuantidadeParcelas
    valorTotalParcelado = valorDoPedido * (1 + 0.8)
    print(f"O valor das parcelas é de: R$ {valorParcelas:.2f} e o valor total do pedido é de: R$ {valorTotalParcelado:.2f}")
    
elif(valorQuantidadeParcelas >= 9 and valorQuantidadeParcelas < 13) :
    valorParcelas = valorDoPedido * (1 + 0.16) / valorQuantidadeParcelas
    valorTotalParcelado = valorDoPedido * (1 + 0.16)
    print(f"O valor das parcelas é de: R$ {valorParcelas:.2f} e o valor total do pedido é de: R$ {valorTotalParcelado:.2f}")
    
else:
    valorParcelas = valorDoPedido * (1 + 0.32) / valorQuantidadeParcelas
    valorTotalParcelado = valorDoPedido * (1 + 0.32)
    print(f"O valor das parcelas é de: R$ {valorParcelas:.2f} e o valor total do pedido é de: R$ {valorTotalParcelado:.2f}")   

