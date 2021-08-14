
![Animation with Turtle](https://user-images.githubusercontent.com/82774834/129449442-31b45c83-3883-4ea9-b70a-c394a2c5ee85.PNG)


# turtle is an in-built library
import turtle

# it will open another new window and we are giving the bg color of that window
turtle.bgcolor("lightpink")
turtle.pensize(1.5)
turtle.speed(0.5)
# color which we want for our animation and drawing
color = ["black","white","black","white","black"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)

turtle.mainloop()
