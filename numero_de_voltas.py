from tkinter import *

root = Tk()
root.title('Contador de voltas')
root.geometry("300x75")

contador = 0

voltas = Label(root, text=f'Número de voltas: {contador}')
voltas.pack()

def comando():
    global contador
    contador += 1
    voltas['text']=f'Número de voltas: {contador}'


botao = Button(root, text='Volta', padx=10, pady=10, command=comando)
botao.pack()


root.mainloop()