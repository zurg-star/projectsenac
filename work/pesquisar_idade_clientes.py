pesquisar_idade = input("Digite uma Idade:")

arquivo_de_clientes = open (
    file= "projectsenac/work/compras_online.csv", 
    mode= "r",
    encoding= "utf-8"
)

registro_de_clientes = arquivo_de_clientes.readlines()

for i in registro_de_clientes:
    value = i.strip().split(",")
    

    nome, idade, endereco, telefone, comprou = value

    if (idade == pesquisar_idade):
        print(f"Cliente {nome}", f"- {idade} anos")
        print(f"    - Fone: {telefone}")
        print(f"    - Endereço: {endereco}")
        print(f"    - O que o Cliente comprou: {comprou}")


arquivo_de_clientes.close()
  



  
    