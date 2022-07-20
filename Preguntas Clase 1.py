#!/usr/bin/env python
# coding: utf-8

# # Preguntas

# ## 1 Suponga que tiene una lista [1, 2, 3, 2, 1] y desea crear una nueva lista sin números dobles, después de resolver este problema, intente reescribirla como una sola línea
# ### Un one liner en programación es un programa existente de una sola línea. Si no logras escribir una sola línea, no te preocupes. el codigo one liner es a menudo difícile de leer y, como hemos aprendido esta semana: los lenguajes de programación están destinados a ser legibles para las personas. Así que no te preocupes si estás usando demasiado código para resolver un problema, debes preguntarte: ¿yo o alguien más entenderá esto dentro de 3 años?

# In[3]:


Lista_1=[1,2,3,4,1]
Set_1= set(Lista_1)
Lista_2=list(Set_1)


print(Lista_2)


# #### Ya que, se repite un valor es importante reconocer cada una de las caracteristicas de los objetos, y para que no existan valores repetidos se debe transformar la primera lista en un "set", y despues regresarle a la caracteristica original una lista.

# ## 2 Slicing puede tener 3 parámetros, inicio, final y paso. Sin embargo, a menudo escribirá o leerá operaciones de corte con menos de 3 parámetros. En esta pregunta, debe volver a escribir todos los ejemplos en operaciones de corte con 3 parámetros. Después de haberlas reescrito, verifique si sus respuestas dan los mismos resultados

# In[4]:


string_1 = 'abcde'
print(string_1[1:3])
print(string_1[-3:-2])

print(string_1[:3])
print(string_1[3:])
print(string_1[:])

print(string_1[-2:])
print(string_1[:-2])

print(string_1[::])
print(string_1[::-1])

print(string_1[:3:1])
print(string_1[:3:-1])

print(string_1[1::])
print(string_1[:1:-1])


# In[46]:


string_2='abcde'
print(string_2[1:3:1])
print(string_2[-3:-5:-2])
print(string_2[0:3:1])
print(string_2[3:5:1])
print(string_2[0:5:1])
print(string_2[-2::1])
print(string_2[-5:-2:])
print(string_2[::])
print(string_2[-1:-6:-1])
print(string_2[0:3:1])
print(string_2[-1:-2:-1])
print(string_2[1:5:1])
print(string_2[:-4:-1])


# ## 3 Hemos construido un diccionario que se puede usar para encontrar el resultado si dos booleanos están conectados con el operador y
# ## Reescribe este diccionario para encontrar el resultado si dos booleanos están conectados con el operador o
# ## Python no tiene un operador XOR, busque en Internet lo que se supone que debe hacer el operador XOR y cree un diccionario que proporcione el resultado de una operación XOR

# In[47]:


age = 40
blood_type = 'A'
my_and = {(True, True): True, (True, False): False, (False, True): False, (False, False): False }
print(my_and[age < 70, blood_type == 'B'])


# In[66]:


age = 40
blood_type = 'A'

my_and = {True: True ,False:False}

print(my_and[age < 70 or blood_type == 'B'])


# In[91]:


age = 40
blood_type = 'A'

my_and = {True: True ,False:False}

print(my_and[operator.xor((age<70),(blood_type =='B'))])
print(my_and[(age<70)^(blood_type=='B')])


# ##### el resultado es True, porque cumple con las normas de logica matematica en la cual, una afirmació y una negación es una verdad.

# ## 4 En 'Las listas pueden contener listas y así formar tablas de múltiples dimensiones' se les mostro una secuencia ganadora en tres en raya. Como es muy importante para el análisis de datos y la visualización de datos que se sienta cómodo trabajando con tablas poli-dimensionales, le pedimos que reescriba la secuencia con un segundo jugador más inteligente (o un jugador que aprendió el juego de memoria) donde el juego termina en un empate.

# In[48]:


tic_tac_toe_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print() 
tic_tac_toe_board[1][1] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print() 
tic_tac_toe_board[1][2] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[0][2] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[2][0] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[0][0] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()# And the next move X wins independent what player O plays


# In[104]:


tic_tac_toe_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print() 
tic_tac_toe_board[0][0] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print() 
tic_tac_toe_board[2][2] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[2][1] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[2][0] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[1][1] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[0][1] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[1][0] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[1][2] = 'O'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()
tic_tac_toe_board[0][2] = 'X'
print(tic_tac_toe_board[0]) 
print(tic_tac_toe_board[1]) 
print(tic_tac_toe_board[2])
print()


# ## 5 Ejecute el siguiente programa, vea si puede encontrar algo extraño y explique el resultado usando su conocimiento de recolección de basura

# In[49]:


list_5 = [1, 2, 3]
print(f"The value of the list refered to by list_5 is {list_5} and its address is {id(list_5)}")
list_5 = [1 , 1, 3]
print(f"The value of the list refered to by list_5 is {list_5} and its address is {id(list_5)}")
list_5 = [1, 1, 4]
print(f"The value of the list refered to by list_5 is {list_5} and its address is {id(list_5)}")


# ##### La Lista se va creando cada vez más y el principio de la recolección de basura es que cada vez que se ejecuta una lista con el mismo nombre esta tiende a ser reemplazada por la nueva y se elimina la anterior

# ## 6 Las cadenas son inmutables, pero ¿por qué funciona lo siguiente? ¿Claramente cambiamos el valor de la cadena llamada string_1? ¿Qué afirmaciones agregaría para aclarar lo que ha sucedido? usar id

# In[109]:


string_1 = "text 1"
print(string_1)
print(string_1)
string_1 = "text 2"

print(id(string_1))
print(id(string_1))


# ##### Porque solo se esta cambiando el contenido, mas no se esta modificando el objeto per se

# In[ ]:




