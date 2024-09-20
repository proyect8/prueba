import streamlit as st

# Función para determinar si el estudiante ha respondido correctamente
def verificar_respuestas(correctas, respuestas):
    return all(respuestas[gen] == correctas[gen] for gen in correctas)

# Formulario para hepatocito
st.title("Transformación de Célula Madre en Hepatocito")

st.write("Responde 'True' o 'False' para las siguientes funciones del hepatocito:")

hepatocito_respuestas = {
    "Descompone y sintetiza grasas": st.text_input("Descompone y sintetiza grasas"),
    "Detoxifica: elimina toxinas": st.text_input("Detoxifica: elimina toxinas"),
    "Producción de bilis": st.text_input("Producción de bilis"),
    "Almacena glucosa en forma de glucógeno": st.text_input("Almacena glucosa en forma de glucógeno"),
    "Síntesis de proteínas": st.text_input("Síntesis de proteínas"),
    "Control de la apoptosis": st.text_input("Control de la apoptosis"),
    "No forma parte de un hepatocito": st.text_input("No forma parte de un hepatocito")
}

# Formulario para neuronas
st.title("Transformación de Célula Madre en Neuronas")

st.write("Responde 'True' o 'False' para las siguientes funciones de las neuronas:")

neurona_respuestas = {
    "Transmiten impulsos eléctricos": st.text_input("Transmiten impulsos eléctricos"),
    "Procesan información motora, sensorial y cognitiva": st.text_input("Procesan información motora, sensorial y cognitiva"),
    "Formación de sinapsis": st.text_input("Formación de sinapsis"),
    "Libera neurotransmisores": st.text_input("Libera neurotransmisores"),
    "No forma parte de una neurona": st.text_input("No forma parte de una neurona")
}

# Formulario para conos
st.title("Transformación de Célula Madre en Conos")

st.write("Responde 'True' o 'False' para las siguientes funciones de los conos:")

conos_respuestas = {
    "Detección de colores rojo, verde y azul": st.text_input("Detección de colores rojo, verde y azul"),
    "Detección de luz brillante": st.text_input("Detección de luz brillante"),
    "Visión de alta resolución": st.text_input("Visión de alta resolución"),
    "Responsable de la visión diurna": st.text_input("Responsable de la visión diurna"),
    "No forma parte de un cono": st.text_input("No forma parte de un cono")
}

# Botón para finalizar
if st.button("Finalizar"):
    # Respuestas correctas para cada tipo de célula
    respuestas_correctas_hepatocito = {
        "Descompone y sintetiza grasas": "True",
        "Detoxifica: elimina toxinas": "True",
        "Producción de bilis": "True",
        "Almacena glucosa en forma de glucógeno": "True",
        "Síntesis de proteínas": "True",
        "Control de la apoptosis": "True",
        "No forma parte de un hepatocito": "False"
    }
    
    respuestas_correctas_neurona = {
        "Transmiten impulsos eléctricos": "True",
        "Procesan información motora, sensorial y cognitiva": "True",
        "Formación de sinapsis": "True",
        "Libera neurotransmisores": "True",
        "No forma parte de una neurona": "False"
    }
    
    respuestas_correctas_conos = {
        "Detección de colores rojo, verde y azul": "True",
        "Detección de luz brillante": "True",
        "Visión de alta resolución": "True",
        "Responsable de la visión diurna": "True",
        "No forma parte de un cono": "False"
    }
    
    # Verificar las respuestas para cada tipo de célula
    correcto_hepatocito = verificar_respuestas(respuestas_correctas_hepatocito, hepatocito_respuestas)
    correcto_neurona = verificar_respuestas(respuestas_correctas_neurona, neurona_respuestas)
    correcto_conos = verificar_respuestas(respuestas_correctas_conos, conos_respuestas)
    
    # Mostrar resultados
    if correcto_hepatocito:
        st.success("¡Has transformado correctamente la célula en un Hepatocito!")
        st.image("https://example.com/hepatocito.png")  # Cambia por la URL real de la imagen del hepatocito
    else:
        st.error("No has logrado transformar correctamente en Hepatocito.")
    
    if correcto_neurona:
        st.success("¡Has transformado correctamente la célula en una Neurona!")
        st.image("https://example.com/neurona.png")  # Cambia por la URL real de la imagen de la neurona
    else:
        st.error("No has logrado transformar correctamente en Neurona.")
    
    if correcto_conos:
        st.success("¡Has transformado correctamente la célula en un Cono!")
        st.image("https://example.com/conos.png")  # Cambia por la URL real de la imagen de los conos
    else:
        st.error("No has logrado transformar correctamente en Cono.")
