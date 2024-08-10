import os
import shutil
# from PIL import Image
import click

EXTENSIONS_LIST = ['.jpg', '.webp', '.jfif', '.jpeg', '.png']
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
    size_img1 = format_bytes(os.path.getsize(img))
    name, extension = os.path.splitext(os.path.basename(img))
    name = (name[:20] + '..' +
            extension) if len(name) > 20 else name + extension

    if not new_img:
        print(f'{C.RED}{size_img1.ljust(12)} -> {"...".ljust(20)}{name}{C.RESET}')
        return

    size_img2 = format_bytes(os.path.getsize(new_img))
    print(f'{size_img1.ljust(12)} {
          C.GREEN}->{C.CYAN} {size_img2.ljust(20)}{C.RESET}{name}')

# Compresses the image.


def compressor(img, new_img, quality=85):
    global compressed, uncompressed
    try:
        picture = Image.open(img)
        picture.save(new_img, optimize=True, quality=quality)
        compressed += 1
        console_log(img, new_img)
    except (OSError, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError):
            uncompressed += 1
            console_log(img)
        elif isinstance(e, OSError):
            picture = picture.convert('RGB')
            picture.save(new_img, optimize=True, quality=quality)
            compressed += 1
            console_log(img, new_img)


def compress_image(image_path):
    global compressed, uncompressed
    img = os.path.abspath(image_path)
    new_img = os.path.abspath(f'compressed_{os.path.basename(img)}')
    compressor(img, new_img)


def compress_images(directory):
    global compressed, uncompressed
    folder = os.path.join(directory, 'compressed-images')

    if os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    for filename in os.listdir(directory):
        name, extension = os.path.splitext(os.path.join(directory, filename))
        if extension.lower() in EXTENSIONS_LIST:
            compressor(name + extension, os.path.join(folder, filename))


def compress_folder(input_folder):
    global compressed, uncompressed
    output_folder = os.path.join(
        os.path.dirname(input_folder), 'compressed-images')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for root, _, files in os.walk(input_folder):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension.lower() in EXTENSIONS_LIST:
                img_path = os.path.join(root, file)
                new_img_path = os.path.join(
                    output_folder, f'{name}_compressed{extension}')
                compressor(img_path, new_img_path)


@click.command()
@click.option('--all', 'mode', flag_value='all', default=False, help='Compress all images in the current directory.')
@click.option('--img', 'mode', type=click.Path(exists=True), help='Compress a single image.')
@click.option('--folder', 'mode', type=click.Path(exists=True), help='Compress all images in a specified folder.')
def cli(mode):
    global compressed, uncompressed

    if mode == 'all':
        compress_images(os.getcwd())
    elif isinstance(mode, str):
        if os.path.isfile(mode):
            compress_image(mode)
        elif os.path.isdir(mode):
            compress_folder(mode)
        else:
            click.echo(f'{C.RED}Invalid path provided.{C.RESET}')
            return
    else:
        click.echo(f'{C.RED}No valid option selected.{C.RESET}')
        return

    click.echo(f'\n\n{C.YELLOW}- Images processed successfully: {compressed}')
    click.echo(f'- !Images with errors: {uncompressed}{C.RESET}\n')


if __name__ == '__main__':
    cli()
