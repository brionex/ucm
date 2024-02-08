class Colors:
    _colors = {
        'r': '\033[0m',
        'black': '#000000',
        'red': '#C51E14',
        'green': '#1DC121',
        'yellow': '#C7C329',
        'blue': '#0A2FC4',
        'magenta': '#C839C5',
        'cyan': '#20C5C6',
        'white': '#C7C7C7',
        'light_black': '#686868',
        'light_red': '#FD6F6B',
        'light_green': '#67F86F',
        'light_yellow': '#FFFA72',
        'light_blue': '#6A76FB',
        'light_magenta': '#FD7CFC',
        'light_cyan': '#68FDFE',
        'light_white': '#FFFFFF',
        'lime_green': '#32CD32',
        'light_coral': '#F08080',
    }


    def __init__(self, config):
        self._colors.update(config)
        self._process_colors()



    # Convierte todos lo colores de Hexadecimal a ANSI.
    # Crea los colores para textos y fondos.
    def _process_colors(self):
        for name, value in self._colors.copy().items():
            if name != 'r':
                self._colors[name] = self.hex_to_ansi(value)
                self._colors[name + '_bg'] = self.hex_to_ansi(value, True)



    def hex_to_ansi(self, hex_color, background=False):
        # Eliminar el carácter '#' si está presente en el código hexadecimal.
        hex_color = hex_color.lstrip('#')

        # Convertir el código hexadecimal a valores RGB.
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

        # Determinar si se está configurando el color de fondo o de texto.
        color_type = '48' if background else '38'
        ansi_color = f"\033[{color_type};2;{r};{g};{b}m"
        return ansi_color



    def apply(self, data):
        # Usa un formateo según el tipo de dato.
        data_type = type(data)

        if data_type is str:
            return self.format_str(data)

        if data_type is dict:
            self.format_dict(data)
            return

        if data_type is list:
            return self.format_list(data)

        if data_type is tuple:
            return tuple(self.format_list(data))

        return f'*{self._colors['red']} Tipo de dato proporcionado no se puede procesar.'



    def format_str(self, string):
        counter = 0
        for name in self._colors.items():
            if f'{{{name}}}' in string:
                counter += 1
                string = string.replace(f'{{{name}}}', self._colors[name])

        return string + (self.colors['r'] if counter else '')



    def format_dict(cls, data):
        for name, value in data.items():
            string = cls.format(value)
            setattr(cls, name, string)



    def format_list(cls, data):
        formatted_list = []
        for string in data:
            formatted_list.append(cls.format(string))

        return formatted_list

