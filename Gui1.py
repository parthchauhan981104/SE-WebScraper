import sys
from PyQt5 import QtCore
# from PyQt5 import Qt
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from functools import partial
import web_scraper
from time import sleep

strc = ''
strb = ''
strq = ''
strn = ''
strm = ''
strw = ''
sc = web_scraper.Scraper()
# strw1 = sc.weather()
app = QApplication(sys.argv)
# p = [0,0,1,1,1,1]
pt = []
p = []
# If you saved the template in `templates/main_window.ui`
ui = uic.loadUi("main1.ui")
ui2 = uic.loadUi("main2.ui")
wel = uic.loadUi('welcome.ui')
log = uic.loadUi('login.ui')
reg = uic.loadUi('register.ui')
er = uic.loadUi('error.ui')
pre = uic.loadUi('preferences.ui')
guests1 = uic.loadUi('guest1.ui')
guests2 = uic.loadUi('guest2.ui')


# welcome screen

def discp(im, st, i):
    print('cricbuzz')
    if i == 1:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui.ic1.setPixmap(QtGui.QPixmap.fromImage(ic))
        ui.txt1.setText(st)
        ui.txt1.setAlignment(QtCore.Qt.AlignTop)
        ui.txt1.setFont(QtGui.QFont('Times', 9))
        ui.txt1.move(30, 50)

    elif i == 2:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui.ic2.setPixmap(QtGui.QPixmap.fromImage(ic))

        ui.txt2.setText(st)
        ui.txt2.setAlignment(QtCore.Qt.AlignTop)
        ui.txt2.setFont(QtGui.QFont('Times', 9))
        ui.txt2.move(30, 50)
    elif i == 3:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui.ic3.setPixmap(QtGui.QPixmap.fromImage(ic))

        ui.txt3.setText(st)
        ui.txt3.setAlignment(QtCore.Qt.AlignTop)
        ui.txt3.setFont(QtGui.QFont('Times', 9))
        ui.txt3.move(30, 50)
    elif i == 4:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui.ic4.setPixmap(QtGui.QPixmap.fromImage(ic))
        ui.txt4.setText(st)
        ui.txt4.setAlignment(QtCore.Qt.AlignTop)
        ui.txt4.setFont(QtGui.QFont('Times', 9))
        ui.txt4.move(30, 50)


def reguser():
    uname = reg.username.text()
    fullname = reg.fullname.text()
    email = reg.email.text()
    passw = reg.password.text()

    v = sc.register(fullname, uname, email, passw)
    print(v)
    if v == 0:
        er.errorm.settext("UserName already Taken")
        er.show()
    else:
        reg.close()


def logscr():
    log.show()


def regscr():
    reg.show()
    reg.save.clicked.connect(reguser)


def guestscr():
    prevg()
    guests1.next.clicked.connect(nextg)
    guests2.prev.clicked.connect(prevg)


def valuser():
    global pt
    global p
    uname = log.uname.text()
    print(uname)
    upass = log.upass.text()
    if uname == "" or upass == "":
        print("empty")
        er.errorm.settext("Enter Username or Password")

        er.show()



    else:
        v = sc.valid_login(uname, upass)
        print(v)
        # v=1

        if v == 1:
            log.close()
            p = sc.get_preferences(uname)
            pt = p
            print(pt)
            prev()
            # mtext = strc + '\n' + '\n' + strb + '\n' + '\n' + strn + '\n' + '\n' + strm + '\n' + '\n' +strq+ '\n' + '\n' +strw
            # mail2 = partial(uname,mtext)
            # ui.email.clicked.connect(mail2)
            pref2 = partial(pref, uname)
            ui.preferences.clicked.connect(pref2)
            # prev2 = partial(prev,p,p)
            # next2 = partial(nexts,p,pt)
            ui.next.clicked.connect(next)
            ui2.prev.clicked.connect(prev)


        else:
            er.errorm.settext("Enter Valid Username or Password")
            er.show()


wel.login.clicked.connect(logscr)
wel.reg.clicked.connect(regscr)
wel.guest.clicked.connect(guestscr)
log.log.clicked.connect(valuser)

wel.show()


