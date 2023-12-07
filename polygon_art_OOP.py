import turtle
import random

class ArtGenerator:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def draw_polygon(self, num_sides, size, position, color, border_size, rotation):
        self.turtle.penup()
        self.turtle.goto(position[0], position[1])
        self.turtle.setheading(rotation)
        self.turtle.color(color)
        self.turtle.pensize(border_size)
        self.turtle.pendown()
        for _ in range(num_sides):
            self.turtle.forward(size)
            self.turtle.left(360/num_sides)
        self.turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def generate_art(self, choice):
        if choice == 1:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                self.draw_polygon(3, size, position, color, border_size, rotation)
        elif choice == 2:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                self.draw_polygon(4, size, position, color, border_size, rotation)
        elif choice == 3:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                self.draw_polygon(5, size, position, color, border_size, rotation)

        elif choice == 4:
        	for _ in range(20):
        		num_sides = random.randint(3, 5)
        		size = random.randint(50, 150)
        		position = [random.randint(-300, 300), random.randint(-200, 200)]
        		color = self.get_new_color()
        		border_size = random.randint(1, 5)
        		rotation = random.randint(0, 360)
        		self.draw_polygon(num_sides, size, position, color, border_size, rotation)

        elif choice == 5:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                for i in range(4):
                	size1 = size  * i
                	self.draw_polygon(3, size1, position, color, border_size, rotation)

        elif choice == 6:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                for i in range(4):
                	size1 = size  * i
                	self.draw_polygon(4, size1, position, color, border_size, rotation)

        elif choice == 7:
            for _ in range(20):
                size = random.randint(50, 150)
                position = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 5)
                rotation = random.randint(0, 360)
                for i in range(4):
                	size1 = size  * i
                	self.draw_polygon(5, size1, position, color, border_size, rotation)

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

        turtle.done()


print("Which art do you want to generate? Enter a number between 1 to 8, inclusive:")
user_choice = int(input())
    
art_generator = ArtGenerator()
art_generator.generate_art(user_choice)
