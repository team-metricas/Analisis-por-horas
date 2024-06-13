# Analisis-por-horas
Se analiza las consultas al modelo por hora.  
Se obtienen los descriptores estadisticos.  

## Requerimientos ##
Descarga del archivo CSV  `medidas_01.csv` mediente la Query `Query_Disparos_de_IA_por_Hora.sql`.  

## Proceso de Ejecucion: ##

La carpeta `/data` No esta incluida en el repositorio, se debe crear una vez clonado al mismo nivel de `/src`  
 
**analisis_metricas_01.py**  
Analiza en el CSV los descriptores estadisticos creando un CSV con esos datos y una imagen indicando la curva de media y desvio standard.  

	
## Entregables ##  
El separador del CSV esta definido como Punto y Coma para que sea levantado automaticamente desde __Excel__  
Archivo `descriptores_estadisticos.csv` en la raiz del repositorio.    
Imagen  `grafico_impacto_por_hora.png`
