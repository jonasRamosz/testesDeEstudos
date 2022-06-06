from tkinter import *

janela = Tk()
class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.visor()
        self.botoes()
        janela.mainloop()

    def tela(self):
        self.janela.title("Calculadora")
        self.janela.configure(background='#1e3743')
        self.janela.geometry('350x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=550, height=700)
        self.janela.minsize(width=150, height=250)

    def visor(self):
        self.visor1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',highlightthickness=3)
        self.visor1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.25)

    def botoes(self):
        self.bt0 = Button(self.janela, text='0', font=('verdana',8, 'bold'))
        self.bt0.place(relx=0.01, rely=0.88, relwidth=0.26, relheight=0.1)

        self.btvirgula = Button(self.janela, text=',', font=('verdana',8, 'bold'))
        self.btvirgula.place(relx=0.27, rely=0.88, relwidth=0.25, relheight=0.1)

        self.btapagar = Button(self.janela, text='←', font=('verdana',8, 'bold'))
        self.btapagar.place(relx=0.52, rely=0.88, relwidth=0.25, relheight=0.1)

        self.btigual = Button(self.janela, text='=', bd=2, bg='#107db2', fg = 'white', font=('verdana',8, 'bold'))
        self.btigual.place(relx=0.79, rely=0.77, relwidth=0.20, relheight=0.21)

        self.bt1 = Button(self.janela, text='1', font=('verdana',8, 'bold'))
        self.bt1.place(relx=0.01, rely=0.77, relwidth=0.26, relheight=0.1)

        self.bt2 = Button(self.janela, text='2', font=('verdana',8, 'bold'))
        self.bt2.place(relx=0.27, rely=0.77, relwidth=0.25, relheight=0.1)

        self.bt3 = Button(self.janela, text='3', font=('verdana',8, 'bold'))
        self.bt3.place(relx=0.52, rely=0.77, relwidth=0.25, relheight=0.1)

        self.bt4 = Button(self.janela, text='4', font=('verdana',8, 'bold'))
        self.bt4.place(relx=0.01, rely=0.66, relwidth=0.26, relheight=0.1)

        self.bt5 = Button(self.janela, text='5', font=('verdana',8, 'bold'))
        self.bt5.place(relx=0.27, rely=0.66, relwidth=0.25, relheight=0.1)

        self.bt6 = Button(self.janela, text='6', font=('verdana',8, 'bold'))
        self.bt6.place(relx=0.52, rely=0.66, relwidth=0.25, relheight=0.1)

        self.btsoma = Button(self.janela, text='+', font=('verdana',8, 'bold'))
        self.btsoma.place(relx=0.77, rely=0.66, relwidth=0.22, relheight=0.1)

        self.bt7 = Button(self.janela, text='7', font=('verdana',8, 'bold'))
        self.bt7.place(relx=0.01, rely=0.55, relwidth=0.26, relheight=0.1)

        self.bt8 = Button(self.janela, text='8', font=('verdana',8, 'bold'))
        self.bt8.place(relx=0.27, rely=0.55, relwidth=0.25, relheight=0.1)

        self.bt9 = Button(self.janela, text='9', font=('verdana',8, 'bold'))
        self.bt9.place(relx=0.52, rely=0.55, relwidth=0.25, relheight=0.1)

        self.btsub = Button(self.janela, text='-', font=('verdana',8, 'bold'))
        self.btsub.place(relx=0.77, rely=0.55, relwidth=0.22, relheight=0.1)

        self.btmult = Button(self.janela, text='X', font=('verdana',8, 'bold'))
        self.btmult.place(relx=0.01, rely=0.44, relwidth=0.26, relheight=0.1)

        self.btdiv = Button(self.janela, text='/', font=('verdana',8, 'bold'))
        self.btdiv.place(relx=0.27, rely=0.44, relwidth=0.25, relheight=0.1)

        self.btraiz = Button(self.janela, text='√', font=('verdana',8, 'bold'))
        self.btraiz.place(relx=0.52, rely=0.44, relwidth=0.25, relheight=0.1)

        self.btporc = Button(self.janela, text='%', font=('verdana',8, 'bold'))
        self.btporc.place(relx=0.77, rely=0.44, relwidth=0.22, relheight=0.1)

        self.btpi = Button(self.janela, text='π', font=('verdana',8, 'bold'))
        self.btpi.place(relx=0.01, rely=0.33, relwidth=0.26, relheight=0.1)

        self.btpot = Button(self.janela, text='^', font=('verdana',8, 'bold'))
        self.btpot.place(relx=0.27, rely=0.33, relwidth=0.25, relheight=0.1)

        self.btpara1 = Button(self.janela, text='(', font=('verdana',8, 'bold'))
        self.btpara1.place(relx=0.52, rely=0.33, relwidth=0.25, relheight=0.1)

        self.btpara2 = Button(self.janela, text=')', font=('verdana',8, 'bold'))
        self.btpara2.place(relx=0.77, rely=0.33, relwidth=0.22, relheight=0.1)


Application()

