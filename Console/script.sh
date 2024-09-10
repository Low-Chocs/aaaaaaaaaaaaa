#!/bin/bash


# Lista de imagenes
images=(
    "ram_py"
    "date_update_py"
    "meme_py"
    "operation_py"
)

# Crear una lista de 10 imagenes seleccionadas aleatoriamente
selected_images=()
for ((i=0; i<10; i++)); do
    selected_images+=("${images[RANDOM % ${#images[@]}]}")
done

# Crear 10 contenedores
for image in "${selected_images[@]}"; do
    sudo docker run -d "$image"
done