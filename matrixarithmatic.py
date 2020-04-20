def matrix_add(matrix1,matrix2):
        result_matrix = []
        if matrix1[2] != matrix2[2] or matrix1[1] != matrix2[1]:
            raise ValueError("Matrix must have same size")
        for cr in range(matrix1[1]):
            result_row = []
            for cc in range(matrix1[2]):
                result_row.append(matrix1[0][cr][cc] + matrix2[0][cr][cc])
            result_matrix.append(result_row)
        return result_matrix

def matrix_sub(matrix1,matrix2):

        result_matrix = []
        if matrix1[1] != matrix2[1] or matrix1[2] != matrix2[2]:
            raise ValueError("Matrix must have same size")
        for cr in range(matrix1[1]):
            result_row = []
            for cc in range(matrix1[2]):
                result_row.append(matrix1[0][cr][cc] - matrix2[0][cr][cc])
            result_matrix.append(result_row)
        return result_matrix


def matrix_mul(matrix1,matrix2):

        result_matrix = []
        if matrix1[2] != matrix2[1]:
            raise ValueError("First Matrix column must equal to Second Matrix row")
        for cra in range(matrix1[1]):
            result_row = []
            for ccb in range(matrix2[2]):
                result_element = 0
                for cca in range(matrix1[2]):
                    result_element += matrix1[0][cra][cca] * matrix2[0][cca][ccb]
                result_row.append(result_element)
            result_matrix.append(result_row)
        return result_matrix

            
def matrix_transpose(matrix):
    result_matrix = []
    for cc in range(matrix[2]):
        result_row = []
        for cr in range(matrix[1]):
            result_row.append(matrix[0][cr][cc])
        result_matrix.append(result_row)
    return result_matrix
    


def print_matrix_form(matrix):
    print("[")
    for i in range(len(matrix)):
        print(matrix[i])
    print("]\n")
    

def matrix_collect(name):
    matrix = []
    row = int(input(f"Enter Row for {name} :" ))
    column = int(input(f"Enter Column for {name} :" ))
    for current_row in range(row):
        element = input(f"Enter the element for row {current_row+1} with space :")
        esplit = element.split(" ")
        while len(esplit) is not column:
            element = input(f"Enter the element for row {current_row+1} with space correctly :")
            esplit = element.split(" ")
        esplitf = [float(x) for x in esplit]
        matrix.append(esplitf)
    return [matrix,row,column]


print("""
Function        Command
Adding          add
Subtracting     sub
Multiplying     mul
Transpose       tran
""")
x = input("Enter the command\n").lower()
if x == 'tran' :
    matrix = matrix_collect("Matrix")
    result = matrix_transpose(matrix)
    
elif x == 'add' or x == 'sub' or x == 'mul' :
    matrix_a = matrix_collect("1st Matrix")
    matrix_b = matrix_collect("2nd Matrix")
    if x == 'add':
        result = matrix_add(matrix_a,matrix_b)
    elif x == 'sub':
        result = matrix_sub(matrix_a,matrix_b)
    else:
        result = matrix_mul(matrix_a,matrix_b)
else:
    result = 0
    print("Invaild")
      




print_matrix_form(result)

    
