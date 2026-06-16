# Abrir o arquivo de dados
arquivo_pacientes = open (
    file="projectsenac/pacientes.csv",
    mode="r",
    encoding="utf-8"
)


# Carregar o conteúdo do arquivo (levar para a memoria)


registros = arquivo_pacientes.readlines() # carregar tudo de uma vez só e devolver uma lista de linhas do arquivo


# Fechar arquivo 
arquivo_pacientes.close()

idade_requisitada = int(input("Idade: "))
# Fazer o parsing de cada uma das linhas 

# pegamos linha por linha (registro)
for registro in registros:
    # "João Silva,28,Rua das Flores 123 - São Paulo,11987654321,Maria Silva"
    valores = registro.strip().split(",")
    nome = valores[0]
    idade = valores[1]  
    telefone = valores[3]

    # filtrar por idade
    if(idade == (idade_requisitada)):
        print(f"Nome: {nome}, Idade: {idade}, Telefone: {telefone}",sep="\n")
        print("---")
# "João Silva,28,Rua das Flores 123 - São Paulo,11987654321,Maria Silva"

# pegamos uma linha da lista de registros e fazemos o split dela usando a vírgula como separador
registro = registros[0] # pegar a primeira linha da lista de registros
# exemplo de linha: "João Silva,28,Rua das Flores 123 - São Paulo,11987654321,Maria Silva"





# "quebrar" cada linha nos campos corretos (nome,idade,endereço,telefone,nome_responsável)
# nome = "João Silva"
# idade = "28"   
# endereço = "Rua das Flores 123 - São Paulo"
# telefone = "(11) 9876-54321"

# listar os pacientes