"""
Visual simulation of TSP using Turtle graphics.
Adapted from: https://www.youtube.com/watch?v=BAejnwN4Ccw
"""

import math
import random
import turtle
from dataclasses import dataclass
from typing import List


# For holding x and y coordinates
@dataclass
class Vector: x: int; y: int

# Trutle configuration
turtle.title("Traveling Salesman Simulation")
screen = turtle.Screen()
screen.setup(width=720, height=480)
screen.bgcolor("black")
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
screen.tracer(0)  # Disable animations

# Separate turtle object for text
text_pen = turtle.Turtle()
text_pen.hideturtle()  # Hide the turtle pointer
text_pen.penup()  # Lift the pen to avoid drawing lines
text_pen.color("white")

# Separate turtle object for progress
prog_pen = turtle.Turtle()
prog_pen.hideturtle()  # Hide the turtle pointer
prog_pen.penup()  # Lift the pen to avoid drawing lines
prog_pen.color("white")

# Turtle object for drawing edge distance/weights
dist_pen = turtle.Turtle()
dist_pen.color("white")
dist_pen.hideturtle()


def add_info(desc):
    """Display info on the top-right portion of the window."""
    text_pen.penup()
    text_pen.goto(
        (screen.window_width() // 2 - 130), (screen.window_height() // 2 - 25 ))
    text_pen.pendown()
    text_pen.clear()
    text_pen.write(desc, align="left", font=("Arial", 14, "normal"))


def update_progress(r, n):
    """Indicate concurrent progress on the top-left portion of the window."""
    progress = "Processing: " + str(round((r/n) * 100, 4))
    prog_pen.penup()
    prog_pen.goto(
        (-1 * screen.window_width() // 2 + 10), (screen.window_height() // 2 - 25))
    prog_pen.pendown()
    prog_pen.clear()
    prog_pen.write(progress + "%", align="left", font=("Arial", 14, "normal"))


def setup(cities: List[Vector]):
    """Setup simulation demo of cities in implicit graph."""
    x_min_lim = -1 * screen.window_width() // 2 + 20
    x_max_lim = 1 * screen.window_width() // 2 - 20
    y_min_lim = -1 * screen.window_width() // 4 + 20
    y_max_lim = 1 * screen.window_width() // 4 - 20
    for i in range(len(cities)):
        cities[i] = Vector(
            random.randint(x_min_lim, x_max_lim), random.randint(y_min_lim, y_max_lim))


def draw(cities: List[Vector]):
    """Draw a path between all cities."""
    total_distance = 0
    for i in range(len(cities)-1):
        # random.shuffle(cities)
        total_distance += join_vertex(cities[i], cities[i+1])
    total_distance += join_vertex(cities[-1], cities[0])  # Go back to source
    print(f"TSP = {total_distance}")
    return total_distance


def swap(cities: List[Vector]):
    """Randomly swap two vectors and redraw cities/paths."""
    a = random.randint(0, len(cities)-1)
    b = random.randint(0, len(cities)-1)
    cities[a], cities[b] = cities[b], cities[a]
    pen.clear()
    text_pen.clear()
    dist_pen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    return draw(cities)  # Returns total TSP tour distance


def draw_finally(cities: List[Vector]):
    """Draw final, most optimal TSP tour."""
    pen.clear()
    pen.color("purple")
    pen.pensize(5)
    text_pen.clear()
    dist_pen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    return draw(cities)  # Returns total TSP tour distance


def create_vector(size: int):
    """Instantiate a sample city size."""
    cities: List[None|Vector] = [None]*size
    setup(cities)
    return cities


def show_distance(a: Vector, b: Vector):
    """Write the distance on the edge connecting a and b."""
    mid_x = (a.x + b.x) / 2
    mid_y = (a.y + b.y) / 2
    dist_pen.penup()
    dist_pen.goto(mid_x, mid_y)
    distance = calc_distance(a, b)
    dist_pen.write(distance, align="center", font=("Arial", 9, "bold"))
    dist_pen.penup()
    return distance


def calc_distance(a: Vector, b: Vector):
    """Calculate the Euclidean distance between a and b."""

    x1 = a.x if a.x > b.x else b.x
    x0 = b.x if x1 == a.x else a.x
    y1 = a.y if a.y > b.y else b.y
    y0 = b.y if y1 == a.y else a.y

    if x0 <= 0 <= x1:
        adj = (-1 * x0) + x1
    else: # elif x0 <= 0 and x1 <= 0:
        adj = abs(x0 - x1)

    if y0 <= 0 <= y1:
        opp = (-1 * y0) + y1
    else: # elif y0 <= 0 and y1 <= 0:
        opp = abs(y0 - y1)

    hyp = math.sqrt((opp**2) + (adj**2))
    # print(f"x0 = {x0}\nx1 = {x1}\ny0 = {y0}\ny1 = {y1}")
    # print(f"opp = {opp}\nadj = {adj}\nhyp = {hyp}\n")

    return round(hyp, 2)


def join_vertex(a: Vector, b: Vector, debug=False):
    """Draw an edge between vertices (Vectors) a and b."""
    if debug: add_info("Rendering...")

    # Vertex A
    pen.penup()
    pen.goto(a.x, a.y)
    pen.pendown()
    pen.dot(10)

    # Vertex B
    pen.penup()
    pen.goto(b.x, b.y)
    pen.pendown()
    pen.dot(10)

    # Edge
    pen.penup()
    pen.goto(a.x, a.y)
    pen.pensize(2)
    pen.pendown()
    pen.goto(b.x, b.y)
    pen.penup()

    distance = show_distance(a, b)
    if debug: add_info("Rendered")
    screen.update()
    return distance


def simulate(nodes):
    """Simulate TSP based on given configurations above."""
    total_cities = create_vector(nodes)
    best_tour = total_cities[:]
    tsp = draw(total_cities)
    trials = math.factorial(nodes)
    for k in range(1, trials+1):
        cur_tsp = swap(total_cities)
        update_progress(k, trials)
        if cur_tsp < tsp:
            tsp = cur_tsp
            best_tour = total_cities[:]
    draw_finally(best_tour)
    print(f"Best TSP tour = {tsp}")
    pen.hideturtle()
    turtle.done()


def test_sim():
    """Basic test: connect two points."""
    v1 = Vector(0,0)
    v2 = Vector(100, 100)
    join_vertex(v1, v2, debug=True)
    pen.hideturtle()
    turtle.done()


if __name__ == "__main__":
    # test_sim()
    simulate(nodes=6)
