from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import ctypes


# -----------------------------
# Vertex Shader
# -----------------------------

vertex_shader_source = """
#version 330 core

layout (location = 0) in vec3 position;

void main()
{
    gl_Position = vec4(position, 1.0);
}
"""


# -----------------------------
# Fragment Shader
# -----------------------------

fragment_shader_source = """
#version 330 core

out vec4 color;

void main()
{
    color = vec4(0.0, 1.0, 0.0, 1.0);
}
"""


# -----------------------------
# Compile Shader
# -----------------------------

def compile_shader(source, shader_type):

    shader = glCreateShader(shader_type)

    glShaderSource(shader, source)
    glCompileShader(shader)

    # Check compilation error
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        print("Shader Compilation Error:")
        print(error)

    return shader


# -----------------------------
# Create Shader Program
# -----------------------------

def create_shader_program():

    vertex_shader = compile_shader(
        vertex_shader_source,
        GL_VERTEX_SHADER
    )

    fragment_shader = compile_shader(
        fragment_shader_source,
        GL_FRAGMENT_SHADER
    )

    program = glCreateProgram()

    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)

    glLinkProgram(program)

    # Check linking error
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(program).decode()
        print("Program Linking Error:")
        print(error)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


# -----------------------------
# Triangle vertices
# -----------------------------

vertices = [
     0.0,  0.6, 0.0,
    -0.6, -0.6, 0.0,
     0.6, -0.6, 0.0
]


shader_program = None
vao = None
vbo = None


# -----------------------------
# Initialize OpenGL
# -----------------------------

def init():

    global shader_program
    global vao
    global vbo

    # Create shader program
    shader_program = create_shader_program()

    # Create Vertex Array Object
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # Create Vertex Buffer Object
    vbo = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Convert Python list to C float array
    vertex_data = (ctypes.c_float * len(vertices))(*vertices)

    glBufferData(
        GL_ARRAY_BUFFER,
        len(vertex_data) * ctypes.sizeof(ctypes.c_float),
        vertex_data,
        GL_STATIC_DRAW
    )

    # Position attribute
    glVertexAttribPointer(
        0,
        3,
        GL_FLOAT,
        GL_FALSE,
        3 * ctypes.sizeof(ctypes.c_float),
        ctypes.c_void_p(0)
    )

    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Background color
    glClearColor(0.0, 0.0, 0.0, 1.0)


# -----------------------------
# Display
# -----------------------------

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Use shader program
    glUseProgram(shader_program)

    # Draw triangle
    glBindVertexArray(vao)

    glDrawArrays(
        GL_TRIANGLES,
        0,
        3
    )

    glBindVertexArray(0)

    glutSwapBuffers()


# -----------------------------
# Main
# -----------------------------

def main():

    glutInit()

    # Request OpenGL 3.3 context
    glutInitContextVersion(3, 3)
    glutInitContextProfile(GLUT_CORE_PROFILE)

    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGBA
    )

    glutInitWindowSize(800, 600)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(
        b"Experiment 8 - Vertex and Fragment Shaders"
    )

    init()

    glutDisplayFunc(display)

    glutMainLoop()


main()