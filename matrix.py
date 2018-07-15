import random
Matrix_A=[]
Matrix_B=[]
public_length=0
public_index_i=0
public_index_j=0
Matrix_public=[]
A_row=int(input('Enter A matrix\'s rows:'))
A_col=int(input('Enter A matrix\'s cols:'))
for i in range(0,A_row):
    Matrix_A.append([])
    for j in range(0,A_col):
        Matrix_A[i].append([])
        Matrix_A[i][j]=random.randint(0,9)
print("Matrix A(",A_row,", ",A_col,"):")
for i in range(0,A_row):
    for j in range(0,A_col):
        print(Matrix_A[i][j],end=' ')
    print(end='\n')
B_row=int(input('Enter B matrix\'s rows:'))
B_col=int(input('Enter B matrix\'s cols:'))
for i in range(0,B_row):
    Matrix_B.append([])
    for j in range(0,B_col):
        Matrix_B[i].append([])
        Matrix_B[i][j]=random.randint(0,9)
print("Matrix B(",B_row,", ",B_col,"):")
for i in range(0,B_row):
    for j in range(0,B_col):
        print(Matrix_B[i][j],end=' ')
    print(end="\n")
print("========== A + B ==========")
if A_row==B_row and A_col==B_col:
    for i in range(0,B_row):
        for j in range(0,B_col):
            print(Matrix_A[i][j]+Matrix_B[i][j],end=' ')
        print(end="\n")
else:
    print("Matrix's size should be in the same size")
print("========== A - B ==========")
if A_row==B_row and A_col==B_col:
    for i in range(0,B_row):
        for j in range(0,B_col):
            print(Matrix_A[i][j]-Matrix_B[i][j],end=' ')
        print(end="\n")
else:
    print("Matrix's size should be in the same size")

print("========== A * B ==========")
if A_col==B_row:
    public_length=A_col
    public_index_i=A_row
    public_index_j=B_col
    for i in range(0,public_index_i):
        Matrix_public.append([])
        for j in range(0,public_index_j):
            Matrix_public[i].append(0)
            for k in range(0,public_length):
                Matrix_public[i][j]+=Matrix_A[i][k]*Matrix_B[k][j]
            print(Matrix_public[i][j],end=' ')
        print(end="\n")
else:
    print("Matrix's size should be in the same size")
    
print("===== the transpose of A*B =====")
for i in range(0,public_index_j):
    for j in range(0,public_index_i):
        print(Matrix_public[j][i],end=' ')
    print(end="\n")
