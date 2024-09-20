import streamlit as st

# Definir las opciones de genes
genes = {
    "Descompone y sintetiza grasas (Hepatocito)": "",
    "Detoxifica: elimina toxinas (Hepatocito)": "",
    "Producción de bilis (Hepatocito)": "",
    "Almacena glucosa en forma de glucógeno (Hepatocito)": "",
    "Síntesis de proteínas (Hepatocito)": "",
    "Control de la apoptosis (Hepatocito)": "",
    
    "Transmiten impulsos eléctricos (Neurona)": "",
    "Procesan información motora, sensorial y cognitiva (Neurona)": "",
    "Formación de sinapsis (Neurona)": "",
    "Libera neurotransmisores (Neurona)": "",
    
    "Detección de colores rojo, verde y azul (Conos)": "",
    "Detección de luz brillante (Conos)": "",
    "Visión de alta resolución (Conos)": "",
    "Responsable de la visión diurna (Conos)": "",
    
    "No forma parte de ninguna de estas células": ""
}

# Título de la aplicación
st.title("Transformación de Células Madre")

# Descripción del ejercicio
st.write("Escribe 'True' o 'False' para las funciones correspondientes de cada célula.")

# Crear un formulario para los genes
with st.form("formulario_genes"):
    genes_respuestas = {}
    for gen, valor in genes.items():
        genes_respuestas[gen] = st.text_input(gen)
    
    # Botón para enviar las respuestas
    submitted = st.form_submit_button("Finalizar")

# Definir la lógica de transformación celular
def determinar_tipo_celula(genes_respuestas):
    # Respuestas correctas para hepatocito
    hepatocito_respuestas = {
        "Descompone y sintetiza grasas (Hepatocito)": "True",
        "Detoxifica: elimina toxinas (Hepatocito)": "True",
        "Producción de bilis (Hepatocito)": "True",
        "Almacena glucosa en forma de glucógeno (Hepatocito)": "True",
        "Síntesis de proteínas (Hepatocito)": "True",
        "Control de la apoptosis (Hepatocito)": "True"
    }
    
    # Respuestas correctas para neuronas
    neurona_respuestas = {
        "Transmiten impulsos eléctricos (Neurona)": "True",
        "Procesan información motora, sensorial y cognitiva (Neurona)": "True",
        "Formación de sinapsis (Neurona)": "True",
        "Libera neurotransmisores (Neurona)": "True"
    }
    
    # Respuestas correctas para conos
    conos_respuestas = {
        "Detección de colores rojo, verde y azul (Conos)": "True",
        "Detección de luz brillante (Conos)": "True",
        "Visión de alta resolución (Conos)": "True",
        "Responsable de la visión diurna (Conos)": "True"
    }
    
    # Respuesta incorrecta (fuera de las funciones)
    otras_respuestas = {
        "No forma parte de ninguna de estas células": "False"
    }
    
    # Comprobar si las respuestas coinciden con alguna célula
    if all(genes_respuestas[gen] == hepatocito_respuestas.get(gen, "False") for gen in hepatocito_respuestas) and genes_respuestas["No forma parte de ninguna de estas células"] == "False":
        return "Hepatocito"
    elif all(genes_respuestas[gen] == neurona_respuestas.get(gen, "False") for gen in neurona_respuestas) and genes_respuestas["No forma parte de ninguna de estas células"] == "False":
        return "Neurona"
    elif all(genes_respuestas[gen] == conos_respuestas.get(gen, "False") for gen in conos_respuestas) and genes_respuestas["No forma parte de ninguna de estas células"] == "False":
        return "Cono"
    else:
        return "Célula madre no diferenciada"

# Mostrar el resultado cuando se envíen los datos
if submitted:
    tipo_celula = determinar_tipo_celula(genes_respuestas)
    
    if tipo_celula == "Hepatocito":
        st.success("¡Has transformado la célula en un **Hepatocito**!")
        st.image("https://example.com/hepatocito.png")  # Imagen del hepatocito
    elif tipo_celula == "Neurona":
        st.success("¡Has transformado la célula en una **Neurona**!")
        st.image("https://example.com/neurona.png")  # Imagen de la neurona
    elif tipo_celula == "Cono":
        st.success("¡Has transformado la célula en un **Cono**!")
        st.image("https://example.com/conos.png")  # Imagen de los conos
    else:
        st.warning("No has logrado transformar correctamente la célula.")
