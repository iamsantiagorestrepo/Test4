def eliminar_duplicados(lista):
    nueva_lista = []
    [nueva_lista.append(x) for x in lista if x not in nueva_lista]
    return nueva_lista

# Ejemplo de uso
lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 6]
resultado = eliminar_duplicados(lista_original)
print("Lista sin duplicados:", resultado)  # Debe imprimir [1, 2, 3, 4, 5, 6]