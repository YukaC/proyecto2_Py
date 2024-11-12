from PIL import Image

def redimensionar_imagen(ruta_imagen, plataforma):
    tamaños = {
        "youtube": (1280, 720),
        "instagram": (1080, 1080),
        "twitter": (1024, 512),
        "facebook": (1200, 630)
    }

    if plataforma not in tamaños:
        raise ValueError("Plataforma no soportada.")

    imagen = Image.open(ruta_imagen)
    imagen.thumbnail(tamaños[plataforma], Image.LANCZOS)
    imagen.show()
    return imagen  # Devuelve la imagen redimensionada para utilizar en otras funciones

# Llamada a la función con los argumentos
ruta = input("Ingrese la ruta de la imagen: ")
plataforma = input("Ingrese la plataforma (YouTube, Instagram, Twitter, Facebook): ").lower()
redimensionar_imagen(ruta, plataforma)