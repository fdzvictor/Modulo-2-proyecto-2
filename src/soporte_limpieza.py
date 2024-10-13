def traductor (dataframe):
 

 cambio_nombre_columnas = {
  
    'CÓDIGO ÓRGÃO SUPERIOR': 'codigo_entidad_superior',
    'NOME ÓRGÃO SUPERIOR': 'nombre_entidad_superior',
    'CÓDIGO ÓRGÃO': 'codigo_organo',
    'NOME ÓRGÃO': 'nombre_organo',
    'CÓDIGO UNIDADE GESTORA': 'codigo_unidad_gestora',
    'NOME UNIDADE GESTORA': 'nombre_unidad_gestora',
    'CATEGORIA ECONÔMICA': 'categoria_economica',
    'ORIGEM RECEITA': 'origen_ingreso',
    'ESPÉCIE RECEITA': 'especie_ingreso',
    'DETALHAMENTO': 'detalle',
    'VALOR PREVISTO ATUALIZADO': 'valor_previsto_actualizado',
    'VALOR LANÇADO': 'valor_lanzado',
    'VALOR REALIZADO': 'valor_realizado',
    'PERCENTUAL REALIZADO': 'porcentaje_realizado',
    'DATA LANÇAMENTO': 'fecha_lanzamiento',
    'ANO EXERCÍCIO': 'ano_ejercicio'
}


 dataframe.rename(columns = cambio_nombre_columnas,inplace= True) 
    
 return dataframe

def anio_a_int (dataframe,año):

#cambiamos nulos de año a año y cambiamos tipo a int (A mordiscos porque no sé optimizarlo :)
 dataframe["anio_ejercicio"].fillna(año, inplace = True)
 dataframe["anio_ejercicio"] = dataframe["anio_ejercicio"].astype(int)

def codigo_nombre (dataframe,cod,nom):

 if type(cod) == str and type(nom) == str:
  #Sacamos valores unicos para renombrar
  cols0y1 = dataframe [[cod,nom]].drop_duplicates().dropna().to_dict("records") 
  #Creamos un codigo para mapear los nombres asignados a los códigos      
  mapping = {item[cod]: item[nom] for item in cols0y1}

  # Usamos map() para rellenar los valores nulos en 'nombre_entidad'
  dataframe[nom] = dataframe[nom].fillna(dataframe[cod].map(mapping))

  #Usamos la misma función de mapeo pero al revés, asignándole a cada código un nombre
  mapping2 = {item[nom]: item[cod] for item in cols0y1}

  # Usamos map() para rellenar los valores nulos en 'codigo_entidad'
  dataframe[cod] = dataframe[cod].fillna(dataframe[nom].map(mapping2))
  #Hemos igualado los nulos en ambas columnas y reducido los valores nulos totales sin perder observaciones
  dataframe[[cod, nom]].shape

  return dataframe

 else:
  print("Código y número han de ser strings!") 