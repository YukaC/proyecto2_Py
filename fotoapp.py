from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Variable global para almacenar la imagen redimensionada
imagen_redimensionada = None

# Función 1: Redimensionar imagen según la plataforma
def redimensionar_imagen(ruta_imagen, plataforma):
    global imagen_redimensionada
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
    imagen_redimensionada = imagen  # Guardar la imagen redimensionada

# Función 2: Ajuste de contraste usando histograma
def ajustar_contraste_histograma():
    if imagen_redimensionada is None:
        raise Exception("Primero debe redimensionar la imagen (Opción 1).")
    
    imagen = np.array(imagen_redimensionada.convert("RGB"))
    imagen_yuv = cv2.cvtColor(imagen, cv2.COLOR_RGB2YUV)
    imagen_yuv[:, :, 0] = cv2.equalizeHist(imagen_yuv[:, :, 0])
    imagen_corregida = cv2.cvtColor(imagen_yuv, cv2.COLOR_YUV2RGB)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(imagen)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Corregida")
    plt.imshow(imagen_corregida)
    plt.axis('off')
    plt.show()

    # Guardar la imagen ecualizada
    imagen_ecualizada_pil = Image.fromarray(imagen_corregida)
    imagen_ecualizada_pil.save("fotos_editadas/imagen_corregida.jpg")
    print("La imagen corregida se ha guardado como 'fotos_editadas/imagen_corregida.jpg'.")

# Función 3: Aplicar filtros
def aplicar_filtro():
    if imagen_redimensionada is None:
        raise Exception("Primero debe redimensionar la imagen (Opción 1).")

    filtros = {
        "original": None,
        "desenfoque": ImageFilter.BLUR,
        "contorno": ImageFilter.CONTOUR,
        "detalle": ImageFilter.DETAIL,
        "realce_bordes": ImageFilter.EDGE_ENHANCE,
        "realce_bordes_mayor": ImageFilter.EDGE_ENHANCE_MORE,
        "relieve": ImageFilter.EMBOSS,
        "encontrar_bordes": ImageFilter.FIND_EDGES,
        "afilar": ImageFilter.SHARPEN,
        "suavizar": ImageFilter.SMOOTH
    }
    
    print("Filtros disponibles: " + ", ".join(filtros.keys()))
    filtro_elegido = input("Ingrese el filtro a aplicar: ").lower()
    
    # Normalizamos el nombre del filtro elegido y verificamos si es válido
    nombre_filtro = filtro_elegido.lower()
    if filtro_elegido not in filtros:
        raise ValueError("Filtro no soportado. Elige uno de: " + ", ".join(filtros.keys()))
    
    # Aplicar todos los filtros y mostrarlos en una figura de subplots
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    fig.suptitle("Aplicación de todos los filtros", fontsize=16)

    for ax, (nombre_filtro, filtro) in zip(axes.flatten(), filtros.items()):
        if nombre_filtro == "original":
            imagen_filt = imagen_redimensionada
        else:
            imagen_filt = imagen_redimensionada.filter(filtro)

        ax.imshow(imagen_filt)
        
        # Poner en rojo el título si es el filtro elegido, y en negro para los demás
        color_titulo = "red" if nombre_filtro == filtro_elegido else "black"
        ax.set_title(nombre_filtro.capitalize(), color=color_titulo)
        ax.axis("off")

    # Guardar la figura con todos los filtros aplicados
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig("fotos_editadas/todos_los_filtros_resultado.jpg")
    plt.show()

# Función 4: Boceto para pintores
def boceto_para_pintores(es_persona):
    if imagen_redimensionada is None:
        raise Exception("Primero debe redimensionar la imagen (Opción 1).")
    if not es_persona:
        raise ValueError("La imagen no contiene una persona.")

    imagen_gris = np.array(imagen_redimensionada.convert("L"))
    bordes = cv2.Canny(cv2.GaussianBlur(imagen_gris, (5, 5), 0), 50, 150)
    imagen_boceto = cv2.cvtColor(bordes, cv2.COLOR_GRAY2RGB)
    Image.fromarray(imagen_boceto).save("fotos_editadas/imagen_boceto.jpg")
    Image.fromarray(imagen_boceto).show()

# Función 5: Menú de opciones
def menu():
    print("Opciones de la aplicación de edición de imágenes:")
    print("1. Redimensionar imagen para una plataforma")
    print("2. Ajustar contraste de una imagen")
    print("3. Aplicar un filtro a una imagen")
    print("4. Crear un boceto para pintores")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción (1-5): ")
    return int(opcion)

# Función de ejecución principal
def main():
    while True:
        try:
            opcion = menu()
            if opcion == 1:
                ruta = input("Ingrese la ruta de la imagen: ")
                plataforma = input("Ingrese la plataforma (YouTube, Instagram, Twitter, Facebook): ").lower()
                redimensionar_imagen(ruta, plataforma)
            elif opcion == 2:
                ajustar_contraste_histograma()
            elif opcion == 3:
                aplicar_filtro()
            elif opcion == 4:
                es_persona = input("¿La imagen contiene una persona? (si/no): ").strip().lower() == "si"
                boceto_para_pintores(es_persona)
            elif opcion == 5:
                print("Hasta la próxima :)")
                Exception
                break
                
            else:
                print("Opción inválida.")
                
        except Exception as e:
            print(f"Error: {e}")
            print("Por favor, intente de nuevo.\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()