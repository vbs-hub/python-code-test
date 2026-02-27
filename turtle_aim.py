from turtle import *
from random import randint
from time import sleep

t = Turtle()
t.color('red')
t.shape('circle')
t.speed(0)
t.shapesize(2, 2, 10) #менять размер черепашки
t.penup()

text = Turtle()
text.hideturtle()  # Прячем саму черепашку
text.penup()
text.speed(0)
text.color('white')


aim_click = 0
miss = 0

def update_text():
    global aim_click, miss
    text.clear()  # Очищаем старый текст
    
    # Пишем попадания
    text.goto(0, 300)
    text.color('blue')
    text.write(f'Попаданий: {aim_click}', align="center", font=("Arial", 16, "bold"))
    text.penup()
    
    # Пишем промахи
    text.goto(0, 270)
    text.color('red')
    text.write(f'Промахов: {miss}', align="center", font=("Arial", 16, "bold"))

def turtle_click(x, y):
    global aim_click, miss
    miss -= 1
    aim_click += 1 
    print(f'Ты попал! Счет: {aim_click}')
    
    t.color('red')
    t.goto(randint(-200, 200), randint(-200, 200))
    update_text()
def turtle_miss(x, y):
    global miss, aim_click
    miss += 1
    print(f'Ты ?! Счет: {miss}')

    t.color('red')
    t.goto(randint(-200, 200), randint(-200, 200))
    update_text()



scr = t.getscreen()
scr.title('Тренировка аима')
scr.bgcolor('black') #менять цвет задних обой
scr.onclick(turtle_miss)
t.onclick(turtle_click)
update_text()

done()
