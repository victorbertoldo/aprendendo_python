from tkinter import *

janela = Tk()
janela.title('Teste Janela')
janela.geometry('800x400')
janela.resizable(False,False)

Label(janela, text='Olá trouxa!', bg='blue', fg='white', padx=30,pady=30).grid(row=0, column=0)

janela.mainloop()