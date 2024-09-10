import sys
import time

# Tamaño aproximado de un entero en Python
size_of_int = sys.getsizeof(0)

# Tamaño del bloque que vamos a asignar en cada iteración (en MB)
block_size_mb = 100  # Puedes ajustar este valor según el consumo que desees
block_size = block_size_mb * 1024 * 1024 // size_of_int  # Convertir MB a cantidad de enteros

# Lista que almacenará bloques de memoria
large_list = []

# Límite de memoria a alcanzar en MB
memory_limit_mb = 2_500

try:    
    total_memory_allocated = 0
    
    while True:
        if total_memory_allocated >= memory_limit_mb:
            # Vaciamos la lista cuando alcanzamos el límite y reiniciamos el conteo
            large_list = []
            total_memory_allocated = 0

        
        # Añadimos bloques de memoria
        large_list.append([0] * block_size)
        total_memory_allocated += block_size_mb

        
        # Tiempo de espera de 0.1 segundos
        time.sleep(1.5)
        
except MemoryError:
    pass
