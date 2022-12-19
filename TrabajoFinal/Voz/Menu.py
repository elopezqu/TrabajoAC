from guizero import App, Text, PushButton, TextBox, ButtonGroup

existe = ""
name = ""
def iniciar():
    print("soy yo "+existe+" "+name)
    
def cargar():
    menu1._close_window()
    menu2 = App(title="Memoria",bg="#00F8D2", height=230)
    mensaje = Text(menu2, text="REGISTRO", size=12, font="Time New Roman", color="blue",height=3 )
    mensaje1 = Text(menu2, text="Tiene una cuenta: ", size=10, font="Time New Roman", color="#f0090f")
    opciones = ButtonGroup(menu2, options=["Si", "No"], selected="No")
    mensaje2 = Text(menu2, text="Ingrese el nombre de su cuenta: ", size=10, font="Time New Roman", color="#f0090f")
    nombre = TextBox(menu2, width=20)
    mensaje3 = Text(menu2, text="", height=0)
    run = PushButton(menu2, command = iniciar, text="INICIAR", width=80)
    global existe 
    existe = opciones.value
    global name
    name = nombre.value

menu1 = App(title="Memoria", bg="#00F8D2", height=250)
mensaje = Text(menu1, text="Bienvenido al juego de memoria", size=20, font="Time New Roman", color="blue",height=3)
jugar = PushButton(menu1, command=cargar, text="JUGAR", width=80)
salir = PushButton(menu1, command=menu1._close_window, text="SALIR", width=80)
menu1.display()


