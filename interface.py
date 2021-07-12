from tkinter import *
import tkinter.ttk as ttk
import cv2
from datetime import datetime, date
from tkinter import *
from PIL import ImageTk ,Image
import webbrowser
import calendar
import serial
import threading
messp ,mess = None,None
import time
import smtplib, ssl
lf=0
path = 'data/'
message1 = """\
Subject: Hi there



This message is sent from Python."""
message2 = """\
Subject: Hi there



This message is sent from Python."""
message3 = """\
Subject: Hi there



This message is sent from Python."""
message4 = """\
Subject: Hi there



This message is sent from Python."""

try:
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.1)
    time.sleep(1)
    print("arduino connected")
except:
    print("error in connecting with arduino")
def sendEmail(message,receiver_email):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "abderrahman1koutit@gmail.com"
    password = "......"  # write yr password here

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("done mail")

def switch():
    global lf
    if lf==0:
        print(0)
        lb.config(text="<<")
        lf61.grid_remove()
        lf62.grid(row=0, column=0)
        lf=1
    else:
        lb.config(text=">>")
        lf62.grid_remove()
        lf61.grid(row=0, column=0)
        lf=0

def aya():
    global mess, data, messp
    while True:
        mess =str(int(p1.state))+";"+str(l1.au)+";"+str(int(l1.state))+";"+str(l1.value)+";"+str(int(f1.state))+"\n"
        if mess == messp:
            try:
                data = arduino.readline()
                data = data.decode("utf8").strip()
                l = data.split(';')
                if len(l)==12:
                    l1.w.set(int(l[0]))
            except:
                pass
        else:
            arduino.write(bytes(str(mess), 'ascii'))
            print("j")
        messp = mess
def OpenUrl():
    webbrowser.open_new('https://weather.com/fr-MA/temps/aujour/l/32.24,-7.95?par=google')


# Interface
class lumiere :
    def __init__(self, frame,row, column, path0, path1,type):
        self.frame = frame
        self.row = row
        self.column = column
        self.path0=path0
        self.path1 = path1
        self.state=False
        self.value=0
        self.au=0
        imag = Image.open(self.path0)
        resize_image = imag.resize((200, 60))
        self.img = ImageTk.PhotoImage(resize_image)
        self.b = Button(self.frame, image=self.img, command=self.update,borderwidth=10)
        self.b.grid(row=self.row, column=self.column,pady=5,padx=50, sticky=W)
        self.b['state']=type
        self.frame.config(borderwidth=0)
        self.w = Scale(self.frame, from_=0, to=10,length=60,sliderlength=5,bg='white', command=self.a)
        self.w.set(5)
        self.w.grid(row=self.row, column=self.column-1,pady=0,padx=0)

    def update(self):
        self.au=0
        self.state= not self.state
        if self.state==False:
            imag = Image.open(self.path0)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        else:
            imag = Image.open(self.path1)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        self.b.config(image=self.img)
    def a(self,value):
        self.au=1
        self.value=value
class clima:
    def __init__(self, fram, row, column,text):
        self.row = row
        self.column = column
        self.text = text
        self.fram = fram
        self.t1=20
        self.t2=25
        #self.frame2 = Frame(self.fram,bg="white")
        #self.frame2.grid(row=self.row, column=self.column,pady=20)
        self.l = Label(self.fram,text=self.text,bg="white",font=("Calibri Light", "20"))
        self.l.grid(row=self.row,column=self.column,sticky=W,columnspan=2,padx=50,pady=10)
        self.lt = Label(self.fram,text="T ambiante :",bg="white",font=("Calibri Light", "13"))
        self.lt.grid(row=self.row+1,column=self.column+1,sticky=W)
        self.e = Entry(self.fram,width=5,background='white')
        self.e.insert(0,str(self.t1))
        self.e.config(state=DISABLED)
        self.e.grid(row=self.row+1,column=self.column+2)
        self.lt = Label(self.fram,text="Régler la température  : ",bg="white",font=("Calibri Light", "13"))
        self.lt.grid(row=self.row+2,column=self.column+1,sticky=W)
        self.e2 = Entry(self.fram,justify=CENTER,width=5,bg='white')
        self.e2.insert(0,str(self.t1))
        self.e2.grid(row=self.row+2,column=self.column+2,pady=15)
        self.fram.config(borderwidth=0)


class B :
    def __init__(self, frame,row, column, path0, path1,type):
        self.frame = frame
        self.row = row
        self.column = column
        self.path0=path0
        self.path1 = path1
        self.state=0
        self.imagg = Image.open(self.path0)
        resize_image = self.imagg.resize((200, 60))
        self.img = ImageTk.PhotoImage(resize_image)
        self.b = Button(self.frame, image=self.img, command=self.update,borderwidth=10)
        self.b.grid(row=self.row, column=self.column,pady=5,padx=50)
        self.b['state']=type
        self.frame.config(borderwidth=0)


    def update(self):
        self.state= not self.state
        if self.state==False:
            imag = Image.open(self.path0)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        else:
            imag = Image.open(self.path1)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        self.b.config(image=self.img)


