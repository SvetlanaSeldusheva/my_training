def get_matrix (n,m,value):
    matrix = []
    for i in range (n):
        matrix.append ([])
        for j in range (m):
            matrix [i].append (value)
    return matrix

print (get_matrix (3,3,7))
print (get_matrix (2,2,10))
print (get_matrix (3,5,42))
print (get_matrix (4,5,13))