from tkinter import *

class JanelaLogin():
    def __init__(self):
        self.root = Tk() # O self faz com que a variavel seja escopo de toda a classe, e qualquer método pode usar a variavel e sem o self dentro do init (metodo construtor) somente o metodo init terá acesso
        self.root.title('Login')

        Label(self.root, text='Faça o login').grid(row=0, column=0, columnspan=2)

        Label(self.root, text='Usuario:').grid(row=1, column=0)

        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Senha:').grid(row=2, column=0)

        self.senha = Entry(self.root)
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='login', bg='green3', width=100).grid(row=3, column=0)

        self.root.mainloop()




JanelaLogin()