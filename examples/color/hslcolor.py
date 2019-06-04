from generativepy import drawing
from generativepy.drawing import makeImage
from generativepy.color import Color, HSL


def draw(canvas):
    canvas.colorMode(HSL)
    for i in range(200):
        for j in range(200):
            canvas.stroke(Color(i/200, j/200, 0.5))
            canvas.point(i + 50, j + 50)

    for i in range(200):
        for j in range(200):
            canvas.stroke(Color(i/200, 0.5, j/200))
            canvas.point(i + 50, j + 300)

    canvas.colorRange(200)
    for i in range(200):
        for j in range(200):
            canvas.stroke(Color(100, i, j))
            canvas.point(i + 50, j + 550)


makeImage("/tmp/hslcolor.png", draw, pixelSize=(300, 800), background=Color(1))
