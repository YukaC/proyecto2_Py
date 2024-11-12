from PIL import Image
import numpy as np
import cv2

def boceto_para_pintores(imagen_redimensionada, es_persona):
    if imagen_redimensionada is None:
        raise Exception("Primero debe redimensionar la imagen.")
    if not es_persona:
        raise ValueError("La imagen no contiene una persona.")

    imagen_gris = np.array(imagen_redimensionada.convert("L"))
    bordes = cv2.Canny(cv2.GaussianBlur(imagen_gris, (5, 5), 0), 50, 150)
    imagen_boceto = cv2.cvtColor(bordes, cv2.COLOR_GRAY2RGB)
    
    # Guardar y mostrar la imagen de boceto
    Image.fromarray(imagen_boceto).save("fotos_editadas/imagen_boceto.jpg")
    print("La imagen boceto se ha guardado como 'imagen_boceto.jpg'.")
    Image.fromarray(imagen_boceto).show()

# Bloque principal
if __name__ == "__main__":
    ruta = input("Ingrese la ruta de la imagen: ")
    es_persona = input("¿La imagen contiene una persona? (si/no): ").strip().lower() == "si"

    try:
        imagen = Image.open(ruta)
        boceto_para_pintores(imagen, es_persona)
    except FileNotFoundError:
        print("No se encontró la imagen en la ruta especificada. Por favor, verifica la ruta.")
    except ValueError as e:
        print(e)