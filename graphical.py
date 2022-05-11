import turtle
import time
from math import *
import random
import DatasavingSQL
import os


def solarSystem():

    win = turtle.Screen()
    win.setup(1300, 1100)
    win.bgcolor('black')
    win.tracer(0)

    sun = turtle.Turtle()
    sun.shape('circle')
    sun.shapesize(5, 5)
    sun.color('yellow')


    class Planet(turtle.Turtle):
        def __init__(self, radius, color, size, star, offset):
            super().__init__(shape='circle')
            self.radius = radius
            self.c = color
            self.color(self.c)
            self.size = size
            self.shapesize(size, size)
            # self.up()
            self.angle = 0
            self.star = star
            self.offset = offset

        def getName(self):
            return self

        def move(self):
            x = self.offset + self.radius * cos(self.angle)  # Angle in radians
            y = self.radius * sin(self.angle) * 0.3

            self.goto(self.star.xcor() + x, self.star.ycor() + y)

    earth = Planet(300, 'blue', 1, sun, 100)
    mercury = Planet(110, 'grey', 0.6, sun, 0)
    venus = Planet(180, 'orange', 0.8, sun, 50)
    mars = Planet(400, 'red', 0.9, sun, 100)
    jupiter = Planet(800, 'brown', 2, sun, 150)
    saturn = Planet(900, '#753304', 1.8, sun, 100)
    uranus = Planet(1000, 'light blue', 1.2, sun, 100)
    neptune = Planet(1100, 'blue', 1, sun, 100)

    moon = Planet(40, 'grey', 0.2, earth, 0)  # Moon a 'planet' that revolves around earth
    phobos = Planet(40, 'grey', 0.2, mars, 0)
    deimos = Planet(35, 'white', 0.2, mars, 0)



    myList = [mercury, venus, earth, moon, mars, phobos, deimos, jupiter, saturn, uranus, neptune]

    id = DatasavingSQL.returnMaxID()
    if id > 8:
        dic = {}
        list = []
        list = DatasavingSQL.getPlanets(list)
        for i in range(len(list)):
            dic[list[i][1]] = Planet(random.randint(100, 1000),
                                     random.choice(['blue', 'grey', 'orange', 'red']),
                                     random.randint(1, 3),
                                     sun, 100)
            myList.append(dic[list[i][1]])



    else:
        return False


    for i in myList:
        i.penup()
        i.goto(i.radius + i.offset, 0)
        if i.star == sun:
            i.pendown()

    asteroid_list = []
    angle = 0.001

    for i in range(500):
        asteroid = Planet(random.randint(540, 580), 'grey', 0.1, sun, 10)
        asteroid.penup()
        asteroid_list.append(asteroid)
        asteroid.angle += angle
        angle += 0.012421

    while True:
        win.update()
        for i in myList:
            i.move()

        # Increase the angle by 0.0x radians (further away - smaller angle change)
        moon.angle += 0.06
        phobos.angle += 0.06
        deimos.angle += 0.08

        mercury.angle += 0.05
        venus.angle += 0.03
        earth.angle += 0.01
        mars.angle += 0.007
        jupiter.angle += 0.007
        saturn.angle += 0.009
        uranus.angle += 0.008
        neptune.angle += 0.009

        for i in range(len(dic)):
            dic[list[i][1]].angle += 0.11

        for i in asteroid_list:
            i.move()
            i.angle += 0.002

        time.sleep(0.01)

        #turtle.done()


def psiuno():
    win = turtle.Screen()
    win.setup(1300, 1100)
    win.bgcolor('black')
    win.register_shape('New Project (3).gif')

    psiuno = turtle.Turtle()
    psiuno.shape('New Project (3).gif')

    t = turtle.textinput("", "Acabou de encontrar um novo planeta! Quer seguir em frente?(s/n)")
    if t.lower() == "s":
        turtle.bye()
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        time.sleep(2)

        for i in ("Ao entrar na atmosfera do planeta deparou-se com a presença de oxigénio em quantidades muito maiores à terra...\n"):
            time.sleep(0.1)
            print(i, end='')

        for i in "...\n":
            time.sleep(0.5)
            print(i, end='')

        for i in ("Quando aterrou no planeta, encontrou um ser aparente a um humano, mas mais pré-histórico."):
            time.sleep(0.1)
            print(i, end='')
        time.sleep(0.1)

        for i in ("Este ser chama-se de 'Rafael' e aparenta falar um idioma parecido ao português.\n\n"):
            time.sleep(0.1)
            print(i, end='')
        time.sleep(0.1)

        for i in "...\n":
            time.sleep(0.5)
            print(i, end='')

        choice = input("\n\nQual o seu nome?")

        print("Cé un nome bon(i)to, ", choice)
        print("\n...\n")
        print("O Rafael diz-te que o nome do planeta é 'Psiuno' e tem as seguintes características:\n"
              "Proximidade ao sol: 1002858322\n"
              "Existência de vida no planeta: V\n"
              "Quantidade de água: 60%\n"
              "Ponto mais alto: 'Mounta Evrst'\n")
        time.sleep(2)
        while 1:
            db = input("Deseja adicionar este planeta na base de dados? (s/n)")
            if db.lower() == "s":
                DatasavingSQL.saveSQLData("Psiuno", (1002858322, "T", 60, "Mounta Evrst"))
                break
            elif db.lower() == "n":
                break
            else:
                print("Valor introduzido inválido.")
        print("\nAgora é hora de ir embora. Adeus Rafael!")
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    else:
        turtle.bye()
        return False





