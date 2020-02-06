from tkinter import *

janela = Tk()
janela.title('Teste')
janela.geometry('500x500')

frame = Frame(janela, width=100, height=50, bg='white').grid(row=0, column=0)
Label(frame, text='Teste do frame').grid(row=0, column=0)




janela.mainloop()