def mail(u, m):
    sc.email(u, m)


def pref(u):
    pre.show()
    setpref2 = partial(setpref, u)
    pre.set.clicked.connect(setpref2)


def setpref(u):
    emlist = []
    if pre.cric.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    if pre.bill.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    if pre.news.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    if pre.mess.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    if pre.quote.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    if pre.weather.isChecked():
        emlist.append(1)
    else:
        emlist.append(0)
    print(emlist)
    sc.set_preferences(u, emlist)
    pre.close()


mic = QtGui.QImage('mainic.jpeg')
mic = mic.scaled(2500, 600, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)

ui.micon.setPixmap(QtGui.QPixmap.fromImage(mic))


# start

def prev():
    try:
        ui2.close()
    except:
        pass

    finally:
        global p
        global pt
        global strc
        global strb
        global strn
        global strm
        global strq
        global strw
        # print(p)
        # ui2.close()
        print("P - " + str(p))
        print("PT - " + str(pt))

        pt = p
        co = p.count(1)
        it = 1
        if p[0] == 1 and it < 5:
            print('cric')
            strc = sc.cricket()
            discp('cb1.jfif', strc, it)
            it += 1
            pt[0] = 2
        if p[1] == 1 and it < 5:
            strb = sc.billboard()
            discp('bill1.jfif', strb, it)
            it += 1
            pt[1] = 2
        if p[2] == 1 and it < 5:
            strn = sc.news()
            discp('toi1.jfif', strn, it)
            it += 1
            pt[2] = 2
        if p[3] == 1 and it < 5:
            strm = sc.mess_menu()
            discp('mm1.jfif', strm, it)
            it += 1
            pt[3] = 2
        if p[4] == 1 and it < 5:
            strq = sc.quote()
            discp('brq1.jfif', strq, it)
            it += 1
            pt[4] = 2
        if p[5] == 1 and it < 5:
            strw = sc.weather()
            discp('weather.jfif', strw, it)
            it += 1
            pt[4] = 2
        for p1 in range(0, 6):
            if it < 5:
                if p[p1] == 0 and p1 == 0:
                    discp('cb1.jfif', sc.cricket(), it)
                    it += 1
                    pt[p1] = 2
                    continue
                if p[p1] == 0 and p1 == 1:
                    discp('bill1.jfif', sc.billboard(), it)
                    it += 1
                    pt[p1] = 2
                    continue
                if p[p1] == 0 and p1 == 2:
                    discp('toi1.jfif', sc.news(), it)
                    it += 1
                    pt[p1] = 2
                    continue
                if p[p1] == 0 and p1 == 3:
                    discp('mm1.jfif', sc.mess_menu(), it)
                    it += 1
                    pt[p1] = 2
                    continue

                if p[p1] == 0 and p1 == 4:
                    discp('brq1.jfif', sc.quote(), it)
                    it += 1
                    pt[p1] = 2
                    continue
                if p[p1] == 0 and p1 == 5:
                    discp('weather.jfif', sc.weather(), it)
                    it += 1
                    pt[p1] = 2
        print("P -" + str(p))
        print("PT -" + str(pt))

        ui.show()


def discn(im, st, i):
    print('a')
    if i == 1:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui2.ic1.setPixmap(QtGui.QPixmap.fromImage(ic))

        ui2.txt1.setText(st)
        ui2.txt1.setAlignment(QtCore.Qt.AlignTop)
        ui2.txt1.setFont(QtGui.QFont('Times', 9))
        ui2.txt1.move(30, 50)
    elif i == 2:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        ui2.ic2.setPixmap(QtGui.QPixmap.fromImage(ic))

        ui2.txt2.setText(st)
        ui2.txt2.setAlignment(QtCore.Qt.AlignTop)
        ui2.txt2.setFont(QtGui.QFont('Times', 9))
        ui2.txt2.move(30, 50)


