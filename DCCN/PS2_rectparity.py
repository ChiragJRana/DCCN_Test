
"""
Exp5 Task 1
Group 2
Chirag Rana 2018130043
Kunal Nalawade 2018130031
Prerak Parekh 2018130035
"""

import numpy
import functools
import operator
import PS2_tests

def even_parity(seq):
    return functools.reduce(operator.xor,seq,0)

def rect_parity(codeword,nrows,ncols): 
    data = codeword[:(nrows*ncols)]
    row_par = codeword[(nrows*ncols):((nrows*ncols)+nrows)]
    col_par = codeword[((nrows*ncols)+nrows):]

    """ print(f"Data: {data}")
    print(f"Row parity {row_par}")
    print(f"Column Parity {col_par}") """

    row_par_status =[0]*nrows
    col_par_status = [0]*ncols

    for i in range(nrows):
        temp_data = data[(i*ncols):((i+1)*ncols)]
        parity = even_parity(temp_data)
    
        """ if parity == row_par[i]:
            print(f"{parity} {row_par[i]} - {parity == row_par[i]}")
        else:
            row_par_status[i] = 1 """
    
        if parity != row_par[i]:
            row_par_status[i] = 1

    for i in range(ncols):
        temp_data = data[i::ncols]
        parity = even_parity(temp_data)
    
        """ if parity == col_par[i]:
            print(f"{parity} {col_par[i]} - {parity == col_par[i]}")
        else:
            col_par_status[i] = 1 """
    
        if parity != col_par[i]:
            col_par_status[i] = 1

    """ print(f"Codeword : {codeword}")
    print(f"nrows: {nrows}")
    print(f"ncols: {ncols}")
    print(f"Row par status: {row_par_status}")
    print(f"Col par status: {col_par_status}")  """
    
    if row_par_status.count(1) == 1 and col_par_status.count(1) == 1:
        row = row_par_status.index(1)
        col = col_par_status.index(1)
        # print(row_par_status,col_par_status)
        # print(row,col)
        if data[row*ncols + col] == 1:
            data[row*ncols + col] = 0
        else:
            data[row*ncols + col] = 1
        return data
    else:
        return data


if __name__ == '__main__':
   PS2_tests.test_correct_errors(rect_parity)
