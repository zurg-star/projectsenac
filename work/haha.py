# Arquivo de clientes de e-comerce..


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
pesquisar = input("O que você Procura?:")   



for i in registro_de_clientes:
    valor = i.strip().split(",")
    nome= valor[0]
    idade= valor[1]
    endereço= valor[2]
    telefone= valor[3]
    comprou= valor[4]    
    

    if pesquisar == "nome":
        print(valor[0])
    if pesquisar == "idade":
        print(valor[1])
    if pesquisar == "endereço":
        print(valor[2])
    if pesquisar == "telefone":
        print(valor[3])
    if pesquisar == "O que o Cliente comprou":
        print(valor[4])






print(f"Nº de {pesquisar} - {len(registro_de_clientes)}")