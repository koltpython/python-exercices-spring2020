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

# Fractal formula changes depends on ever or odd number of lines.
# TODO: find theta


# Set initial position of turtle.
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
# Set animation speed.
turtle.speed(ANIMATION_SPEED)

# TODO: Draw num_lines times lines, with turtle tilted
# by angle degrees after each line is drawn.
# Hint: use forward & left functions


# freeze screen until user exits.
turtle.done()
