from tkinter import messagebox

from graphviz import Digraph

list_error = []

class CError:
    def __int__(self, linea, columna, descripcion):
        self.linea = linea
        self.columna = columna
        self.descripcion = descripcion

def insert_error(error : CError):
    global list_error
    list_error.append(error)

def report_errors():
    global list_error
    s = Digraph('structs', filename='reporteTabla.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>Linea</TD><TD>Columna</TD><TD>Descripcion</TD></TR> '
    if len(list_error)>0:
        for t in list_error:
            c+= '<TR>\n'
            c+= '<TD>\n'
            c+= str(t.linea)
            c+= '\n</TD><TD>'
            c+= str(t.columna)
            c+= '\n</TD><TD>'
            c+= str(t.descripcion)
            c+= '\n</TD></TR>'
        c += '</TABLE>>, ];'
        s.body.append(c)
        s.view()
    else:
        messagebox.showinfo(message="Lexico y sintatico correcto", title="Correcto")
    list_error = []