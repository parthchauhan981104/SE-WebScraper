import sys
from PyQt5 import QtCore
#from PyQt5 import Qt
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import web_scraper

sc = web_scraper.Scraper()
app = QApplication(sys.argv)
p = [0,0,1,1,1,1]
pt = p
# If you saved the template in `templates/main_window.ui`
ui = uic.loadUi("main1.ui")






def discp(im,st,i):
   if i==1 :
       ic = QtGui.QImage(im)
       ic = ic.scaled(350,25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
       ui.ic1.setPixmap(QtGui.QPixmap.fromImage(ic))
       ui.txt1.setText(st)
       ui.txt1.setAlignment(QtCore.Qt.AlignTop)
       ui.txt1.setFont(QtGui.QFont('Times',9))
       ui.txt1.move(30,50)
   elif i==2:
       ic = QtGui.QImage(im)
       ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
       ui.ic2.setPixmap(QtGui.QPixmap.fromImage(ic))

       ui.txt2.setText(st)
       ui.txt2.setAlignment(QtCore.Qt.AlignTop)
       ui.txt2.setFont(QtGui.QFont('Times', 9))
       ui.txt2.move(30, 50)
   elif i==3:
       ic = QtGui.QImage(im)
       ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
       ui.ic3.setPixmap(QtGui.QPixmap.fromImage(ic))

       ui.txt3.setText(st)
       ui.txt3.setAlignment(QtCore.Qt.AlignTop)
       ui.txt3.setFont(QtGui.QFont('Times', 9))
       ui.txt3.move(30, 50)
   elif i==4:
       ic = QtGui.QImage(im)
       ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
       ui.ic4.setPixmap(QtGui.QPixmap.fromImage(ic))

       ui.txt4.setText(st)
       ui.txt4.setAlignment(QtCore.Qt.AlignTop)
       ui.txt4.setFont(QtGui.QFont('Times', 9))
       ui.txt4.move(30, 50)

co = p.count(1)
it=1
def prev():
    co = p.count(1)
    it=1
    if p[0] == 1 and it <5:
        discp('cb1.jfif', sc.cricket(), it)
        it+=1
        pt[0] =2
    if p[1] == 1 and it <5:
        discp('bill1.jfif',sc.billboard() , it)
        it += 1
        pt[1] = 2
    if p[2] == 1 and it <5:
        discp('toi1.jfif', sc.news(), it)
        it += 1
        pt[2] = 2
    if p[3] == 1 and it <5:
        discp('mm1.jfif', sc.mess_menu(), it)
        it += 1
        pt[3] = 2
    if p[4] == 1 and it <5:
        discp('brq1.jfif', sc.quote(), it)
        it += 1
        pt[4] =2
    if p[5] == 1 and it<5:
        discp('weather.jfif', sc.weather(), it)
    ui.show()



def next():
    ite = 1
    for p2 in p:
        if pt[p2] ==2:
            continue
        if pt[p2] ==1 and p2 ==0:
            discp('cb1.jfif', sc.cricket(),ite)
            ite+=1
        if pt[p2] ==1 and p2 ==1:
            discp('bill1.jfif', sc.billboard(), ite)
            ite+=1
        if pt[p2] ==1 and p2 ==2:
            discp('toi1.jfif', sc.news(), ite)
            ite+=1
        if pt[p2] == 1 and p2 == 3:
            discp('mm1.jfif', sc.mess_menu(), ite)
            ite += 1
        if pt[p2] == 1 and p2 == 4:
            discp('brq1.jfif', sc.quote(), ite)
            ite += 1
        if pt[p2] == 1 and p2 == 5:
            discp('weather.jfif', sc.weather(), ite)
            ite += 1

    #ui.close()



#ui.next.clicked.connect(ui.close())





# def guest():
#     def prevg():
#         discp('cb1.jfif', sc.cricket(), 1)
#         discp('bill1.jfif', sc.billboard(), 2)
#         discp('toi1.jfif', sc.news(), 3)
#         discp('mm1.jfif', sc.mess_menu(), 4)
#     def nextg():
#         discp('brq1.jfif', sc.quote(), 1)
#         discp('weather.jfif', sc.weather(), 2)






prev()



sys.exit(app.exec_())