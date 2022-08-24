"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
def multiplo():
    base = 2500
    divisible = False
    divisores = range(2,21)
    par = 0
    impar = 0
    while 1:
        
        for i in divisores:

            if base % i == 0:
                par +=1
                
        if par == len(divisores):
            return base
        par = 0
        base += 1
    
        
##        for i in range(2, divisores):
##            print(i)
##            if base % i == 0:
##                estado = True
##            else:
##                break
##        if divisible == True:
##            return divisible

print(multiplo())
