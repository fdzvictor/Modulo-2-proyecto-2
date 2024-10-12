def traductor (dataframe):
 

    cambio_nombre_columnas = {
    columnas_acortadas = {
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

}
    dataframe.rename(columns = cambio_nombre_columnas,inplace= True) 
    
    return dataframe