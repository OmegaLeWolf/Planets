import os
from time import sleep

import DatasavingSQL
import animacoes
import graphical


class SistemaPlanetario:
    dicio_sistema = {
        "poeira interestrelar": "Poeira interestrelar, é uma poeira que existe no espaço ou caiu no planeta terra.",
        "satélites Naturais": "Um satélite natural é um corpo astronómico que orbita um planeta ou corpo pequeno de um sistema solar. Satélites naturais são mais popularmente referidos como luas, uma derivação da lua da terra.",
        "asteróides": "Os asteroides são corpos rochosos de estrutura metálica que orbitam em torno do sol como os planetas, mas que possuem uma massa muito pequena em comparação a eles.",
        "planeta": "Um planeta é um corpo celeste que orbita uma estrela ou um remanescente de estrela, com massa suficiente para se tornar esférico pela sua própria gravidade, mas não ao ponto de causar fusão termonuclear, e que tenha limpado de planetesimais a sua região vizinha (dominância orbital).",
        "meteoro": "Meteoro, chamado popularmente de estrela cadente ou estrela fugaz, designa o fenómeno luminoso observado quando da passagem de um meteoroide pela atmosfera terrestre.",
        "cometa": "Um cometa é um pequeno corpo gelado do Sistema Solar que, ao passar perto do Sol, aquece e começa a liberar gases, processo que é chamado de desgaseificação. Isso produz uma atmosfera visível ou coma e, às vezes, também uma cauda"
    }


class SistemaSolar(SistemaPlanetario):
    # https://stackoverflow.com/questions/53347379/how-to-use-input-as-a-name-for-object-in-python
    def __init__(self, prox, exist, quant, alt):
        self.proximidade_do_sol = prox
        self.existencia_de_vida = exist
        self.quantidade_de_agua = quant
        self.ponto_mais_alto = alt

    def planetInfo(self):
        print("Proximidade do sol: ", self.proximidade_do_sol)
        print("Existência de vida: ", self.existencia_de_vida)
        print("Quantidade de água: ", self.quantidade_de_agua)
        print("Ponto mais alto: ", self.ponto_mais_alto)
        return ""

    def planetInfoVar(self):
        return self.proximidade_do_sol, self.existencia_de_vida, self.quantidade_de_agua, self.ponto_mais_alto

    planetas = [
        "Mercúrio",
        "Vénus",
        "Terra",
        "Marte",
        "Júpiter",
        "Saturno",
        "Urano",
        "Neptuno"
    ]


class Planeta(SistemaSolar):
    proximidade_do_sol = float
    existencia_de_vida = bool
    quantidade_de_agua = float
    ponto_mais_alto = str

    def earthInfoVar(self):
        return self.proximidade_do_sol, self.existencia_de_vida, self.quantidade_de_agua, self.ponto_mais_alto

    def vetorEarth(self):
        op = ["Nome: Terra", "Proximidade do sol: ", "Existência de vida: ", "Quantidade de água: ",
              "Ponto mais alto: "]
        vet = [0] * 4
        for i in range(len(vet)):
            vet[i] = terra.earthInfoVar()[i]

        print(op[0])
        for i in range(len(vet)):
            print(op[i + 1], vet[i])




terra = Planeta(3, True, 70.5, "Monte Everest")

planets = {}


def adicionarPlaneta():
    # https://stackoverflow.com/questions/53347379/how-to-use-input-as-a-name-for-object-in-python
    name = input("Qual o nome do planeta que quer adicionar?\n")
    prox = input("Qual a distância em km do sol?\n")
    exist = input("Existe vida no seu planeta?(V/F)\n")
    quant = input("Quanta água tem o seu planeta?\n")
    alt = input("Qual o nome do ponto mais alto do seu planeta?\n")
    planets[name] = SistemaSolar(prox, exist, quant, alt)


def removerPlaneta():
    DatasavingSQL.showTables()
    id = int(input("\nInsira o ID do planeta que deseja remover.\n"))
    DatasavingSQL.deleteData(id)



def verPlanetas():
    DatasavingSQL.showTables()


def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def viagemPsiuno():
    clearScreen()

    msg = "A iniciar a sua viagem...."
    time = 0.1
    for i in msg:
        print(i, end='')
        sleep(time)
        if i == ".":
            time = 1

    clearScreen()

    i = 0
    while i != 5:
        clearScreen()

        print(animacoes.ani)
        sleep(2)

        clearScreen()

        print(animacoes.ani2)
        sleep(2)

        i += 1

    msg = "3 2 1 ... Descolagem!"
    time = 1
    for i in msg:
        print(i, end='')
        sleep(time)
        if i == ".":
            time = 0.1

    sleep(5)
    clearScreen()

    animacoes.anims()






# print("Nome: ", list(planets.keys())[0])
# print(planets[list(planets.keys())[0]].planetInfo())

while 1:

    print("\n[1] Dicionário\n"
          "[2] Lista de planetas\n"
          "[3] Informação sobre a terra\n"
          "[4] Adicionar planeta à Base de Dados\n"
          "[5] Remover planeta da Base de Dados\n"
          "[6] Ver Base de Dados dos planetas\n"
          "[7] Inicar viagem a Psiuno\n"
          "[8] Ver sistema solar\n"
          "[9] Sair\n")

    menu = int(input("Insira a opção desejada:\n"))

    if menu == 1:
        for i in range(len(terra.dicio_sistema.keys())):
            print(list(terra.dicio_sistema.keys())[i])

        while 1:
            men1 = input("Selecione um termo para verificar o seu significado:\n")
            try:
                print(terra.dicio_sistema[men1.lower()])
                break
            except KeyError:
                print("Opção inválida!")

    elif menu == 2:
        print("Os planetas conhecidos no sistema solar são:\n")  # b)
        for i in range(len(terra.planetas)):
            print(terra.planetas[i])

#terra = Planeta(3, True, 70.5, "Monte Everest")

    elif menu == 3:
        terra.vetorEarth()


    elif menu == 4:
        adicionarPlaneta()

    elif menu == 5:
        removerPlaneta()

    elif menu == 6:
        verPlanetas()

    elif menu == 7:
        viagemPsiuno()
        graphical.psiuno()

    elif menu == 8:
        graphical.solarSystem()

    elif menu == 9:
        exit()

    else:
        print("Valor introduzido inválido")
        continue

    # Automatic update to database of all values
    dat = []

for i in range(len(planets.keys())):
    dat = planets[list(planets.keys())[i]].planetInfoVar()
    name = list(planets.keys())[i]
    DatasavingSQL.saveSQLData(name, dat)
