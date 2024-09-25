import streamlit as st

# Título y subtítulo de la aplicación
st.title("Gen Programación")
st.subheader("Programa las células para poder llegar al objetivo")

# Función para determinar si el estudiante ha respondido correctamente y contar aciertos
def verificar_respuestas(correctas, respuestas):
    aciertos = sum(respuestas[gen] == correctas[gen] for gen in correctas)
    total = len(correctas)
    return aciertos, total

# Formulario para hepatocito
st.subheader("Transformación de Célula Madre en Hepatocito")
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

# Botón para finalizar
if st.button("Finalizar"):
    # Respuestas correctas para el hepatocito
    respuestas_correctas_hepatocito = {
        "Descompone y sintetiza grasas": "True",
        "Detoxifica: elimina toxinas": "True",
        "Producción de bilis": "True",
        "Almacena glucosa en forma de glucógeno": "True",
        "Síntesis de proteínas": "True",
        "Control de la apoptosis": "True",
        "No forma parte de un hepatocito": "False"
    }

    # Verificar las respuestas para el hepatocito
    aciertos_hepatocito, total_hepatocito = verificar_respuestas(respuestas_correctas_hepatocito, hepatocito_respuestas)

    # Mostrar resultados
    st.subheader("Resultados")

    if aciertos_hepatocito == total_hepatocito:
        st.success(f"¡Has transformado correctamente la célula en un Hepatocito! Aciertos: {aciertos_hepatocito}/{total_hepatocito}")
        st.image("https://raw.githubusercontent.com/proyect8/prueba/fbf5f39c954ce635d1a4598dfb0b97a222b74d7c/hepatocyte_image.jpeg", width=300)  # Imagen del Hepatocito
    else:
        st.error(f"No has logrado transformar correctamente en Hepatocito. Aciertos: {aciertos_hepatocito}/{total_hepatocito}")
