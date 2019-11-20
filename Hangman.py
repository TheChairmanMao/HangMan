import random
import turtle
import math
import time

word_list = [
    "Abate", "Abstract", "Abysmal", "Accordingly", "Acquisition", "Adapt", "Adept", "Adequate", "Advent", \
    "Adversarial", "Advocate", "Aesthetic", "Afford", "Agitate", "Allow", "Allude", "Altercation", "Ambiguous", \
    "Ambitious", "Ambivalence", "Analogous", "Annihilate", "Anomaly", "Anticipate", "Antipathy", "Apex", \
    "Apprehension", "Articulate", "Artificial", "Assertion", "Austere", "Authenticity", "Avenue", "Avid"
]
secret = random.choice(word_list).lower()
print(f"The secret word is {secret}")

turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(1600, 800)
screen.bgcolor("black")

t = turtle.getturtle()
t.shape("turtle")
t.color(138, 3, 3)
t.width(5)
t.speed(0)
t.penup()
t.color("blue")
t.speed(0)
t.hideturtle()

myLoc = (0,0)

wrong = []

correct = []

topfont = 70
top = turtle.Turtle()
top.shape("turtle")
top.width(5)
top.speed(0)
top.penup()
top.color("blue")
top.speed(0)
top.goto( -750, -350)
top.setheading(0)
top.hideturtle()

bottem = turtle.Turtle()
bottem.shape("turtle")
bottem.width(5)
bottem.penup()
bottem.color('yellow')
bottem.speed(0)
bottem.goto(-700, -300)
bottem.hideturtle()

def turtles():
    jerry = turtle.Turtle()
    jerry.shape("turtle")
    jerry.color(138, 3, 3)
    jerry.width(5)
    jerry.penup()
    jerry.color("red")
    jerry.speed(0)
    jerry.goto(600, 40)

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color(138, 3, 3)
    bob.width(5)
    bob.penup()
    bob.color("orange")
    bob.speed(0)
    bob.goto(600, 60)

    sam = turtle.Turtle()
    sam.shape("turtle")
    sam.width(5)
    sam.penup()
    sam.color("green")
    sam.speed(0)
    sam.goto(600,80)

    bryan = turtle.Turtle()
    bryan.shape("turtle")
    bryan.width(5)
    bryan.penup()
    bryan.color("purple")
    bryan.speed(0)
    bryan.goto(600, 100)

    larry = turtle.Turtle()
    larry.shape("turtle")
    larry.width(5)
    larry.penup()
    larry.color("white")
    larry.speed(0)
    larry.goto(600, 120)

    mike = turtle.Turtle()
    mike.shape("turtle")
    mike.width(5)
    mike.penup()
    mike.color("brown")
    mike.speed(0)
    mike.goto(600, 140)

    robert = turtle.Turtle()
    robert.shape("turtle")
    robert.width(5)
    robert.penup()
    robert.color("gray")
    robert.speed(0)
    robert.goto(600, 160)

    john = turtle.Turtle()
    john.shape("turtle")
    john.width(5)
    john.penup()
    john.color("pink")
    john.speed(0)
    john.goto(600, 180)

    greg = turtle.Turtle()
    greg.shape("turtle")
    greg.width(5)
    greg.penup()
    greg.color("aquamarine")
    greg.speed(0)
    greg.goto(600, 200)

    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.width(5)
    chris.penup()
    chris.color("magenta")
    chris.speed(0)
    chris.goto(600, 220)

    richard = turtle.Turtle()
    richard.shape("turtle")
    richard.width(5)
    richard.penup()
    richard.color("maroon")
    richard.speed(0)
    richard.goto(600, 240)

turtles()

def gallows():
    t.forward(250)
    t.right(90)
    t.forward(300)
    t.left(90)

    t.pendown()
    t.forward(450)
    t.backward(225)
    t.left(90)
    t.forward(650)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(100)

def head():
    t.right(90)
    t.circle(48)

def body():
    t.left(90)
    t.penup()
    t.forward(96)
    t.pendown()
    t.forward(200)

def leftarm():
    t.pendown()
    t.backward(170)
    t.right(50)
    t.forward(100)

def rightarm():
    t.backward(100)
    t.left(100)
    t.forward(100)

def rightleg():
    t.backward(100)
    t.right(50)
    t.forward(170)
    t.left(30)
    t.forward(130)

def leftleg():
    t.backward(130)
    t.left(300)
    t.forward(130)

def eyeone():
    global myLoc
    t.backward(130)
    t.left(30)
    t.backward(200)
    t.right(180)
    myLoc = t.position()
    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.left(45)
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.backward(20)

def eyetwo():
    t.penup()
    t.goto(myLoc)
    t.left(45)
    t.forward(50)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.left(45)
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.backward(20)

