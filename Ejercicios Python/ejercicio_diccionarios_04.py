estudiantes = {}
max_estudiantes = 10

for i in range(1, max_estudiantes + 1):
    nombre = input(f"Introduce el nombre del estudiante {i}: ")
    nota = float(input(f"Introduce la nota de {nombre}: "))

    estudiantes[str(i)] = {"nombre": nombre, "nota": nota}

    continuar = input("¿Quieres añadir otro estudiante? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nLista de estudiantes y sus notas:")
for clave, datos in estudiantes.items():
    print(f"{clave}: {datos['nombre']} - Nota: {datos['nota']}")