def next():
    global strc
    global strb
    global strn
    global strm
    global strq
    global strw
    global pt
    ite = 1
    print(pt)
    for p2 in range(0, 6):
        if pt[p2] == 2:
            continue
        if pt[p2] == 1 and p2 == 0:
            strc = sc.cricket()
            discn('cb1.jfif', strc, ite)
            ite += 1
        if pt[p2] == 1 and p2 == 1:
            strb = sc.billboard()
            discn('bill1.jfif', strb, ite)
            ite += 1
        if pt[p2] == 1 and p2 == 2:
            strn = sc.news()
            discn('toi1.jfif', strn, ite)
            ite += 1
        if pt[p2] == 1 and p2 == 3:
            strm = sc.mess_menu()
            discn('mm1.jfif', strm, ite)
            ite += 1
        if pt[p2] == 1 and p2 == 4:
            print('12345')
            strq = sc.quote()
            discn('brq1.jfif', strq, ite)
            ite += 1
        if pt[p2] == 1 and p2 == 5:
            strw = sc.weather()
            discn('weather.jfif', strw, ite)
            ite += 1

    for p1 in range(0, 6):
        if pt[p1] == 2:
            continue
        if pt[p1] == 0 and p1 == 0:
            discn('cb1.jfif', sc.cricket(), ite)
            ite += 1
        if pt[p1] == 0 and p1 == 1:
            discn('bill1.jfif', sc.billboard(), ite)
            ite += 1
        if pt[p1] == 0 and p1 == 2:
            discn('toi1.jfif', sc.news(), ite)
            ite += 1
        if pt[p1] == 0 and p1 == 3:
            discn('mm1.jfif', sc.mess_menu(), ite)
            ite += 1
        if pt[p1] == 0 and p1 == 4:
            discn('brq1.jfif', sc.quote(), ite)
            ite += 1
        if pt[p1] == 0 and p1 == 5:
            print('1234456')

            discn('weather.jfif', sc.weather(), ite)
            ite += 1
            print("P -" + str(p))
            print("PT -" + str(pt))
    ui.close()
    ui2.show()


# ui.next.clicked.connect(ui.close())

def discpg(im, st, i):
    if i == 1:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests1.ic1.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests1.txt1.setText(st)
        guests1.txt1.setAlignment(QtCore.Qt.AlignTop)
        guests1.txt1.setFont(QtGui.QFont('Times', 9))
        guests1.txt1.move(30, 50)
    elif i == 2:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests1.ic2.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests1.txt2.setText(st)
        guests1.txt2.setAlignment(QtCore.Qt.AlignTop)
        guests1.txt2.setFont(QtGui.QFont('Times', 9))
        guests1.txt2.move(30, 50)
    elif i == 3:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests1.ic3.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests1.txt3.setText(st)
        guests1.txt3.setAlignment(QtCore.Qt.AlignTop)
        guests1.txt3.setFont(QtGui.QFont('Times', 9))
        guests1.txt3.move(30, 50)
    elif i == 4:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests1.ic4.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests1.txt4.setText(st)
        guests1.txt4.setAlignment(QtCore.Qt.AlignTop)
        guests1.txt4.setFont(QtGui.QFont('Times', 9))
        guests1.txt4.move(30, 50)


def discng(im, st, i):
    if i == 1:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests2.ic1.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests2.txt1.setText(st)
        guests2.txt1.setAlignment(QtCore.Qt.AlignTop)
        guests2.txt1.setFont(QtGui.QFont('Times', 9))
        guests2.txt1.move(30, 50)
    elif i == 2:
        ic = QtGui.QImage(im)
        ic = ic.scaled(350, 25, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        guests2.ic2.setPixmap(QtGui.QPixmap.fromImage(ic))

        guests2.txt2.setText(st)
        guests2.txt2.setAlignment(QtCore.Qt.AlignTop)
        guests2.txt2.setFont(QtGui.QFont('Times', 9))
        guests2.txt2.move(30, 50)


def prevg():
    discpg('cb1.jfif', sc.cricket(), 1)
    discpg('bill1.jfif', sc.billboard(), 2)
    discpg('toi1.jfif', sc.news(), 3)
    discpg('mm1.jfif', sc.mess_menu(), 4)
    guests1.show()


def nextg():
    guests1.close()
    discng('brq1.jfif', sc.quote(), 1)
    discng('weather.jfif', sc.weather(), 2)
    guests2.show()


sys.exit(app.exec_())