class F:
    def __init__(self, frame, row, column, path0, path1, type):
        self.frame = frame
        self.row = row
        self.column = column
        self.path0 = path0
        self.path1 = path1
        self.state = False
        self.imagg = Image.open(self.path0)
        resize_image = self.imagg.resize((200, 60))
        self.img = ImageTk.PhotoImage(resize_image)
        self.b = Button(self.frame, image=self.img, command=self.update, borderwidth=10)
        self.b.grid(row=self.row, column=self.column, pady=5, padx=50)
        self.b['state'] = type
        self.frame.config(borderwidth=0)
        self.w = Scale(self.frame, from_=0, to=90, length=60, sliderlength=5, bg='white')
        self.w.grid(row=self.row, column=self.column - 1, pady=0, padx=0)

    def update(self):
        self.state = not self.state
        if self.state == False:
            imag = Image.open(self.path0)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        else:
            imag = Image.open(self.path1)
            resize_image = imag.resize((200, 60))
            self.img = ImageTk.PhotoImage(resize_image)
        self.b.config(image=self.img)

def h() :
    frame1.grid(row=0, column=2, sticky=N, pady=5)
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()
    frame6.grid_remove()
    #frame7.grid_remove()
    label_title1 = Label(frame1, text=" Welcome to GO SMART ", font=("Arial Black", 35), bg='White')
    label_title1.grid(row=0,column=0,sticky=N,columnspan=50,padx=10)
    frame8 = Frame(frame1, width=100, height=100, background="white")
    frame8.grid(row=1, column=0, sticky=N)
    def update():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        day = now.strftime("%D")
        curr_date = date.today()
        jr = calendar.day_name[curr_date.weekday()]
        ltime.config(text=current_time, font=("Helvetica", "65"))
        d.config(text=jr + " " + day, font=("Helvetica", "25"))
        root.after(1000, update)
    ltime = Label(frame8, text="No_data", background="white")
    ltime.grid(row=1, column=0, columnspan=3,pady=20,padx=10)
    d = Label(frame8, text='NONE', fg='gray', background="white")
    d.grid(row=2, column=0, columnspan=3)
    #ima = Label(frame1, text="hello", image=im)
    #ima.grid(row=3,column=0,columnspan=3)
    vt = Label(frame8, text="11°C , Benguerir", background="white", font=("Helvetica", "20"),fg='#EDB92F')
    vt.grid(row=3, column=1,pady=15)
    update()

def l() :
    frame1.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()
    frame6.grid_remove()
    frame2.grid(row=0, column=2,padx=80)
    label_title2 = Label(frame2, text=" Lumière : ", font=("Cambria",35 ), bg='White')
    label_title2.grid(row=0,column=0,columnspan=4,sticky=S,padx=20,pady=25)

def f() :
    frame1.grid_remove()
    frame2.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()
    frame6.grid_remove()
    frame3.grid(row=0, column=2,padx=80,sticky=N,pady=10)
    label_title3 = Label(frame3, text=" Fenêtres : ", font=("Cambria", 35), bg='White')
    label_title3.grid(row=0, column=0, columnspan=4, pady=50)



def p() :
    frame4.grid(row=0, column=2,sticky=N,pady=20,padx=100)
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()
    frame5.grid_remove()
    frame6.grid_remove()
    label_title3 = Label(frame4, text=" Portes : ", font=("Cambria", 35), bg='White')
    label_title3.grid(row=0, column=0,columnspan=2,pady=50,sticky=S,padx=20)


def c() :
    frame5.grid(row=0, column=2)
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame6.grid_remove()
    label_title3 = Label(frame5, text=" Climatisation : ", font=("Cambria", 35), bg='White')
    label_title3.grid(row=0, column=0, columnspan=7, pady=5)



def i() :
    frame6.grid(row=0, column=2)
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()


#creer une fenetre
root = Tk()

#personnaliser cette fenêtre
root.title("GO-SMART")
root.geometry('990x720')
root.config(background='white')
frame7 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame7.place(x=135,y=0)
frame = LabelFrame(root, height=720, width=130, highlightcolor="black")
frame.grid(row=0,column=0)

image = Image.open(path+'hh.png')
image = image.resize((130, 113))
home=ImageTk.PhotoImage(image)
b1 = Button(frame,image=home,command=h)
b1.grid(row=0,column=0)

