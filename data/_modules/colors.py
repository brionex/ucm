class Colors:

    colors = {
        'r': '\033[0m',
        'black': '#000000',
        'red': '#C51E14',
        'green': '#1DC121',
        'yellow': '#C7C329',
        'blue': '#0A2FC4',
        'magenta': '#C839C5',
        'cyan': '#20C5C6',
        'white': '#C7C7C7',
        'lightBlack': '#686868',
        'lightRed': '#FD6F6B',
        'lightGreen': '#67F86F',
        'lightYellow': '#FFFA72',
        'lightBlue': '#6A76FB',
        'lightMagenta': '#FD7CFC',
        'lightCyan': '#68FDFE',
        'lightWhite': '#FFFFFF',
        'limeGreen': '#32CD32',
        'lightCoral': '#F08080',
    }

    # Cambia a False en la primera instancia.
    first_instance = True



    def __new__(cls, *args):
        # Transforma los colores de Hexadecimal a ANSI.
        if Colors.first_instance:
            cls.process_color()
            Colors.first_instance = False

        # Usa un formateo según el tipo de dato.
        data = args[0]
        data_type = type(data)

        if data_type is str:
            return cls.format(data)
        
        elif data_type is dict:
            cls.format_dict(data)
        
        elif data_type is list:
            return cls.format_list(data)
        
        elif data_type is tuple:
            return tuple(cls.format_list(data))
        
        else:
            raise TypeError(f'*{cls.colors['red']} Tipo de dato proporcionado no se puede procesar.')

        return super().__new__(cls)



    @classmethod
    def format(cls, string):
        counter = 0
        for name in cls.colors.keys():
            if f'{{{name}}}' in string:
                counter+=1
                string = string.replace(f'{{{name}}}', cls.colors[name])

        return string + cls.colors['r'] if counter else 'aa'


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
