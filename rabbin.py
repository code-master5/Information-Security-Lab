import random
import sys

def is_probable_prime(n, k = 7):

   if n < 6: 
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
 
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  
               elif x == n - 1:
                  a = 0  
                  break  
            if a:
               return False 
      return True  
inp = input("enter the number ")


if is_probable_prime(inp):
	print 'true'
else:
	print 'false'
