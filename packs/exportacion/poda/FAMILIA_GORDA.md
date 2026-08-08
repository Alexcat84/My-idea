# Familia gorda de exportacion, para tu poda

El umbral de 0,90 del censo no la agrupo. Aqui van los **9** nodos a coseno >= 0,78
del mas central (`documentacion_exportacion`), que es donde vive la duplicacion que el censo no vio.

De ellos, **2** ya caen en los 7 clusters del indice y
**7** no.

**Borra las lineas de lo que NO debe fundirse.**

| sim | titulo | visto | ¿en cluster? |
|---:|---|---:|:-:|
| 1.000 | **Documentación de Exportación** `documentacion_exportacion` | 0 | **NO** |
| 0.857 | **Documentación Básica de Exportación (Pro Forma Invoice, Co** `documentacion_exportacion_basica` | 0 | **NO** |
| 0.852 | **Investigación de Regulaciones de Importación de Gobiernos ** `import_regulations_foreign_governments` | 0 | **NO** |
| 0.812 | **Declaración de Control de Destino (Antidiversion Clause)** `antidiversion_clause` | 0 | si |
| 0.809 | **Determinar si se necesita Licencia de Exportación** `licencia_exportacion_regulaciones` | 0 | **NO** |
| 0.802 | **Certificado de Origen (COO)** `certificado_de_origen_coo` | 0 | **NO** |
| 0.797 | **Cláusula Antidesviación (Destination Control Statement)** `clausula_antidesviacion` | 0 | si |
| 0.793 | **Etiquetado y Marcado de Exportación (Labeling)** `etiquetado_exportacion` | 0 | **NO** |
| 0.788 | **Cumplimiento de las Export Administration Regulations (EAR** `export_administration_regulations` | 0 | **NO** |