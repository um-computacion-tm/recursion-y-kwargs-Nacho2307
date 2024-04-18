





def buscar_id(*args, **kwargs):
    for persona, atributos in kwargs.items():
        igual = True
        for arg in args:
            if arg not in atributos.values():
                igual = False
                break
        if igual:
            return persona
    return 'No se encuentra en la base de datos'

database0 = {
    "persona0": {
        "primer_nombre": "Mateo",
        "segundo_nombre": "Ezequiel",
        "primer_apellido": "Carvajal",
        "segundo_apellido": "Ojeda"
    },
    "persona1": {
        "primer_nombre": "Mauro",
        "segundo_nombre": "David",
        "primer_apellido": "Arrigo",
        "segundo_apellido": "Barroso"
    },
    "persona2": {
        "primer_nombre": "Matias",
        "segundo_nombre": "David",
        "primer_apellido": "Rojas",
        "segundo_apellido": "Verde"
    },
    "persona3": {
        "primer_nombre": "Ignacio",
        "segundo_nombre": "",
        "primer_apellido": "Aguilera",
        "segundo_apellido": "Baigorria"
    }
}

ID = buscar_id("Ignacio", "Diego", "Aguilera", "Baigorria", **database0)
print('Id_persona:', ID)
