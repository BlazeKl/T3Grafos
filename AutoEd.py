#AutoEdUtem, Editor de Automatas y Arboles
#1,2021
#Felipe Perez Cares
#Alex Bidart Orellana
#Alex Pino Moya
#Pablo Sepulveda Fernandez
#Oscar Munos Retamal
#
#librerias
import collections
import tkinter as tk
from typing import Collection
from funciones.clasegrafo import grafo

#variables
global pos_x, pos_y, click, vert, cant_v, cant_a, j, grafo_n, peso
pos_x = 0
pos_y = 0
click = 0
vert = [0 for x in range(999)]
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
            arista = lienzo.create_line(pos_x, pos_y, x, y, fill='black', width=2)
            grafo_n.set_p(peso,i,j)
            grafo_n.set_p(peso,j,i)
            lienzo.tag_lower(arista)
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
    menu.title('Detalles de grafo')
    menu.resizable(0,0)
    frame1 = tk.Frame(menu)
    frame1.grid(row=0, column=0)
    text = tk.Label(frame1, text="Peso")
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
    frame3.grid(row=4, column=0)
    text = tk.Label(frame3, text="Numero de regiones : ")
    text.grid(row=10, column=0)
    tabla = tk.Entry(frame3, width=5, bg='black', fg='white')
    tabla.grid(row=10, column=1)
    tabla.insert(tk.END, grafo_n.n_regiones(cant_a,cant_v))
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

#inicio ventana
ventana = tk.Tk()
ventana.geometry('640x510+0+0')
ventana.title('Editor de grafos')
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
btn = tk.Button(frame_btn, text="PRIM", command=detalles)
btn.grid(row=0, column=2)
btn = tk.Button(frame_btn, text="KRUSKAL", command=detalles)
btn.grid(row=0, column=3)
ventana.mainloop()