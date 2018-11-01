import sys,os
from PyQt4 import QtGui, QtCore
import MainWindow,DownloadWindow






app = QtGui.QApplication(sys.argv)


win = MainWindow.Ui_MainWindow()
win.show()
#win.move(0, 0)

#win2 = DownloadWindow.Ui_MainWindow()
#win2.show()
#win2.move(882, 0)

sys.exit(app.exec_())

