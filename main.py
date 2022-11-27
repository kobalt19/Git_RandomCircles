from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import random
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawCircles(qp)
            qp.end()

    def drawCircles(self, qp):
        size = w, h = self.size().width(), self.size().height()
        for _ in range(20):
            color = QtGui.QColor(*(int(random() * 255) for _ in range(3)))
            qp.setBrush(color)
            center = int(w * random()), int(h * random())
            r = int(min(size) // 3 * random())
            qp.drawEllipse(QtCore.QPoint(*center), r, r)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
