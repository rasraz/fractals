"""
برای اجرای برنامه نیار است برنامه های زیر نصب باشد:
- python
- numpy
- matplotlib
- turtle
- pillow
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import turtle
import random

def mandelbrot():
    "این تایع برای فرمول برخال است(با تغببر در این تابع میتوان به برخال جدید دست یافنت)"
    def mandelbrot_set(threshold,zx,zy,cx=0,cy=0):
        c=complex(zx,zy)
        z=complex(cx,cy)
        for i in range(threshold):
            z=z**2+c
            if abs(z)>4.:return i
        return threshold-1

    "این برای مقادیر اولیه width,height,x,y است"
    x_start, y_start=-2, -1.5
    width, height=3, 3
    "این مقدار مشخض کننده تعداد تکرار کلی برای رسیدن به شکل است(قابل تغیر)"
    density_per_unit=200
    "این دستورات برای رسم نمودار اولیه تابع است"
    re= np.linspace(x_start,x_start+width,width*density_per_unit)
    im= np.linspace(y_start,y_start+height,height*density_per_unit)
    fig= plt.figure(figsize=(10,10))
    ax=plt.axes()
    "این تابع برای رسم انیمیشن برخال است"
    def animate(i):
        ax.clear()
        ax.set_xticks([],[])
        ax.set_yticks([],[])
        X=np.empty((len(re),len(im)))
        threshold=round(1.15**(i+1)) # تعداد تکرار
        for i in range(len(re)):
            for j in range(len(im)):
                X[i,j]=mandelbrot_set(threshold,re[i],im[j])
        img=ax.imshow(X.T,interpolation='bicubic',cmap='magma')
        return [img]
    "این تابع برای اجرایی کردن دستورات انیمیشن و ذخیره آن به عنوان یک گیف است"
    anim=animation.FuncAnimation(fig,animate,frames=45,interval=120,blit=True)
    anim.save('mandelbrot.gif',writer='pillow')

def julia():
    "این تایع برای فرمول برخال است(با تغببر در این تابع میتوان به برخال جدید دست یافنت)"
    def julia_set(threshold,zx,zy,cx,cy):
        c=complex(cx,cy)
        z=complex(zx,zy)
        for i in range(threshold):
            z=z**2+c
            if abs(z)>4.:return i
        return threshold-1

    "این برای مقادیر اولیه width,height,x,y است"
    x_start, y_start=-2, -2
    width, height=4, 4
    "این مقدار مشخض کننده تعداد تکرار کلی برای رسیدن به شکل است(قابل تغیر)"
    density_per_unit=200
    "این دستورات برای رسم نمودار اولیه تابع است"
    re= np.linspace(x_start,x_start+width,width*density_per_unit)
    im= np.linspace(y_start,y_start+height,height*density_per_unit)
    "این مقدار مشخض کننده تعداد تکرار کلی برای رسیدن به شکل است(قابل تغیر)"
    threshold=20
    frames=100
    r=0.7885
    a=np.linspace(0,2*np.pi,frames)
    fig= plt.figure(figsize=(10,10))
    ax=plt.axes()
    "این تابع برای رسم انیمیشن برخال است"
    def animate(i):
        ax.clear()
        ax.set_xticks([],[])
        ax.set_yticks([],[])
        X=np.empty((len(re),len(im)))
        cx,cy=r*np.cos(a[i]),r*np.sin(a[i]) # باعث تغییر
        for i in range(len(re)):
            for j in range(len(im)):
                X[i,j]=julia_set(threshold,re[i],im[j],cx,cy)
        img=ax.imshow(X.T,interpolation='bicubic',cmap='magma')
        return [img]
    "این تابع برای اجرایی کردن دستورات انیمیشن و ذخیره آن به عنوان یک گیف است"
    anim=animation.FuncAnimation(fig,animate,frames=frames,interval=50,blit=True)
    anim.save('julia.gif',writer='pillow')

def tree_1(pr):
    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Fractal Tree!') 
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black')
    wn.setup(1200, 1200)
    "این تابع دستورات فرمول رسم فرکتال است"
    def treeFractal(turtle, size, width,pr):
        if width < 1:width = 1
        turtle.width(width)
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if pr==0:return
        "شاخه را به ظول  مقدار داده شده رسم میکند"
        turtle.forward(size)
        "۳۵ درجه به چپ"
        turtle.left(35)
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, size / 2, width - 0.5,pr-1)
        "۷۰ درجه به راست(زاویه بین دو شاخه)"
        turtle.right(70)
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, size / 2, width - 0.5,pr-1)
        "۳۵ درجه به چپ"
        turtle.left(35)
        turtle.penup()
        turtle.backward(size)
        turtle.pendown()

    "جهت رسم فرکتال"
    myTurtle.left(90)
    myTurtle.penup()
    myTurtle.backward(300)
    myTurtle.pendown()
    myTurtle.speed(0)
    "فراخوانی دستورات اجرایی رسم فرکتال"
    treeFractal(myTurtle, 300, 4,pr)

    wn.exitonclick()

def tree_2(pr):

    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Fractal Tree!')
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black') 
    wn.setup(1200, 1200) 
    "این تابع دستورات فرمول رسم فرکتال است"
    def treeFractal(turtle, size,pr):
        # base case
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if pr==0:return
        "شاخه را به ظول  مقدار داده شده رسم میکند"
        turtle.forward(size)
        "۴۵ درجه به چپ"
        turtle.left(45)
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, 3 * size / 4,pr-1)
        "۹۰ درجه به راست(زاویه بین دو شاخه)"
        turtle.right(90)
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, 3 * size / 4,pr-1)
        "۴۵ درجه به چپ"
        turtle.left(45)
        turtle.penup()
        turtle.backward(size)
        turtle.pendown()

    myTurtle.width(1)
    myTurtle.penup()
    myTurtle.goto(0,-300)
    myTurtle.pendown()
    "جهت رسم فرکتال"
    myTurtle.left(90)
    myTurtle.speed(0)
    "فراخوانی دستورات اجرایی رسم فرکتال"
    treeFractal(myTurtle, 100,5)

    wn.exitonclick()

def tree_3(pr):
    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Fractal Tree!') 
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black') 
    wn.setup(1200, 1200) 
    "این تابع دستورات فرمول رسم فرکتال است"
    def treeFractal(turtle, size,pr):
        # base case
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if pr==0:return
        turtle.forward(size)
        "۴۵ درجه به چپ"
        turtle.left(30)
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, 3 * size / 4,pr-1)
        "۹۰ درجه به راست(زاویه بین دو شاخه)"            
        turtle.right(60) 
        "تابع را دوباره فراخوانی میکند"
        treeFractal(turtle, 3 * size / 4,pr-1)
        "۴۵ درجه به چپ"
        turtle.left(30)
        turtle.backward(size)

    "جهت رسم فرکتال"
    myTurtle.left(90)
    myTurtle.speed(0)
    myTurtle.penup()
    myTurtle.goto(0,-300)
    myTurtle.pendown()
    "فراخوانی دستورات اجرایی رسم فرکتال"
    treeFractal(myTurtle, 100,pr)

    wn.exitonclick()

def koch(pr):
    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Recursive Circles!') 
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black') 
    wn.setup(1200, 1200) 

    "این تابه فرمول اجرایی برای برخال مخ است"
    def kochOneSide(turtle, length, depth):
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if depth == 0:
            "رسم خط به اندازه مقدار وارذه"
            turtle.forward(length)
            return
        "تابغ را دوباره فراخوانی میکند"
        kochOneSide(turtle, length / 3, depth - 1)
        "۶۰ درجه به راست"
        turtle.right(60)
        "تابغ را دوباره فراخوانی میکند"
        kochOneSide(turtle, length / 3, depth - 1)
        "۱۲۰ درجه به چپ"
        turtle.left(120)
        "تابغ را دوباره فراخوانی میکند"
        kochOneSide(turtle, length / 3, depth - 1)
        "۶۰ درجه به راست"
        turtle.right(60)
        "تابغ را دوباره فراخوانی میکند"
        kochOneSide(turtle, length / 3, depth - 1)

    "تابع مشخص کننده مثلث اولیه"
    def kochSnowFlake(myTurtle, length, depth):
        myTurtle.penup()
        myTurtle.setposition(-length / 2, 0)
        myTurtle.pendown()
        for i in range(3):
            kochOneSide(myTurtle, length, depth)
            myTurtle.left(120)

    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    myTurtle.speed(0)
    kochSnowFlake(myTurtle, 300, pr)
    wn.exitonclick()

def circle():
    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Recursive Circles!')
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black') 
    wn.setup(1200, 1200) 
    
    "نابع قرمول کلی برخال"
    def drawCircle(turtle, x, y, radius):
        turtle.penup()
        turtle.setposition(x, y)
        turtle.pendown()
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        turtle.circle(radius)

        if radius > 8:
            turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            "تابع را با مقادیر جدید(شعاع نصف قبلی و مختصات چهار جهت دایره)"
            drawCircle(turtle, x + radius, y + radius / 2, radius / 2)
            drawCircle(turtle, x - radius, y + radius / 2, radius / 2)
            drawCircle(turtle, x, y - radius / 2, radius / 2)
            drawCircle(turtle, x, y + 3 *radius / 2, radius / 2)

        else :return


    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    myTurtle.speed(0)
    myTurtle.right(90)
    "تعین شعاع دایره"
    radius = 100
    myTurtle.penup()
    myTurtle.forward(radius)
    myTurtle.pendown()
    myTurtle.left(90)

    drawCircle(myTurtle, myTurtle.position()[0],  myTurtle.position()[1], radius)

    wn.exitonclick()

def eight_feathered_flower(pr):
    wn = turtle.Screen()
    wn.colormode(255) 
    wn.title('Fractal Tree!') 
    myTurtle = turtle.Turtle()
    wn.setup(1200, 1200)
    wn.bgcolor('black') 
    wn.setup(1200, 1200) 
    "تابغ فرمول برخال"
    def treeFractal(turtle, size,pr):
        # base case
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if pr==0:return
        "شاخه را رسم میکند"
        turtle.forward(size)
        "۲۵ درجه به راست"
        turtle.left(25) 
        "تابع را مجدد فرا خوانی میکند"
        treeFractal(turtle, 2*size/3,pr-1)
        "۵۰ درجه به راست"
        turtle.right(50) 
        "تابع را مجدد فراخوانی میکند"
        treeFractal(turtle, 2*size/3,pr-1)
        "۲۵ درجه به چپ"
        turtle.left(25)
        turtle.backward(size)

    myTurtle.speed(0)
    "هر ۴۵ درجه یک درخت جدید رسم میکند"
    for i in range(1,9):
        treeFractal(myTurtle, 100,pr)
        myTurtle.left(i*45)

    wn.exitonclick()

commands="""
mandelbrot
julia
tree_1
tree_2
tree_3
koch
circle
flower
--------------------------
command: 
"""
while True:
    command_user=input(commands).strip()
    m=True
    if command_user=='mandelbrot':mandelbrot()
    elif command_user=='julia':julia()
    elif command_user=='tree_1':
        while m:
            try:number=int(input('number: '))
            except:print('not number !');continue
            tree_1(number)
            m=False
    elif command_user=='tree_2':
        while m:
            try:number=int(input('number: '))
            except:print('not number !');continue
            tree_2(number)
            m=False
    elif command_user=='tree_3':
        while m:
            try:number=int(input('number: '))
            except:print('not number !');continue
            tree_3(number)
            m=False
    elif command_user=='koch':
        while m:
            try:number=int(input('number: '))
            except:print('not number !');continue
            koch(number)
            m=False
    elif command_user=='circle':circle()
    elif command_user=='flower':
        while m:
            try:number=int(input('number: '))
            except:print('not number !');continue
            eight_feathered_flower(number)
            m=False
    else:print('command is not! plase try again')
