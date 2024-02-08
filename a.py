from modules.colors import Colors

c = Colors({
    'red': '#fff'
})

c1 = c.apply('1 cyan::ucmd - Crea, lista y elimina comandos.')

c2 = c.apply({
    'ucmd': '2 cyan::ucmd - Crea, lista y elimina comandos.'
})

c3 = c.apply([
    '3 cyan::ucmd - Crea, lista y elimina comandos.'
])

c4 = c.apply((
    '4 cyan::ucmd - Crea, lista y elimina comandos.',
    '4 cyan::ucmd - Crea, lista y elimina comandos.',
))


print(c1)
print(c2.ucmd)
print(c3[0])
print(c4[0])
print(c.list_colors())


# print(c.list_colors())
# print(c.ucmd)
