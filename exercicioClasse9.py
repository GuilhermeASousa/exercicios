class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto ({self.x}, {self.y})')


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    print("O centro do retângulo é:")
    centro.imprimir()


def main():
    ponto_inicial = Ponto(1, 1)
    retangulo = Retangulo(ponto_inicial, 4, 3)

    while True:
        print("\nMenu:")
        print("1. Imprimir centro do retângulo")
        print("2. Alterar valores do retângulo")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            imprimir_centro(retangulo)
        elif escolha == "2":
            novo_x = float(input("Novo valor de x para o ponto inicial: "))
            novo_y = float(input("Novo valor de y para o ponto inicial: "))
            nova_largura = float(input("Nova largura do retângulo: "))
            nova_altura = float(input("Nova altura do retângulo: "))
            ponto_inicial = Ponto(novo_x, novo_y)
            retangulo = Retangulo(ponto_inicial, nova_largura, nova_altura)
            print("Valores do retângulo alterados com sucesso.")
        elif escolha == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()