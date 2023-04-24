import string
import threading
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Gui import *
import timeit
from multiprocessing import Process

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()
sayacVeri = 0
sayacThread = 0
stop_words = set(stopwords.words('english'))
file = open("rows2.csv","r")
list = file.readlines()
file.close()
veriAdedi = 0
index = []
combo = ""
ortak = 0
thread = 0
girilenOran = 0

def benzerlik(t1,t2):
    list1 = t1.split()
    list2 = t2.split()
    ortak = 0
    uzunluk = 0
    kelime = []

    for i in list1:
        if i in list2:
            if i not in kelime:
                kelime.append(i)
                if list1.count(i) == list2.count(i):
                    ortak += list1.count(i)
                elif list1.count(i) < list2.count(i):
                    ortak += list1.count(i)
                else:
                    ortak += list2.count(i)

    if len(list1) > len(list2):
        uzunluk = len(list1)
    else:
        uzunluk = len(list2)

    oran = (ortak/uzunluk)*100
    return oran

def VerileriOlustur():
    #file = open("rows.csv", "r")
    #list = file.readlines()
    #file.close()
    #file = open("rows2.csv", "w")
    for i in list:
        while i.find("\"") != -1:
            j = i.find("\"")
            try:
                i = i[0:j] + '' + i[j + 1:]
                while 1:
                    j += 1
                    if (i[j] == ","):
                        i = i[0:j] + '' + i[j + 1:]
                    elif (i[j] == "\""):
                        i = i[0:j] + '' + i[j + 1:]
                        break
            except: pass

        a = i.rsplit(",")
        try:
            if not (a[1] == "" or a[3] == "" or a[7] == "" or a[8] == "" or a[9] == "" or a[17] == ""):
                product = ""
                issue = ""
                company = a[7]
                state = a[8]
                zipCode = a[9]
                complaintID = a[17]

                word_tokens = word_tokenize(a[1])
                for w in word_tokens:
                    if w not in stop_words:
                        product = product + " " + w
                word_tokens = word_tokenize(a[3])
                for w in word_tokens:
                    if w not in stop_words:
                        issue = issue + " " + w

                list2 = [product.strip(), issue.strip(), company, state, zipCode, complaintID]
                veriler = []
                for k in list2:
                    word = k.split()
                    table = str.maketrans("", "", string.punctuation)
                    stripped = [w.translate(table) for w in word]
                    str = " ".join(stripped)
                    veriler.append(str)

                text = veriler[0] + "," + veriler[1] + "," + veriler[2] + "," + veriler[3] + "," + veriler[4] + "," + veriler[5] + "\n"
                if text.count("XXX") == 0:
                    print(text)
                    #file.write(text)
        except: pass
    #file.close()

def fonk(i,k,th):
    global sayacVeri, sayacThread, combo, veriAdedi, index, ortak, thread, girilenOran

    try:
        control = 0
        start = timeit.default_timer()
        if thread == 0:
            dongu = len(list)
        else:
            dongu = int(th * (len(list) / thread))
        while (i < dongu) and (sayacVeri <= veriAdedi):
            if k == 0:
                control = 1
            while (k < len(list)) and (sayacVeri <= veriAdedi):
                veri1 = list[i].rsplit(",")
                veri2 = list[k].rsplit(",")
                text1 = ""
                text2 = ""
                if ortak != -1:
                    if veri1[ortak] != veri2[ortak]:
                        k += 1
                        continue

                if len(index) != 0:
                    for j in index:
                        text1 += veri1[j] + " "
                        text2 += veri2[j] + " "

                oran = int(benzerlik(text1, text2))

                if oran >= girilenOran:
                    # print(text1, text2, oran)
                    # print("*********************************************************************************")
                    print(sayacVeri)
                    for q in range(6):
                        ui.Tableveriler.setItem(sayacVeri, q, QTableWidgetItem(veri1[q]))
                        ui.Tableveriler.setItem(sayacVeri, q + 6, QTableWidgetItem(veri2[q]))
                    ui.Tableveriler.setItem(sayacVeri, 12, QTableWidgetItem(str(oran)))
                    sayacVeri += 1
                k += 1

            if control == 1:
                break
            i += 1
            k = i + 1

        stop = timeit.default_timer()
        if thread != 0:
            ui.Tabtime.setItem(0, th, QTableWidgetItem(str(stop - start)))
        ui.statusbar.clearMessage()
        ui.statusbar.showMessage("Veri aktarımı başarılı.", 100000000)
    except Exception as error: print(error)

def TabloOlustur():
    try:
        global sayacThread, combo, veriAdedi, index, ortak, thread, girilenOran
        start = timeit.default_timer()
        veriAdedi = int(ui.Lineveriadeti.text())
        girilenOran = int(ui.Linebenzerlik.text())
        combo = ui.comboOrtak.currentText()
        thread = int(ui.Linethread.text())
        ortak = int(combo[0]) - 2
        if ui.Checkproduct.isChecked():
            index.append(0)
        if ui.Checkissue.isChecked():
            index.append(1)
        if ui.Checkstate.isChecked():
            index.append(2)
        if ui.Checkcompany.isChecked():
            index.append(3)
        if ui.Checkzipcode.isChecked():
            index.append(4)
        if ui.Checkcomplaintid.isChecked():
            index.append(5)

        ui.statusbar.clearMessage()
        ui.statusbar.showMessage("Lütfen bekleyiniz...", 100000000)

        ui.Tabtime.clear()
        ui.Tabtime.setHorizontalHeaderLabels(("Total_Time", "Thread_1", "Thread_2", "Thread_3", "Thread_4", "Thread_5",
                                              "Thread_6", "Thread_7", "Thread_8",))
        if ui.Lineveriadeti.text() == "" or ui.Linebenzerlik == "" or ui.Linethread.text() == "" or ui.comboOrtak.currentText() == "":
            ui.statusbar.showMessage("Tüm alanları doldurun !!!!",10000)
        else:
            global sayacVeri
            veriAdedi = int(ui.Lineveriadeti.text())
            sayacVeri = 0
            ui.Tableveriler.clear()
            ui.Tableveriler.setHorizontalHeaderLabels(("Product_1", "Issue_1", "Company_1", "State_1", "ZipCode_1",
                                                       "complaintID_1", "Product_2", "Issue_2", "Company_2", "State_2",
                                                       "ZipCode_2", "complaintID_2", "Oran"))
            i = 1
            thread = int(ui.Linethread.text())
            cmp = ui.Linecomplaint.text()
            if cmp != "":
                while (i < len(list)) and (sayacVeri <= veriAdedi):
                    veri = list[i].rsplit(",")
                    if cmp == veri[5].strip():
                        if thread == 0:
                            fonk(i, 0, 0)
                        else:
                            threading.Thread(target=fonk, args=(i, 0, thread,)).start()
                        break
                    i += 1
            else:
                if thread == 0:
                    fonk(1,2,0)
                else:
                    j = 0
                    threads = []
                    dongu = int(len(list) / thread)
                    while j < thread:
                        sayacThread = 0
                        threads.append(threading.Thread(target=fonk, args=(i + (dongu * j), i + (dongu * j) + 1, j+1,)))
                        j += 1
                    sayacThread = 0
                    for k in threads:
                        k.start()
                        sayacThread += 1
                    for k in threads:
                        k.join()
        stop = timeit.default_timer()
        ui.Tabtime.setItem(0, 0, QTableWidgetItem(str(stop - start)))
    except Exception as error: print(error)

ui.BtnShow.clicked.connect(TabloOlustur)

sys.exit(uygulama.exec_())