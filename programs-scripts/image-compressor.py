# NOTAS
#

import sys
import shutil
from os import path, mkdir, listdir
from PIL import Image

EXTENSIONS_LIST = ['.jpg', '.webp', '.jfif', '.jpeg', '.png']
DIRNAME = None
compressed = 0
uncompressed = 0


class C:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


# Function to format file size.
def format_bytes(size_bytes):
    if size_bytes >= 1e9:
        return f'GB {size_bytes / 1e9:.2f}'
    if size_bytes >= 1e6:
        return f'MB {size_bytes / 1e6:.2f}'
    if size_bytes >= 1e3:
        return f'KB {size_bytes / 1e3:.2f}'
    return f'B  {size_bytes}'


# Shows the log of each image with the size difference.
def console_log(img, new_img=False):
    size_img1 = format_bytes(path.getsize(img))

    name, extension = path.splitext(path.basename(img))
    name = (name[:20] + '..' +
            extension) if len(name) > 20 else name + extension

    if (not new_img):
        print(f'{C.RED}{size_img1.ljust(12)} -> {"...".ljust(20)}{name}{C.RESET}')
        return

    size_img2 = format_bytes(path.getsize(new_img))
    print(f'{size_img1.ljust(12)} {C.GREEN}->{C.CYAN} {size_img2.ljust(20)}{C.RESET}{name}')



# Compresses the image.
def compressor(img, new_img):
    global compressed, uncompressed

    resolucion_minima_ancho = 1920
    resolucion_minima_alto = 1080
    
    imagen = Image.open(img)
    # Obtiene las dimensiones originales de la imagen
    ancho_original, alto_original = imagen.size

    # Calcula la relación de aspecto original
    relacion_aspecto = ancho_original / alto_original

    # Calcula las nuevas dimensiones manteniendo la proporción
    if (ancho_original / resolucion_minima_ancho) > (alto_original / resolucion_minima_alto):
        nuevo_ancho = resolucion_minima_ancho
        nuevo_alto = int(nuevo_ancho / relacion_aspecto)
    else:
        nuevo_alto = resolucion_minima_alto
        nuevo_ancho = int(nuevo_alto * relacion_aspecto)

    # Redimensiona la imagen a las nuevas dimensiones
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

    # Guarda la imagen redimensionada en un nuevo archivo
    imagen_redimensionada.save(new_img)

    # Cierra la imagen original (opcional)
    imagen.close()


    print('img')
    return
    # if path.exists(img):
    try:
        picture = Image.open(img)
        picture.save(new_img, optimize=True, quality=30)
        compressed += 1

    except (OSError, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError):
            uncompressed += 1
            console_log(img)
            return

        elif isinstance(e, OSError):
            picture = picture.convert('RGB')
            picture.save(new_img, optimize=True, quality=30)
            compressed += 1

    console_log(img, new_img)
    return

    # console_log(img)
    # uncompressed += 1



# compress an image
def compress_image():
    name_img = path.normpath(sys.argv[2])
    img = path.abspath(name_img)
    new_img = path.join(DIRNAME, f'compressed_{name_img}')
    compressor(img, new_img)



# compress multiple images.
def compress_images():
    folder = path.join(DIRNAME, 'compressed-images')
 
    if path.isdir(folder):
        shutil.rmtree(folder)
    mkdir(folder)

    for filename in listdir(DIRNAME):
        name, extension = path.splitext(path.join(DIRNAME, filename))
        if extension.lower() in EXTENSIONS_LIST:
            compressor(name + extension, path.join(folder, filename))



def main():
    global DIRNAME
    DIRNAME = sys.argv[1]

    for i in sys.argv:
        print(f'>: {i}')

    print()
    return
    
    print()
    if len(sys.argv) == 2:
        compress_images()
    
    elif len(sys.argv) == 3 and path.exists(sys.argv[2]):
        compress_image()

    else:
        print('\033[91m!Image file does not exist.\033[0m\n')
        return

    print(f'\n\n{C.YELLOW}- Images processed successfully: {compressed}')
    print(f'- !Images with errors: {uncompressed}{C.RESET}\n')


# Initial flow of the program.
if __name__ == '__main__' and len(sys.argv) > 1: main()
