arquivo_pacientes = open("pacientes.csv","r",encoding="utf-8")

# primeiro descartamos o cabeçalho (1a linha)
arquivo_pacientes.readline()

# ler um registro do arquivo (até o final do arquivo_pacientes)
registros = arquivo_pacientes.readlines()
# ler uma linha
for um_registro in registros:
    # "quebrar" a linha nos campos corretos (nome,idade,endereço,telefone,nome_responsável)
    dados_do_registro = um_registro.strip().split(",")

    # guardar cada dado em uma variável
    nome, idade, endereco, telefone, nome_responsavel = dados_do_registro

    # imprimir as variáveis formatadas como registro:
    print(f"Paciente: {nome}", f"- {idade} anos")
    print(f"Fone: {telefone}",f"End.: {endereco}")
    print(f"Responsável: {nome_responsavel}")
    print()

arquivo_pacientes.close()