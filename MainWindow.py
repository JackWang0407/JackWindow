# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os, threading
import JackSearch
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.ButtonToSearch()
            #print "return pressed"

    def ButtonToSearch(self):
        keyword = unicode(self.lineEdit_2.text())

        if keyword == "":
            self.label_3.setText(_translate("MainWindow", "請輸入搜尋番號", None))
            return

        thd = threading.Thread(target=self.SearchInfo, args=(keyword,))
        thd.start()
        thd2 = threading.Thread(target=self.GetOpenloadVideoDownloadInfo, args=(keyword,))
        thd2.start()

        #Clear
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.lineEdit.setText(_translate("MainWindow", "", None))
        self.label_3.setText(_translate("MainWindow", "搜尋"+self.lineEdit_2.text()+"中...", None))
        self.lineEdit_3.setText(_translate("MainWindow", "", None))
        self.lineEdit_4.setText(_translate("MainWindow", "", None))
        self.lineEdit_5.setText(_translate("MainWindow", "", None))
        self.lineEdit_6.setText(_translate("MainWindow", "", None))
        self.lineEdit_7.setText(_translate("MainWindow", "", None))
        self.lineEdit_8.setText(_translate("MainWindow", "", None))
        self.lineEdit_9.setText(_translate("MainWindow", "", None))
        self.lineEdit_10.setText(_translate("MainWindow", "", None))
        self.lineEdit_11.setText(_translate("MainWindow", "", None))
        self.lineEdit_12.setText(_translate("MainWindow", "", None))
        self.pushButton_2.setText(_translate("MainWindow", "重新命名", None))
        self.pushButton_3.setText(_translate("MainWindow", "加入下載", None))

    def ButtonToRenameFile(self):
        FilePath = unicode(self.lineEdit.text())
        Filename = os.path.basename(FilePath)
        FileSubname = os.path.splitext(Filename)[1]
        Filename = os.path.splitext(Filename)[0]
        FilePath = os.path.dirname(FilePath) + "/"
        # print "FilePath = "+FilePath
        # print "Filename = "+Filename
        # print "FileSubname = "+FileSubname
        NewFilename = unicode(self.lineEdit_10.text())
        # print NewFilename
        NewNumber = unicode(self.lineEdit_5.text())
        # print FilePath + NewNumber
        # print FilePath + NewFilename + FileSubname
        # print FilePath + NewFilename+".jpg"
        if not os.path.isdir(FilePath + NewNumber):
            os.mkdir(FilePath + NewNumber)
        os.rename("tmp.jpg", FilePath + NewNumber + "/" + NewFilename + ".jpg")
        os.rename(unicode(self.lineEdit.text()), FilePath + NewNumber + "/" + NewFilename + FileSubname)
        self.pushButton_2.setEnabled(False)

    def ButtonToDownload(self):
        path = unicode(self.lineEdit_11.text())
        filename = unicode(self.lineEdit_12.text())
        #print path
        #print filename
        thd = threading.Thread(target=JackSearch.GetOpenloadVideo, args=(path,filename))
        thd.start()
        #JackSearch.GetOpenloadVideo(path, filename)
        self.pushButton_3.setEnabled(False)

    def SearchInfo(self, keyword):

        SearchResult = JackSearch.Get7MMVedioInfo(keyword)
        #print SearchResult
        if SearchResult["result"] == "PASS":
            self.lineEdit_3.setText(_translate("MainWindow", SearchResult["title"], None))
            self.lineEdit_4.setText(_translate("MainWindow", SearchResult["avers"], None))
            self.lineEdit_5.setText(_translate("MainWindow", SearchResult["number"], None))
            self.lineEdit_6.setText(_translate("MainWindow", SearchResult["date"], None))
            self.lineEdit_7.setText(_translate("MainWindow", SearchResult["video_long"], None))
            self.lineEdit_8.setText(_translate("MainWindow", SearchResult["company"], None))
            self.lineEdit_9.setText(_translate("MainWindow", SearchResult["maker"], None))
            renamefile = "["+SearchResult["number"]+"] "+SearchResult["title"]+" - "+SearchResult["avers"]+" - "+SearchResult["date"]
            self.lineEdit_10.setText(_translate("MainWindow", renamefile, None))
            QtCore.QObject.emit(self.SearchInfo_Done, QtCore.SIGNAL("SearchInfo_Done"))
            self.pushButton_2.setEnabled(True)

            if SearchResult['have'] == "YES":
                self.pushButton_2.setText(_translate("MainWindow", "已經存在", None))
                self.pushButton_2.setEnabled(False)
                self.pushButton_3.setText(_translate("MainWindow", "已經存在", None))
                self.pushButton_3.setEnabled(False)
                time.sleep(5)
                #self.pushButton_2.setText(_translate("MainWindow", "重新命名", None))
                #self.pushButton_2.setEnabled(True)
                #self.pushButton_3.setText(_translate("MainWindow", "加入下載", None))
                #self.pushButton_3.setEnabled(True)

        else:
            self.label_3.setText(_translate("MainWindow", "沒有搜尋到 " + self.lineEdit_2.text() + " 的相關訊息", None))

            if SearchResult['have'] == "YES":
                self.label_3.setText(_translate("MainWindow", "沒有搜尋到 " + self.lineEdit_2.text() + " 的相關訊息, 但在 AvList 已經存在", None))

            time.sleep(5)
            self.label_3.setText(_translate("MainWindow", "", None))


    def GetOpenloadVideoDownloadInfo(self, keyword):
        SearchResult = JackSearch.GetOpenloadVideoDownloadInfo(keyword)
        #print SearchResult
        if SearchResult["result"] == "PASS":
            self.lineEdit_11.setText(_translate("MainWindow", SearchResult["url"], None))
            self.lineEdit_12.setText(_translate("MainWindow", SearchResult["filename"], None))
            self.pushButton_3.setEnabled(True)
        else:
            #self.statusbar.showMessage(u"沒有搜尋到"+ self.lineEdit_2.text() +u"的下載資源")
            #time.sleep(5)
            #self.statusbar.clearMessage()
            pass

    def dragEnterEvent(self, event):
        event.accept()

    def SearchInfo_Done_Action(self):
        tmp_img = QtGui.QPixmap("tmp.jpg").scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(tmp_img)

    def GetOpenloadVideoDownloadInfo_Action(self):
        print ""

    def dropEvent(self, event):
        st = str(event.mimeData().urls())
        st = st.replace("[PyQt4.QtCore.QUrl(u'file:///", "")
        st = st.replace("'), ", ",")
        st = st.replace("PyQt4.QtCore.QUrl(u'file:///", "")
        st = st.replace("')]", "")
        st = st.decode('unicode_escape')
        self.lineEdit.setText(_translate("MainWindow", st, None))
        self.lineEdit_2.setText(os.path.splitext(os.path.basename(st))[0])
        keyword = os.path.splitext(os.path.basename(st))[0]
        thd = threading.Thread(target=self.SearchInfo, args=(keyword,))
        thd.start()
        thd2 = threading.Thread(target=self.GetOpenloadVideoDownloadInfo, args=(keyword,))
        thd2.start()

        #Clear
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.label_3.setText(_translate("MainWindow", u"搜尋"+os.path.splitext(os.path.basename(st))[0]+u"中...", None))
        self.lineEdit_3.setText(_translate("MainWindow", "", None))
        self.lineEdit_4.setText(_translate("MainWindow", "", None))
        self.lineEdit_5.setText(_translate("MainWindow", "", None))
        self.lineEdit_6.setText(_translate("MainWindow", "", None))
        self.lineEdit_7.setText(_translate("MainWindow", "", None))
        self.lineEdit_8.setText(_translate("MainWindow", "", None))
        self.lineEdit_9.setText(_translate("MainWindow", "", None))
        self.lineEdit_10.setText(_translate("MainWindow", "", None))
        self.lineEdit_11.setText(_translate("MainWindow", "", None))
        self.lineEdit_12.setText(_translate("MainWindow", "", None))
        self.pushButton_2.setText(_translate("MainWindow", "重新命名", None))
        self.pushButton_3.setText(_translate("MainWindow", "加入下載", None))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(862, 901)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 841, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 751, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(710, 40, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 841, 641))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 800, 540))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 570, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 570, 781, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 590, 41, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 610, 41, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(350, 610, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(170, 610, 51, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 590, 781, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 610, 111, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 610, 111, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(390, 610, 111, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(510, 610, 41, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(550, 610, 111, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(670, 610, 41, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(710, 610, 121, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 710, 841, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 40, 121, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 20, 821, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 780, 841, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 40, 121, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 20, 751, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 40, 621, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Search", None))
        self.groupBox.setTitle(_translate("MainWindow", "搜尋目標", None))
        self.label.setText(_translate("MainWindow", "檔案路徑", None))
        self.label_2.setText(_translate("MainWindow", "搜尋番號", None))
        self.pushButton.setText(_translate("MainWindow", "開始搜尋", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "搜尋結果", None))
        self.label_3.setText(_translate("MainWindow", "", None))
        self.label_4.setText(_translate("MainWindow", "片名", None))
        self.label_5.setText(_translate("MainWindow", "演員", None))
        self.label_6.setText(_translate("MainWindow", "番號", None))
        self.label_7.setText(_translate("MainWindow", "片長", None))
        self.label_8.setText(_translate("MainWindow", "發售日", None))
        self.label_9.setText(_translate("MainWindow", "公司", None))
        self.label_10.setText(_translate("MainWindow", "導演", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "重新命名", None))
        self.pushButton_2.setText(_translate("MainWindow", "重新命名", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "下載資源", None))
        self.pushButton_3.setText(_translate("MainWindow", "加入下載", None))
        self.label_11.setText(_translate("MainWindow", "下載路徑", None))
        self.label_12.setText(_translate("MainWindow", "下載檔名", None))
        self.menu.setTitle(_translate("MainWindow", "搜尋", None))
        self.menu_2.setTitle(_translate("MainWindow", "下載", None))

    def slot_scroll(self):
        print "press menu"

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.SearchInfo_Done = QtCore.QObject()
        self.GetOpenloadVideoDownloadInfo_Done = QtCore.QObject()
        QtCore.QObject.connect(self.SearchInfo_Done, QtCore.SIGNAL("SearchInfo_Done"), self.SearchInfo_Done_Action)
        QtCore.QObject.connect(self.GetOpenloadVideoDownloadInfo_Done, QtCore.SIGNAL("GetOpenloadVideoDownloadInfo_Done"), self.GetOpenloadVideoDownloadInfo_Action)
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.ButtonToRenameFile)
        self.pushButton_3.clicked.connect(self.ButtonToDownload)
        self.pushButton.clicked.connect(self.ButtonToSearch)
        self.setAcceptDrops(True)

        self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent)


    def closeEvent(self, event):
        JackSearch.OnExit()

        return


        #action = self.menubar.addAction("new")
        #self.connect(action, QtCore.SIGNAL("triggered()"), self.slot_scroll)







