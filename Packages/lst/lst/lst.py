import pathlib
import sys

def listdir_txt(ruta_str=None):
    """ Obtiene la lista de archivos de ruta_str y regresa sólo los que son
    archivos de texto. Si ruta_str es None entonces se muestran los
    archivos de la carpeta actual '.' """
    if ruta_str == None:
        ruta_str = "."
    ruta = pathlib.Path(ruta_str)
    archivos = []
    for item in ruta.iterdir():  # como ruta es de tipo PosixPath o WindowsPath
        if item.is_file():  # Si el item es un archivo lo agregamos a la lista
            ## Complementa con un if y una función para determinar si el archivo es de
            ## texto entonces lo agregamos a la lista, si no, no hacemos nada y pasamos
            ## al siguiente
            archivos.append(item)
        else:  # Si el item no es un archivo entonces es una carpeta y otenemos la lista de arcivos
            lista_archivos_subruta = listdir_txt(str(item))  # <-ruta
            archivos = archivos + lista_archivos_subruta  # Lo concatemos a la lista de archivos[]
    return archivos

def main(argv):
    """ Función principal del programa """
    if len(argv) != 2:
        print("Error de sintaxis, la sintaxis correcta es: lst.py CARPETA")
        sys.exit(1)
        
    # Se obtiene la lista de archivos a partir de ruta
    archivos = listdir_txt(argv[1])  # Se asume que existirá una función que resolverá la tarea
    
    # Se imprime la lista
    for nom in archivos:
        print(nom)

if __name__ == "__main__":
    # print(sys.argv)
    main(sys.argv)  # ["lst.py", "."]

