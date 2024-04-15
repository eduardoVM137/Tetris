import random
import threading
import time
import string

# Formas de las piezas
Figuras = [
    [['[]', '[]', '[]', '[]']],  # Barra 0
    [['[]', '[]'], ['[]', '[]']],  # Cuadro 1
    [['[]', '[]', '  '], ['  ', '[]', '[]']],  # Z 2
    [['  ', '[]', '[]'], ['[]', '[]', '  ']],  # Z invertida 3  [['  ', '[]', '[]'], ['[]', '[]', '  ']],
    [['[]', '[]', '[]'], ['  ', '[]', '  ']],  # T 4
    [['[]', '[]', '[]'], ['[]', '  ', '  ']],  # L izquierda 5
    [['[]', '[]', '[]'], ['  ', '  ', '[]']],  # L derecha 6
] 
       
Figura_Seleccionada=2
Posicion_Fila_Figura=0 
Posicion_Columna_PrimerCorchete=0
Posicion_Fila_Ultima=0

matriz = [['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '], 
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', '  ', '  ', '  ', '  ']]

 
    

     
def PosicionPrimerCorchete():
    for fila in matriz:
        x=0
        for valor in fila:
            if(valor=="[]"):
                return fila,x
            x+=1
    return 0
def PosicionUltimoCorchete(ultimafila):#buscar en donde empieza despues de una linea en blanco
    bandera =False
    for fila in matriz:#hay que recorrer mejor la fila y no la matriz completa ,asi 
        x=0
        bandera=True
        for valor in fila:
            if(valor=="[]"):
                bandera=False
            x+=1
            
    return bandera

def Insertar_Figura():
    global Figura_Seleccionada
    Figura_Seleccionada =random.randint(1, 6)
    Fila_A_Insertar=-1
    posicion_corchete=0
    global Posicion_Columna_PrimerCorchete
    Posicion_Columna_PrimerCorchete=0
    global Posicion_Fila_Figura
    Posicion_Fila_Figura=0
    bandera=True
    
    for segmento in Figuras[Figura_Seleccionada]:
        Fila_A_Insertar+=1 
        posicion_corchete=0
        for valores in segmento: 
            if(valores=="[]"):
                matriz[Fila_A_Insertar][posicion_corchete]=valores
                if  Posicion_Columna_PrimerCorchete==0 and bandera :
                    Posicion_Columna_PrimerCorchete=posicion_corchete
                    bandera=False
            posicion_corchete+=1
                    
                
                
     
      #Rotar y aparecerla en x lugar
     
def MostrarMatriz():
    for fila in matriz:
     for elemento in fila: 
        print('|' + elemento , end='')
     print()
        
    return None
           
def Rotar_Figura():
    return ""
        
def Puede_Bajar_laFigura(ultimafila):#buscar la cantidad de cuados en la fila e iterar despues confirmar si cada uno entra,
    #checar como quitar las esquinas de las z y l ver que no colicionen con otra cosa
    #checo si abajo de ahi tiene un corchete
    ultimoCorchete=1
    for x in range(len(matriz[ultimafila])):
        if(matriz[ultimafila][x]=="[]"):
            if len(matriz)-1>ultimafila: 
              if len(matriz)-1==ultimafila:
                return False 
              if matriz[ultimafila+1][ultimoCorchete]=="[]": 
                MostrarMatriz()
                return False    
    
         
    return True
    
def Bajar_Figura():#Hacer un algoritmo que use la matriz figura para insertar una nueva imagen,y validar cada uno de sus corchetes no colisionen
  
        
    if (Figura_Seleccionada==0 and Puede_Bajar_laFigura(Posicion_Fila_Figura)): # 0 Barra ,ver si es horizontal hacer un metodo final 
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  "  
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+2]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+3]="  "
         
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+1]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+2]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+3]="[]" 
        
        
        return True
    
    if (Figura_Seleccionada==1 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # 1 Cuadrado
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  "  
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete]="[]"
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete+1]="[]"
        
        return True
        
    if (Figura_Seleccionada==2 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # Z invertida 2  [['  ', '[]', '[]'], ['[]', '[]', '  ']],
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  "
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+2]="  "
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete]="[]"  
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete+1]="[]"
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete+2]="[]"
        
        return True
    if (Figura_Seleccionada==3 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # Z invertida 3  [['  ', '[]', '[]'], ['[]', '[]', '  ']],
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  "
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete-1]="  " 
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete]="[]" 
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete]="[]"
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete-1]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+1]="[]"
        return True

    if (Figura_Seleccionada==4 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # 4 T
        
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  " 
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+2]="  "  
        
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+2]="[]"   
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete+1]="[]"
        
        return True
    if (Figura_Seleccionada==5 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # 5 L IZQ
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  " 
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+2]="  "  
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+1]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+2]="[]"
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete]="[]"
        
        return True

    if (Figura_Seleccionada==6 and Puede_Bajar_laFigura(Posicion_Fila_Figura+1)): # 6 L DERE
        
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete]="  "
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+1]="  " 
        matriz[Posicion_Fila_Figura][Posicion_Columna_PrimerCorchete+2]="  "  
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete+1]="[]"
        matriz[Posicion_Fila_Figura+1][Posicion_Columna_PrimerCorchete]="[]"
        matriz[Posicion_Fila_Figura+2][Posicion_Columna_PrimerCorchete+2]="[]"
        
        return True
    return False
        
         
            
        
             
                        
 
   
# Ejecutar la función luego de 3 segundos.
def ActualizarPantalla():
    while True:  
        Insertar_Figura() 
        print(MostrarMatriz()) 
        filas = len(matriz) - 2 #se resta el tamaño del arreglo para que sea igual al iterar y uno mas para que no use valores fuera del arreglo
        global Posicion_Fila_Figura
        Posicion_Fila_Figura=0
        time.sleep(2)
        for fila_actual in range(filas): 
           
            print(MostrarMatriz()) 
            if (Bajar_Figura()):
                print(MostrarMatriz()) 
                time.sleep(1)
                Posicion_Fila_Figura+=1#para mover basta con sumarle 1 o restarle 1 a la 
            else:
                 break  
             
        print("HAZ PERDIDO ,SE TE ACABO EL TIEMPO")   
    

def IniciarJuego():
 ActualizarPantalla()

    



IniciarJuego()