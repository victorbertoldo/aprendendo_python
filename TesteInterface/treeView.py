from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Janela teste')

tree = ttk.Treeview(janela, selectmode="browse", column=("col1", "col2","col3"), show='headings')

tree.column("col1",width=200, minwidth=50, stretch=NO)
tree.heading("#1", text='Nome')

tree.column("col2",width=100, minwidth=50, stretch=NO)
tree.heading("#2", text='Idade')

tree.column("col3",width=300, minwidth=50, stretch=NO)
tree.heading("#3", text='Endereço')

tree.grid(row=0, column=0)


janela.mainloop()