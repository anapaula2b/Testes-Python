from re import T
import requests
from tkinter import *



janela = Tk()
janela.title('Caucoladora')
janela.geometry('840x480')

def somar() :
    texto ='Isso é um testes'
    texto_teste["text"] = texto


texto_orientacao = Label(janela, text = 'Digite os numeros para somalos')
texto_orientacao.grid(column=0, row=0, padx=10, pady=20)

botao = Button(janela, text='Somar', command=somar)
botao.grid(column=0, row=1, padx=10, pady=20)

texto_teste = Label(janela, text='Clica ai')
texto_teste.grid(column=0, row=2, padx=10, pady=20)

janela.mainloop()

