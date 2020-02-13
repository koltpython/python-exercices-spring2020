# This program draws a design using repeated circles.
import turtle

# Constants
RADIUS = 100            # Radius of each circle
ANIMATION_SPEED = 0    # Animation speed

# Take number of circles to drow from user.
number_circles = int(input('Enter number of circles to draw: '))

# Calculate turtle tilt angle after each cirle is drawn.
angle = 360 / number_circles

# Set the animation speed
turtle.speed(ANIMATION_SPEED)

# TODO: Draw number_circles times circles, with the turtle tilted
# by angle degrees after each circle is drawn.

counter = 0
while counter < number_circles:
    turtle.circle(RADIUS)
    turtle.left(angle)
    counter += 1

# freeze screen until user exits.
turtle.done()
