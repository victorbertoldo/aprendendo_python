from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Janela teste')

tree = ttk.Treeview(janela, selectmode="browse", column=("col1", "col2","col3", "col4"), show='headings')

tree.column("col1",width=200, minwidth=50, stretch=NO)
tree.heading("#1", text='Nome')

tree.column("col2",width=100, minwidth=50, stretch=NO)
tree.heading("#2", text='Idade')

tree.column("col3",width=300, minwidth=50, stretch=NO)
tree.heading("#3", text='Endereço')

tree.column("col4",width=50, minwidth=50, stretch=NO)
tree.heading("#4", text='ID')

elementos = ["Jão", "23", "Rua das bananas lt 15", 1]


for i in range(0,4):
    tree.insert("", END, values=elementos, tag=i)

tree.grid(row=0, column=0)


janela.mainloop()