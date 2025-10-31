import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class livro:
    nome: str
    autor: str
    categoria: str
    preco: str

lista_livros = []
QUANTIDADE_LIVROS = 3


for i in range(QUANTIDADE_LIVROS):
    os.system("cls")
    livros = livro(nome=input("Digite o nome: "),
                autor=input("Digite o autor: "),
                categoria=input("Digite a categoria: "),
                preco=input("Digite o preço: "))
    lista_livros.append(livros)
    
print()
print("Salvando os dados. ")
arquivo = "catalogo_livros.txt"

with open(arquivo, "a") as arquivo_livro: 
    for livros in lista_livros:
        arquivo_livro.write(f"\nnome do livro: {livros.nome} \nAutor: {livros.autor} \nCategoria: {livros.categoria} \nPreco: {livros.preco}")
    print("Salvo com sucesso!!!")