# PRUEBA TÉCNICA ADEN
Crear un módulo de Odoo versión 15 o superior
El módulo debe cumplir con los siguientes requisitos:

### Modelo Alumno
Contendrá los siguientes datos:

- Nombre
- Apellido
- Fecha de nacimiento
- Nro de legajo
- Email
- Teléfono
- Dirección
- País

### Modelo Programa
Contendrá los siguientes campos:

- Nombre
- Descripción

### Modelo Inscripción
Permite registrar que un alumno está inscrito en un programa.

### Controlador
A través de un controlador, se debe crear un endpoint de método GET, que reciba un `id` de programa y retorne la lista de todos los alumnos que están inscritos en dicho programa. 

### Ejemplo de respuesta:
```json
[
  {
    "nombre": "Pedro",
    "apellido": "Mendoza",
    "legajo": 12548,
    "fecha_nacimiento": "1990-01-01",
    "email": "pedro@gmail.com",
    "telefono": "+549261554121",
    "pais": {
      "id": 587,
      "nombre": "Argentina"
    }
  },
  {
    "nombre": "Philipp",
    "apellido": "Anderson",
    "legajo": 12549,
    "fecha_nacimiento": "1989-04-30",
    "email": "philipp.anderson@test.com",
    "telefono": "+54912311111",
    "pais": {
      "id": 587,
      "nombre": "Argentina"
    }
  }
]
```
## Puntos a tener en cuenta:
- Todos los modelos deben tener sus vistas y ser accesibles desde el sistema a través
de los menúes.
- No es necesario crear permisos ni grupos para acceder a los modelos, pero se
considera un plus.
- El endpoint puede ser público, no es necesario generar autenticación