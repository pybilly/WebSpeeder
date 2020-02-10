# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from requests import get
from time import time
def getSpeed(urls,self):
    speeds=[]
    try:
        for i in urls:
            time1 = time()
            get(i)
            time2 = time()
            timeDelta = str(round((time2 - time1), 2))+"s"
            # print(timeDelta)
            speeds.append(timeDelta)
        return speeds
    except Exception as e:
        QtWidgets.QMessageBox.critical(self,"WebSpeeder-Error Happened","%s"%repr(e))
        print(repr(e),str(e),sep="\n")
        return -1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 429)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 631, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.type1 = QtWidgets.QComboBox(self.centralwidget)
        self.type1.setGeometry(QtCore.QRect(20, 110, 561, 31))
        self.type1.setObjectName("type1")
        self.test1 = QtWidgets.QPushButton(self.centralwidget)
        self.test1.setGeometry(QtCore.QRect(220, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("宋体-PUA")
        font.setPointSize(12)
        self.test1.setFont(font)
        self.test1.setObjectName("test1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.type2 = QtWidgets.QComboBox(self.centralwidget)
        self.type2.setGeometry(QtCore.QRect(20, 270, 561, 31))
        self.type2.setObjectName("type2")
        self.test2 = QtWidgets.QPushButton(self.centralwidget)
        self.test2.setGeometry(QtCore.QRect(220, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("宋体-PUA")
        font.setPointSize(12)
        self.test2.setFont(font)
        self.test2.setObjectName("test2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 631, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_domain = QtWidgets.QAction(MainWindow)
        self.action_domain.setObjectName("action_domain")
        self.menuHelp.addAction(self.action_domain)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WebUpDown宽带测速器"))
        self.label.setText(_translate("MainWindow", "宽带测速器"))
        self.label_2.setText(_translate("MainWindow", "国内"))
        self.test1.setText(_translate("MainWindow", "测试所选项"))
        self.label_3.setText(_translate("MainWindow", "国外"))
        self.test2.setText(_translate("MainWindow", "测试所选项"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.action_domain.setText(_translate("MainWindow", "官网主页"))


class WebSpeeder(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(WebSpeeder, self).__init__(parent=None)
        self.setupUi(self)
        self.options={
            "搜索引擎":{
                "百度":"http://www.baidu.com/",
                "搜狗":"http://www.sogou.com/",
                "360 So":"https://www.so.com/",
                "谷歌中国":"http://www.google.cn/",
                "必应中国":"http://cn.bing.com/",
                "中搜":"http://www.zhongsou.com/"
            },
            "聊天软件":{
                "微信":"http://weixin.qq.com/",
                "腾讯QQ":"http://im.qq.com/",
                "钉钉":"http://www.dingtalk.com/",
                "新浪微博":"http://www.weibo.com/",
                "腾讯微博":"http://t.qq.com/",
                "163邮箱":"http://mail.163.com/",

            },
            "视频直播":{
                "爱奇艺":"http://www.iqiyi.com/",
                "优酷":"http://www.youku.com/",
                "腾讯视频":"http://v.qq.com/",
                "哔哩哔哩":"http://www.bilibili.com/"
            },
            "新闻网站":{
                "网易新闻":"http://www.163.com/",
                "腾讯新闻":"http://www.qq.com/",
                "百度新闻":"http://news.baidu.com/",
                "今日头条":"http://www.toutiao.com/"
            },
            "音乐网站":{
                "QQ音乐":"http://y.qq.com/",
                "网易云音乐":"http://music.163.com/",
                "千千音乐":"http://music.baidu.com/",
                "酷我音乐":"http://www.kuwo.cn/",
                "酷狗音乐":"http://www.kugou.com/"
            },
            "博客社区":{
                "简书":"http://www.jianshu.com/",
                "知乎":"http://www.zhihu.com/",
                "天涯论坛":"http://www.tianya.cn/",
                "新浪网":"http://www.sina.com.cn/"
            },
            "Program Website":{
                "GitHub":"http://www.github.com/",
                "GitHub Pages":"http://www.github.io/",
                "Python Software":"http://www.python.org/",
                "Java":"http://www.java.com/",
                "MySQL AB":"http://www.mysql.com/"
            },
            "Company":{
                "Microsoft":"http://www.microsoft.com/",
                "Oracle":"http://www.oracle.com/",
                "Amazon":"http://www.amazon.com/",
                "Apple Inc.":"http://www.apple.com/"
            },
            "Foreign commonly used":{
                "Google":"http://www.google.com/",
                "FaceBook":"http://www.facebook.com/",
                "Twitter":"http://www.twitter.com/",
                "YouTube":"http://www.youtube.com/"
            }




        }
        self.type1.addItems([
            "搜索引擎",
            "聊天软件",
            "视频直播",
            "新闻网站",
            "音乐网站",
            "博客社区",
            "输入一个网址……"
                             ])
        self.type2.addItems([
            "Program Website",
            "Company",
            "Foreign commonly used",
            "Input..."
        ])
        self.test1.clicked.connect(self.test1_)
        self.test2.clicked.connect(self.test2_)
        self.action_domain.triggered.connect(self.openweb)
    def test1_(self):
        option=self.type1.currentText()
        if option != "输入一个网址……":
            options = self.options[option]
            webs = self.options[option].values()
            speeds = getSpeed(urls=webs, self=self)
            if speeds == -1:
                return -1

            str_ = ""
            for i in speeds:
                str_ += "%s : %s\n" % (list(options)[speeds.index(i)], i)

            QtWidgets.QMessageBox.information(self, "WebSpeeder", str_)
        else:
            url=QtWidgets.QInputDialog.getText(self,"WebSpeeder","键入一个网址",text="http://")[0]
            speed=getSpeed([url],self)
            if speed != -1:
                QtWidgets.QMessageBox.information(self, "WebSpeeder", "此网站测速结果：%s" % speed[0],)
    def test2_(self):
        option=self.type2.currentText()
        if option != "Input...":
            options = self.options[option]
            webs = self.options[option].values()
            speeds = getSpeed(urls=webs, self=self)
            if speeds == -1:
                return -1

            str_ = ""
            for i in speeds:
                str_ += "%s : %s\n" % (list(options)[speeds.index(i)], i)

            QtWidgets.QMessageBox.information(self, "WebSpeeder", str_)
        else:
            url=QtWidgets.QInputDialog.getText(self,"WebSpeeder","Input a URL...",text="http://")[0]
            speed=getSpeed([url],self)
            if speed != -1:
                QtWidgets.QMessageBox.information(self, "WebSpeeder", "Speed measurement results for this site：%s" % speed[0],)
    def openweb(self):
        from webbrowser import open_new_tab
        open_new_tab("https://pybilly.github.io/WebSpeeder/")
        QtWidgets.QMessageBox.information(self,"WebSpeeder","OK!")
app=QtWidgets.QApplication(sys.argv)
frame=WebSpeeder()
frame.show()
app.exec_()


