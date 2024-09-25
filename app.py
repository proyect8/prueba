import streamlit as st

# Título y subtítulo de la aplicación
st.title("Gen Programación")
st.subheader("Escribe el código en Python para activar y desactivar los genes y convertir la célula madre en un Hepatocito")

# Explicación para el estudiante
st.write("Escribe el código utilizando condicionales como `if`, `elif`, y `else` para activar o desactivar los genes. Por ejemplo:")
st.code("""
if self.gene_visiondiurna == False:
    pass
elif self.gene_formacionorina == False:
    pass
""", language="python")

# Input para que el estudiante escriba el "código"
codigo_estudiante = st.text_area("Escribe tu código aquí:")

# Botón para evaluar el código
if st.button("Evaluar Código"):
    # Definir las respuestas correctas
    respuestas_correctas = {
        "gene_visiondiurna": False,
        "gene_formacionorina": False,
        "gene_mantenimientoglucosa": True,
        "gene_liberacionacidosgrasos": True,
        "gene_sintesisproteinas": True,
        "gene_controlapoptosis": True,
        "gene_controlpresionarterial": False
    }
    
    # Diccionario para guardar las respuestas del estudiante
    respuestas_estudiante = {
        "gene_visiondiurna": None,
        "gene_formacionorina": None,
        "gene_mantenimientoglucosa": None,
        "gene_liberacionacidosgrasos": None,
        "gene_sintesisproteinas": None,
        "gene_controlapoptosis": None,
        "gene_controlpresionarterial": None
    }

    # Evaluar el código del estudiante de manera segura
    try:
        # Ejecutar el código del estudiante
        exec(codigo_estudiante, {}, respuestas_estudiante)

        # Verificar cuántos aciertos tiene el estudiante
        aciertos = sum(respuestas_estudiante[gen] == respuestas_correctas[gen] for gen in respuestas_correctas)
        total = len(respuestas_correctas)

        # Mostrar resultados
        if aciertos == total:
            st.success(f"¡Has activado correctamente los genes para convertir la célula en un Hepatocito! Aciertos: {aciertos}/{total}")
            st.image("hepatocyte_image.jpeg", width=300)  # Imagen del Hepatocito desde la ruta local
        else:
            st.error(f"No has logrado activar correctamente los genes. Aciertos: {aciertos}/{total}")
            st.write("Revisa el código que has escrito.")
    
    except Exception as e:
        st.error(f"Error en el código: {e}")
        st.write("Asegúrate de que el código esté bien escrito y que uses correctamente las condicionales.")
