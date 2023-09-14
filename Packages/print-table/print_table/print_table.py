def print_table(datos):
    """ Imprime en forma de tabla la lista de listas contenida en datos """
    ancho_max = [0] * len(datos[0])
    for fila in datos:
        for i, col in enumerate(fila):
            col_str = str(col)
            if len(col_str) > ancho_max[i]:
                ancho_max[i] = len(col_str)
    for fila in datos:
        cols = [f"{val:{ancho_max[i]}}" for i, val in enumerate(fila)]
        linea = " | ".join(cols)
        print(linea)

