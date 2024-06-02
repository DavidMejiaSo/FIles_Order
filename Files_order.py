import os
import shutil
from argparse import ArgumentParser

# Definimos las extensiones de archivos y las carpetas correspondientes
extensiones_documentos = {
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"],
    "Fotos": [".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx"],
    "Musica": [".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"],
    "Instaladore" :[".exe"],
    "Tabs":[".gp", ".gp[0-9]*"]
    ,"otros": [".py", ".rar", ".zip", ".html", ".tmp", ".dat",  ".deb", 
              ".dmg", ".psd", ".c", ".asm", ".java", ".rst"]
}

# Función para crear carpetas si no existen
def crear_carpetas_si_no_existen(carpetas, ruta):
    for carpeta in carpetas:
        os.makedirs(os.path.join(ruta, carpeta), exist_ok=True)

# Función para mover archivos a sus carpetas correspondientes
def mover_archivos(ruta_origen, ruta_destino, excepciones=[]):
    for archivo in os.listdir(ruta_origen):
        if archivo in excepciones:
            continue
        
        ruta_archivo = os.path.join(ruta_origen, archivo)
        if os.path.isfile(ruta_archivo):
            for carpeta, extensiones in extensiones_documentos.items():
                if archivo.endswith(tuple(extensiones)):
                    shutil.move(ruta_archivo, os.path.join(ruta_destino, carpeta))
                    print(f"Movido: {archivo} a {carpeta}")
                    break

# Función principal
def main():
    parser = ArgumentParser()
    parser.add_argument("-rf", "--directoryFile", help="Ruta de los archivos a organizar", type=str, default="./")
    parser.add_argument("-ro", "--directoryOutput", help="Ruta donde se crearán las carpetas", type=str, default="./")
    args = parser.parse_args()

    carpetas = list(extensiones_documentos.keys())
    crear_carpetas_si_no_existen(carpetas, args.directoryOutput)
    mover_archivos(args.directoryFile, args.directoryOutput, excepciones=[__file__, "requirements.txt"])

if __name__ == "__main__":
    main()
