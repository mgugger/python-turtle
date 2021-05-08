import turtle
import random

t = turtle.Turtle()
t.speed("fastest")

# Der Screen ist der Hintergrund, fuer welchen wir eine bestimmte Farbe setzen
screen = turtle.Screen()
screen.bgcolor("darkblue")

# [] definiert eine Liste mit Farben, welche in der Variable colors abgespeichert werden
colors = ["white", "lightblue", "lightgrey"]

# Teilaufgabe 1
def schneeflocke_spitze(s):
  """
  Zeichnet den aeussersten Teil einer Schneeflocke
  s = Groesse
  """

# Teilaufgabe 2
def schneeflocke_ast(s):
  """ 
  Zeichnet den Ast einer Schneeflocke bestehend aus 4 Spitzen (schneeflocke_spitze())
  s = Groesse
  """
  for i in range(4):
    schneeflocke_spitze(s)

def schneeflocke(s):
  """
  Die Methode schneeflocke(s) zeichnet eine Schneeflocke mit Groesse s, bestehend aus 8 Aesten.
  """
  for i in range(8):
    schneeflocke_ast(s)
    t.left(45)

# Teilaufabe 3
def stern(s):
  """ 
  Die Methode stern(s) zeichnet einen Stern mit Groesse s.
  Vervollstaendigen sie den Code mittels Turtle.
  """

  # Gezeichnete Figuren werden mittels den nachfolgenden Zeilen mit einer Farbe ausgefuellt
  t.fillcolor("yellow")
  t.begin_fill()
    
  # Ergaenzen Sie ihren Code hier

  # Ende des eigenen Codes
  
  # Gezeichnete Figuren werden mittels der nachfolgenden Zeile nicht mehr ausgefuellt.
  t.end_fill()

def set_pen_to_random_position():
  """
  Die Methode setzt den Stift auf eine zufaellige Position.
  """
  # random.randint(min,max) waehlt eine zuefallige Zahl zwischen dem Wert min und dem Wert max aus.
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  
  t.penup()
  # Setzen der Turtle auf die zuefaellige Position.
  t.setpos(x,y)
  t.pendown()

def set_pen_to_random_color():
  # random.choice([]) waehlt ein zufaelliges Element aus einer Liste aus.
  color = random.choice(colors)
  # setze die Farbe des Stifts auf die zuefaellig gewaehlte Farbe
  t.pencolor(color)

# Hauptteil
for i in range(5):
  set_pen_to_random_color()
  set_pen_to_random_position()  
  schneeflocke(10)
  set_pen_to_random_position()
  stern(30)