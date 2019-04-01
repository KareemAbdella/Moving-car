from random import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

z = 0
angle = 0
x = 0
forward = True

L = 0

a = randrange(-3, 3)


def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 600)
    gluLookAt(8, 9, 10,
              0.25, 5, 0,
              0, 1, 0)
    ()
    glClearColor(1, 1, 1, 1)


def Road():
    glTranslate(0, 0.5, 6.5)
    glScale(100, 1, 0.5)
    glColor3f(0, 0, 0)
    glutSolidCube(2)
    glLoadIdentity()
    glTranslate(0, 0.5, -6.5)
    glScale(100, 1, 0.5)
    glColor3f(0, 0, 0)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(100, 0, 6)
    glVertex(100, 0, -6)
    glVertex(-100, 0, -6)
    glVertex(-100, 0, 6)
    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-10, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glTranslate(-5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()
    glLoadIdentity()





def draw():
    global angle
    global x
    global forward
    global z
    global L
    global a

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.4, 0, 1, 1)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glClear(GL_DEPTH_BUFFER_BIT)
    Road()

    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5 + z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0, 0, 1)

    glutWireTorus(0.125, 0.5, 10, 10)
    glLoadIdentity()
    glColor3f(0, 0, 1)

    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5 + z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    # draw_XYZ()
    glColor3f(1, 0, 0)
    glTranslate(x, 0, z)
    glScale(1, 0.25, 0.5)
    glRotate(90, 1, 0, 0)
    glutSolidCube(5)

    glLoadIdentity()

    glTranslate(x, 5 * 0.25, z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(0, 0, 1)
    glLoadIdentity()

    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, - 0.5 * 0.5 * 5 + z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, -0.5 * 0.5 * 5 + z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()

    glColor3f(1, 0, 0)
    glTranslate(L, a, 0)
    glutSolidSphere(0.7, 100, 100)

    glutSwapBuffers()

    if L < 10:
        L += 0.3
    else:
        L = -60
    if L == -60:
        a = randrange(-5, 5)

    if forward:
        angle -= 0.1
        x += 0.2
        if x > 10:
            forward = False
    else:
        angle += 0.1
        x -= 0.3
        if x < -60:
            x=10
            forward = True


def rotate():
    glRotate(-90, 0, 1, 0)
    draw()


z = 0


def arrowHandler(key, x, y):
    global z
    if key == GLUT_KEY_RIGHT:
        z -= 1
        if z < -5:
            z = -5
    elif key == GLUT_KEY_LEFT:
        z += 1
        if z > 5:
            z = 5


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car Task")
myInit()
glutDisplayFunc(rotate)
glutIdleFunc(rotate)
glutSpecialFunc(arrowHandler)
glutMainLoop()
