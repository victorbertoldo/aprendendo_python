from tkinter import *

def calcular():
    print(peso.get())

janela = Tk()
janela.title('Calcule seu IMC!')
janela.geometry('800x400')
janela.resizable(False,False)

Label(janela, text='Insira seus dados:').grid(row=0, column=0, columnspan=2)
Label(janela, text='Insira o peso:').grid(row=1, column=0)
peso = Entry(janela)
peso.grid(row=1, column=1)

Label(janela, text='Insira sua altura:').grid(row=2, column=0)
altura = Entry(janela)
altura.grid(row=2,column=1)

Button(janela, text='Calcular', command=calcular).grid(row=3, column=0)

resposta = Label(janela, text='resposta')
resposta.grid(row=3, column=1)

janela.mainloop()