import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def ajustar_contraste_histograma(imagen):
    imagen_array = np.array(imagen.convert("RGB"))
    imagen_yuv = cv2.cvtColor(imagen_array, cv2.COLOR_RGB2YUV)
    imagen_yuv[:, :, 0] = cv2.equalizeHist(imagen_yuv[:, :, 0])
    imagen_corregida = cv2.cvtColor(imagen_yuv, cv2.COLOR_YUV2RGB)
    
    # Mostrar la imagen original y la ecualizada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(imagen_array)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Ecualizada")
    plt.imshow(imagen_corregida)
    plt.axis('off')
    plt.show()

    # Guardar la imagen ecualizada
    plt.imsave("fotos_editadas/imagen_corregida.jpg", imagen_corregida)
    print("La imagen ecualizada se ha guardado como 'imagen_corregida.jpg'.")

# Bloque principal
if __name__ == "__main__":
    ruta = input("Ingrese la ruta de la imagen: ")
    try:
        imagen = Image.open(ruta)
        ajustar_contraste_histograma(imagen)
    except FileNotFoundError:
        print("No se encontró la imagen en la ruta especificada. Por favor, verifica la ruta.")