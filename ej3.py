from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def aplicar_filtro(imagen, filtro_elegido):
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
    
    if filtro_elegido not in filtros:
        raise ValueError("Filtro no soportado. Elige uno de: " + ", ".join(filtros.keys()))

    # Aplicar todos los filtros y mostrarlos en una figura de subplots
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    fig.suptitle("Aplicación de todos los filtros", fontsize=16)

    for ax, (nombre_filtro, filtro) in zip(axes.flatten(), filtros.items()):
        if nombre_filtro == "original":
            imagen_filt = imagen
        else:
            imagen_filt = imagen.filter(filtro)

        ax.imshow(imagen_filt)
        color_titulo = "red" if nombre_filtro == filtro_elegido else "black"
        ax.set_title(nombre_filtro.capitalize(), color=color_titulo)
        ax.axis("off")

    # Guardar la figura con todos los filtros aplicados
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig("fotos_editadas/todos_los_filtros_resultado.jpg")
    print("La imagen con todos los filtros aplicados se ha guardado como 'todos_los_filtros_resultado.jpg'.")
    plt.show()

# Bloque principal
if __name__ == "__main__":
    ruta = input("Ingrese la ruta de la imagen: ")
    filtro = input("Ingrese el filtro a aplicar (desenfoque, contorno, detalle, realce_bordes, realce_bordes_mayor, relieve, encontrar_bordes, afilar, suavizar): ").lower()

    try:
        imagen = Image.open(ruta)
        aplicar_filtro(imagen, filtro)
    except FileNotFoundError:
        print("No se encontró la imagen en la ruta especificada. Por favor, verifica la ruta.")
    except ValueError as e:
        print(e)