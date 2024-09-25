import streamlit as st

# Título y subtítulo de la aplicación
st.title("Gen Programación")
st.subheader("Activa y desactiva estos genes mediante comandos de programación para convertir la célula madre en un Hepatocito")

# Función para verificar si los genes están correctamente activados/desactivados
def verificar_genes(correctas, respuestas):
    aciertos = sum(respuestas[gen] == correctas[gen] for gen in correctas)
    total = len(correctas)
    return aciertos, total

# Formulario para activación/desactivación de genes
st.write("Escribe 'True' para activar o 'False' para desactivar los siguientes genes:")

gene_respuestas = {
    "Gene_VisiónDiurna": st.text_input("Gene_VisiónDiurna"),
    "Gene_FormaciónOrina": st.text_input("Gene_FormaciónOrina"),
    "Gene_MantenimientoGlucosa": st.text_input("Gene_MantenimientoGlucosa"),
    "Gene_LiberaciónÁcidosGrasos": st.text_input("Gene_LiberaciónÁcidosGrasos"),
    "Gene_SintesisProteinas": st.text_input("Gene_SintesisProteinas"),
    "Gene_ControlApoptosis": st.text_input("Gene_ControlApoptosis"),
    "Gene_ControlPresiónArterial": st.text_input("Gene_ControlPresiónArterial")
}

# Botón para finalizar
if st.button("Finalizar"):
    # Respuestas correctas para convertir en Hepatocito
    respuestas_correctas = {
        "Gene_VisiónDiurna": "False",
        "Gene_FormaciónOrina": "False",
        "Gene_MantenimientoGlucosa": "True",
        "Gene_LiberaciónÁcidosGrasos": "True",
        "Gene_SintesisProteinas": "True",
        "Gene_ControlApoptosis": "True",
        "Gene_ControlPresiónArterial": "False"
    }

    # Verificar las respuestas de los genes
    aciertos, total = verificar_genes(respuestas_correctas, gene_respuestas)

    # Mostrar resultados
    st.subheader("Resultados")
    
    if aciertos == total:
        st.success(f"¡Has activado correctamente los genes para convertir la célula en un Hepatocito! Aciertos: {aciertos}/{total}")
        # Mostrar la imagen desde la ruta local
        st.image("hepatocyte_image.jpeg", width=300)  # Imagen del Hepatocito desde la ruta local
    else:
        st.error(f"No has logrado activar correctamente los genes. Aciertos: {aciertos}/{total}")
