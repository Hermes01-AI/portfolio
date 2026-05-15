import turtle

def draw_logo():
    # Setup the screen
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Solar Powered EV Charging Station Logo")
    
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(5)

    # 1. Draw the outer circle (The Station/Global feel)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("#0A610E") # Dark Green for Eco-friendliness
    t.begin_fill()
    t.circle(200)
    t.end_fill()

    # 2. Draw the Sun (Solar Energy)
    t.penup()
    t.goto(-70, 50)
    t.pendown()
    t.color("#FFD600") # Bright Yellow
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    # 3. Draw the Lightning Bolt (Electric Power)
    t.penup()
    t.goto(20, 80)
    t.color("white")
    t.begin_fill()
    # Path for a lightning bolt shape
    t.goto(60, 0)
    t.goto(30, 0)
    t.goto(50, -80)
    t.goto(10, 20)
    t.goto(40, 20)
    t.goto(20, 80)
    t.end_fill()

    # 4. Text - Project Name
    t.penup()
    t.goto(0, -250)
    t.color("#201479")
    t.write("SOLAR SYSTEM & EV Chargers", align="center", font=("Arial", 16, "bold"))

    t.hideturtle()
    print("Logo generation complete!")
    screen.mainloop()

if __name__ == "__main__":
    draw_logo()