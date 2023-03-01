
#Rafael Guedes 
#Github: https://github.com/guedes2142
#---------------------------------------------------------------------
#! git remote add origin https://github.com/guedes2142/Max-encryp.git
#! git branch -M main
#! git push -u origin main
#---------------------------------------------------------------------

import tkinter
from tkinter import *
from tkinter import messagebox
import base64
import datetime
import webbrowser

tk = Tk()
tk.geometry('300x530')
tk.config(bg='black')
tk.resizable(width=False, height=False)
tk.title('Max encryp    ')
tk.iconphoto(False, PhotoImage(file='icone.png'))

data = datetime.datetime.now()
ano = data.year
mes = data.month
dia = data.day

def new_window1():
    
    webbrowser.open('https://github.com/guedes2142')


def donothing():

    menubar = Menu(tk)
    filemenu = Menu(menubar, tearoff=0)
   
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=new_window1)
    helpmenu.add_command(label="About...", command=new_window1)
    menubar.add_cascade(label="Menu", menu=helpmenu)
  
    tk.config(menu=menubar)
    
donothing()

# --------------------------------------------------------------------------------------
def encoder():
    
    INPUT = textOne.get("1.0", "end-1c")
    encoderText = INPUT
    while True:

        if encoderText == '':
            messagebox.showerror(
                'Atenção', 'Campo de texto vazio nada foi salvo')
            break

        urlSafeEncodedBytes = base64.urlsafe_b64encode(
            encoderText.encode("utf-8"))
        urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")

        with open('texto.txt', 'a') as f:
            f.writelines(f'Data: {dia}/{mes}/{ano}: {urlSafeEncodedStr}\n')

        messagebox.showinfo('Successo', 'A informação foi encriptada com sucesso\n'
                            'um arquivo .txt foi salvo no mesma pasta desde programa\n'
                            'com o nome texto.txt')
        messagebox.showwarning('Atenção', 'Este método não é para usar como forma\n'
        'absoluta para esconder suas informações, não está totalmente segura\n'
        'use apenas em sua máquina local e não divulgue nem compartilhe\n'
        'o seu código não perca o arquivo salve uma cópia do mesmo em pendrive para mais segurança')
        labelTree['text'] = urlSafeEncodedStr
        break

def decoder():

    while True:
        
        OUTPUT = textTwo.get("1.0", "end-1c")
        coded = (OUTPUT)
        
        if OUTPUT == '':
            messagebox.showerror(
                'Atenção', 'Campo de texto vazio nada foi descodificado nem salvo')
            break
        
        decodedBytes = base64.b64decode(coded)
        decodedStr = str(decodedBytes, "utf-8")

        with open('decoded.txt', 'a') as f:
            f.writelines(f'Data: {dia}/{mes}/{ano}: {decodedStr}\n')

        messagebox.showinfo('Successo', 'A informação foi descriptografada com sucesso\n'
                            'um arquivo .txt foi salvo no mesma pasta desde programa\n'
                            'com o nome decoded.txt')
        labelTree['text'] = decodedStr
        break

frameOne = Frame(tk, width=300, height=250, bg='red')
frameOne.grid(row=0, column=0, sticky=NSEW)
frameTwo = Frame(tk, width=300, height=250, bg="white")
frameTwo.grid(row=1, column=0, sticky=NSEW)
frameTree = Frame(tk, width=300, height=100, bg='black')
frameTree.grid(row=3, column=0, sticky=NSEW)
# --------------------------------------------------------------------------------------

labelOne = Label(frameOne, width=42, height=1,
                 text="Criptografar", background='black', fg='white')
labelOne.grid(row=0, column=0, sticky=NSEW)
textOne = Text(frameOne, width=10, height=10, bg='white')
textOne.grid(row=1, column=0, sticky=NSEW)
bntOne = Button(frameOne, width=1, height=1, command=encoder,
                text="Click aqui para criptografar", bg='purple', fg='white', font=('Verdana 10'))
bntOne.grid(row=2, column=0, sticky=NSEW)
# --------------------------------------------------------------------------------------

labelTwo = Label(frameTwo, width=42, height=1,
                 text="Descriptografar", background='black', fg='white')
labelTwo.grid(row=0, column=0, sticky=NSEW)
textTwo = Text(frameTwo, width=10, height=10, bg='white')
textTwo.grid(row=1, column=0, sticky=NSEW)
bntTwo = Button(frameTwo, command=decoder, width=1, height=1,
                text="Click aqui para descriptografar", bg='purple', fg='white', font=('Verdana 10'))
bntTwo.grid(row=2, column=0, sticky=NSEW)
# --------------------------------------------------------------------------------------
labelTree = Label(tk, width=30, height=1, text='', font=(
    'Verdana 10 italic'), background='black', fg='white')
labelTree.grid(row=3, column=0, sticky=NSEW)

tk.mainloop()
