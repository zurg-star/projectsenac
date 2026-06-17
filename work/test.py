arquivo_de_clientes = open (
    file= "projectsenac/work/compras_online.csv", 
    mode= "r",
    encoding= "utf-8"
)

registro_de_clientes = arquivo_de_clientes.readlines()
arquivo_de_clientes.close()


print("1. Nome")
print("2. Idade")
print("3. Endereço")
print("4. Telefone")
print("5. O que o Cliente comprou")
pesquisar = int(input("O que você Procura?:"))   



for i in registro_de_clientes:
    valor = i.strip().split(",")
    nome= valor[0]
    idade= valor[1]
    endereço= valor[2]
    telefone= valor[3]
    comprou= valor[4]    
    
    if pesquisar == 1:
        print(nome)
        print(f"N° de nomes clientes{len(nome)}")
    elif pesquisar == 2:
        print(idade)
        print(f"N° de idades clientes{len(idade)}")
    elif pesquisar == 3:
        print(endereço)
        print(f"N° de endereços clientes{len(endereço)}")
    elif pesquisar == 4:
        print(telefone)
        print(f"N° de telefones clientes{len(telefone)}")
    elif pesquisar == 5:
        print(comprou)
        print(f"N° de compras de clientes{len(comprou)}")
    else:
        print("error")