def mouth():
    t.penup()
    t.goto(myLoc)
    t.left(45)
    t.left(90)
    t.forward(30)
    t.pendown()
    t.right(90)
    for i in range(5):
        t.forward(5)
        t.right(15)
    t.penup()
    t.goto(myLoc)
    t.left(45)
    t.left(90)
    t.forward(30)
    t.pendown()
    t.left(90)
    for i in range(7):
        t.forward(5)
        t.left(15)

def rightfoot():
    t.penup()
    t.goto(myLoc)
    t.setheading(0)
    t.left(90)
    t.backward(200)
    t.left(180)
    t.left(30)
    t.forward(130)
    t.left(80)
    t.pendown()
    t.forward(20)
    for i in range(7):
        t.forward(4)
        t.right(15)
    t.left(10)
    t.forward(15)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(25)

def leftfoot():
    t.penup()
    t.goto(myLoc)
    t.right(15)
    t.backward(200)
    t.right(180)
    t.right(30)
    t.forward(130)
    t.right(80)
    t.pendown()
    t.forward(20)
    for i in range(7):
        t.forward(4)
        t.left(15)
    t.right(10)
    t.forward(15)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(25)

def nose():
    t.penup()
    t.goto(myLoc)
    t.setheading(0)
    t.left(90)
    t.forward(50)
    t.pendown()
    t.right(100)
    t.forward(15)
    t.right(140)
    t.forward(15)
    t.penup()
    t.goto(myLoc)

def hair():
    t.setheading(0)
    t.left(90)
    t.forward(100)
    t.pendown()
    t.left(20)
    t.forward(25)
    t.backward(25)
    t.right(70)
    t.forward(25)
    t.backward(25)
    t.left(23)
    t.forward(25)
    t.backward(25)
    t.hideturtle()

wronggusses = 0
MAX = 13
screenWord = ""

def updateDrawing():
    if wronggusses == 0:
        gallows()
    if wronggusses == 1:
        head()
    if wronggusses == 2:
        body()
    if wronggusses == 3:
        leftarm()
    if wronggusses == 4:
        rightarm()
    if wronggusses == 5:
        rightleg()
    if wronggusses == 6:
        leftleg()
    if wronggusses == 7:
        eyeone()
    if wronggusses == 8:
        eyetwo()
    if wronggusses == 9:
        mouth()
    if wronggusses == 10:
        rightfoot()
    if wronggusses == 11:
        leftfoot()
    if wronggusses == 12:
        nose()
    if wronggusses == 13:
        hair()

def drawWords():
    global screenWord
    bottem.clear()
    bottem.penup()
    bottem.goto(-700, -200)
    bottem.setheading(0)
    bottem.pendown()
    screenWord = ""
    for letter in secret:
        if letter in correct:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "
    bottem.write(screenWord, align="left", font=("Arial", 70, "normal"))
    bottem.penup()
    bottem.setheading
    bottem.pendown()

gameOn = True

def drawWrong():
    top.clear()
    letterString = "Wrong Letters: "
    for l in wrong:
        letterString +=l + ", "
    letterString = letterString[0:-2]
    top.write(letterString, move=False, align="left", font=("Arial", 40, "normal"))

def writeError(msg):
    top.clear()
    top.write(msg, move=False, align="left", font=("Arial", 40, "normal"))
    time.sleep(2)
    top.clear()

def winLose(win):
    top.clear()
    if win:
        top.write("You Win!", move = False, align = "left", font = ("Arial", topfont, "normal"))
    else:
        top.write("You are trash!", move = False, align = "left", font = ("Arial", topfont, "normal"))

def getWordGuess():
    getWordGuess = screen.textinput("Guess it", "Enter your word")
    if getWordGuess.lower() == secret:
        winLose(True)
        return True
    else:
        winLose(False)
        time.sleep(1)
        writeError(f"The word is {secret}.")
        return False
def getGuess():
    badLetter = ""
    for letter in wrong:
        badLetter += letter + ", "
    boxTitle = "Letters Used:" + badLetter
    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word.")
    return theGuess

updateDrawing()
while gameOn:
    drawWords()
    guess = getGuess()
    guess = str(guess)
    if wronggusses >= MAX:
        writeError("No More Guesses. You Suck")
        gameOn = False
        writeError(f"The word is {secret}.")
    else:
        if "_" not in screenWord:
            writeError("You Win. Now Leave.")
            gameOn = False
            break
        else:
            drawWords()
            guess = getGuess()
            guess = str(guess)
            if guess == "$$":
                gameOn = getWordGuess()
            elif len(guess) !=1:
                writeError("I need a single letter. Guess Again.")
                drawWrong()
            elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
                writeError("Not a letter. Try Again.")
                drawWrong()

            else:
                if guess.lower() in secret.lower():
                    correct.append(guess.lower())
                    drawWords()
                else:
                    if guess.lower() not in wrong:
                        wrong.append(guess.lower())
                        wronggusses +=1
                        drawWrong()
                        updateDrawing()
                    else:
                        writeError("Please enter a different letter")
                        draw
