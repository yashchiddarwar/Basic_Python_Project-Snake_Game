from turtle import Turtle, Screen
screen = Screen()

turt = Turtle()
score = 25
turt.color("purple")
turt.write(f"Score: {score}", False, "center", ('Arial', 25, 'normal'))
screen.exitonclick()