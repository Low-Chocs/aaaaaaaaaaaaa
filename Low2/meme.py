import requests
import time

def get_meme():
    # URL de la API de memes
    url = "https://meme-api.com/gimme"
    
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Decodificar la respuesta JSON
            data = response.json()
            
            # Extraer información del meme
            post_link = data.get('postLink', 'No post link')
            subreddit = data.get('subreddit', 'No subreddit')
            title = data.get('title', 'No title')
            meme_url = data.get('url', 'No URL')
            author = data.get('author', 'No author')
            ups = data.get('ups', 0)
            preview_images = data.get('preview', [])
            
            # Mostrar la información del meme
            print(f"URL: {meme_url}")
            

                
        else:
            print(f"Error: Received status code {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Request exception occurred: {str(e)}")

if __name__ == "__main__":
    while True:
        get_meme()
        time.sleep(5)  # Esperar 5 segundos antes de la siguiente consulta
