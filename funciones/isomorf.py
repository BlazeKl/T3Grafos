import tkinter as tk
from tkinter import messagebox
from .clasegrafo import grafo


def v_isomorfismo(x: grafo,v,d):
    global grafo_n2,pos_x, pos_y, click, vert, cant_v, cant_a, j
    grafo_n2 = grafo(1000)
    pos_x = 0
    pos_y = 0
    click = 0
    vert = [0 for x in range(999)]
    cant_v = 0
    cant_a = 0
    j = 0
    vert = [0 for x in range(999)]

    def add_nodo(event):
        global vert, cant_v
        print("Insertando nodo")
        print("(",+event.x,",",+event.y,")")
        vert[cant_v] = canv.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill='black', activeoutline='green', activewidth=3)
        canv.create_text(event.x-13, event.y-13, text=chr(97+cant_v))
        canv.tag_bind(vert[cant_v], '<Button-3>', lambda event, var1 = cant_v, var2 = event.x, var3 = event.y: add_arista(event,var1,var2,var3))
        cant_v += 1

    def add_arista(event,i, x, y):
        global pos_x, pos_y, j, grafo_n2, is_dirigido2, cant_a
        global click
        if click:
            print("insertando arista end =", chr(97+i))
            if grafo_n2.get_p(j,i) == 0:
                    cant_a += 1
            if d:
                if i == j:
                    print("bucle")
                    arista = canv.create_line(x, y, x-25, y, x-25, y+25, x, y+25, x, y, arrow=tk.LAST, arrowshape=(16,20,6), fill='black', width=2, smooth=1)
                else:
                    arista = canv.create_line(pos_x, pos_y, x, y, arrow=tk.LAST, arrowshape=(16,20,6), fill='black', width=2)  
                grafo_n2.set_n(1,j,i)
                grafo_n2.sum_p(1,j,i)

            else:
                if i == j:
                    print("bucle")
                    arista = canv.create_line(x, y, x-25, y, x-25, y+25, x, y+25, x, y, fill='black', width=2, smooth=1)
                    grafo_n2.set_n(1,i,j)
                    grafo_n2.sum_p(1,i,j)
                else:
                    arista = canv.create_line(pos_x, pos_y, x, y, fill='black', width=2)
                    grafo_n2.set_n(1,i,j)
                    grafo_n2.set_n(1,j,i)
                    grafo_n2.sum_p(1,i,j)
                    grafo_n2.sum_p(1,j,i)
            canv.tag_lower(arista)
            print("(",+x,",",+y,")")
            click=0
        else:
            print("insertando arista start = ",chr(97+i))
            pos_x = x
            pos_y = y
            j = i
            print("(",+pos_x,",",+pos_y,")")
            click=1

    def limpiar_canvas():
        print("limpiar canvas")
        global pos_x, pos_y, click, vert, cant_v, cant_a, grafo_n2
        canv.delete("all")
        pos_x=0
        pos_y=0
        z=0
        click = 0
        vert = [0 for x in range(999)]
        cant_v = 0
        cant_a = 0
        grafo_n2 = grafo(1000)

    def comparar_g(graf: grafo, x: grafo, v):
        if (cant_v != v):
            messagebox.showinfo("Resultado", "No son isomorfos")
        else:
            res = True
            for i in range(0,v):
                for j in range(0,v):
                    if graf.get_p(i,j) != x.get_p(i,j):
                        res = False
            if res:
                messagebox.showinfo("Resultado", "Son isomorfos")
            else:
                messagebox.showinfo("Resultado", "No son isomorfos")

    menu = tk.Tk()
    menu.title("Grafo a comparar")
    menu.geometry('640x510+640+0')
    menu.resizable(height=0, width=0)
    frame1 = tk.Frame(menu)
    frame1.grid(row=0, column=0)
    canv = tk.Canvas(frame1, width=640, height=480, background='green yellow')
    canv.grid(row=0, column=0)
    canv.bind('<Button-1>', add_nodo)
    frame2 = tk.Frame(menu)
    frame2.grid(row=1, column=0)
    btn = tk.Button(frame2, text="Comparar", command=lambda: comparar_g(grafo_n2, x, v))
    btn.grid(row=0, column=0)
    x.print_mat(v)
    menu.mainloop()