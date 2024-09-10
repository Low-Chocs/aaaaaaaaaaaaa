import random
import math
import time

# Inicializamos la segunda variable con un valor random entre 1 y 1000
variable = random.randint(1, 1000)
iteraciones = 0

# Limite superior e inferior para la variable
LIMITE_SUPERIOR = 1e6
LIMITE_INFERIOR = -1e6

while True:
    # Generamos un número aleatorio entre 1 y 6 para agregar más operaciones
    operacion = random.randint(1, 6)
    
    # Iteramos y controlamos cuántas veces hemos hecho una operación
    iteraciones += 1
    
    if operacion == 1:
        # Sumar la variable consigo misma
        variable += variable
        
    elif operacion == 2:
        # Restar la variable consigo misma
        variable -= variable
        
    elif operacion == 3:
        # Multiplicar la variable consigo misma
        variable *= variable
        
    elif operacion == 4:
        # Sacar la raíz cuadrada de la variable
        if variable < 0:
            # Si es menor a 0, le asignamos un valor random entre 1 y 1000
            variable = random.randint(1, 1000)
        else:
            variable = int(math.sqrt(variable))
    
    elif operacion == 5:
        # Exponenciación: elevar la variable a un exponente entre 2 y 5
        exponente = random.randint(2, 5)
        variable = math.pow(variable, exponente)
    
    elif operacion == 6:
        # Logaritmo natural, solo si la variable es positiva
        if variable > 0:
            variable = math.log(variable)
        else:
            # Si no es posible calcular logaritmo, asignamos un nuevo valor
            variable = random.randint(1, 1000)
    
    # Evitar que la variable se haga demasiado grande o demasiado pequeña
    if variable > LIMITE_SUPERIOR:
        variable = random.randint(1, 1000)
        
    if variable < LIMITE_INFERIOR:
        variable = random.randint(1, 1000)
    
    # Monitorizar valores extremos (infinito, indefinido, etc.)
    if math.isinf(variable) or math.isnan(variable):
        variable = random.randint(1, 1000)
    
    # Esperar 0.5 segundos antes de la siguiente iteración
    time.sleep(0.0005)
