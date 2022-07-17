import pandas as pd
import numpy as np
import math as math
import sympy as sp
#Se importan las librerias tales como pandas o numpy para entrada y salida de valores matemáticos

MM=9999
Colm=[]
Row=["Z"]
#Se define columnas y filas para la matriz
print("*****MÉTODO DE LA GRAN M********\n")

print("EJERCICIO #1 (Minimizar 6X1+5X2)\n")
Mode=2
Urs=1
Sol=2
V=2
C=3
#Existen dos modos, 1 es maximizar mientras que 1 es minimizar
#Se define además la existencia de valores mayores o iguales que con Sol
#Se definen 2 variables X (V) y 3 ecuaciones (C)

con=[]
Added=[]
ZZ=[]
#Imprime el problema
Zeroline=["Z ="]
Printcc=[]
counter1=1
#Define la ecuación solución Z
for i in range(0,C+1):
  if i==0:
    #Elige los valores de X1 y X2 en Z, y procede a sumarlos a ambos en la impresión
    for k in range(1,V+1):
      if k==1:
        Z=6
      elif k==2:
        Z=5
      ZZ.append(Z)
      Colm=Colm+["x_"+str(counter1)]
      if Z>0:
        Zeroline.append("+"+str(Z)+" "+"x"+str(counter1))
      elif Z<0:
        Zeroline.append(str(Z)+" "+"x"+str(counter1))
      counter1=counter1+1
    ZZ.append(0)
    Added.append(ZZ)
  # Elige los tipos de ecuaciones, si es tipo 3 es mayor o igual que, 2 es igual y 1 es menor o igual que
  else:
    if Sol==2:
      if i==1:
        Type=2
      if i==2:
        Type=3
      if i==3:
        Type=1
      con.append(Type)
    else:
      Type=1
      con.append(Type)
    Addx=[]
    Printc=[]
    for j in range(0,V+1):
      if j==V:
        Xin = float(0)
        if i==1:
          Xin=3
        if i==2:
          Xin=6
        if i==3:
          Xin=4
        # Recoge los valores finales de las ecuaciones y se juntan con el tipo de ecuación para la impresión.
        Addx.append(Xin)
        if Type==1:
          Printc.append("<="+str(Xin))
        elif Type==2:
          Printc.append("="+str(Xin))
        elif Type==3:
          Printc.append(">="+str(Xin))
      else:
        Xin = float(0)
        if i==1 and j==0:
          Xin=3
        if i==1 and j==1:
          Xin=1
        if i==2 and j==0:
          Xin=4
        if i==2 and j==1:
          Xin=3
        if i==3 and j==0:
          Xin=1
        if i==3 and j==1:
          Xin=2
        # Recoge todos los valores de X1 y X2 para cada una de las ecuaciones.
        Addx.append(Xin)
        if Xin<0:
          Printc.append(str(Xin)+" "+"x"+str(j+1))
        elif Xin>0:
          Printc.append("+"+str(Xin)+" "+"x"+str(j+1))
    Added.append(Addx)
    Printcc=Printcc+[Printc]
RHS=[]
# A partir de aca regleja los datos dados como el problema las ecuaciones a las cuales esta sujeto,
# Crea también matriz de valores para Z, X1, X2 y las variables artificiales y de holgura.
for i in range(0,len(Added)):
  RHS.append(Added[i][-1])
  Added[i].pop(-1)
counter2=1
counter3=1
for i in range(1,len(con)+1):
  # Define la posición de las fila de holgura junto a sus variables.
  if con[i-1]==1:
    Row=Row+["S_"+str(counter2)]
    Colm=Colm+["s_"+str(counter2)]

    counter2=counter2+1
    for j in range(0,len(Added)):
      if j != i:
        Added[j].append(0)
      else:
        Added[j].append(1)

  # Define la posición de las fila de variables artificiales junto a sus variables.
  elif con[i-1]==2:
    Colm=Colm+["R_"+str(counter3)]
    Row=Row+["R_"+str(counter3)]
    counter3=counter3+1
    for jj in range(0,len(Added)):
      if jj == 0:
        if Mode==1:
          Added[jj].append(-MM)
        elif Mode==2:
          Added[jj].append(MM)
      elif jj==i:
        Added[jj].append(1)
      elif (jj !=0 and jj !=i):
        Added[jj].append(0)
  # Realiza el resto de la tabla con X1 y X2 y Z.
  elif con[i-1]==3:
    Colm=Colm+["s_"+str(counter2)]
    Colm=Colm+["R_"+str(counter3)]
    Row=Row+["R_"+str(counter3)]
    counter2=counter2+1
    counter3=counter3+1
    for jjj in range(0,len(Added)):
      if jjj==0:
        if Mode==1:
          Added[jjj].append(0)
          Added[jjj].append(-MM)
        elif Mode==2:
          Added[jjj].append(0)
          Added[jjj].append(MM)
      elif jjj==i:
        Added[jjj].append(-1)
        Added[jjj].append(1)
      elif (jjj != 0 and jjj != i):
        Added[jjj].append(0)
        Added[jjj].append(0)
for i in range(len(RHS)):
  Added[i].append(RHS[i])
Added=np.array(Added)

# Verifica si el Modo es 1 y si es asi, se maximiza.
if Mode==1:
  Added[0]=-1*(Added[0])
Added=np.array(Added).tolist()
A=Added

