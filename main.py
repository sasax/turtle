# Python program to draw a turtle
import turtle
import time


# Function that draws the turtle
def drawBar(t, height, color):
    # Get turtle t to draw one bar
    # of height

    # Start filling this shape
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    # stop filling the shape
    t.end_fill()


# Driver Code


# Set up the window and its
# attributes
wn = turtle.Screen()

xs = [3, 6, 2, 5, 0, 9, 10, 7, 1, 4, 8]

border = 10


def hex_to_RGB(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    return "#" + format(RGB[0], 'x') + format(RGB[1], 'x') + format(RGB[2], 'x')


def linear_gradient(n=307, start_hex="#000000", finish_hex="#FFFFFF"):
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    RGB_list = ["#000000"]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)]
        # Add it to our list of output colors
        RGB_list.append(RGB_to_hex(curr_vector))
    return RGB_list


def drawGraph(xs):
    wn.tracer(0, 0)

    maxheight = max(xs)
    numbers = len(xs)

    wn.setworldcoordinates(0 - border, 0 - border,
                           40 * numbers + border,
                           maxheight + border)

    # Create tess and set some attributes
    tess = turtle.Turtle()
    tess.pensize(3)

    for i in range(len(xs)):
        drawBar(tess, xs[i],
                linear_gradient(len(xs))[xs[i]])
    turtle.update()

    time.sleep(0.5)

    turtle.clear()

    turtle.reset()
    turtle.clearscreen()


def swap(array, position1, position2):
    array[position1], array[position2] = array[position2], array[position1]
    return array




def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list

def bubble_sort(array):

    drawGraph(array)
    swapPositions(array, 1, 2)
    drawGraph(array)
    swapPositions(array, 2, 3)
    drawGraph(array)
    swapPositions(array, 3, 4)
    drawGraph(array)
    swapPositions(array, 6, 7)
    drawGraph(array)
    swapPositions(array, 7, 8)
    drawGraph(array)
    swapPositions(array, 8, 9)
    drawGraph(array)
    swapPositions(array, 9, 10)
    drawGraph(array)
    swapPositions(array, 0, 1)
    drawGraph(array)
    swapPositions(array, 2, 3)
    drawGraph(array)
    swapPositions(array, 5, 6)
    drawGraph(array)
    swapPositions(array, 6, 7)
    drawGraph(array)
    swapPositions(array, 7, 8)
    drawGraph(array)
    swapPositions(array, 8, 9)
    drawGraph(array)
    swapPositions(array, 1, 2)
    drawGraph(array)
    swapPositions(array, 5, 6)
    drawGraph(array)
    swapPositions(array, 6, 7)
    drawGraph(array)
    swapPositions(array, 0, 1)
    drawGraph(array)
    swapPositions(array, 4, 5)
    drawGraph(array)
    swapPositions(array, 5, 6)
    drawGraph(array)
    swapPositions(array, 3, 4)
    drawGraph(array)
    swapPositions(array, 4, 5)
    drawGraph(array)
    swapPositions(array, 2, 3)
    drawGraph(array)
    swapPositions(array, 1, 2)

bubble_sort(xs)

wn.exitonclick()
