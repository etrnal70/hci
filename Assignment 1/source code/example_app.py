import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

def Nuclear():
    msgbox = tk.messagebox.askquestion('NUCLEAR ALERTS', 'ARE YOU SURE TO ALERT NUCLEAR ALARM?', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'NUCLEAR ALARM HAS BEEN ALERTED')

def AmberAlertState():
    msgbox = tk.messagebox.askquestion('AMBER ALERT STATE ', 'ARE YOU SURE TO ACTIVATE AMBER ALERT STATE ', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'AMBER ALERTED STATE ALARM HAS BEEN ALERTED')

def AmberAlertKauai():
    msgbox = tk.messagebox.askquestion('AMBER ALERT KAUAI COUNTRY ALERTS', 'ARE YOU SURE TO ACTIVATE AMBER ALERT KAUAI COUNTRY ?', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'AMBER ALERT KAUAI COUNTRY ALARM HAS BEEN ALERTED')

def TsunamiWarning():
    msgbox = tk.messagebox.askquestion('TSUNAMI WARNING ALERTS', 'ARE YOU SURE TO ALERT TSUNAMI WARNING ALARM?', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'TSUNAMI WARNING ALARM HAS BEEN ALERTED')

def HighSurfWarning():
    msgbox = tk.messagebox.askquestion('HIGH SURF WARNING ALERTS', 'ARE YOU SURE TO ALERT HIGH SURF WARNING ALARM?', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'HIGH SURF WARNING ALARM HAS BEEN ALERTED')

def Landslide():
    msgbox = tk.messagebox.askquestion('LANDSLIDE ALERTS', 'ARE YOU SURE TO ALERT LANDSLIDE ALARM?', icon='warning')
    if msgbox == 'yes':
        tk.messagebox.showwarning('Alarm Alerted', 'LANDSLIDE ALARM HAS BEEN ALERTED')

def DrillPacom():
    msgbox = tk.messagebox.askquestion('(DRILL) PACOM ALERTS', 'ARE YOU SURE TO ALERT (DRILL) PACOM ALARM?', icon='info')
    if msgbox == 'yes':
        tk.messagebox.showinfo('Alarm Alerted', '(DRILL) PACOM ALARM HAS BEEN ALERTED')

def TestAmber():
    msgbox = tk.messagebox.askquestion('(TEST) AMBER ALERT', 'ARE YOU SURE TO ALERT (TEST) AMBER ALERT ALARM?', icon='info')
    if msgbox == 'yes':
        tk.messagebox.showinfo('Alarm Alerted', '(TEST) AMBER ALERT ALARM HAS BEEN ALERTED')

def TestTsunami():
    msgbox = tk.messagebox.askquestion('(TEST) TSUNAMI WARNING ALERTS', 'ARE YOU SURE TO ALERT (TEST) TSUNAMI WARNING ALARM?', icon='info')
    if msgbox == 'yes':
        tk.messagebox.showinfo('Alarm Alerted', '(TEST) TSUNAMI WARNING ALARM HAS BEEN ALERTED')
    
def CancelAlarm():
    msgbox = tk.messagebox.askquestion('CANCEL ALARM', 'ARE YOU SURE TO CANCEL THE ALERT?', icon='info')
    if msgbox == 'yes':
        tk.messagebox.showinfo('Alarm Canceled', 'ALARM HAS BEEN CANCELED')
    

#create object
root = tk.Tk(className='Python Examples - Window Color')
root.iconbitmap("AlaramIcon.ico")

#create Font
TitleFont = tkFont.Font(family="Trebuchet MS", size=22, weight="bold")

#create title
root.title("Hawaii False Alarm")
root.geometry("1250x660")
root['bg']="#f39292"

# Create label title
titleLabel = tk.Label(root, text='Hawaii Command Alerts', font=TitleFont, bg='#69ADC6', borderwidth=5, relief="solid")
titleLabel.place(x=640,y=50, anchor='center',height=60, width=400)