#METODO DE LA GRAN M CALCULO

if Sol == 2:
  print("*-*-*-*-*-*-*-*(Problema)*-*-*-*-*-*-*")
  print(*Zeroline, sep=' ')
  print("Sujeto a:")
  for i in range(0, len(Printcc)):
    print(*Printcc[i], sep=' ')
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)
  MM = 9999
  Mdisplay = sp.symbols("M")
  # Muestra el problema
  A = np.array(A, dtype=float)
  Zero = []
  for i in range(len(A[0])):
    if (A[0][i] != MM):
      Zero.append(A[0][i])
    else:
      Zero.append(Mdisplay)
  B = np.delete(A, 0, axis=0)
  B = np.array(B).tolist()
  AA = []
  AA.append(Zero)
  for i in range(len(B)):
    AA.append(B[i])
  # Realiza y verifica las variables para mostrar primera tabla
  print("------------------(Tabla: 1 )----------------")
  print(pd.DataFrame(AA, index=Row, columns=Colm + ["RHS"]))

  Mcolm = []
  Mrow = []
  for i in range(len(A[0])):
    if (A[0][i] == MM):
      Mcolm.append(i)
  for i in range(1, len(A)):
    for j in Mcolm:
      if A[i][j] == 1:
        Mrow.append(i)
  Mrow = np.array(Mrow)
  # Verifica el pivote 1 y añade apropiadamente los valores con M
  # Prepara la segunda tabla
  row = []
  rowq = []
  for i in Mrow:
    row = -MM * (A[i])
    rowq = [element * -Mdisplay for element in AA[i]]
    A[0] = np.add(row, A[0])
    AA[0] = np.add(rowq, AA[0])
    row = []

  print("------------------(Tabla: 2 )----------------")
  print(pd.DataFrame(AA, index=Row, columns=Colm + ["RHS"]))
  xz = 3  # (xz=Counter for Table Number)
  # ___________________________________________________________________#
  MA = 0
  while min(A[0, :-1]) < 0 or MA == 1:
    if MA != 1:
      k = np.argmin(A[0, :-1])
    test = []
    for i in range(1, A.shape[0]):
      if (A[i, k] < 0) or (A[i, k] == 0):
        test.append(math.inf)
        continue
      else:
        test.append(A[i, -1] / A[i, k])
    test = np.array(test)
    # Empieza a verificar los pivotes y divide X1 o X2 hasta encontrarlo.
    s = 0
    for i in test:
      if i == min(test[0:]):
        s = s + 1
    if s > 1 and min(test) != math.inf:
      print("***************(Tenemos degenerancia en esta tabla)*********************")
    elif min(test) == math.inf:
      print("***************(Hay valores ilimitados en esta tabla)************************")
      break
    # Verifica el tipo de datos existente en la tabla actual.
    n = int(np.argmin(test[0:])) + 1
    PashneRow = np.divide(A[n], A[n][k])
    PashneRowq = np.divide(AA[n], AA[n][k])
    A = np.array(A).tolist()
    AA = np.array(AA).tolist()
    print("***************************")
    print(Colm[k], "Entrada \t", Row[n], "Salida")
    print("***************************")
    Row[n] = Colm[k]
    # Entra las ecuaciones de dedución de renglones a partir del pivote y calcula.
    for j in range(len(A)):
      Newrow = []
      if j == n:
        A[n] = np.divide(A[n], A[n][k])
        AA[n] = np.divide(AA[n], AA[n][k], dtype=float)
        continue
      else:
        Newrow = PashneRow
        Newrowq = PashneRowq
        Newrow = Newrow * (-1)
        Newrowq = Newrowq * (-1)
        Newrow = Newrow * A[j][k]
        Newrowq = Newrowq * AA[j][k]
        Newrow = list(Newrow)
        Newrowq = list(Newrowq)
        added = np.add(Newrow, A[j])
        addedq = np.add(Newrowq, AA[j])
        A[j] = list(added)
        AA[j] = list(addedq)
    A = np.array(A, dtype=float)
    limiti = 0
    for i in range(0, len(A[0])):
      limiti = sp.limit(AA[0][i], Mdisplay, 0)
      if math.isclose(limiti, A[0][i]):
        AA[0][i] = A[0][i]
    # Se realiza las multiples ecuaciones a cada una de los renglones a parte del renglón del pivote
    # Después se rearma la tabla.
    print("--------------- (Tabla:", xz, ")------------------")
    print(pd.DataFrame(AA, index=Row, columns=Colm + ["RHS"]))
    xz = xz + 1
    # Verifica la respuesta y si es unica.
    MA = 0
    if Urs != 2:
      for i in range(0, V):
        if A[0][i] == 0 and Colm[i] not in Row:
          k = i
          MA = 1
          print("*****Tenemos multiples respuestas!!!!*****")
  Righth = round(A[0][-1], 3)
  # Termina el calculo y finalmente tiene el valor de Z
  if Mode == 1 and min(test) != math.inf:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("El valor optimo de Z es =", Righth)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  elif Mode == 2 and min(test) != math.inf:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("El valor optimo de Z es =", -1 * Righth)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  # Imprime el valor de Z

  # Si la respuesta es incorrecta o inviable, la muestra en display.
  Row = str(Row)
  if (Row.find("R_") != -1):
    print("---------------------Respuesta Inviable----------------------")
