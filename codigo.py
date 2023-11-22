def longitud_numero(numero):
    longitud= len(str(abs(numero)))
    return longitud

x = int (input("Por favor, ingrese un número de semilla: "))
n=0
a=x
e = str(1)
while(0!=e):
    
    n=n+1
    print(f"Ejercicio: {n}")
    print(f"Xi: {a}")
    b=a**2
    print(f"Xi^2: {b}")
    c = longitud_numero(b)
    print(f"Longitud: {c}")
    a=str(b)
    if c>=8:
        a= a[2:6]
    else:
            a= a[1:5]
    a=int(a)
    print(f"centro: {a}")
    e=a/10000
    print(f"RI: {e}")
    print(f" ")
