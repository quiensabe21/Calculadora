from tkinter import*
from tkinter import ttk
import math

root= Tk()
root.title("Calculadora")
root.geometry("+500+800")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos =ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style= "mainframe.TFrame")
mainframe.grid(column =0, row=0,sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


#estilos Labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', anchor="e")



entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
Label_entrada1.grid(column =0, row=0, columnspan= 4, sticky=(W, N, E, S))


entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe,textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column =0, row=1, columnspan= 4, sticky=(W, N, E, S))

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton')
# estilos_botones_numeros.map('Botones_numeros. TButton',foreground =[{'active','red'}], backgroung =[{'active', 'black'}])
estilos_botones_numeros.map(
    'Botones_numeros.TButton',
    foreground=[('active', 'red')],
    background=[('active', 'black')]
)

esilos_botones_borrar =ttk.Style()



button0 = ttk.Button(mainframe, text = "0", style="Botones_numeros.TButton",command=lambda:ingresarvalor('0'))
button1 = ttk.Button(mainframe, text = "1", style="Botones_numeros.TButton",command=lambda:ingresarvalor('1'))
button2 = ttk.Button(mainframe, text = "2", style="Botones_numeros.TButton",command=lambda:ingresarvalor('2'))
button3 = ttk.Button(mainframe, text = "3", style="Botones_numeros.TButton",command=lambda:ingresarvalor('3'))
button4 = ttk.Button(mainframe, text = "4", style="Botones_numeros.TButton",command=lambda:ingresarvalor('4'))
button5 = ttk.Button(mainframe, text = "5", style="Botones_numeros.TButton",command=lambda:ingresarvalor('5'))
button6 = ttk.Button(mainframe, text = "6", style="Botones_numeros.TButton",command=lambda:ingresarvalor('6'))
button7 = ttk.Button(mainframe, text = "7", style="Botones_numeros.TButton",command=lambda:ingresarvalor('7'))
button8 = ttk.Button(mainframe, text = "8", style="Botones_numeros.TButton",command=lambda:ingresarvalor('8'))
button9 = ttk.Button(mainframe, text = "9", style="Botones_numeros.TButton",command=lambda:ingresarvalor('9'))

button_borrar = ttk.Button(mainframe, text = chr(9003),command=lambda:borrar())
button_borrar_todo = ttk.Button(mainframe, text = "C",command=lambda:borrartodo())
button_parentesis1 = ttk.Button(mainframe, text = "(")
button_parentesis2 = ttk.Button(mainframe, text = ")")
button_punto = ttk.Button(mainframe, text = ".")


button_division = ttk.Button (mainframe, text=chr(247),command=lambda: ingresarvalor('/')) 
button_multiplicacion= ttk.Button(mainframe, text="x",command=lambda:ingresarvalor('*'))
button_resta =ttk. Button (mainframe, text="-",command=lambda:ingresarvalor('-'))
button_suma = ttk.Button (mainframe, text="+",command=lambda:ingresarvalor('+'))


button_igual = ttk. Button (mainframe, text="=",command=lambda:ingresarvalor('=')) 
button_raiz_cuadrada = ttk. Button (mainframe, text="√",command=lambda:raizcuadrada())

def ingresarvalor(tecla):
    if tecla >= '0' and tecla <= '9' or tecla =='(' or tecla ==')' or tecla =='.':
        entrada2.set(entrada2.get()+tecla)

    if tecla == '*' or tecla =='/' or tecla == '+'or tecla == '-':
        if tecla=='*':
            entrada1.set(entrada2.get()+'*')
        elif tecla == '/':
            entrada1.set(entrada2.get()+'/')
        elif tecla =='+':
             entrada1.set(entrada2.get()+'+')
        elif tecla =='-':
            entrada1.set(entrada2.get()+'-')
            
        entrada2.set('')

    if tecla=='=':
        entrada1.set(entrada1.get()+ entrada2.get())  
        resultado = eval(entrada1.get()) 
        entrada2.set(resultado)

def raizcuadrada():
    entrada1.set('')
    resultado =math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
    
def borrar():
    inicio = 0
    final = len(entrada2.get()) #150
    
    entrada2.set(entrada2.get()[inicio:final-1])
    
def borrartodo():
    entrada1.set('')
    entrada2.set('')    
#Botones en pantalla

button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid (column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W, N, E, S))



root, mainloop()




