from graphviz import Digraph, Graph
class mapas:
    def graphviz(self,filas,columnas,texto):
        
        x = ""
        tr_inicio = '''<TR>'''
        tr_fin = '''</TR>'''
        cuerpo = ""


        dot = Digraph(filename='Mapa', format= 'png')


        for k in range(1,filas+1):
            for j in range(1,columnas+1):
                i = ejecutar.buscar_coordenadas(k,j,texto).color
                try:
                    if i == "black":
                        x = x+'''<TD BGCOLOR="black"><FONT> </FONT></TD>'''


                    elif i == "green":
                        x = x+'''<TD BGCOLOR="green"><FONT> </FONT></TD>'''

                    
                    elif i == "blue":
                        x = x+'''<TD BGCOLOR="blue"><FONT> </FONT></TD>'''


                    elif i == "gray":
                        x = x+'''<TD BGCOLOR="gray"><FONT> </FONT></TD>'''
       
                    else:
                        x = x+'''<TD BGCOLOR="white"><FONT> </FONT></TD>'''

                except:
                    print("Error", i)
                    break
            cuerpo = cuerpo +tr_inicio+x+tr_fin            

        dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
                
                '''+cuerpo+'''

        </TABLE>>''')

                #generar salto de linea

                
        dot.view()

    def buscar_coordenadas(self,x2,y2,matriz):
        aux = matriz
        

        for j in range(1,y2):            
            aux = aux.derecha
        for i in range(1,x2):
            aux = aux.abajo
        return aux



# texto = "********************""*** **             *""*** *****E*****C****""*** ***** ***** ***R""E                   ""*** ** ** ** ** ****""*** ** ** ** ** **R*""*                  *""*** ** ** ** ** ****""*** ** ** ** ** ****""***                *""*** ** ** ** ** ****""*** **  E ** *R ****""*** *****         C*""*** *****C***** ****"
# print(texto)
ejecutar = mapas()
# ejecutar.graphviz(20,texto)       