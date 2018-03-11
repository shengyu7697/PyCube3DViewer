#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtOpenGL
from PyQt4.QtCore import *
from OpenGL import GLU
from OpenGL.GL import *
from numpy import array

def drawCube():
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0) # green
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.5, 0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glColor3f(1.0, 0.0, 0.0) # red
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glColor3f(0.0, 0.0, 1.0) # blue
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glColor3f(1.0, 1.0, 1.0) # white
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()

def drawAxis(len):
    glBegin(GL_LINES)
    # x axis
    glColor3f(1.0, 0.0, 0.0) # red
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(len, 0.0, 0.0)
    # y axis
    glColor3f(0.0, 1.0, 0.0) # green
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, len, 0.0)
    # z axis
    glColor3f(0.0, 0.0, 1.0) # blue
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, len)
    glEnd();

def cv2gl(pos):
    return [-pos[0], -pos[1], pos[2]]

class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.yRotDeg = 0.0
        self.pos = [0.0, 0.0, -5.0]

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 150))
        self.initGeometry()

        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, width, height):
        if height == 0: height = 1

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        
        glLoadIdentity()
        
        # gluPerspective
        aspect = width / float(height)
        GLU.gluPerspective(45.0, aspect, 0.1, 100.0)

        # gluLookAt
        eye = (0.0, 0.0, 0.0)
        center = (0.0, 0.0, 1.0)
        up = (0.0, 1.0, 0.0)
        GLU.gluLookAt(eye[0], eye[1], eye[2], center[0], center[1], center[2], up[0], up[1], up[2])

        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslate(self.pos[0], self.pos[1], self.pos[2])
        #glTranslate(0.0, 0.0, -5.0)
        #glScale(20.0, 20.0, 20.0)
        #glRotate(self.yRotDeg, 0.2, 1.0, 0.3)
        #glRotate(self.yRotDeg, 0.0, 1.0, 0.0)
        #glTranslate(-0.5, -0.5, -0.5)

        #glEnableClientState(GL_VERTEX_ARRAY)
        #glEnableClientState(GL_COLOR_ARRAY)
        #glVertexPointerf(self.cubeVtxArray)
        #glColorPointerf(self.cubeClrArray)
        #glDrawElementsui(GL_QUADS, self.cubeIdxArray)
        
        drawCube()
        #drawAxis(1)

    def initGeometry(self):
        self.cubeVtxArray = array(
                [[0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.0, 1.0],
                 [1.0, 0.0, 1.0],
                 [1.0, 1.0, 1.0],
                 [0.0, 1.0, 1.0]])
        self.cubeIdxArray = [
                0, 1, 2, 3,
                3, 2, 6, 7,
                1, 0, 4, 5,
                2, 1, 5, 6,
                0, 3, 7, 4,
                7, 6, 5, 4 ]
        self.cubeClrArray = [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [1.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                [1.0, 0.0, 1.0],
                [1.0, 1.0, 1.0],
                [0.0, 1.0, 1.0]]

    def spin(self):
        self.yRotDeg = (self.yRotDeg  + 1) % 360.0
        self.parent.statusBar().showMessage('rotation %f' % self.yRotDeg)
        self.updateGL()

    def updatePos(self, pos):
        print 'updatePos: %f %f %f' % (pos[0], pos[1], pos[2])
        self.pos = pos
        self.parent.statusBar().showMessage('pos: %f %f %f' % (pos[0], pos[1], pos[2]))
        self.updateGL()

class Worker(QThread):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.pos = [0.0, 0.0, -4.0]

    def run(self):
        #f = open('pose.log')
        #line = f.readline()
        for line in open('pose.log'):
        	#print line
        	listWords = line.split(",")
        	scale = 100.0
        	listFloat = [float(listWords[0]) * scale, float(listWords[1]) * scale, float(listWords[2]) * scale]
        	pos = cv2gl(listFloat)
        	self.emit(SIGNAL("pos"), pos)
        	time.sleep(0.05)
        #f.close
        #for x in range(0, 20):
        #    self.pos[2] = self.pos[2] - 0.2
        #    self.emit(SIGNAL("pos"), self.pos)
        #    time.sleep(0.3)
        #print self.pos

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(640, 480)
        self.setWindowTitle('Cube 3D Viewer')

        self.initActions()
        self.initMenus()

        glWidget = GLWidget(self)
        self.setCentralWidget(glWidget)

        #timer = QtCore.QTimer(self)
        #timer.setInterval(20)
        #QtCore.QObject.connect(timer, QtCore.SIGNAL('timeout()'), glWidget.spin)
        #timer.start()

        self.work = Worker()
        self.connect(self.work, SIGNAL("pos"), glWidget.updatePos)
        self.work.start()

    def updateUI(self, pos):
        print 'updateUI: %.1f %.1f %.1f' % (pos[0], pos[1], pos[2])

    def initActions(self):
        self.exitAction = QtGui.QAction('Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.connect(self.exitAction, QtCore.SIGNAL('triggered()'), self.close)

    def initMenus(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.exitAction)

    def close(self):
        QtGui.qApp.quit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    m = MainWindow()
    m.show()

    sys.exit(app.exec_())