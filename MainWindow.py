import sys,os
from os.path import exists
import pandas as pd
pd.options.mode.chained_assignment = None
import serial
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from FirstUI import Ui_MainWindow
from SecondUI import Ui_Form
from Momo import MomoPayment
import threading,time,datetime
DURATION_INT = 100
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.dataItems = self.getDataItems()
        
        self.checkPayment = 0
        self.totalCost=0
        self.initButtonEvent()
        
    def show(self):
        # command to run
        self.main_win.show()
    #khởi tạo sự kiện nút nhấn
    def initButtonEvent(self):
        ##      Khung chọn hàng
        #Item 1
        self.uic.selectBtn1_1.clicked.connect(self.addItem)
        self.uic.addItem1_1.clicked.connect(self.addItem)
        self.uic.minusItem1_1.clicked.connect(self.addItem)
        #Item 2
        self.uic.selectBtn1_2.clicked.connect(self.addItem)
        self.uic.addItem1_2.clicked.connect(self.addItem)
        self.uic.minusItem1_2.clicked.connect(self.addItem)
        #item 3
        self.uic.selectBtn1_3.clicked.connect(self.addItem)
        self.uic.addItem1_3.clicked.connect(self.addItem)
        self.uic.minusItem1_3.clicked.connect(self.addItem)
        #item 4
        self.uic.selectBtn1_4.clicked.connect(self.addItem)
        self.uic.addItem1_4.clicked.connect(self.addItem)
        self.uic.minusItem1_4.clicked.connect(self.addItem)
        #item 5
        self.uic.selectBtn1_5.clicked.connect(self.addItem)
        self.uic.addItem1_5.clicked.connect(self.addItem)
        self.uic.minusItem1_5.clicked.connect(self.addItem)
        #item 6
        self.uic.selectBtn1_6.clicked.connect(self.addItem)
        self.uic.addItem1_6.clicked.connect(self.addItem)
        self.uic.minusItem1_6.clicked.connect(self.addItem)
        #item 7
        self.uic.selectBtn1_7.clicked.connect(self.addItem)
        self.uic.addItem1_7.clicked.connect(self.addItem)
        self.uic.minusItem1_7.clicked.connect(self.addItem)
        #item 8
        self.uic.selectBtn1_8.clicked.connect(self.addItem)
        self.uic.addItem1_8.clicked.connect(self.addItem)
        self.uic.minusItem1_8.clicked.connect(self.addItem)
        #item 9
        self.uic.selectBtn1_9.clicked.connect(self.addItem)
        self.uic.addItem1_9.clicked.connect(self.addItem)
        self.uic.minusItem1_9.clicked.connect(self.addItem)
        #item 10
        self.uic.selectBtn1_10.clicked.connect(self.addItem)
        self.uic.addItem1_10.clicked.connect(self.addItem)
        self.uic.minusItem1_10.clicked.connect(self.addItem)
        #item 11
        self.uic.selectBtn1_11.clicked.connect(self.addItem)
        self.uic.addItem1_11.clicked.connect(self.addItem)
        self.uic.minusItem1_11.clicked.connect(self.addItem)
        #item 12
        self.uic.selectBtn1_12.clicked.connect(self.addItem)
        self.uic.addItem1_12.clicked.connect(self.addItem)
        self.uic.minusItem1_12.clicked.connect(self.addItem)
        #item 13
        self.uic.selectBtn1_13.clicked.connect(self.addItem)
        self.uic.addItem1_13.clicked.connect(self.addItem)
        self.uic.minusItem1_13.clicked.connect(self.addItem)
        #item 14
        self.uic.selectBtn1_14.clicked.connect(self.addItem)
        self.uic.addItem1_14.clicked.connect(self.addItem)
        self.uic.minusItem1_14.clicked.connect(self.addItem)
        #item 15
        self.uic.selectBtn1_15.clicked.connect(self.addItem)
        self.uic.addItem1_15.clicked.connect(self.addItem)
        self.uic.minusItem1_15.clicked.connect(self.addItem)
        #item 16
        self.uic.selectBtn1_16.clicked.connect(self.addItem)
        self.uic.addItem1_16.clicked.connect(self.addItem)
        self.uic.minusItem1_16.clicked.connect(self.addItem)
        #item 17
        self.uic.selectBtn1_17.clicked.connect(self.addItem)
        self.uic.addItem1_17.clicked.connect(self.addItem)
        self.uic.minusItem1_17.clicked.connect(self.addItem)
        #item 18
        self.uic.selectBtn1_18.clicked.connect(self.addItem)
        self.uic.addItem1_18.clicked.connect(self.addItem)
        self.uic.minusItem1_18.clicked.connect(self.addItem)
        #item 19
        self.uic.selectBtn1_19.clicked.connect(self.addItem)
        self.uic.addItem1_19.clicked.connect(self.addItem)
        self.uic.minusItem1_19.clicked.connect(self.addItem)
        #item 20
        self.uic.selectBtn1_20.clicked.connect(self.addItem)
        self.uic.addItem1_20.clicked.connect(self.addItem)
        self.uic.minusItem1_20.clicked.connect(self.addItem)

        #mở màn hình thanh toán khi bấm nút thanh toán
        self.uic.payButton.clicked.connect(self.openPaymentDialog)
        #xóa giỏ hàng
        self.uic.cancelButton.clicked.connect(self.clearCart)

        self.uic.adjustFrame1.hide()
        self.uic.adjustFrame2.hide()
        self.uic.adjustFrame3.hide()
        self.uic.adjustFrame4.hide()
        self.uic.adjustFrame5.hide()
        self.uic.adjustFrame6.hide()
        self.uic.adjustFrame7.hide()
        self.uic.adjustFrame8.hide()
        self.uic.adjustFrame9.hide()
        self.uic.adjustFrame10.hide()
        self.uic.adjustFrame11.hide()
        self.uic.adjustFrame12.hide()
        self.uic.adjustFrame13.hide()
        self.uic.adjustFrame14.hide()
        self.uic.adjustFrame15.hide()
        self.uic.adjustFrame16.hide()
        self.uic.adjustFrame17.hide()
        self.uic.adjustFrame18.hide()
        self.uic.adjustFrame19.hide()
        self.uic.adjustFrame20.hide()
    #hàm lấy dữ liệu item 
    def getDataItems(self):
        df1 = pd.read_csv('StoreList\FoodItems.csv')
        df2 = pd.read_csv('StoreList\BeverageItems.csv')
        df3 = pd.read_csv('StoreList\otherItems.csv')
        df = pd.concat([df1,df2,df3])
        df.to_csv('StoreList\Items.csv')
        df = pd.read_csv('StoreList\Items.csv')
        return df
    #hàm thêm item muốn mua
    def addItem(self, item):
        buttonHandle = self.main_win.sender()
        buttonClicked = buttonHandle.objectName()
        print(buttonClicked)
        if buttonClicked.split('_')[0] ==  'selectBtn1' : #nhận dạng nút bấm
            #lấy tên item theo tên label
            itemSelectedIndex = int(''.join(filter(str.isdigit, buttonClicked[10:])))-1
            print(itemSelectedIndex)
            self.dataItems['Amount'][itemSelectedIndex] = self.dataItems['Amount'][itemSelectedIndex]+1
        elif buttonClicked.split('_')[0] == 'addItem1' : #nhận dạng nút bấm
            #lấy tên item theo tên label
            itemSelectedIndex = int(''.join(filter(str.isdigit, buttonClicked[8:])))-1
            print(itemSelectedIndex)
            self.dataItems['Amount'][itemSelectedIndex] = self.dataItems['Amount'][itemSelectedIndex]+1
        elif buttonClicked.split('_')[0] == 'minusItem1': #nhận dạng nút bấm
            #lấy tên item theo tên label
            itemSelectedIndex = int(''.join(filter(str.isdigit, buttonClicked[10:])))-1
            itemSelectedIndex = int(''.join(filter(str.isdigit, buttonClicked[10:])))-1
            print(itemSelectedIndex)
            if self.dataItems['Amount'][itemSelectedIndex] >0:
                self.dataItems['Amount'][itemSelectedIndex] = self.dataItems['Amount'][itemSelectedIndex]-1
            
        print(self.dataItems['Amount'])
        #self.sendDate2Hardware()
        #Hiện thi số lượng item
        self.displayAmount()
        self.addItemInCart()
        self.calculateCost()
    #hàm hiện thị số lượng item được chọn
    def displayAmount(self):
        if self.dataItems['Amount'][0] != 0:
            self.uic.adjustFrame1.show()
            self.uic.countItem1_1.setText(str(self.dataItems['Amount'][0]))
        else:
            self.uic.adjustFrame1.hide()

        if self.dataItems['Amount'][1] != 0:
            self.uic.adjustFrame2.show()
            self.uic.countItem1_2.setText(str(self.dataItems['Amount'][1]))
        else:
            self.uic.adjustFrame2.hide()
        if self.dataItems['Amount'][2] != 0:
            self.uic.adjustFrame3.show()
            self.uic.countItem1_3.setText(str(self.dataItems['Amount'][2]))
        else:
            self.uic.adjustFrame3.hide()
        if self.dataItems['Amount'][3] != 0:
            self.uic.adjustFrame4.show()
            self.uic.countItem1_4.setText(str(self.dataItems['Amount'][3]))
        else:
            self.uic.adjustFrame4.hide()
        if self.dataItems['Amount'][4] != 0:
            self.uic.adjustFrame5.show()
            self.uic.countItem1_5.setText(str(self.dataItems['Amount'][4]))
        else:
            self.uic.adjustFrame5.hide()
        if self.dataItems['Amount'][5] != 0:
            self.uic.adjustFrame6.show()
            self.uic.countItem1_6.setText(str(self.dataItems['Amount'][5]))
        else:
            self.uic.adjustFrame6.hide()
        if self.dataItems['Amount'][6] != 0:
            self.uic.adjustFrame7.show()
            self.uic.countItem1_7.setText(str(self.dataItems['Amount'][6]))
        else:
            self.uic.adjustFrame7.hide()
        if self.dataItems['Amount'][7] != 0:
            self.uic.adjustFrame8.show()
            self.uic.countItem1_8.setText(str(self.dataItems['Amount'][7]))
        else:
            self.uic.adjustFrame8.hide()
        if self.dataItems['Amount'][8] != 0:
            self.uic.adjustFrame9.show()
            self.uic.countItem1_9.setText(str(self.dataItems['Amount'][8]))
        else:
            self.uic.adjustFrame9.hide()
        if self.dataItems['Amount'][9] != 0:
            self.uic.adjustFrame10.show()
            self.uic.countItem1_10.setText(str(self.dataItems['Amount'][9]))
        else:
            self.uic.adjustFrame10.hide()
        if self.dataItems['Amount'][10] != 0:
            self.uic.adjustFrame11.show()
            self.uic.countItem1_11.setText(str(self.dataItems['Amount'][10]))
        else:
            self.uic.adjustFrame11.hide()
        if self.dataItems['Amount'][11] != 0:
            self.uic.adjustFrame12.show()
            self.uic.countItem1_12.setText(str(self.dataItems['Amount'][11]))
        else:
            self.uic.adjustFrame12.hide()
        if self.dataItems['Amount'][12] != 0:
            self.uic.adjustFrame13.show()
            self.uic.countItem1_13.setText(str(self.dataItems['Amount'][12]))
        else:
            self.uic.adjustFrame13.hide()
        if self.dataItems['Amount'][13] != 0:
            self.uic.adjustFrame14.show()
            self.uic.countItem1_14.setText(str(self.dataItems['Amount'][13]))
        else:
            self.uic.adjustFrame14.hide()
        if self.dataItems['Amount'][14] != 0:
            self.uic.adjustFrame15.show()
            self.uic.countItem1_15.setText(str(self.dataItems['Amount'][14]))
        else:
            self.uic.adjustFrame15.hide()
        if self.dataItems['Amount'][15] != 0:
            self.uic.adjustFrame16.show()
            self.uic.countItem1_16.setText(str(self.dataItems['Amount'][15]))
        else:
            self.uic.adjustFrame16.hide()
        if self.dataItems['Amount'][16] != 0:
            self.uic.adjustFrame17.show()
            self.uic.countItem1_17.setText(str(self.dataItems['Amount'][16]))
        else:
            self.uic.adjustFrame17.hide()
        if self.dataItems['Amount'][17] != 0:
            self.uic.adjustFrame18.show()
            self.uic.countItem1_18.setText(str(self.dataItems['Amount'][17]))
        else:
            self.uic.adjustFrame18.hide()
        if self.dataItems['Amount'][18] != 0:
            self.uic.adjustFrame19.show()
            self.uic.countItem1_19.setText(str(self.dataItems['Amount'][18]))
        else:
            self.uic.adjustFrame19.hide()
        if self.dataItems['Amount'][19] != 0:
            self.uic.adjustFrame20.show()
            self.uic.countItem1_20.setText(str(self.dataItems['Amount'][19]))
        else:
            self.uic.adjustFrame20.hide()
         
    #hàm hiện thị thêm hàng đợi
    def addItemInCart(self):
        self.uic.nameItemList.clear()
        self.uic.amountItemList.clear()
        self.uic.costItemList.clear()
        for index in self.dataItems.index:
            if self.dataItems['Amount'][index] != 0:
                self.uic.nameItemList.addItem(str(self.dataItems['Name'][index]))
                self.uic.amountItemList.addItem("x "+str(self.dataItems['Amount'][index]))
                self.uic.costItemList.addItem(str(self.dataItems['Cost'][index]*self.dataItems['Amount'][index]))
        
    #hàm tính tổng tiền phải trả    
    def calculateCost(self):
        self.dataItems['TotalCost'] = self.dataItems['Amount']*self.dataItems['Cost']
        self.totalCost = self.dataItems['TotalCost'].sum()
        self.uic.totalCost.setText(str(self.dataItems['TotalCost'].sum()) )
    #hiện thị mã QR thanh toán
    def openPaymentDialog(self):
        if self.totalCost != 0 :
            self.paymentWindow = QtWidgets.QWidget()
            self.uic2 = Ui_Form()
            self.uic2.setupUi(self.paymentWindow)
            self.paymentWindow.show()
            self.uic2.cancelPay.clicked.connect(self.closePaymentDialog)
            self.momo = MomoPayment(self.totalCost)
            self.momo.requestQRCode()
            self.uic2.label.setPixmap(QtGui.QPixmap("qr.png")) 
            self.timer_start()
            self.update_gui()
    #đóng thanh toán
    def closePaymentDialog(self):
        self.paymentWindow.close()
        self.my_qtimer.stop()
        os.remove("qr.png")
    #xóa giỏ hàng 
    def clearCart(self):
        self.totalCost = 0
        self.uic.totalCost.setText(str(self.totalCost)) 
        self.dataItems['Amount']=0
        self.displayAmount()
        self.addItemInCart()
    #Hàm thời gian và kiểm tra giao dịch
    def timer_start(self):
        self.time_left_int = DURATION_INT

        self.my_qtimer = QtCore.QTimer()
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()
    def timer_timeout(self):
        self.time_left_int -= 1
        #self.momo.checkPayment()
        if self.time_left_int < 0:
            self.time_left_int = DURATION_INT
            self.paymentWindow.close()
            self.my_qtimer.stop()
        elif self.time_left_int >0 and self.momo.success_payment != True:
            self.momo.checkPayment()
            #self.exportLogs(self.momo.log)
        self.update_gui()
    def update_gui(self):
        self.uic2.timeLabel.setText(str(int(self.time_left_int/60)) +":"+str(self.time_left_int%60))
        if self.momo.success_payment ==True :
            self.uic2.label_4.setStyleSheet("background-color: rgb(85, 255, 0);color: rgb(255, 255, 255);")
            self.uic2.label_4.setText("Thanh toán thành công")
            self.exportLogs(self.momo.log)
            time.sleep(2)
            self.my_qtimer.stop()
            self.sendDate2Hardware()
            self.clearCart()
            self.momo.success_payment = False
            self.paymentWindow.close()
    #lưu nhật kí
    def exportLogs(self,log):
        header_log = ['Name',"Amount","Time"]
        currentDateTime = datetime.datetime.now().strftime("%m-%d-%Y")
        logPath = f"logs\{currentDateTime}.csv"
        file_exists = exists(logPath)
        if file_exists :
            df = pd.read_csv(logPath)
            print(df)
            df.loc[len(df.index)] = log
            print(df)
            df.to_csv(logPath, encoding='utf-8',header = header_log , index =False)
        else:
            df = pd.DataFrame([log])
            df.to_csv(logPath, encoding='utf-8',header = header_log , index =False)
    #hàm gửi data xuống phần cứng
    def sendDate2Hardware(self):
        serialData='&'
        for amount in self.dataItems['Amount']:
            serialData = serialData + str(amount)+':'
        serialData = serialData + "#"
        print (serialData)
        try:
            hardware = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
            while True:
                hardware.write(serialData.encode())
                time.sleep(0.05)
                data = hardware.readline(2)
                if data == 'OK':
                    break
        except:
            print ("Không thể kết nối với cổng COM!")