image1 = Image.open(path +'ll.png')
image1 = image1.resize((130, 113))
luminosite = ImageTk.PhotoImage(image1)
b2 = Button(frame,image=luminosite,command=l)
b2.grid(row=1,column=0)

image2 = Image.open(path +'ff.png')
image2 = image2.resize((130, 113))
Fenetres = ImageTk.PhotoImage(image2)
b3 = Button(frame,image=Fenetres,command=f)
b3.grid(row=2,column=0)

image3 = Image.open(path +'p.png')
image3 = image3.resize((130, 113))
Portes = ImageTk.PhotoImage(image3)
b4 = Button(frame,image=Portes ,command=p)
b4.grid(row=3,column=0)

image4 = Image.open(path +'cc.png')
image4 = image4.resize((130, 113))
Climatisation = ImageTk.PhotoImage(image4)
b6 = Button(frame,image=Climatisation ,command=c)
b6.grid(row=4,column=0)

image5 = Image.open(path +'nn.png')
image5 = image5.resize((130, 113))
info = ImageTk.PhotoImage(image5)
b5 = Button(frame,image=info ,highlightcolor='black',command=i )
b5.grid(row=5,column=0)

frame1 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame1.grid(row=0,column=2,sticky=N,padx=15,pady=5)


frame9 = LabelFrame(frame1, height=50, width=500,highlightcolor="black")
frame9.grid(row=6,column=0)
frame10 = LabelFrame(frame1, height=250, width=360,highlightcolor="black",bg='white')
frame10.place(x=436,y=400)
i = Image.open(path +'RC.jpeg')
i = i.resize((350, 300))
d = ImageTk.PhotoImage(i)
dare = Label(frame1, image=d)
dare.grid(row=1, column=3,padx=75,pady=20,rowspan=3,sticky=NE)

h1= B(frame1, 2, 0, path +'AF.png',path +'AO.png', NORMAL)
h2= B(frame1, 3, 0, path +'QF.png',path +'QO.png', NORMAL)
h3= B(frame1, 4, 0, path +'VF.png',path +'VO.png', NORMAL)

ii3 = Image.open(path +'FEU.png')
ii3 = ii3.resize((50, 50))
iii3 = ImageTk.PhotoImage(ii3)
h4 = Button(frame9, image=iii3,command=lambda:sendEmail(message1,"Aya.BENTOUMIA@emines.um6p.ma") )
h4.grid(row=6, column=0)

ii4 = Image.open(path +'br.png')
ii4 = ii4.resize((50, 50))
iii4 = ImageTk.PhotoImage(ii4)
h5 = Button(frame9, image=iii4,command=lambda:sendEmail(message2,"Aya.BENTOUMIA@emines.um6p.ma"))
h5.grid(row=6, column=2)

ii5 = Image.open(path +'notiff.png')
ii5 = ii5.resize((50, 50))
iii5 = ImageTk.PhotoImage(ii5)
h6 = Button(frame9, image=iii5)
h6.grid(row=6, column=4)

ii6 = Image.open(path +'pom.jpg')
ii6 = ii6.resize((50, 50))
iii6 = ImageTk.PhotoImage(ii6)
h7 = Button(frame9, image=iii6,command=lambda:sendEmail(message4,"Aya.BENTOUMIA@emines.um6p.ma"))
h7.grid(row=6, column=6)



frame2 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame2.grid(row=0,column=2,sticky=N,pady=10)

frame3 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame3.grid(row=0,column=2)

frame4 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame4.grid(row=0,column=2)

frame5 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame5.grid(row=0,column=2)

frame6 = LabelFrame(root, height=720, width=850, highlightcolor="black",background="white")
frame6.grid(row=0,column=2)

im = ImageTk.PhotoImage(Image.open(path +'w1.png'))

im1 = Image.open(path +'CGN.png')
im1 = im1.resize((70, 70))
cc1 = ImageTk.PhotoImage(im1)
ccc1 = Button(frame5, image=cc1)
ccc1.grid(row=10,column=1,pady=25)
label1 = Label( frame5, text="Désactiver le climatiseur" ,font=("Calibri Light", "12"),bg='white')
label1.grid(row=11,column=1)
im2 = Image.open(path +'CGM.png')
im2 = im2.resize((70, 70))
cc2 = ImageTk.PhotoImage(im2)
ccc2 = Button(frame5, image=cc2)
ccc2.grid(row=10, column=3,pady=25)
label2 = Label( frame5, text="Vitesse moyenne" ,font=("Calibri Light", "12"),bg='white')
label2.grid(row=11,column=3)
im3 = Image.open(path +'CGC.png')
im3 = im3.resize((70, 70))
cc3 = ImageTk.PhotoImage(im3)
ccc3 = Button(frame5, image=cc3)
ccc3.grid(row=10, column=5,pady=25)
label3 = Label( frame5, text="Vitesse Forte" ,font=("Calibri Light", "12"),bg='white')
label3.grid(row=11,column=5)

