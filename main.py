from ctypes import alignment
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import os

def btn_agendar():
    try:
        tempo = int(tempo_usr.get())
        tempo = tempo * 60
        return os.system(f"shutdown /s /t {tempo}")
    except:
        return False

def cancelar():
    return os.system("shutdown /a")

def testaEntradaInteiro(valor):
    if valor.isdigit():
        return True
    else:
        return False


root = Tk()
root.geometry('300x250')
root.title('Agendar Desligamento')
root.resizable(False, False)
root.configure(bg='#fff', border=1)
p1 = PhotoImage(file='C:\\Users\\Usuário\\Downloads\\icone.png')
root.iconphoto(False,p1)


tempo_usr= StringVar()

l1= ttk.Label(text='Agendar Desligamento', padding=5 , font='tahoma')
l1.place(relx=0.26, rely=0.2)

btn_sair = ttk.Button(root, text= 'Sair', command=lambda: root.quit())
btn_sair.place(relx=0.4 , rely=0.8)

btn_cancela = ttk.Button(root, text="Cancelar Agendamento" , command=cancelar)
btn_cancela.place(relx= 0.3 , rely=0.62)

btn_agendar = ttk.Button(root, text='Agendar', command=btn_agendar)
btn_agendar.place(relx=0.4, rely=0.5)


entry_usr = ttk.Entry(root, cursor='clock',textvariable=tempo_usr, width=40,validatecommand=(testaEntradaInteiro,'%P'))
entry_usr.place(relx=0.1 , rely=0.4)

root.mainloop()
