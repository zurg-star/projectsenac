# trabalho com a lista compras_online.csv...

arquivo_de_clientes = open (
    file= "inclass/compras_online.csv", 
    mode= "r",
    encoding= "utf-8"
)

registro_de_clientes = arquivo_de_clientes.readlines()
arquivo_de_clientes.close()
pesquisar = input("O que você Procura?: ")

for i in registro_de_clientes:
    valor = i.strip().split(",")
    nome= valor[0]
    idade= valor[1]
    endereço= valor[2]
    telefone= valor[3]
    comprou= valor[4]    

    if (valor in (pesquisar)):
        print(valor)