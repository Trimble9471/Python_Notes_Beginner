#Creating a module to compute the greatest common divisor

#Function to return the gcd of two integers
def gcd(n1,n2):

    #initialize gcd and k
    gcd = 1
    k = 2  #Possible gcd

    #Create a while loop and 1.c.c is k cannot be greater than n1 and n2
    while k <= n1 and k <= n2:

        #Check if k equally divides into the two integers
        if n1 % k == 0 and n2 % k ==0:
            #Update the gcd to k
            gcd = k

        #Increment k by 1
        k += 1

    #Return the gcd to the caller
    return gcd


    
