import turtle


# Classe base para todas as figuras

class Figura:
    def __init__(self, cor, tamanho, posicao):
        self.cor = cor
        self.tamanho = tamanho
        self.posicao = posicao

    def desenhar(self):
        pass

    def mover_para_posicao(self):
        turtle.penup()
        turtle.goto(self.posicao)
        turtle.pendown()
        turtle.color(self.cor)



# Subclasses das formas

class Quadrado(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(4):
            turtle.forward(self.tamanho)
            turtle.right(90)

class Triangulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(3):
            turtle.forward(self.tamanho)
            turtle.right(120)

class Circulo(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        turtle.circle(self.tamanho)

class Hexagono(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(6):
            turtle.forward(self.tamanho)
            turtle.right(60)

class Estrela(Figura):
    def desenhar(self):
        self.mover_para_posicao()
        for _ in range(5):
            turtle.forward(self.tamanho)
            turtle.right(144)  # Ângulo para formar a estrela



# Função do menu

def menu():
    print("\nEscolha uma forma para desenhar:")
    print("1 - Quadrado")
    print("2 - Triângulo")
    print("3 - Círculo")
    print("4 - Hexágono")
    print("5 - Estrela")
    print("0 - Sair")
    return input("Opção: ")


# Programa principal

turtle.speed(5)

while True:
    opcao = menu()

    if opcao == "0":
        break

    cor = input("Digite a cor: ")
    tamanho = int(input("Digite o tamanho: "))
    x = int(input("Posição X: "))
    y = int(input("Posição Y: "))

    if opcao == "1":
        forma = Quadrado(cor, tamanho, (x, y))
    elif opcao == "2":
        forma = Triangulo(cor, tamanho, (x, y))
    elif opcao == "3":
        forma = Circulo(cor, tamanho, (x, y))
    elif opcao == "4":
        forma = Hexagono(cor, tamanho, (x, y))
    elif opcao == "5":
        forma = Estrela(cor, tamanho, (x, y))
    else:
        print("Opção inválida!")
        continue

    forma.desenhar()

turtle.done()
