
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle = 0.0


def init():
    glClearColor(0.08, 0.08, 0.14, 1.0)
    glEnable(GL_DEPTH_TEST)


def draw_cube():
    # Define the 8 vertices of the cube
    vertices = [
        (-1, -1, -1),
        ( 1, -1, -1),
        ( 1,  1, -1),
        (-1,  1, -1),
        (-1, -1,  1),
        ( 1, -1,  1),
        ( 1,  1,  1),
        (-1,  1,  1)
    ]

    # Each face contains 4 vertex indices and one color
    faces = [
        ((0, 1, 2, 3), (0.75, 0.40, 0.60)),  # Mauve
        ((4, 5, 6, 7), (0.40, 0.65, 0.90)),  # Blue
        ((0, 4, 7, 3), (0.70, 0.50, 0.80)),  # Purple
        ((1, 5, 6, 2), (0.90, 0.65, 0.40)),  # Orange
        ((3, 2, 6, 7), (0.50, 0.80, 0.65)),  # Green
        ((0, 1, 5, 4), (0.90, 0.75, 0.80))   # Pink
    ]

    glBegin(GL_QUADS)

    for face, color in faces:
        glColor3fv(color)

        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])

    glEnd()


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Viewing transformation: position the camera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(
        4, 3, 6,       # Camera position
        0, 0, 0,       # Point the camera looks at
        0, 1, 0        # Up direction
    )

    # Rotate the cube to show its 3D shape
    glRotatef(angle, 0, 1, 0)
    glRotatef(20, 1, 0, 0)

    draw_cube()

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1

    # Viewport mapping
    glViewport(0, 0, width, height)

    # Projection transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(
        45.0,                 # Field of view
        width / float(height),# Aspect ratio
        0.1,                  # Near clipping plane
        100.0                 # Far clipping plane
    )

    glMatrixMode(GL_MODELVIEW)


def update(value):
    global angle

    angle += 1.0
    if angle >= 360:
        angle = 0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(
        GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
    )

    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Viewing Pipeline")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
