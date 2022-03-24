from Nodos import Nodo, Nuevo_Nodo
from robots import Nodo_dron, Nuevo_nodo_dron

class mapas:
    def graphviz():
        mapa = Nuevo_Nodo.devolver
        z = 0
        x = ""
        tr_inicio = '''<TR>'''
        tr_fin = '''</TR>'''
        cuerpo = ""


        dot = Digraph(filename='Grafica de pisos', format= 'png')
        
        z = int(patron_encontrado.columna)
        w = 0
        print("z: ", z)

        for i in codigo_piso.codigo:
                if i == "W":
                    x = x+'''<TD BGCOLOR="white"><FONT >W</FONT></TD>'''
                    w = w + 1
                    if w == z:
                        cuerpo = cuerpo +tr_inicio+x+tr_fin
                        x = ""
                        w = 0
                elif i == "B":
                    x = x+'''<TD BGCOLOR="black"><FONT COLOR="white">B</FONT></TD>'''
                    w = w + 1
                    if w == z:
                        cuerpo = cuerpo +tr_inicio+x+tr_fin
                        x = ""
                        w = 0
                else:
                    None

        dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
                
                '''+cuerpo+'''

        </TABLE>>''')

                #generar salto de linea

                
        dot.view()


        