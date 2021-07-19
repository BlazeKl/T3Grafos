#AutoEdUtem, Editor de Automatas y Arboles
#1,2021
#Felipe Perez Cares
#Alex Bidart Orellana
#Alex Pino Moya
#Pablo Sepulveda Fernandez
#Oscar Munos Retamal
#
#librerias

import tkinter as tk
from tkinter import ttk
from funciones.clasegrafo import grafo
from funciones.claseauto import automata
from PIL import Image, ImageTk

#variables
global pos_x, pos_y, click, vert, cant_v, cant_a, j, grafo_n, peso
pos_x = 0
pos_y = 0
click = 0
vert = [0 for x in range(999)]
arista = [[0 for x in range(999)] for y in range(999)]
cant_v = 0
cant_a = 0
j = 0
grafo_n = grafo(1000)
peso = ""

def add_nodo(event):
    global vert, cant_v
    print("Insertando nodo")
    print("(",+event.x,",",+event.y,")")
    vert[cant_v] = lienzo.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill='black', activeoutline='green', activewidth=3)
    lienzo.create_text(event.x-13, event.y-13, text=chr(97+cant_v))
    lienzo.tag_bind(vert[cant_v], '<Button-3>', lambda event, var1 = cant_v, var2 = event.x, var3 = event.y: add_arista(event,var1,var2,var3))
    cant_v += 1

def add_arista(event,i, x, y):
    global pos_x, pos_y, j, grafo_n, cant_a, peso
    global click
    def closew(var1,var2):
        global peso
        peso = var2.get()
        if peso.isdigit():
            if peso != "0":
                var1.destroy()

    def ing_peso(a, b):
        text_label = "Peso de '" + chr(97+b) + "' a '" + chr(97+a) + "'"
        print(text_label)
        nbox = tk.Tk()
        nbox.title("Peso")
        nbox.resizable(0,0)
        frame = tk.Frame(nbox)
        frame.grid(row=0, column=0)
        tex = tk.Label(frame, text=text_label)
        tex.grid(row=0, column=0)
        ent = tk.Entry(frame)
        ent.grid(row=1, column=0)
        btn = tk.Button(frame, text="Ok", command=lambda: closew(nbox,ent))
        btn.grid(row=2, column=0)
        nbox.wait_window()

    if click:
        print("insertando arista end =", chr(97+i))
        if grafo_n.get_p(j,i) == 0:
                cant_a += 1
        if i == j:
            print("bucle")
            warn = tk.Tk()
            warn.title("Error")
            warn.resizable(0,0)
            wframe = tk.Frame(warn)
            wframe.grid(row=0, column=0)
            tk.Label(wframe, text="No se permiten bucles").grid(row=0, column=0)
            tk.Button(wframe, text="Ok", command=lambda: warn.destroy()).grid(row=1, column=0)
        else:
            ing_peso(i,j)
            peso = int(peso)
            arista[i][j] = lienzo.create_line(pos_x, pos_y, x, y, fill='black', width=2)
            grafo_n.set_p(peso,i,j)
            grafo_n.set_p(peso,j,i)
            lienzo.tag_lower(arista[i][j])
        print("(",+x,",",+y,")")
        click=0
    else:
        print("insertando arista start = ",chr(97+i))
        pos_x = x
        pos_y = y
        j = i
        print("(",+pos_x,",",+pos_y,")")
        click=1

