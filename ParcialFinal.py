import random


def burbuja(lista):
    datos = lista[:]
    iteraciones = 0
    n = len(datos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            iteraciones += 1
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos, iteraciones


def seleccion(lista):
    datos = lista[:]
    iteraciones = 0
    n = len(datos)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            iteraciones += 1
            if datos[j] < datos[minimo]:
                minimo = j
        datos[i], datos[minimo] = datos[minimo], datos[i]
    return datos, iteraciones


def insercion(lista):
    datos = lista[:]
    iteraciones = 0
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1
        while j >= 0:
            iteraciones += 1
            if datos[j] > actual:
                datos[j + 1] = datos[j]
                j -= 1
            else:
                break
        datos[j + 1] = actual
    return datos, iteraciones


def shell_sort(lista):
    datos = lista[:]
    iteraciones = 0
    n = len(datos)
    brecha = n // 2
    while brecha > 0:
        for i in range(brecha, n):
            actual = datos[i]
            j = i
            while j >= brecha:
                iteraciones += 1
                if datos[j - brecha] > actual:
                    datos[j] = datos[j - brecha]
                    j -= brecha
                else:
                    break
            datos[j] = actual
        brecha //= 2
    return datos, iteraciones


ALGORITMOS = {
    1: ("Burbuja", burbuja),
    2: ("Selección", seleccion),
    3: ("Inserción", insercion),
    4: ("Shell Sort", shell_sort),
}


def mostrar_menu():
    print("\n=== MENÚ DE ORDENAMIENTO ===")
    for numero, (nombre, _) in ALGORITMOS.items():
        print(f"{numero}. {nombre}")


def pedir_opcion(mensaje, excluir=None):
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")
            continue
        if opcion not in ALGORITMOS:
            print("Opción fuera del menú.")
        elif opcion == excluir:
            print("Elija un algoritmo diferente al primero.")
        else:
            return opcion


def main():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista aleatoria:", lista)

    mostrar_menu()
    primera = pedir_opcion("Elija el primer algoritmo: ")
    segunda = pedir_opcion("Elija el segundo algoritmo: ", excluir=primera)

    resultados = []
    for opcion in (primera, segunda):
        nombre, funcion = ALGORITMOS[opcion]
        ordenada, iteraciones = funcion(lista)
        resultados.append((nombre, iteraciones))
        print(f"\n{nombre}")
        print("Lista ordenada:", ordenada)
        print("Iteraciones:", iteraciones)

    print("\n=== COMPARACIÓN ===")
    (nombre1, it1), (nombre2, it2) = resultados
    if it1 < it2:
        print(f"{nombre1} usó menos iteraciones ({it1} contra {it2}).")
    elif it2 < it1:
        print(f"{nombre2} usó menos iteraciones ({it2} contra {it1}).")
    else:
        print(f"Ambos usaron la misma cantidad de iteraciones ({it1}).")


if __name__ == "__main__":
    main()