#Create Label 1 
LabelTitle1 = tk.Label(root,bg='red', text='Nuclear Alerts',  font=TitleFont, borderwidth=4, relief="ridge")
LabelTitle1.place(height=115,width=300,x=10,y=100)
Label1 = tk.Label(root,bg='purple', borderwidth=4, relief="ridge")
Label1.place(height=345,width=300,x=10,y=215)

#create Label 2
LabelTitle2 = tk.Label(root,bg='yellow', text='Amber Alerts',  font=TitleFont, borderwidth=4, relief="ridge")
LabelTitle2.place(height=115,width=300,x=320,y=100)
Label2 = tk.Label(root,bg='purple', borderwidth=4, relief="ridge")
Label2.place(height=345,width=300,x=320,y=215)

#create Label 3
LabelTitle3 = tk.Label(root,bg='cyan', text='Weather Alerts',  font=TitleFont, borderwidth=4, relief="ridge")
LabelTitle3.place(height=115,width=300,x=630,y=100)
Label3 = tk.Label(root,bg='purple', borderwidth=4, relief="ridge")
Label3.place(height=345,width=300,x=630,y=215)

#create Label 4
LabelTitle4 = tk.Label(root,bg='green', text='Drill/Tests',  font=TitleFont, borderwidth=4, relief="ridge")
LabelTitle4.place(height=115,width=300,x=940,y=100)
Label4 = tk.Label(root,bg='purple', borderwidth=4, relief="ridge")
Label4.place(height=345,width=300,x=940,y=215)


#---------------------create Button-----------------------

#label1
PacomButton = tk.Button(root, text="PACOM - State", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=Nuclear)
PacomButton.place(height=75, width=260, x=30, y=235)


#label2
AmberAlertStateButton = tk.Button(root, text="Amber Alert - State", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=AmberAlertState)
AmberAlertStateButton.place(height=75, width=260, x=340, y=235)

AmberAlertKauaiButton = tk.Button(root, text="Amber Alert - Kauai Country", font=("Trebuchet MS", 14), borderwidth=10, relief="raised", command=AmberAlertKauai)
AmberAlertKauaiButton.place(height=75, width=260, x=340, y=350)

#label3
TsunamiWarningButton = tk.Button(root, text="Tsunami Warning - State", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=TsunamiWarning)
TsunamiWarningButton.place(height=75, width=260, x=650, y=235)

HighSurfWarningButton = tk.Button(root, text="High Surf Warning - Shores", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=HighSurfWarning)
HighSurfWarningButton.place(height=75, width=260, x=650, y=350)

LandslideButton = tk.Button(root, text="Landslide - Road Closure", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=Landslide)
LandslideButton.place(height=75, width=260, x=650, y=465)

#label4
DrillPacomButton = tk.Button(root, text="(DRILL) PACOM - State", font=("Trebuchet MS", 14), borderwidth=12, relief="raised", command=DrillPacom)
DrillPacomButton.place(height=75, width=260, x=960, y=235)

TestAmberAlertButton = tk.Button(root, text="(TEST) AMBER Alert", font=("Trebuchet MS", 14), borderwidth=12, relief="raised",command=TestAmber)
TestAmberAlertButton.place(height=75, width=260, x=960, y=350)

TestTsunamiWarningButton = tk.Button(root, text="(TEST) Tsunami Warning", font=("Trebuchet MS", 14), borderwidth=12, relief="raised",command=TestTsunami)
TestTsunamiWarningButton.place(height=75, width=260, x=960, y=465)

#CancelAlarm
cancelButton = tk.Button(root, text='BMD False Alarm', font=('bold', 18), bg='#F4B400', borderwidth=12, relief="raised", command=CancelAlarm, fg="red")
cancelButton.place(x=620,y=610, anchor='center',height=60, width=230)

#Start Apps
root.mainloop()

