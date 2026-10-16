from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    # Set the background color
    glClearColor(0.05, 0.05, 0.10, 1.0)

    # Enable depth testing for 3D objects
    glEnable(GL_DEPTH_TEST)

    # Enable lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Enable smooth shading
    glShadeModel(GL_SMOOTH)

    # Ambient light
    ambient_light = [0.2, 0.2, 0.2, 1.0]

    # Diffuse light
    diffuse_light = [0.8, 0.8, 0.8, 1.0]

    # Specular light
    specular_light = [1.0, 1.0, 1.0, 1.0]

    # Position of the light source
    light_position = [3.0, 3.0, 3.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Material properties of the sphere
    material_ambient = [0.2, 0.2, 0.6, 1.0]
    material_diffuse = [0.2, 0.3, 0.9, 1.0]
    material_specular = [1.0, 1.0, 1.0, 1.0]

    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)

    # Shininess controls the size of the highlight
    glMaterialf(GL_FRONT, GL_SHININESS, 60.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Position the camera
    gluLookAt(
        0.0, 0.0, 5.0,
        0.0, 0.0, 0.0,
        0.0, 1.0, 0.0
    )

    # Draw a 3D sphere
    glutSolidSphere(1.0, 80, 80)

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45.0, width / height, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Phong Illumination Model")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == "__main__":
    main()
