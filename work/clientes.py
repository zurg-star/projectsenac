# Arquivo de clientes de e-comerce..


arquivo_de_clientes = open (
    file= "projectsenac/work/compras_online.csv", 
    mode= "r",
    encoding= "utf-8"
)

registro_de_clientes = arquivo_de_clientes.readlines()
arquivo_de_clientes.close()


print("1. Cliente: *digite*")
print("     - Nome")
print("     - Idade")
print("     - Endereço")
print("     - Telefone")
print("     - O que o Cliente comprou")
print("2. Registro de Clientes")
pesquisar = input("O que você Procura?:")   



for i in registro_de_clientes:
    valor = i.strip().split(",")
    nome= valor[0]
    idade= valor[1]
    endereço= valor[2]
    telefone= valor[3]
    comprou= valor[4]    
    

    if pesquisar == "nome":
        print(f"['{valor[0]}']")
    if pesquisar == "idade":
        print(f"['{valor[0]}'] tem {valor[1]} anos")
    if pesquisar == "endereço":
        print(f"['{valor[0]}'] mora na [{valor[2]}]")
    if pesquisar == "telefone":
        print(f"['{valor[0]}'] - [{valor[3]}]")
    if pesquisar == "O que o Cliente comprou":
        print(f"['{valor[0]}'] comprou ['{valor[4]}']")
    if pesquisar == "2":
        print(registro_de_clientes)


print(f"Nº de clientes: {len(registro_de_clientes)}") 