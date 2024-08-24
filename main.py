import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QMenu, QSystemTrayIcon
from PyQt5.QtGui import QIcon, QMovie, QCursor
from PyQt5.QtCore import Qt

class SparkPet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.movie = None 
        self.initUI()
        self.initTrayIcon()

    def initUI(self):
        self.setGeometry(1650, 20, 200, 200)
        self.setWindowTitle("Spark Pet")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.initGifLabel()
        self.show()

    def initGifLabel(self):
        self.gifLabel = QLabel(self)
        self.gifLabel.setGeometry(0, 0, 200, 200)
        self.displayGif("PetGIF/move.gif")

    def displayGif(self, path):
        if self.movie:
            self.movie.stop() 
            self.movie.deleteLater()
        self.movie = QMovie(path)
        self.movie.setScaledSize(self.size())
        self.gifLabel.setMovie(self.movie)
        self.movie.start()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.startDrag(e.pos())

    def mouseMoveEvent(self, e):
        if hasattr(self, 'dragStartPos'):
            self.move(e.globalPos() - self.dragStartPos)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.stopDrag()

    def startDrag(self, pos):
        self.dragStartPos = pos
        self.setCursor(QCursor(Qt.ClosedHandCursor))
        self.displayGif("PetGIF/stay.gif")

    def stopDrag(self):
        self.displayGif("PetGIF/move.gif")
        self.unsetCursor()
        del self.dragStartPos

    def initTrayIcon(self):
        trayIcon = QSystemTrayIcon(QIcon("PetGIF/favicon.ico"), self)
        trayIcon.setContextMenu(self.createTrayMenu())
        self.trayIcon = trayIcon 
        trayIcon.show()

    def createTrayMenu(self):
        menu = QMenu(self)
        menu.addAction("Exit", self.close)
        return menu

    def closeEvent(self, e):
        self.trayIcon.setVisible(False)
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Spark_Pet = SparkPet()
    sys.exit(app.exec_())
