from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH = 800
HEIGHT = 600

# Clipping window
XMIN = 200
XMAX = 600
YMIN = 150
YMAX = 450

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# Find the region code of a point
def compute_code(x, y):
    code = INSIDE

    if x < XMIN:
        code |= LEFT
    elif x > XMAX:
        code |= RIGHT

    if y < YMIN:
        code |= BOTTOM
    elif y > YMAX:
        code |= TOP

    return code


# Cohen-Sutherland line clipping
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    accept = False

    while True:

        # Both points are inside
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Line is completely outside
        elif (code1 & code2) != 0:
            break

        else:
            # Choose the point outside the clipping window
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (YMAX - y1) / (y2 - y1)
                y = YMAX

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (YMIN - y1) / (y2 - y1)
                y = YMIN

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (XMAX - x1) / (x2 - x1)
                x = XMAX

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (XMIN - x1) / (x2 - x1)
                x = XMIN

            # Replace the outside point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return x1, y1, x2, y2
    else:
        return None


# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw clipping window
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(XMIN, YMIN)
    glVertex2f(XMAX, YMIN)
    glVertex2f(XMAX, YMAX)
    glVertex2f(XMIN, YMAX)
    glEnd()

    # Original line
    x1, y1 = 100, 100
    x2, y2 = 700, 500

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    # Perform clipping
    clipped_line = cohen_sutherland(x1, y1, x2, y2)

    # Draw clipped line
    if clipped_line:
        cx1, cy1, cx2, cy2 = clipped_line

        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(cx1, cy1)
        glVertex2f(cx2, cy2)
        glEnd()

    glFlush()


# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, WIDTH, 0, HEIGHT)


# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Cohen-Sutherland Line Clipping")

    init()
    glutDisplayFunc(display)

    glutMainLoop()


main()