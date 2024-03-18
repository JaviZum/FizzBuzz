def fizzbuzz(primer, ultimo):
    

    for numero in range(primer, ultimo + 1):
      
      if numero == 0: #Si no lo añadimos nos da que 0 es divisible por 3 y 5, por resultar el resto 0.
        print(numero)
      
      elif numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
      
      elif numero % 3 == 0:
        print("Fizz")
      
      elif numero % 5 == 0:
        print("Buzz")
      
      else:
        print(numero)

fizzbuzz(0, 75)