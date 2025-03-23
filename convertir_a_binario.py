N = int(input("Ingrese el numero del que quiera saber su binario : \n"))
def binario(N):
    R = 0
    B = ""
    if N == 0 :
        return 0
    while N>=1:
        R = int(N%2)
        N = int(N/2)
        B = str(R)+B
    return B
NB = binario(N)
print(f"El numero {N} en binario es {NB}")