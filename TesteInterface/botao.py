from tkinter import *

def mostrar():
    armazenarLabel['text'] = 'botão foi clicado'

janela = Tk()
janela.title('Teste Janela')
janela.geometry('800x400')
janela.resizable(False,False)

Button(janela, text='Clique aqui', bg='purple', fg='gray', height=10, width=20, command=mostrar).grid(row=0, column=0)

armazenarLabel = Label(janela, text='ainda não clicou')
armazenarLabel.grid(row=1, column=0)

janela.mainloop()