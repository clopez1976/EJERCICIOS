def maximo(num1, num2):
    if num1>num2:
        nmax=num1
    elif num2>num1:
        nmax=num2
    else:
        nmax="Los números son iguales"
    return nmax

print(maximo(16,16))