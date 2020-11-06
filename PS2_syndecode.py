
from numpy import *
import numpy as np
import math

def mod2(A):
    for i in range(2):
        A[A%2==i] = i
    return A

def Log2(x): 
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

def intToBin(key, n, k):
    return bin(key)[2:].zfill(n-k)

def syndrome_decode(codeword, n, k, G):
    print(f"n:{n}")
    print(f"k:{k}")
    print(f"Codeword: {codeword}")
    print(f"Matrix G: {G}")
    codeMatrix = np.matrix(codeword)
    
    print(f"codeMatrix:{codeMatrix}")
    codeTranspose = codeMatrix.transpose()
    
    print(f"codeTranspose:{codeTranspose}")
    A = G[: , k:] 
    I = np.identity(n-k,dtype=int)
    A_Transpose = A.transpose()
 
    H = np.concatenate((A_Transpose,I),axis=1)
    """ print(f'A \n{A}')
    print(f'H \n{H}') """

    Syndrome = np.dot(H,codeTranspose)
    Syndrome = mod2(Syndrome)
    
    print(f'Syndrome \n{Syndrome}')
    Syndrome = Syndrome.transpose()
    SynArr = np.array(Syndrome)
    SynArr = SynArr.reshape(-1)
    
    print(f'SynArr \n{SynArr}')
    synlist = []
    for x in SynArr:
        synlist.append(x)
    
    print(f'SynList \n{synlist}')
    syndrome = ''.join(map(str, synlist))
    print(f"Syndrome string: {syndrome}")

    check_str = '0'*(n-k)
    if(syndrome == check_str):
        print(codeword[:k])
        print("No error")
        return codeword[:k]
    else:
        codeIndex = {intToBin(key, n, k): None for key in range(1,n+1)}
        print(f"CodeIndex:\n{codeIndex}")
        p_count = k
        d_count = 0
        for i in range(1,n+1):
            index = intToBin(i,n,k)
            if(isPowerOfTwo(i)):
                codeIndex[index] = p_count
                p_count = p_count + 1
            else:
                codeIndex[index] = d_count
                d_count = d_count + 1
        print(f"CodeIndex\n{codeIndex}")
        error_index = codeIndex.get(syndrome)
        print(f"error_index\n{error_index}")
        print(f"Error index: ",error_index)
        if codeword[error_index] == 0:
            codeword[error_index] = 1
        else:
            codeword[error_index] = 0
        print(codeword[:k])
        return codeword[:k]

G1 = matrix('1 0 0 0 1 1 0; 0 1 0 0 1 0 1; 0 0 1 0 0 1 1; 0 0 0 1 1 1 1', dtype=int)
codeword = [0, 0, 0, 0, 1, 1, 1]
result = syndrome_decode(codeword, 7, 4, G1)
print(f"Result: ",result)