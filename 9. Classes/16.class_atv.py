import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class livro:
    titulo: str
    ano: int
    autor: Autor

    def mostrar_dados(self):
        print(f"\ntítulo do livro: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"O autor: {self.autor.nome}")
        print(f"A biografia do autor: {self.autor.biografia}")
        



cliente = livro(titulo=input("Qual o nome do livro: "),
                ano=int(input("Qual ano foi publicado: ")),
                autor=Autor(nome=input("Qual o nome do autor: "),
                            biografia=input("Qual a biografia do autor: ")))


os.system("cls")
print("=== Mostrando dados ===")
cliente.mostrar_dados()
