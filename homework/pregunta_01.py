"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    

    

    # Leer el archivo línea por línea
    with open("files/input/clusters_report.txt", "r") as file:
        lines = file.readlines()

    # Variables para almacenar los datos procesados
    data = []
    current_row = {"Cluster": None, "Cantidad de palabras clave": None, 
                  "Porcentaje de palabras clave": None, "Principales palabras clave": []}

    # Procesar cada línea del archivo
    for line in lines:
        line = line.strip()
        if line.startswith(tuple(str(i) for i in range(1, 15))):  # Detecta el inicio de un nuevo cluster
            if current_row["Cluster"]: 
                cadena=" ".join(current_row["Principales palabras clave"])
                cadena=cadena.replace(".", "")
                current_row["Principales palabras clave"] = cadena # Si ya hay datos, guárdalos
                
                data.append(current_row)
          
            # Crear una nueva fila
            parts = line.split()
             # Divide los elementos
            current_row = {
                "Cluster": int(parts[0]),
                "Cantidad de palabras clave": int(parts[1]),
                "Porcentaje de palabras clave": float(parts[2].replace(",", ".")),
                "Principales palabras clave": parts[4:]
                
            }
        elif line:
          # Las líneas adicionales son palabras clave
          current_row["Principales palabras clave"].append(" ".join(line.split()))
        # Guardar el último grupo
    if current_row["Cluster"]:
      cadena=" ".join(current_row["Principales palabras clave"])
      cadena=cadena.replace(".", "")
      current_row["Principales palabras clave"] = cadena
      data.append(current_row)
        

    
    # Convertir los datos en un DataFrame
    df = pd.DataFrame(data)
    df.columns = df.columns.map(lambda x: x.strip().lower().replace(" ", "_"))
    return df
    
    

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
pregunta_01()