p1 = B(frame4, 1, 0, path +'EF.png',path +'EO.png', NORMAL)
p2 = B(frame4, 2, 0, path +'Garage F.png',path +'Garage O.png', NORMAL)
p3 = B(frame4, 3, 0, path +'chambre 1 F.png',path +'Chambre 1 O.png', NORMAL)
# p4 = B(frame4, 4, 0, path +'BF.png',path +'BO.png', NORMAL)
p5 = B(frame4, 1, 1, path +'Chambre 2 F.png',path +'Chambre 2 O.png', NORMAL)
p6 = B(frame4, 2, 1, path +'cuisine F.png',path +'Cuisine O.png', NORMAL)
p7 = B(frame4, 3, 1, path +'WF.png',path +path +'WO.png', NORMAL)
p8 = B(frame4, 4, 1, path +'Terrasse F.png',path +'Terrasse O.png', NORMAL)

f1 = F(frame3, 1, 1, path +'SF.png',path +'SO.png', NORMAL)
f2 = F(frame3, 2, 1, path +'cuF.png',path +'cuO.png', NORMAL)
f3 = F(frame3, 1, 3, path +'c1F.png',path +'c1O.png', NORMAL)
f4 = F(frame3, 2, 3, path +'c2F.png',path +'c2O.png', NORMAL)
# f5 = F(frame3, 3, 1, path +'BIF.png',path +'BIO.png', NORMAL)
f5 = F(frame3, 3, 1, path +'Roof F.png',path +'Roof O.png', NORMAL)

l1 = lumiere(frame2, 1, 1, path +'Entrée off.png',path +'Entrée on.png', NORMAL)
l2 = lumiere(frame2, 2, 1, path +'garage 1 off.png',path +'garage1 on.png', NORMAL)
# l3 = lumiere(frame2, 3, 1, path +'garage 2 off.png',path +'garage 2 on.png', NORMAL)
l3 = lumiere(frame2, 3, 1, path +'Couloir off.png',path +'Couloir on.png', NORMAL)
# l4 = lumiere(frame2, 4, 1, path +'Biblio off.png',path +'Biblio on.png', NORMAL)
l5 = lumiere(frame2, 5, 1, path +'Escalier off.png',path +'escaliers on.png', NORMAL)
l6 = lumiere(frame2, 1, 3, path +'terrasse off.png',path +'terrasse on.png', NORMAL)
l7 = lumiere(frame2, 2, 3, path +'Wc off.png',path +'wc on.png', NORMAL)
l8 = lumiere(frame2, 3, 3, path +'Cuisine off.png',path +'Cuisine on.png', NORMAL)
l9 = lumiere(frame2, 4, 1, path +'Salon off.png',path +'Salon on.png', NORMAL)
l8 = lumiere(frame2, 4, 3, path +'chambre_parents_off.png',path +'chambre_parents_on.png', NORMAL)
l9 = lumiere(frame2, 5, 3, path +'chambre_à_enfants_off.png',path +'chambre_à_enfants_on.png', NORMAL)
# l10 = 
# l11 = lumiere(frame2, 6, 1, path +'Salon off.png',path +'Salon on.png', NORMAL)


c1 = clima(frame5, 1, 0, "Salon :")
c2 = clima(frame5, 4, 0, "Cuisine :")
c3 = clima(frame5, 7, 0, "Chambre Parents :")
c4 = clima(frame5, 1,4,  "Chambre Enfants :")
# c5 = clima(frame5, 4,4,  "Bibliothèque :")
c6 = clima(frame5, 7,4,  "WC :")
"""
image7 = Image.open(path +'RC.png')
image7 = image7.resize((600, 600))
imm1 = ImageTk.PhotoImage(image7)
j1 = Button(frame6, image=imm1, highlightcolor='black')
j1.grid(row=0, column=0)
"""

i61 = Image.open(path +'p1.jpeg')
i61 = i61.resize((830, 700))
i61 = ImageTk.PhotoImage(i61)
lf61=Label(frame6,image=i61)
i62 = Image.open(path +'p2.jpeg')
i62 = i62.resize((830, 700))
i62 = ImageTk.PhotoImage(i62)
lf62=Label(frame6,image=i62)
lb = Button(frame6, text='>>',command=switch,font=("Calibri Light", "20"))
lb.place(x=790,y=650)
lf61.grid(row=0,column=0)
h()
p = threading.Thread(target=aya, name='arduino')
p.start()
#afficher
root.mainloop()