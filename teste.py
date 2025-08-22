#função para pedir o nome

def obter_nome():
    while True:
        nome = input("Digite seu nome").strip()
        if nome:
            return nome 
        else:
            print("Nome não pode estar vazio. Tente novamente.")

#função para pedir idade
def obter_idade():
    while True:
        idade_str = input("Digite sua idade: ")
        if idade_str.isdigit():
            return int(idade_str)
        else:
            print("Por favor, digite uma idade válida ( apenas números).")

#função para verificar maioridade
def verificar_maioridade(idade):
    return idade >= 18

# programa principal
nome = obter_nome
idade = obter_idade

#verificar maioridade
if verificar_maioridade(idade):
    print(f"\n olá, {nome}! você tem {idade} anos e é maior de idade.")
else:
    print(f"\n olá, {nome}! você tem {idade} anos e é menor de idade.")

