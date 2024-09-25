import streamlit as st
import ast

# Título y subtítulo de la aplicación
st.title("Gen Programación")
st.subheader("Escribe las condiciones de activación de los genes usando lógica de programación para convertir la célula madre en un Hepatocito")

# Función para analizar el código y extraer las condiciones
def analizar_codigo(codigo):
    try:
        # Parseamos el código ingresado
        tree = ast.parse(codigo)
        condiciones = {}

        # Recorremos el árbol de sintaxis abstracta (AST) para analizar las condiciones
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                variable = node.test.left.id  # La variable de la condición (ej: gene_visiondiurna)
                valor = ast.literal_eval(node.test.comparators[0])  # El valor booleano (ej: False)
                condiciones[variable] = valor

        return condiciones, None
    except Exception as e:
        return None, str(e)

# Función para verificar si los genes están correctamente activados/desactivados
def verificar_genes(condiciones):
    respuestas_correctas = {
        "gene_visiondiurna": False,
        "formacionorina": False,
        "gene_mantenimientoglucosa": True,
        "gene_liberacionacidosgrasos": True,
        "gene_sintesisproteinas": True,
        "gene_controlapoptosis": True,
        "gene_controlpresionarterial": False
    }
    aciertos = sum(respuestas_correctas.get(gen) == cond for gen, cond in condiciones.items())
    total = len(respuestas_correctas)
    return aciertos, total

# Ejemplo de cómo debe ingresar el código el estudiante
st.code("""
if gene_visiondiurna == False:
elif formacionorina == False:
elif gene_mantenimientoglucosa == True:
elif gene_liberacionacidosgrasos == True:
elif gene_sintesisproteinas == True:
elif gene_controlapoptosis == True:
elif gene_controlpresionarterial == False:
""", language='python')

# Entrada de código por parte del estudiante
codigo_usuario = st.text_area("Escribe tus condiciones aquí (solo if y elif):")

# Botón para finalizar
if st.button("Finalizar"):
    # Analizar el código ingresado
    condiciones, error = analizar_codigo(codigo_usuario)

    if error:
        st.error(f"Error en el código: {error}")
    elif condiciones:
        # Verificar si las condiciones son correctas
        aciertos, total = verificar_genes(condiciones)

        # Mostrar resultados
        if aciertos == total:
            st.success(f"¡Has activado correctamente los genes para convertir la célula en un Hepatocito! Aciertos: {aciertos}/{total}")
            st.image("hepatocyte_image.jpeg", width=300)  # Imagen del Hepatocito desde la ruta local
        else:
            st.error(f"No has logrado activar correctamente los genes. Aciertos: {aciertos}/{total}")
    else:
        st.error("No se encontraron condiciones válidas en tu código.")
