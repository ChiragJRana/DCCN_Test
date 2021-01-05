
# Test file for 6.02 linear block codes lab
import operator
import math,numpy,random
from numpy import *
import functools
import operator


# construct a (nrows*ncols+nrows+ncols,nrows*ncols,3) codeword
def codeword(data,nrows,ncols):
    result = data[:]

    # compute row parity bits
    for r in range(nrows):
        result.append(int(not even_parity(data[r*ncols:(r+1)*ncols])))

    # compute column parity bits
    for c in range(ncols):
        result.append(int(not even_parity(data[c:len(data):ncols])))

    return result



# convert integer to binary list of specified size (lsb first)
def int2bin(c,size=8):
    return [ (c >> i) % 2 for i in range(size)]

def test_correct_errors(correct_errors):
    # test the decoder on a particular value, returns True if failed
    def run_test(test,nrows,ncols,expected,msg):
        result = correct_errors(test[:],nrows,ncols)
        if result != expected:
            print("Error detected while testing",msg)
            print("Test code word:",test)
            print("Expected:",expected)
            print("Received:",result)
            return True
        return False

    # test all 256 data values for 8 data bits
    print('Testing all 2**n = 256 valid codewords')
    for i in range(256):
        data = int2bin(i)
        if run_test(codeword(data,2,4),2,4,data,"valid codewords"): return

    print('...passed')

    # test all single-bit errors (should be corrected)
    print('Testing all possible single-bit errors')

    for count in range(256):
        good = codeword(int2bin((count)),4,2)
        for i in range(14):
            bad = good[:]
            bad[i] ^= 1
            if run_test(bad,4,2,good[0:8],"correctable single-bit errors (bit %d)" % i): return

    print('...passed')

    print('(8,4) rectangular parity code successfully passed all 0,1 and 2 bit error tests')

def even_parity(seq):
    return functools.reduce(operator.xor,seq,0)
