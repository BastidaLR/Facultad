import numpy as np
from random import randint


'''
Initializes a square matrix of size x size shape
'''
def initial_square_matrix_generator(size): 
    initial_matrix = np.zeros(shape=(size,size))
    return initial_matrix

'''
Fills any square matrix with random integers from 0 to 5
'''
def random_fill(matrix):
    for i in range(0,len(matrix[0])):
        for j in range(0,len(matrix[0])):
            matrix[i][j] = randint(0,5)
    return matrix



'''
Segundo problema de la tarea
'''

#Definición del vector a 
a = [1,2,3]

#Definición del tensor de segundo orden phi
row_1 = [3,2,1]
row_2 = [4,7,8]
row_3 = [2,1,3]
phi = np.zeros(shape=(3,3))
for i in range(0,len(phi[0])):
    phi[0,i] = row_1[i]
    phi[1,i] = row_2[i]
    phi[2,i] = row_3[i]


#Llamamos a las funciones random_fill e initial_square_matrix_generator para hacer una función inicial 
initial_matrix = random_fill(initial_square_matrix_generator(3))



def a_tilde(initial_matrix,a_i):
    a_tilde = []
    for i in range(0,len(initial_matrix[0])):
        addition = 0 
        for j in range(0,len(initial_matrix[0])):
            addition = addition + a_i[j] * initial_matrix[i][j]
        a_tilde.append(addition)
    return a_tilde



def phi_tilde(initial_matrix, phi_i_j):
    phi_tilde_tilde = np.zeros(shape=(3,3))
    b = len(initial_matrix[0])
    for i in range(0,b):
        for j in range(0,b):
            for k in range(0,b):
                for s in range(0,b):
                    phi_tilde_tilde[i][j] = initial_matrix[i][k] * initial_matrix[j][s] * phi_i_j[k][s]
    return phi_tilde_tilde




'''
Tercer problema de la tarea sobre las invariantes que define Reddy
'''

def sum_over_list(lista):
    suma = 0
    for i in range(0,len(lista)):
        suma = suma + lista[i]
    return suma


def trace_matrix(matrix):
    suma = 0 
    for i in range(0,len(matrix[0])):
        suma = suma + matrix[i][i]
    return suma


def multiplicación_resta(matrix):
    suma = 0 
    for i in range(0,len(matrix[0])):
        for j in range(0,len(matrix[0])):
            suma = 0.5 * (matrix[i][i] * matrix[j][j] - matrix[i][j] * matrix[j][i])
    return suma


def determinante(matrix):
    suma = np.linalg.det(matrix)
    return suma

'''
A continuación una función que imprime los valores de los parámetros que nos piden para el problema 3.
Notar que como todas las funciones y los tensores a y phi están previamente definidos, la única
variable que le pasamos a esta función es la matriz de enteros aleatoros (initial_matrix). Esto se hizo de este
modo para facilitar la implementación de la rutina que ejercute esto mismo para las cinco diferentes matrices
aleatorias del problema 5
'''
def show_results(initial_matrix):
    print("a_{ii} es igual a: " + str(sum_over_list(a)))
    print("La traza de phi es: " + str(trace_matrix(phi)))
    print("El tercer parámetro que nos piden es: " + str(multiplicación_resta(phi)))
    print("El determinante de phi es: " + str(round(determinante(phi),3)))
    
    print("\n")
    print("Los mismos parámetros para para los tensores con tilde son:")
    print("a_{ii}_tilde es igual a: " + str(sum_over_list(a_tilde(initial_matrix,a))))
    print("La traza de phi es: " + str(trace_matrix(phi_tilde(initial_matrix,phi))))
    print("El tercer parámetro que nos piden es: " + str(multiplicación_resta(phi_tilde(initial_matrix,phi))))
    print("El determinante de phi es: " + str(round(determinante(phi_tilde(initial_matrix,phi)),3)))
    
def show_only_tilde_results(initial_matrix):
    print("Los mismos parámetros para para los tensores con tilde son:")
    print("a_{ii}_tilde es igual a: " + str(sum_over_list(a_tilde(initial_matrix,a))))
    print("La traza de phi tilde es: " + str(trace_matrix(phi_tilde(initial_matrix,phi))))
    print("El tercer parámetro que nos piden es: " + str(multiplicación_resta(phi_tilde(initial_matrix,phi))))
    print("El determinante de phi tilde es: " + str(round(determinante(phi_tilde(initial_matrix,phi)),3)))
    
    
'''
Para correr la función show_results y ver el resultado de los parámetros que nos piden en el problema,
cambiar el valor de la variable 'Mostrar_resultados' a True para visualizarlos 
'''
Mostrar_resultados = False

if Mostrar_resultados:
    show_results(initial_matrix)
    
    
    
    
'''
Quinto problema de la tarea sobre la rutina que itere lo hecho para el tercer problema pero para cinco 
matrices diferentes
'''

'''
Función que genera cinco matrices cuadradas de tamaño 3x3 y le aplica las funciones que se definieron anteriormente
muestra también la matriz de enteros aleatorios con la que se está operando para que sea más claro lo que 
ocurre
'''
def iteración(integer):
    counter = 0
    while counter < integer:
        initial_matrix = random_fill(initial_square_matrix_generator(3))
        print(initial_matrix)
        show_only_tilde_results(initial_matrix)
        print(4*"\n")
        counter = counter + 1
        

'''
Nuevamente, cambiar el valor de Mostrar_iteración a True para ver los resultados. También se puede cambiar el
5 que es parámetros de iteración() por cualquier otro enter para mostrar los resultados para más
matrices aleatorias
'''
Mostrar_iteración = True

if Mostrar_iteración:
    iteración(5)
