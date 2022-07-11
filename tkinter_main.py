from cProfile import label
from email.mime import image
from tkinter import *
from img import *
import posiciona


def saveEmp():
    f2.forget()
    f1.pack()


def saveProd():
    f3.forget()
    f1.pack()
    


def cadProd():
    f1.forget()
    f3.pack()


def cadEmp():
    f1.forget()
    f2.pack()





entrycolor = '#0E0D0D'

app = Tk()
app.geometry('700x700+350+150')
app.resizable(width=False, height=False)
app.title('Banco sem nome...')



#========================= -= = ==========- =-=--= -==========------

app.bind('<Button-1>', posiciona.inicio_place)
app.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, app))
app.bind('<Button-2>', lambda arg: posiciona.para_geometry(app))



#====== = = -------------======================= = == ===================
#+=================  MENU PRINCIPAL  -------------=======================
#-------------======================= -------------======================

f1 = Frame(app)
f1.pack()
f2 = Frame(app)
f3 = Frame(app)


#====== = = -------------======================= = == ===================
#+=================  FRAME 1  -------------=======================
#-------------======================= -------------======================

backg1 = PhotoImage(file = 'img/principal.png')
btemp1 = PhotoImage(file= 'img/btEmp.png')
btprod1 = PhotoImage(file='img/btProd.png')
btmain = PhotoImage(file='img/menu_bt.png')



back = Label(f1,image = backg1)

back.pack()


BTemp = Button(f1,image = btemp1,command=cadEmp)
BTemp.place(width=224, height=222, x=42, y=408)


BTprod = Button(f1,image = btprod1,command=cadProd)
BTprod.place(width=224, height=220, x=432, y=407)



bt_main = Button(f1,image = btmain,bd=0)
bt_main.place(width=61, height=64, x=302, y=483)

#====     == = = -------------======================= = == ===================
#+=================  FRAME 2  -------------=======================
#-------------======================= -------------======================



back2 = PhotoImage (file='img/empresa_cad.png')


backg2 = Label(f2,image=back2)


empEntry = Entry(f2,foreground='white',background=entrycolor,font='60',justify=CENTER,bd=0)
empEntry.place(width=474, height=90, x=116, y=148)

backg2.pack()

saveBYT = Button(f2,image=btmain,bd=0,command=saveEmp)
saveBYT.place(width=68, height=65, x=315, y=317)

#====     == = = -------------======================= = == ===================
#+=================  FRAME 3  -------------=======================
#-------------======================= -------------======================



back3 = PhotoImage(file='img/cad_prod.png')


backg3 = Label(f3,image=back3)
backg3.pack()

BTprod = Button(f3,image=btmain,bd=0,command=saveProd)
BTprod.place(width=64, height=57, x=321, y=641)

entrynom = Entry(f3,foreground='white',background=entrycolor,bd=0,justify=CENTER)
entrynom.place(width=290, height=42, x=198, y=346)

entryEmp = Entry(f3,foreground='white',background=entrycolor,bd=0,justify=CENTER)
entryEmp.place(width=290, height=38, x=199, y=492)
app.mainloop()