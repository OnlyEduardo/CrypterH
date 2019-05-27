#!/bin/env python3


# Eduardo Leal <eduardoleal.contact@gmail.com>
# encriptador e decriptador

import hashlib
from tkinter import *
from tkinter.ttk import *

creditos = "Encrypter/Decrypter - 2019.\n" \
           "\nPrograma feito por: Eduardo Ribeiro Leal\n" \
           "<eduardoleal.contact@gmail.com>\n\n"

class Main:
    def __init__(self, master):
        self.abas = Notebook(master)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)
        self.frame_aba5 = Frame(self.abas)

        # aba1 inicio
        self.fontedefault = ("Arial", "10")
        self.titlefont = ("Calibri", "14", "bold")

        self.conteiner01 = Frame(self.frame_aba1)
        self.conteiner01.pack(pady=10)

        self.conteiner02 = Frame(self.frame_aba1)
        self.conteiner02.pack(padx=20)

        self.conteiner03 = Frame(self.frame_aba1)
        self.conteiner03.pack(padx=20)

        self.conteiner04 = Frame(self.frame_aba1)
        self.conteiner04.pack(pady=20, padx=5)

        self.conteiner05 = Frame(self.frame_aba1)
        self.conteiner05.pack(pady=20)

        self.titulo = Label(self.conteiner01,
                            text="Cifra de César", font=self.titlefont)
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
        self.rot.pack(side=LEFT, padx=25)

        self.Codificar = Button(self.conteiner04)
        self.Codificar["text"] = "Codificar"
        self.Codificar["command"] = self.codifica_cesar
        self.Codificar.pack(side=LEFT, padx=12)

        self.decodificar = Button(self.conteiner04)
        self.decodificar["text"] = "Decodificar"
        self.decodificar["command"] = self.decodifica_cesar
        self.decodificar.pack(side=LEFT, padx=12)

        self.rotLabel = Label(self.conteiner05,
                              text="Resultado: ", font=self.fontedefault)
        self.rotLabel.pack(side=LEFT)
        self.mensagem = Label(self.conteiner05, text="...", font=self.fontedefault)
        self.mensagem.pack(side=LEFT)
        # FIM ABA 1
        # self.label1 = Label(self.frame_aba1, text="Esta é a aba 1")
        # self.label1.pack(padx=100, pady=100)

        # INICIO ABA 2
        self.fontedefault = ("Arial", "10")
        self.titlefont = ("Calibri", "14", "bold")

        self.counta1 = Frame(self.frame_aba2)
        self.counta1.pack(pady=10)

        self.counta2 = Frame(self.frame_aba2)
        self.counta2.pack(padx=20)

        self.counta3 = Frame(self.frame_aba2)
        self.counta3.pack(padx=20)

        self.counta4 = Frame(self.frame_aba2)
        self.counta4.pack(pady=20, padx=5)

        self.counta5 = Frame(self.frame_aba2)
        self.counta5.pack(pady=20)

        self.titulo = Label(self.counta1,
                            text="Hash MD5", font=self.titlefont)
        self.titulo.pack()

        self.texto2Label = Label(self.counta2, text="Digite o texto que será codificado:      ", font=self.fontedefault)
        self.texto2Label.pack(side=LEFT)

        self.texto2 = Entry(self.counta2)
        self.texto2["width"] = 25
        self.texto2["font"] = self.fontedefault
        self.texto2.pack(side=LEFT)

        self.Codificar2 = Button(self.counta4)
        self.Codificar2["text"] = "Codificar"
        self.Codificar2["command"] = self.codifica_md5
        self.Codificar2.pack(side=LEFT, padx=12)

        self.mensagem2 = Label(self.counta5, text="Resultado: ...", font=self.fontedefault)
        self.mensagem2.pack(side=LEFT)
        # FIM ABA 2
        # self.label2 = Label(self.frame_aba2, text="Esta é a aba 2")
        # self.label2.pack(padx=650, pady=250)

        # INICIO ABA 3
        self.fontedefault = ("Arial", "10")
        self.titlefont = ("Calibri", "14", "bold")

        self.counta1o = Frame(self.frame_aba3)
        self.counta1o.pack(pady=10)

        self.counta2o = Frame(self.frame_aba3)
        self.counta2o.pack(padx=20)

        self.counta3o = Frame(self.frame_aba3)
        self.counta3o.pack(padx=20)

        self.counta4o = Frame(self.frame_aba3)
        self.counta4o.pack(pady=20, padx=5)

        self.counta5o = Frame(self.frame_aba3)
        self.counta5o.pack(pady=20)

        self.titulo = Label(self.counta1o,
                            text="Hash Sha-1", font=self.titlefont)
        self.titulo.pack()

        self.texto3Label = Label(self.counta2o,
                                 text="Digite o texto que será codificado:      ", font=self.fontedefault)
        self.texto3Label.pack(side=LEFT)

        self.texto3 = Entry(self.counta2o)
        self.texto3["width"] = 25
        self.texto3["font"] = self.fontedefault
        self.texto3.pack(side=LEFT)

        self.Codificar3 = Button(self.counta4o)
        self.Codificar3["text"] = "Codificar"
        self.Codificar3["command"] = self.codifica_sha1
        self.Codificar3.pack(side=LEFT, padx=12)

        self.mensagem3 = Label(self.counta5o, text="Resultado: ...", font=self.fontedefault)
        self.mensagem3.pack(side=LEFT)
        # FIM ABA 3
        # self.label3 = Label(self.frame_aba3, text="Esta é a aba 3")
        # self.label3.pack(padx=650, pady=250)

        # INICIO ABA 4

        self.fontedefault = ("Arial", "10")
        self.titlefont = ("Calibri", "14", "bold")

        self.conteiner1o = Frame(self.frame_aba4)
        self.conteiner1o.pack(pady=10)

        self.conteiner2o = Frame(self.frame_aba4)
        self.conteiner2o.pack(padx=20)

        self.conteiner3o = Frame(self.frame_aba4)
        self.conteiner3o.pack(padx=20)

        self.conteiner4o = Frame(self.frame_aba4)
        self.conteiner4o.pack(pady=20, padx=5)

        self.conteiner5o = Frame(self.frame_aba4)
        self.conteiner5o.pack(pady=20)

        self.titulo = Label(self.conteiner1o,
                            text="Hash SHA-256", font=self.titlefont)
        self.titulo.pack()

        self.texto3Label = Label(self.conteiner2o,
                                 text="Digite o texto que será codificado:      ", font=self.fontedefault)
        self.texto3Label.pack(side=LEFT)

        self.texto4 = Entry(self.conteiner2o)
        self.texto4["width"] = 25
        self.texto4["font"] = self.fontedefault
        self.texto4.pack(side=LEFT)

        self.Codificar4 = Button(self.conteiner4o)
        self.Codificar4["text"] = "Codificar"
        self.Codificar4["command"] = self.codifica_sha256
        self.Codificar4.pack(side=LEFT, padx=12)

        self.mensagem4 = Label(self.conteiner5o, text="Resultado: ...", font=self.fontedefault)
        self.mensagem4.pack(side=LEFT)

        # FIM ABA 4

        # INICIO ABA 5

        self.conteiner1ou = Frame(self.frame_aba5)
        self.conteiner1ou.pack(pady=10)

        self.conteiner2ou = Frame(self.frame_aba5)
        self.conteiner2ou.pack(padx=20)

        self.titulo = Label(self.conteiner1ou,
                            text="Créditos", font=self.titlefont)
        self.titulo.pack()

        self.mensagem5 = Label(self.conteiner2ou, text=creditos, font=self.fontedefault)
        self.mensagem5.pack(side=LEFT)

        # FIM ABA 5

        self.abas.add(self.frame_aba1, text="Cifra de César")
        self.abas.add(self.frame_aba2, text="Hash MD5")
        self.abas.add(self.frame_aba3, text="Hash SHA-1")
        self.abas.add(self.frame_aba4, text="Hash SHA-256")
        self.abas.add(self.frame_aba5, text="Créditos")
        self.abas.pack()

    def codifica_cesar(self):
        texto = self.texto.get()
        rot = self.rot.get()

        for i in "!@#$%¨&*()_+§¬¢£³²¹/?ºª|<>,.:;~^}{[]-´*":
            if i in texto:
                self.mensagem["text"] = 'O texto "{}", possui valores inválidos\n' \
                                        'Não use acentos ou caracteres especiais'.format(texto)
                return None

        if rot == "":
            rot = 0
            self.mensagem["text"] = 'O texto "{}", encriptado com rotação {} é: {}'.format(texto, rot, texto)
            return None

        rot = int(rot)
        texto = texto.lower()
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        novo_texto = ''

        if rot > 26 or rot < 0:
            self.mensagem["text"] = 'Digite um valor entre 0 e 25\n Digite um valor válido!'
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

    def decodifica_cesar(self):
        texto = self.texto.get()
        rot = self.rot.get()
        texto = texto.lower()

        for i in "!@#$%¨&*()_+§¬¢£³²¹/?ºª|<>,.:;~^}{[]-´*":
            if i in texto:
                self.mensagem["text"] = 'O texto "{}", possui valores inválidos\n' \
                                        'Não use acentos ou caracteres especiais'.format(texto)
                return None

        if rot == "":
            rot = 0
            self.mensagem["text"] = 'O texto "{}", decriptado com rotação {} é: {}'.format(texto, rot, texto)
            return None

        rot = int(rot)

        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        novo_texto = ''

        if rot > 26 or rot < 0:
            self.mensagem["text"] = 'Digite um valor entre 0 e 25\n Digite um valor válido!'
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

    def codifica_md5(self):
        texto = self.texto2.get()
        novo_texto = hashlib.md5(texto.encode()).hexdigest()

        self.mensagem2["text"] = 'Resultado: "{}" Em MD5 é: "{}"'.format(texto, novo_texto)

    def codifica_sha1(self):
        texto = self.texto3.get()
        novo_texto = hashlib.sha1(texto.encode()).hexdigest()
        self.mensagem3["text"] = 'Resultado: "{}" Em SHA-1 é: "{}"'.format(texto, novo_texto)

    def codifica_sha256(self):
        texto = self.texto4.get()
        novo_texto = hashlib.sha256(texto.encode()).hexdigest()
        self.mensagem4["text"] = 'Resultado: "{}" Em SHA-256 é: "{}"'.format(texto, novo_texto)


root = Tk()
root.title("Encrypter/Decrypter.\n2019")
root.geometry("500x250+400+250")
Main(root)
root.iconbitmap('icon.ico')
root.mainloop()
