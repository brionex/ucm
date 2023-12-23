class Colors:

    colors = {
        'r': '\033[0m',   # reset
        'red': '#E74856',
        'green': '#00ff00',
        'yellow': '#ffff00',
        'blue': '#0000ff',
        'magenta': '#ff00ff',
        'cyan': '#00ffff',
        'cafe': '#6D4D27',
        'black': '#000',
        'white': '#fff'
    }

    first_instance = True



    def __new__(cls, *args):
        # Cambia los colores de hexadecimal a ANSI en la primera instancia.
        if Colors.first_instance:
            cls.process_color()
            Colors.first_instance = False

        data = args[0]
        if type(data) is str:
            return cls.format(data)
        
        elif type(data) is dict:
            cls.format_dict(data)
        
        elif type(data) is list:
            return cls.format_list(data)
        
        elif type(data) is tuple:
            return tuple(cls.format_list(data))
        
        else:
            raise TypeError(f'{cls.colors['red']}Tipo de dato no valido.')
            

        return super().__new__(cls)
    


    @classmethod
    def format(cls, string):
        for name in cls.colors.keys():
            string = string.replace(f'{{{name}}}', cls.colors[name])

        return string + cls.colors['r']


    @classmethod
    def format_dict(cls, data):  
        for name, value in data.items():
            string = cls.format(value)
            setattr(cls, name, string)


    @classmethod
    def format_list(cls, data):
        formatted_list = []
        for string in data:
            formatted_list.append(cls.format(string))
        
        return formatted_list


    @classmethod
    def process_color(cls):
        # Convierte todos lo colores de Hexadecimal a ANSI.
        # Crea los colores para textos y fondos.
        for name, value in cls.colors.copy().items():
            if name == 'r':
                continue
            cls.colors[name] = cls.hex_to_ANSI(value)
            cls.colors[name + '_bg'] = cls.hex_to_ANSI(value, True)



    @classmethod
    def hex_to_ANSI(cls, hex_color, background=False):
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
