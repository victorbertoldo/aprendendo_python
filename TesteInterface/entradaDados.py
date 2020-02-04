from tkinter import *

janela = Tk()
janela.title('Teste Janela')
janela.geometry('800x400')
janela.resizable(False,False)


# O show mascara o que está sendo digitado pelo usario
Entry(janela, bg='gray', fg='orange', show='*').grid(row=0, column=0)

janela.mainloop()