def detalles():
    menu = tk.Tk()
    menu.title('Detalles de grafo arbol original')
    menu.resizable(0,0)
    frame1 = tk.Frame(menu)
    frame1.grid(row=0, column=0)
    text = tk.Label(frame1, text="Peso Arbol Original")
    text.grid(row=0, column=0)
    frame2 = tk.Frame(menu)
    frame2.grid(row=1, column=0)
    for ii in range(0, cant_v+1):
        tabla = tk.Entry(frame2, width=5, bg='green', fg='white')
        tabla.grid(row=0, column=ii)
        tabla.insert(tk.END, chr(96+ii))
    for ii in range(0, cant_v+1):
        tabla = tk.Entry(frame2, width=5, bg='green', fg='white')
        tabla.grid(row=ii, column=0)
        tabla.insert(tk.END, chr(96+ii))
    for ii in range(0, cant_v):
        for jj in range(0, cant_v):
            if grafo_n.get_p(ii,jj) > 0:
                tabla = tk.Entry(frame2, width=5, bg='blue', fg='white')
            else:
                tabla = tk.Entry(frame2, width=5, bg='black', fg='white')
            tabla.grid(row=1+ii, column=1+jj)
            tabla.insert(tk.END, grafo_n.get_p(ii,jj))
    tabla = tk.Entry(frame2, width=5, bg='green', fg='white')
    tabla.grid(row=0, column=0)
    tabla.insert(tk.END, "P")
    frame3 = tk.Frame(menu)
    frame3.grid(row=2, column=0)
    text = tk.Label(frame3, text="Numero de regiones : ")
    text.grid(row=0, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=0, column=1)
    tabla.insert(tk.END, grafo_n.n_regiones(cant_a,cant_v))
    kruskal = grafo_n.l_kruskal(cant_v)
    # frame4 = tk.Frame(menu)
    # frame4.grid(row=3, column=0)
    # text = tk.Label(frame4, text="Kruskal")
    # text.grid(row=0, column=0)
    # frame5 = tk.Frame(menu)
    # frame5.grid(row=4, column=0)
    # for ii in range(0, cant_v+1):
    #     tabla = tk.Entry(frame5, width=5, bg='green', fg='white')
    #     tabla.grid(row=0, column=ii)
    #     tabla.insert(tk.END, chr(96+ii))
    # for ii in range(0, cant_v+1):
    #     tabla = tk.Entry(frame5, width=5, bg='green', fg='white')
    #     tabla.grid(row=ii, column=0)
    #     tabla.insert(tk.END, chr(96+ii))
    # for ii in range(0, cant_v):
    #     for jj in range(0, cant_v):
    #         if kruskal[ii][jj] > 0:
    #             tabla = tk.Entry(frame5, width=5, bg='blue', fg='white')
    #         else:
    #             tabla = tk.Entry(frame5, width=5, bg='black', fg='white')
    #         tabla.grid(row=1+ii, column=1+jj)
    #         tabla.insert(tk.END, kruskal[ii][jj])
    # tabla = tk.Entry(frame5, width=5, bg='green', fg='white')
    # tabla.grid(row=0, column=0)
    # tabla.insert(tk.END, "K")
    # frame6 = tk.Frame(menu)
    # frame6.grid(row=5, column=0)
    # prim = grafo_n.l_prim(cant_v,0)
    # text = tk.Label(frame6, text="PRIM")
    # text.grid(row=0, column=0)
    # frame7 = tk.Frame(menu)
    # frame7.grid(row=6, column=0)
    # for ii in range(0, cant_v+1):
    #     tabla = tk.Entry(frame7, width=5, bg='green', fg='white')
    #     tabla.grid(row=0, column=ii)
    #     tabla.insert(tk.END, chr(96+ii))
    # for ii in range(0, cant_v+1):
    #     tabla = tk.Entry(frame7, width=5, bg='green', fg='white')
    #     tabla.grid(row=ii, column=0)
    #     tabla.insert(tk.END, chr(96+ii))
    # for ii in range(0, cant_v):
    #     for jj in range(0, cant_v):
    #         if prim[ii][jj] > 0:
    #             tabla = tk.Entry(frame7, width=5, bg='blue', fg='white')
    #         else:
    #             tabla = tk.Entry(frame7, width=5, bg='black', fg='white')
    #         tabla.grid(row=1+ii, column=1+jj)
    #         tabla.insert(tk.END, prim[ii][jj])
    # tabla = tk.Entry(frame7, width=5, bg='green', fg='white')
    # tabla.grid(row=0, column=0)
    # tabla.insert(tk.END, "P")
    print(grafo_n.l_kruskal2(cant_v))
    menu.mainloop

def limpiar_canvas():
    print("limpiar canvas")
    global pos_x, pos_y, click, vert, cant_v, cant_a, grafo_n
    lienzo.delete("all")
    pos_x=0
    pos_y=0
    click = 0
    vert = [0 for x in range(999)]
    cant_v = 0
    cant_a = 0
    grafo_n = grafo(1000)

def pintar_k():
    global vert
    #print(grafo_n.l_kruskal(cant_v))
    kruskal = grafo_n.l_kruskal2(cant_v)
    for ii in range(0,cant_v):
        for jj in range(0,cant_v):
            lienzo.itemconfig(arista[ii][jj], fill="light blue")
    for ii in kruskal:
        print(ii)
        print(ord(ii[1])-97,ord(ii[2])-97)
        z = ord(ii[1])-97
        w = ord(ii[2])-97
        lienzo.itemconfig(vert[z], fill="red")
        lienzo.itemconfig(vert[w], fill="red")
        lienzo.itemconfig(arista[z][w], fill="red")
        lienzo.itemconfig(arista[w][z], fill="red")
    # for ii in range(0,cant_v):
    #     for jj in range(0,cant_v):
    #         lienzo.itemconfig(arista[ii][jj], fill="light blue")
    # for ii in range(0,cant_v):
    #     for jj in range(0,cant_v):
    #         if kruskal[ii][jj] != 0:
    #             lienzo.itemconfig(vert[ii], fill="red")
    #             lienzo.itemconfig(vert[jj], fill="red")
    #             lienzo.itemconfig(arista[ii][jj], fill="red")

