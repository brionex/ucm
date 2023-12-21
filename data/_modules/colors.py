class Colors:

    colors = {
        'r': '#ffffff',   # reset
        'red': '#E74856',
        'green': '#00ff00',
        'yellow': '#ffff00',
        'blue': '#0000ff',
        'magenta': '#ff00ff',
        'cyan': '#00ffff',
        'cafe': '#6D4D27'
    }

    
    def apply(string):
        for key in Colors.colors:
            string = string.replace(f'/{key}/', Colors.colors[key])
        return string + Colors.colors['r']


    def __init_subclass__(cls):
        super().__init_subclass__()
        for name, value in Colors.colors.items():
            Colors.colors[name] = Colors.hex_to_ANSI(value)


        for name, value in cls.__dict__.items():
            if isinstance(value, str):
                setattr(cls, name, Colors.apply(value))


    def hex_to_ANSI(hex_color, background=False):
        # Eliminar el carácter '#' si está presente en el código hexadecimal
        hex_color = hex_color.lstrip('#')

        # Convertir el código hexadecimal a valores RGB
        if len(hex_color) == 3:
            r = int(hex_color[0] * 2, 16)
            g = int(hex_color[1] * 2, 16)
            b = int(hex_color[2] * 2, 16)
        elif len(hex_color) == 6:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
        else:
            raise ValueError("El código de color debe tener 3 o 6 dígitos")

        # Determinar si se está configurando el color de fondo o de texto
        color_type = '48' if background else '38'
        ANSI_color = f"\033[{color_type};2;{r};{g};{b}m"
        return ANSI_color    

        