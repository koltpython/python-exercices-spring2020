# This program draws design using repeated lines.
import turtle

# Constants
START_X = -200          # Starting X coordinate
START_Y = 0             # Starting Y coordinate
LINE_LENGTH = 400       # Length of each line
ANIMATION_SPEED = 10     # Animation speed
BIG_ANGLE = 0           # Angle to be substracted from

# Get number of lines to be drawn as an input from user.
num_lines = int(
    input('Please enter the number of lines you want in your star: '))

# You should not accept values smaller than 5 and request for a new value until user enters a valid value
# TODO: input validation
while num_lines < 5:
    num_lines = int(
        input('Please enter the number of lines you want in your star: '))
# Fractal formula changes depends on ever or odd number of lines.
# TODO: find theta

if num_lines % 2 == 0:
    theta = 180 - (360 / num_lines)
else:
    theta = 180 - (180 / num_lines)


# Set initial position of turtle.
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
# Set animation speed.
turtle.speed(ANIMATION_SPEED)

# TODO: Draw num_lines times lines, with turtle tilted
# by angle degrees after each line is drawn.
# Hint: use forward & left functions
counter = 0
while counter < num_lines:
    turtle.forward(LINE_LENGTH)
    turtle.left(theta)
    counter += 1

# freeze screen until user exits.
turtle.done()