def pintar_p():
    global vert, init_v, opts, cant_v
    opts = [0 for i in range(cant_v)]
    for ii in range(0,cant_v):
        opts[ii] = chr(97+ii)
    def closew(vent, ent, opts):
        global init_v
        if ent.get() in opts:
            init_v = ent.get()
            vent.destroy()
    winit_v = tk.Tk()
    winit_v.title("Vertice")
    winit_v.resizable(0,0)
    framew = tk.Frame(winit_v)
    framew.grid(row=0, column=0)
    tex = tk.Label(framew, text="Ingrese vertice inicial")
    tex.grid(row=0, column=0)
    ent = ttk.Combobox(framew,values=opts)
    ent.grid(row=1, column=0)
    btn = tk.Button(framew, text="Ok", command=lambda: closew(winit_v, ent, opts))
    btn.grid(row=2, column=0)
    winit_v.wait_window()
    print("Vertice inicial ",+ord(init_v)-97)
    prim = grafo_n.l_prim(cant_v, ord(init_v)-97)
    for ii in range(0,cant_v):
        for jj in range(0,cant_v):
            lienzo.itemconfig(arista[ii][jj], fill="light blue")
    for ii in range(0,cant_v):
        for jj in range(0,cant_v):
            if prim[ii][jj] != 0:
                lienzo.itemconfig(vert[ii], fill="red")
                lienzo.itemconfig(vert[jj], fill="red")
                print(ii,jj)
                lienzo.itemconfig(arista[ii][jj], fill="red")

#inicio ventanas
global option
option = 0
def sel_arb(ven):
    global option
    option = 1
    ven.destroy()

def sel_aut(ven):
    global option
    option = 2
    ven.destroy()

root = tk.Tk()
root.title("AutoEd")
root.resizable(0,0)
framr = tk.Frame(root)
framr.grid(row=0, column=0)
text = tk.Label(framr, text="Eliga editor")
text.grid(row=0, column=0)
bt = tk.Button(framr, text="Arboles", command=lambda: sel_arb(root))
bt.grid(row=1, column=0)
bt = tk.Button(framr, text="Automatas", command=lambda: sel_aut(root))
bt.grid(row=1, column=1)
root.wait_window()

if option == 1:
    ventana = tk.Tk()
    ventana.geometry('640x510+0+0')
    ventana.title('Editor de arboles')
    ventana.resizable(0,0)
    frame_canv = tk.Frame(ventana)
    frame_canv.pack(side="top", fill="both")
    lienzo = tk.Canvas(frame_canv, width=640, height=480, background='light blue')
    lienzo.grid(row=0, column=0)
    lienzo.bind('<Button-1>', add_nodo)
    frame_btn = tk.Frame(ventana)
    frame_btn.pack(side="top", fill="both")
    btn = tk.Button(frame_btn, text="Detalles", command=detalles)
    btn.grid(row=0, column=0)
    btn = tk.Button(frame_btn, text="Limpiar", command=limpiar_canvas)
    btn.grid(row=0, column=1)
    btn = tk.Button(frame_btn, text="PRIM", command=pintar_p)
    btn.grid(row=0, column=2)
    btn = tk.Button(frame_btn, text="KRUSKAL", command=pintar_k)
    btn.grid(row=0, column=3)
    ventana.mainloop()

