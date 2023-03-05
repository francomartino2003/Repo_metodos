
def suma_vectores(vector1, vector2):
    #el vector1 debe tener la misma longitud que el vector2
    i = 0
    while i < len(vector1):
        vector1[i] += vector2[i]
        i+= 1
    return vector1

def resta_vectores(vector1, vector2):
    #el vector1 debe tener la misma longitud que el vector2
    i = 0
    while i < len(vector1):
        vector1[i] -= vector2[i]
        i+= 1
    return vector1

def suma_matrices(matriz1, matriz2):
    #la matriz1 debe tener la misma longitud que la matriz2
    i = 0
    while i < len(matriz1):
        matriz1[i] = suma_vectores(matriz1[i],matriz2[i])
        i+= 1
    return matriz1

def resta_matrices(matriz1, matriz2):
    #la matriz1 debe tener la misma longitud que la matriz2
    i = 0
    while i < len(matriz1):
        matriz1[i] = resta_vectores(matriz1[i],matriz2[i])
        i+= 1
    return matriz1


vec1 = [1,2,3]
vec2 = [0,1,-1]
print(suma_vectores(vec1,vec2))
vec1 = [1,2,3]
vec2 = [0,1,-1]
print(resta_vectores(vec1,vec2))
mat1 = [[1, 2, 3],
        [3, 2, 0],
        [1, -1, 0]]
mat2 = [[1, 3, -2],
        [2, 2, 0],
        [1, -1, 0]]
print(suma_matrices(mat1,mat2))
mat1 = [[1, 2, 3],
        [3, 2, 0],
        [1, -1, 0]]
mat2 = [[1, 3, -2],
        [2, 2, 0],
        [1, -1, 0]]
print(resta_matrices(mat1,mat2))