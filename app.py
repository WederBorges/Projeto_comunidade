import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
janela.title("Gestão de Produtos")
janela.geometry("700x600")
titulo_inicial = tk.Label(text="Preencha os dados do produto abaixo", font="Arial")
titulo_inicial.place(x=150, y= 100)

nome = tk.Label(text="Nome Produto")
nome.place(x=20, y=200)
nome_caixa = tk.Entry()
nome_caixa.place(x= 140, y=200)



janela.mainloop()