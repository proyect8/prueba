import streamlit as st

# Definir las opciones de genes
genes = {
    "Gen_A (Neural)": False,
    "Gen_B (Hepatocito)": False,
    "Gen_C (Proliferación celular)": False,
    "Gen_D (Apoptosis)": False,
    "Gen_lipidosmetabolismo": False,
    "Gen_detox": False
}

# Título de la aplicación
st.title("Transformación de Células Madre")

# Descripción del ejercicio
st.write("Selecciona True o False para los siguientes genes para transformar la célula madre.")

# Crear un formulario para los genes
with st.form("formulario_genes"):
    # Generar casillas de verificación para cada gen
    genes_seleccionados = {}
    for gen, valor in genes.items():
        genes_seleccionados[gen] = st.checkbox(gen, value=valor)
    
    # Botón para enviar las respuestas
    submitted = st.form_submit_button("Transformar")

# Definir la lógica de transformación celular
def determinar_tipo_celula(genes_seleccionados):
    # Lógica para transformar a hepatocito
    if (
        genes_seleccionados["Gen_B (Hepatocito)"]
        and genes_seleccionados["Gen_C (Proliferación celular)"]
        and genes_seleccionados["Gen_lipidosmetabolismo"]
        and genes_seleccionados["Gen_detox"]
        and not genes_seleccionados["Gen_A (Neural)"]
        and not genes_seleccionados["Gen_D (Apoptosis)"]
    ):
        return "Hepatocito"
    
    # Lógica para transformar a neurona
    elif (
        genes_seleccionados["Gen_A (Neural)"]
        and not genes_seleccionados["Gen_B (Hepatocito)"]
        and not genes_seleccionados["Gen_lipidosmetabolismo"]
        and not genes_seleccionados["Gen_detox"]
    ):
        return "Neurona"
    
    # Puedes agregar más tipos de células aquí con más lógica
    else:
        return "Célula madre no diferenciada"

# Mostrar el resultado cuando se envíen los datos
if submitted:
    tipo_celula = determinar_tipo_celula(genes_seleccionados)
    st.write(f"¡Has transformado la célula en un **{tipo_celula}**!")

