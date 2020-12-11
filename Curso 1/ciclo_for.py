


#Cambair correros
def cambiar(email,dom_v,dom_n):

    if "@" + dom_v in email:
        index=email.index("@"+dom_v)
        dom_n=email[0:index]+"@"+dom_n

        return dom_n

    return email


print(cambiar("c.diaz@hotmail.com","hotmail.com","gmail.com"))

def first_and_last(message):
    
    if len(message)>0:
        if message[0]==message[-1]:
            return True
        else:
            return False
    else: 
        return False


def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

def prueba():
    for n in range(0,10):
        print(n, factorial(n))

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

def domino():

    for izquierda in range(7):
        for derecha in range(izquierda,7):
            print(("["+str(izquierda)+" / "+str(derecha)+"]"), end ="")
        print()

#domino()
#print(sum_squares(10)) # Should be 285