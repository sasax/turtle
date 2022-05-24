import turtle
import time


# Funktion, die die Schildkröte zeichnet
def drawBar(t, height, color):

    # Fängt an, diese Form zu füllen
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

    # Hört auf, diese Form zu füllen
    t.end_fill()


wn = turtle.Screen()

# Array welches zu sortieren ist
xs = [3, 6, 2, 5, 0, 9, 10, 7, 1, 4, 8]

border = 10


def hex_to_RGB(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # range(Start, Stop[, Schritt])
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    ''' [255,255,255] -> "#FFFFFF" '''
    # format(eingabe, 'x'),  x steht für Hexadezimal
    return "#" + format(RGB[0], 'x') + format(RGB[1], 'x') + format(RGB[2], 'x')


def linear_gradient(n=307):
    # Übersetzt Anfongsfarbe und Endfarbe in RGB-Form.
    s = hex_to_RGB("#000000")
    f = hex_to_RGB("#FFFFFF")
    # Initialisiert die Startfarbe weiss
    RGB_list = ["#000000"]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    # Berechnet die Farben für jeden gleichmäßig verteilten Wert von 1 bis n
    for t in range(1, n):
        #  Sätzt die Farben, um so tiefer die Zahl um so heller
        curr_vector = [int((float(t) / (n - 1)) * 255) for j in range(3)]
        # Fügt die Zahl in das Array ein.
        RGB_list.append(RGB_to_hex(curr_vector))
    return RGB_list


def drawGraph(xs):
    # Die Schildkröte zeichnet alles auf einmal
    wn.tracer(0, 0)

    # findet das grösste Element der Liste heraus
    maxheight = max(xs)

    # zählt wieviele Zahlen zu sortieren sind
    numbers = len(xs)

    # Passt die Grösse des Anzeigefenster an
    wn.setworldcoordinates(0 - border, 0 - border,
                           40 * numbers + border,
                           maxheight + border)

    tess = turtle.Turtle()
    tess.pensize(3)

    # Iteriert durch jeden Balken und zeichnet ihn auch
    for i in range(len(xs)):
        drawBar(tess, xs[i],
                linear_gradient(len(xs))[xs[i]])
    turtle.update()

    time.sleep(1.5)


    # löscht die Oberfläche
    turtle.clear()
    turtle.reset()
    turtle.clearscreen()



# Tauscht das Element von der pos1 mit dem Element von pos2 aus
def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2 - 1)

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
    drawGraph(array)

bubble_sort(xs)

#
wn.exitonclick()
