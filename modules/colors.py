class Colors:
    _colors = {
        'r': '\033[0m',
        'red': '#FD6F6B',
        'cyan': '#20C5C6',
        'gray': '#686868',
        'blue': '#6A76FB',
        'lime': '#67F86F',
        'white': '#FFFFFF',
        'coral': '#F08080',
        'black': '#000000',
        'green': '#1DC121',
        'yellow': '#FFFA72',
        'magenta': '#FD7CFC',
    }


    def __init__(self, config=None):
        if config:
            self._colors.update(config)
        self._process_colors()


    # Convierte todos lo colores de Hexadecimal a ANSI.
    # Crea los colores para textos y fondos.
    def _process_colors(self):
        for name, value in self._colors.copy().items():
            if name != 'r':
                self._colors[name] = self._hex_to_ansi(value)
                self._colors[name + '_bg'] = self._hex_to_ansi(value, True)



    def _hex_to_ansi(self, hex_color, background=False):
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



    # Aplica el formateo dependiendo del tipo de dato proporcionado.
    def apply(self, data):
        data_type = type(data)

        if data_type is str:
            return self._format_str(data)

        if data_type is dict:
            return self._format_dict(data)

        if data_type is list:
            return self._format_list(data)

        if data_type is tuple:
            return tuple(self._format_list(data))

        print(f'*{self._colors['red']} Tipo de dato proporcionado no se puede procesar.')
        return None



    def _format_str(self, string):
        for name, value in self._colors.items():
            if name in string:
                string = string.replace(f'{name}::', value)
                print(string)
        return string + (self._colors['r'])



    def _format_dict(self, data):
        formatted_dict = {
            name: self._format_str(value) for name, value in data.items()
        }
        new_class = type('newClass', (object,), formatted_dict)
        return new_class



    def _format_list(self, data):
        formatted_list = []
        for string in data:
            formatted_list.append(self._format_str(string))
        return formatted_list



    def list_colors(self):
        print('\n')
        for name, value in self._colors.items():
            if not '_bg' in name:
                print(value + name)
            print(self._colors['r'],  end="")
        print('\n')
