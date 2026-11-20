import pandas as pd
import matplotlib.pyplot as plt
## Caleb Dorado NC = 0039
# 1. Crear diccionario con datos de empleados
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
}
print("\n Analisis Exploratorio de Datos EDA")
print("\n Exploratory Data Analysis por ---> Caleb Dorado NC = 0039")
print("\n 5. Crear el diccionario con 10 listas y 6 elementos")
# 2 Convertir deccionario DataFrame
df = pd.DataFrame(empleados)
print("\n --- TABLA ORIGINAL DE EMPLEADOS ---")
print(df)
# 3. Exportar los datos a CSV
print("\n -+-+-Convertir el DataFrame en archivo CSV-+-+-")
df.to_csv(
    'empleados_industria_0039.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n ✅ Archivo CSV creado correctamente")
# 4. Leer el archivo CSV
print("\n +-+- 8. Leer los datos desde el archivo CSV +-+-")
print("empleados_industria_0039.csv")
df = pd.read_csv('empleados_industria_0039.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("\n -+-+-9. Análisis Exploratorio de Datos (EDA) +-+-+")
# 5. Primeros y últimos registros
print("\n-+-+-+ 1. PRIMEROS REGISTROS (Head):-+-+-+-")
print(df.head(3)) # Muestra los primeros 3
print("\n-+-+-+2. ÚLTIMOS REGISTROS (Tail):-+-++-+")
print(df.tail(2)) # Muestra los últimos 2
# 6. Dimensiones y estructura
print("\n-+-+ 6. Dimensiones y estructura -+-+-+")
print(df) # Mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza
print("\n+-+-+7. ESTADÍSTICAS DESCRIPTIVAS:+-+-+-")
print(df.describe())
print("\n+-+--+8. VALORES FALTANTES (Nulls):+-+-+-")
print(df.isnull().sum())
print("\n+-+-+-9. REGISTROS DUPLICADOS:+-+-+-+")
print(df.duplicated().sum())
print("\n-+-+-10. VALORES ÚNICOS POR COLUMNA:+-+-+-")
print(df.nunique())
print("Departamentos únicos:", df['departamento'].unique())
# 8. Análisis específico
print(df)
print("-------------------------------------------------------------------")
print("\n11. EMPLEADOS POR DEPARTAMENTO:")
print(df['departamento'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario'].mean())
print("13. SALARIO MÁXIMO: $", df['salario'].max())
print("14. SALARIO MÍNIMO: $", df['salario'].min())

# 9. Ordenamiento, filtrado y agrupación
print(" 9. Ordenamiento, filtrado y agrupación")

print("\n-+-+-+ 15. EMPLEADOS ORDENADOS POR SALARIO (Mayor a menor):+-+-+-")
print(df.sort_values(by='salario', ascending=False))

print("\n16. EMPLEADOS CON SALARIO MAYOR A $15,000:")
filtro = df[df['salario'] > 15000]
print(filtro)

print("\n17. RESUMEN POR DEPARTAMENTO:")
resumen = df.groupby('departamento').agg(
    empleados=('id_empleado', 'count'),
    salario_promedio=('salario', 'mean'),
    salario_maximo=('salario', 'max')
)
print(resumen)
print("\n-+-+18. Gráfica de barras: Empleados por departamento+----")
# 18. Gráfica de barras: Empleados por departamento
conteo = df['departamento'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Empleados por departamento Caleb Dorado 0039')
plt.xlabel('Departamento 0039')
plt.ylabel('Cantidad de empleados 0039')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Salarios por empleado
print("Gráfica de barras: Salarios por empleado")
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario'], color='lightgreen')
plt.title('Salario mensual por empleado EDA por Caleb 0039')
plt.xlabel('Empleado')
plt.ylabel('Salario en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de edades
print("20. Histograma: Distribución de edades")
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de edades de empleados por Caleb 0039')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 21. Gráfica de dispersión: Edad vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['edad'], df['salario'], color='red', s=100)
plt.title('Relación entre edad y salario Caleb Dorado NC = 0039')
plt.xlabel('Edad')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 22. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot) Caleb 0039')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas por Caleb 0039')
plt.tight_layout()
plt.show()