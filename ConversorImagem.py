from tkinter import *
from tkinter import messagebox
from PIL import Image, PdfImagePlugin
from tkinter.filedialog import *

janela = Tk()
janela.title("TESTE")
janela.configure(background="#222")
janela.geometry("800x400")

titulo = Label(janela, text="CONVERSOR DE IMAGEM", font="verdana 20 bold underline", fg="#ffbc46", bg='#222')
titulo.place(x=200, y=1)




def novo_Arquivo():
    caminho = askopenfilename()
    imagem = Image.open(caminho)
    imagem_altura, imagem_largura = imagem.size


    label_Tam_original = Label(janela, text="Figura Original(AxL): " + str(imagem_altura) + " X " + str(imagem_largura), fg="gold", bg="#2f2f2f")
    label_Tam_original.place(x=310, y=120)

    label_Altura = Label(janela, text=" Digite a nova altura ", width=28, height=2, font="Courier 10", bg="#222", fg="#fff")
    label_Altura.place(x=300, y=160)

    label_Largura = Label(janela, text=" Digite a nova Largura ", width=28, height=2,font="Courier 10", fg="#fff", bg="#222")
    label_Largura.place(x=300, y=220)

    entrada_Altura = Entry(janela, width=35, justify="center")
    entrada_Altura.place(x=300, y=190)

    entrada_Largura = Entry(janela, width=35, justify="center")
    entrada_Largura.place(x=300, y=250)

    def converter():
        altura = int(entrada_Altura.get())
        largura = int(entrada_Largura.get())
        novo_Valor = (altura, largura)
        nova_imagem = imagem.resize(novo_Valor)
        imagem_salvar = asksaveasfilename()
        nova_imagem.save(imagem_salvar + ".JPG")
        messagebox.showinfo(title="Aviso!", message="Criado com Sucesso!")


    botao_Converter = Button(janela, text="Converter", width=10, height=1, font=5, bg="#ffbc46", fg="black", command=converter)
    botao_Converter.place(x=350, y=320)


botao = Button(janela, text="Abrir Arquivo", font="13", command=novo_Arquivo, bg="green", fg="#fff")
botao.place(x=350, y=80)

buttonSair = Button(janela, text="SAIR", font="arial 10", command=janela.destroy, fg="#fff", bg="red")
buttonSair.place(x=700, y=340)
janela.mainloop()
