import time

"""
Secuencia de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

1  2  3  4  5  6  7   8   9   10  11   12   13

fibonacci(x) =
  Si x es 1 o 2 entonces el resultado es 1
  En otro el resultado es la suma de los dos anteriores

fibonacci(1) = 1 
fibonacci(2) = 1
fibonacci(x) = fibonacci(x - 1) + fibonacci(x - 2)
"""

def optimizacion(fibo):
  memoria = {}

  def fibo_optimizado(x):
    if x not in memoria:
      memoria[x] = fibo(x)
    return memoria[x]

  return fibo_optimizado

@optimizacion
def fibo(x):
  if x == 1 or x == 2:
    return 1
  
  return fibo(x - 1) + fibo(x - 2)

start_time = time.time() # Tomando el tiempo inicial

print("fibo(500) =", fibo(500))

end_time = time.time() # Tomando el tiempo final

segundos = end_time - start_time

print("El algoritmo tardo {} segundos".format(segundos))