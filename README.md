# 🎓 Análisis del Rendimiento Académico de Estudiantes

## 📌 Tema
**Educación**

## 📊 Propuesta de Análisis
Este proyecto tiene como objetivo explorar el impacto de distintos factores demográficos y sociales en el rendimiento académico de los estudiantes. Se analiza cómo variables como el género, etnia, almuerzo escolar, preparación previa, entre otras, afectan los puntajes obtenidos en matemáticas, lectura y escritura.

---

## 🗂️ Dataset
**Student Performance Dataset**  
🔗 [Disponible en Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

---

### 📌 Columnas clave:
- `gender`
- `race/ethnicity`
- `parental level of education`
- `lunch`
- `test preparation course`
- `math score`
- `reading score`
- `writing score`

Este conjunto de datos es limpio, pequeño y excelente para análisis exploratorio. Contiene variables categóricas y numéricas que permiten diversas visualizaciones.

---

## ❓ Preguntas de Análisis Propuestas

1. ¿Cuál es la distribución de calificaciones en matemáticas, lectura y escritura entre todos los estudiantes?  
   → **Gráfico:** Histogramas

2. ¿Qué género obtiene en promedio mejores resultados en matemáticas, lectura y escritura?  
   → **Gráfico:** Barras con `groupby('gender')`

3. ¿Influye el nivel educativo de los padres en las calificaciones de los estudiantes?  
   → **Gráfico:** Boxplot o barras agrupadas por `parental level of education`

4. ¿Los estudiantes que completaron el curso de preparación obtienen mejores resultados?  
   → **Gráfico:** Boxplot o barras comparativas con `groupby('test preparation course')`

5. ¿Qué combinación de género y almuerzo escolar se asocia con promedios más altos o bajos?  
   → **Gráfico:** Barras múltiples con `groupby(['gender', 'lunch'])`

6. ¿Existen diferencias significativas en el rendimiento por grupo étnico?  
   → **Gráfico:** Barras o violin plot con `groupby('race/ethnicity')`

7. ¿Cuál es la correlación entre las tres calificaciones?  
   → **Gráfico:** Heatmap de correlación (`math`, `reading`, `writing` scores)

8. ¿Cuál es la calificación promedio por tipo de almuerzo (estándar vs. reducido)?  
   → **Gráfico:** Barras con `groupby('lunch')`

9. ¿Qué porcentaje de estudiantes obtuvo más de 90 puntos en las tres asignaturas?  
   → **Métrica y pie chart:** Condición sobre las tres columnas de puntajes

10. ¿Cuál es la distribución conjunta de notas entre matemáticas y escritura (o lectura)?  
    → **Gráfico:** Scatter plot o joint plot

---

## 📚 Requisitos

- Python 3.10 o superior  
- Virtualenv o entorno virtual similar  
- Navegador web moderno (para abrir Jupyter Notebook)

---

## 🧰 Librerías utilizadas

- `pandas`  
- `numpy`  
- `matplotlib`  
- `seaborn`  
- `tabulate`  
- `Jupyter Notebook`

---

## 🧪 Ejecución

1. Clonar este repositorio o descargar los archivos.
2. Crear un entorno virtual y activar:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   .\venv\Scripts\activate   # En Windows

   pip install -r requirements.txt
   ```
3. Abrir el archivo `notebook.ipynb` en Jupyter Notebook.

---

## ✍️ Autor
✍️ **Desarrollado por:** **Deyton Riasco Ortiz and Samuel Izquierdo Bonilla**  
📅 **Fecha:** 2025  
> All team members contributed to coding, analysis, and presentation.

---