# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:08:28 2020

@author: Problem 7
"""

import numpy as np
import sys

def SieveErastothenes(n):
    ''' 
    return an array with all the prime numbers smaller than n,
    using the Sive of Erastothenes algorithm
    '''
    primes = np.array(range(1, n+1))
    prime_filter = np.array([True]*n)
    for i in range(1,n):
        if prime_filter[i]==True:
            prime = primes[i]
            sieve = list(range(i+prime, n, prime))
            prime_filter[sieve] = False
    return primes[prime_filter]

def main():
    n = int(sys.argv[1])
    #print(f'type of n i {type(n)}')
    number = int(sys.argv[2])
    primes = SieveErastothenes(n)
    prime = primes[number]
    print(f'The {number}th prime number is {prime}' )
    

if __name__=="__main__":
    main()
    
#a=SieveErastothenes(1000000)
#a[10001]