if option == 2:
    def final(num1,num2,tran,vinit,fin):
        print("paso final")
        if not vinit.get():
            return 0
        print("Listo")
        print("//Lista de datos//")
        print("Estados: ",+num1)
        print("Letras: ",+num2)
        print("Transiciones: ")
        for ii in range(0,num1*num2):
            print(tran[ii].get())
        print("Inicial: ", vinit.get())
        print("Finales")
        for ii in range(0,num1):
            print("Q",+ii,": ",+fin[ii].get())
        cont = 0
        estados = []
        transiciones = []
        inicial = [vinit.get()]
        alfa = []
        terminal = []
        for ii in range(0,num1):
            estados.append("Q"+str(ii))
        for ii in range(0,num1):
            for jj in range(0,num2):
                transiciones.append(("Q"+str(ii),tran[cont].get(),chr(97+jj)))
                cont = cont + 1
        for ii in range(0,num2):
            alfa.append(chr(97+ii))
        for ii in range(0,num1):
            if fin[ii].get() == 1:
                terminal.append("Q"+str(ii))
        print("//Datos transformados para clase automata")
        print(estados)
        print(transiciones)
        print(inicial)
        print(alfa)
        print(terminal)
        auto = automata()
        auto.set_estados(estados)
        auto.set_tran(transiciones)
        auto.set_inicial(inicial)
        auto.set_alfa(alfa)
        auto.set_final(terminal)
        auto.bdraw()
        load = Image.open("Digraph.gv.gif")
        render = ImageTk.PhotoImage(load)
        frame5 = tk.Frame(ventana)
        frame5.grid(row=4, column=0)
        img = tk.Label(frame5, image=render)
        img.image = render
        img.grid(row=0, column=0)

    def paso4(num2,num1,tran): # num1 = cantidad de estados, num2 = cantidad de letras (abc), inter = arreglo de intersecciones
        print("paso 3")
        for ii in range(0,num2*num1):
            if not tran[ii].get():
                return 0
        print("Listo")
        l_est = [0 for x in range(0,num1)]  
        cbox = [0 for x in range(0,num1)]  
        b_fin = [tk.IntVar() for x in range(0,num1)]        #arreglo de booleanos
        for ii in range(0,num1):
            l_est[ii] = "Q"+str(ii)
        frame4 = tk.Frame(ventana)
        frame4.grid(row=3, column=0)
        text = tk.Label(frame4, text="Inicial")
        text.grid(row=0, column=0)
        vinit = ttk.Combobox(frame4, values=l_est, width=5)
        vinit.grid(row=0, column=1)
        text = tk.Label(frame4, text="Finales")
        text.grid(row=0, column=2)
        for ii in range(0,num1):
            cbox[ii] = tk.Checkbutton(frame4, text=l_est[ii], variable=b_fin[ii], onvalue=1, offvalue=0, fg="green")
            cbox[ii].grid(row=0, column=3+ii)
        btn = tk.Button(frame4, text="Draw", command=lambda: final(num1,num2,tran,vinit,b_fin))
        btn.grid(row=1,column=0)    

    def paso3(num2,num1):
        print("paso 2")
        if num2.isdigit():
            if int(num2) != 0:
                print("es numero > 0")
            else:
                return 0
        else:
            return 0
        print("Listo")
        fila = 0
        num2 = int(num2)
        opts = [0 for x in range(0,num1)]
        tran = [0 for x in range(0,num1*num2)]
        for ii in range(0,num1):
            opts[ii] = "Q"+str(ii)
        frame3 = tk.Frame(ventana)
        frame3.grid(row=2, column=0)
        cont = 0
        for ii in range(0,num1):
            texto = "Conexiones para Q"+str(ii)
            text = tk.Label(frame3, text=texto)
            text.grid(row=fila, column=0)
            fila = fila + 1
            for jj in range(0,num2):
                texto = "Transicion para "+chr(97+jj)
                text = tk.Label(frame3, text=texto)
                text.grid(row=fila, column=0)
                tran[cont] = ttk.Combobox(frame3,values=opts, width=5)
                tran[cont].grid(row=fila, column=1)
                fila = fila + 1
                cont = cont + 1
        btn = tk.Button(frame3, text="OK", command=lambda: paso4(num2,num1,tran))
        btn.grid(row=fila+1, column=0)
        

    def paso2(num1): #Ingresar abc, verifica si el numero de estados es un numero > 0
        print("paso 1")
        if num1.isdigit():
            if int(num1) > 0:
                print("es numero > 0")
            else:
                return 0
        else:
            return 0
        print("Listo")
        num1 = int(num1)
        frame2 = tk.Frame(ventana)
        frame2.grid(row=1, column=0)
        text = tk.Label(frame2, text="Cantidad de letras (abc..): ")
        text.grid(row=0, column=0)
        ent2 = tk.Entry(frame2, width=5)
        ent2.grid(row=0, column=1)
        btn = tk.Button(frame2, text="OK", command=lambda: paso3(ent2.get(),num1))
        btn.grid(row=0, column=2)

    ventana = tk.Tk()
    # ventana.geometry('640x510+0+0')
    ventana.title('Editor de automatas')
    ventana.resizable(0,0)
    frame1 = tk.Frame(ventana)
    frame1.grid(row=0, column=0)
    text = tk.Label(frame1, text="Cantidad de estados: ")
    text.grid(row=0, column=0)
    ent = tk.Entry(frame1, width=5)
    ent.grid(row=0, column=1)
    btn = tk.Button(frame1, text="OK", command=lambda: paso2(ent.get()))
    btn.grid(row=0, column=2)
    ventana.mainloop()