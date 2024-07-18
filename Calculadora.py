from tkinter import *

# |=======| INSTANCIANDO A JANAELA |=======|
calculadora = Tk()
calculadora.geometry("303x215")
calculadora.title = ("CALCULADORA")

titulo  = Label(calculadora, text = 'CALCULADORA', font = 20) 

display = Label(calculadora, text = '', width = 30, borderwidth = 5, background = '#d3d3d3', fg = 'black')

# |=======| FUNÇOES |=======|

# ======= APERTAR O BOTÃO - FAZER APARECER NO DISPLAY =======
def pressionar_botao(valor):
    global expressao
    expressao += str(valor)
    display.config(text=expressao)

# ======= FUNÇÃO DE CALCULAR =======
def calcular():
    global expressao
    try:
        resultado = str(eval(expressao)) # eval() -> função que pega expressão e realiza o calulo
        display.config(text=resultado)
        expressao = resultado
    except:
        display.config(text='ERRO')
        expressao = ""

# ======= FUNÇÃO PARA LIMPAR DISPLAY =======
def limpar():
    global expressao
    expressao = ''
    display.config(text='')


# |=======| GRID (FORMA DE MOSTRAR) |=======|

titulo.grid(row = 0, column = 0, columnspan = 4)

display.grid(row = 1, column = 0, rowspan = 2, columnspan = 4)

# |=======| BOTOES |=======|

botoes = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    'c', '0', '=', '+'
]

row_val = 3
col_val = 0

limpar() # CHAMANDO FUNÇÃO PARA LIMPAR DISPLAY

# ======= COLOCANDO OS BOTÕES =======
for botao in botoes:
    if botao == '=':
        Button(calculadora, text=botao, bg='red', font=5, width=6, height=1, command=calcular).grid(row=row_val, column=col_val)
    elif botao == 'c':
        Button(calculadora, text=botao, bg='red', font=5, width=6, height=1, command=limpar).grid(row=row_val, column=col_val)
    else:
        Button(calculadora, text=botao, bg='white', font=5, width=6, height=1, command=lambda b=botao: pressionar_botao(b)).grid(row=row_val, column=col_val)

    # COLUNAS E LINHAS
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


# # |=======| MAINLOOP |=======|

calculadora.mainloop()