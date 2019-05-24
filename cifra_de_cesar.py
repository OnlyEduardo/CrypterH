#!/bin/env python3


# Eduardo Leal <eduardoleal.contact@gmail.com>
# encriptador e decriptador

from tkinter import *


class cifra_de_cesar_GUI:
    def __init__(self, master=None):
        pass

    def cesar(self, master):
        self.fontedefault = ("Arial", "10")

        self.conteiner01 = Frame(master)
        self.conteiner01["pady"] = 10
        self.conteiner01.pack()

        self.conteiner02 = Frame(master)
        self.conteiner02["padx"] = 20
        self.conteiner02.pack()

        self.conteiner03 = Frame(master)
        self.conteiner03["padx"] = 20
        self.conteiner03.pack()

        self.conteiner04 = Frame(master)
        self.conteiner04["pady"] = 20
        self.conteiner04["padx"] = 5
        self.conteiner04.pack()

        self.conteiner05 = Frame(master)
        self.conteiner05["pady"] = 20
        self.conteiner05.pack()

        self.titulo = Label(self.conteiner01,
                            text="Cifra de César")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.textoLabel = Label(self.conteiner02,
                                text="Digite o texto que será codificado:      ", font=self.fontedefault)
        self.textoLabel.pack(side=LEFT)

        self.texto = Entry(self.conteiner02)
        self.texto["width"] = 25
        self.texto["font"] = self.fontedefault
        self.texto.pack(side=LEFT)

        self.rotLabel = Label(self.conteiner03,
                              text="Digite a rotação que será usada(0-25):", font=self.fontedefault)
        self.rotLabel.pack(side=LEFT)

        self.rot = Entry(self.conteiner03)
        self.rot["width"] = 25
        self.rot["font"] = self.fontedefault
        self.rot.pack(side=LEFT)

        self.Codificar = Button(self.conteiner04)
        self.Codificar["text"] = "Codificar"
        self.Codificar["font"] = ("Calibri", "10")
        self.Codificar["width"] = 12
        self.Codificar["command"] = self.codifica
        self.Codificar.pack(side=LEFT)

        self.decodificar = Button(self.conteiner04)
        self.decodificar["text"] = "Decodificar"
        self.decodificar["font"] = ("Calibri", "10")
        self.decodificar["width"] = 12
        self.decodificar["command"] = self.decodifica
        self.decodificar.pack(side=LEFT)

        self.rotLabel = Label(self.conteiner05,
                              text="Resultado: ", font=self.fontedefault)
        self.rotLabel.pack(side=LEFT)
        self.mensagem = Label(self.conteiner05, text="...", font=self.fontedefault, fg="green")
        self.mensagem.pack(side=LEFT)

    def codifica(self):
        texto = self.texto.get()
        rot = self.rot.get()

        for i in "!@#$%¨&*()_+§¬¢£³²¹/?ºª|<>,.:;~^}{[]-´*":
            if i in texto:
                self.mensagem["text"] = 'O texto "{}", possui valores inválidos\n' \
                                        'Não use acentos ou caracteres especiais'.format(texto)
                self.mensagem["fg"] = "red"
                return None

        if rot == "":
            rot = 0
            self.mensagem["text"] = 'O texto "{}", encriptado com rotação {} é: {}'.format(texto, rot, texto)
            self.mensagem["fg"] = "green"
            return None

        rot = int(rot)
        texto = texto.lower()
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        novo_texto = ''

        if rot > 26 or rot < 0:
            self.mensagem["text"] = 'Digite um valor entre 0 e 25\n Digite um valor válido!'
            self.mensagem["fg"] = "red"
            return None

        for caractere in texto:
            if caractere in alfabeto:
                num = alfabeto.find(caractere)
                num = num + rot
                if num >= len(alfabeto):
                    num = num - len(alfabeto)
                elif num < 0:
                    num = num + len(alfabeto)
                novo_texto = novo_texto + alfabeto[num]
            else:
                novo_texto = novo_texto + caractere

        self.mensagem["text"] = 'O texto "{}", encriptado com rotação {} é: {}'.format(texto, rot, novo_texto)
        self.mensagem["fg"] = "green"

    def decodifica(self):
        texto = self.texto.get()
        rot = self.rot.get()
        texto = texto.lower()

        for i in "!@#$%¨&*()_+§¬¢£³²¹/?ºª|<>,.:;~^}{[]-´*":
            if i in texto:
                self.mensagem["text"] = 'O texto "{}", possui valores inválidos\n' \
                                        'Não use acentos ou caracteres especiais'.format(texto)
                self.mensagem["fg"] = "red"
                return None

        if rot == "":
            rot = 0
            self.mensagem["text"] = 'O texto "{}", decriptado com rotação {} é: {}'.format(texto, rot, texto)
            self.mensagem["fg"] = "green"
            return None

        rot = int(rot)

        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        novo_texto = ''

        if rot > 26 or rot < 0:
            self.mensagem["text"] = 'Digite um valor entre 0 e 25\n Digite um valor válido!'
            self.mensagem["fg"] = "red"
            return None

        for caractere in texto:
            if caractere in alfabeto:
                num = alfabeto.find(caractere)
                num = num - rot
                if num >= len(alfabeto):
                    num = num - len(alfabeto)
                elif num < 0:
                    num = num + len(alfabeto)
                novo_texto = novo_texto + alfabeto[num]
            else:
                novo_texto = novo_texto + caractere

        self.mensagem["text"] = 'O texto "{}", decriptado com rotação {} é: {}'.format(texto, rot, novo_texto)
        self.mensagem["fg"] = "green"


root = Tk()
root.title("Cifra de César. Feito por: Eduardo Leal, BSI - 2019/1")
cifra_de_cesar_GUI(root)
root.geometry("650x250+250+250")
root.mainloop()
