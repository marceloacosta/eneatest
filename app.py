import streamlit as st
from collections import OrderedDict

# Inicialización de las puntuaciones
scores = {i: 0 for i in range(1, 10)}

# Preguntas para cada tipo
# Preguntas para cada tipo
questions = {
    1: [
        "Siento una fuerte necesidad de hacer las cosas correctamente.",
        "Me molesta mucho la injusticia y la imperfección.",
        "A menudo me encuentro criticando a mí mismo y a los demás.",
        "Me cuesta trabajo perdonar mis errores.",
        "La organización y el orden me hacen sentir a gusto."
    ],
    2: [
        "Pongo las necesidades de los demás antes que las mías.",
        "Me siento poco valorado cuando mis actos de bondad pasan desapercibidos.",
        "Las relaciones son más importantes para mí que los logros personales.",
        "Me cuesta decir 'no' a las solicitudes.",
        "Tengo un don para saber lo que la gente necesita."
    ],
    3: [
        "El éxito y los logros me motivan.",
        "Soy adaptable y puedo encajar en cualquier situación.",
        "Los demás me ven como un modelo a seguir para el éxito.",
        "Temo al fracaso.",
        "A menudo pongo tareas y metas antes que las relaciones personales."
    ],
    4: [
        "Siento que soy fundamentalmente diferente a los demás.",
        "Busco crear una identidad única para mí mismo.",
        "La autenticidad es muy importante para mí.",
        "A menudo me siento incomprendido.",
        "Siento una fuerte conexión con las expresiones artísticas."
    ],
    5: [
        "Prefiero observar antes de participar.",
        "Siento que tengo recursos emocionales y mentales limitados.",
        "Valoro el conocimiento y la competencia.",
        "Prefiero estar solo la mayor parte del tiempo.",
        "A menudo me sumerjo profundamente en mis intereses."
    ],
    6: [
        "La lealtad es muy importante para mí.",
        "A menudo me preocupo por el futuro y lo que podría salir mal.",
        "Busco seguridad y apoyo en un grupo o autoridad.",
        "Tengo problemas de confianza.",
        "Me siento más cómodo con las reglas y las estructuras claras."
    ],
    7: [
        "Evito el dolor emocional a través de la distracción o la planificación.",
        "Me encanta probar cosas nuevas y tener experiencias diversas.",
        "Encuentro difícil centrarme en una sola cosa a la vez.",
        "Siento que la vida es una aventura llena de posibilidades.",
        "Temo perderme de experiencias emocionantes."
    ],
    8: [
        "Disfruto estando en control de las situaciones.",
        "No me gusta mostrar mi vulnerabilidad.",
        "Me siento cómodo tomando decisiones para un grupo.",
        "Defiendo lo que creo sin importar las consecuencias.",
        "Detesto sentirme controlado por otros."
    ],
    9: [
        "Evito conflictos siempre que sea posible.",
        "Me cuesta mucho ponerme a mí mismo primero.",
        "Busco la armonía y el equilibrio en mis relaciones.",
        "Es difícil para mí expresar mis propios deseos y necesidades.",
        "Me siento más a gusto en un ambiente tranquilo."
    ]
}


# Función para mostrar preguntas
# Función para mostrar preguntas
def display_questions(type_num, questions):
    st.subheader(f"Tipo {type_num}")
    for idx, q in enumerate(questions):
        st.markdown(f"<span style='font-size: 1.2em; font-weight: bold;'>{q}</span>", unsafe_allow_html=True)
        st.write('1: No me identifico en absoluto ---- 5: Siempre me identifico')
        unique_key = f"{type_num}-{idx}"
        score = st.radio(
            "",
            options=[1, 2, 3, 4, 5],
            key=unique_key
        )
        scores[type_num] += score

# Función para determinar el ala
def find_wing(main_type):
    # Identifica los tipos adyacentes (alas)
    if main_type == 1:
        adjacent_types = [9, 2]
    elif main_type == 9:
        adjacent_types = [8, 1]
    else:
        adjacent_types = [main_type - 1, main_type + 1]
    
    # Encuentra el tipo adyacente con la puntuación más alta
    wing = max(adjacent_types, key=lambda x: scores[x])
    return wing

# App principal
def main():
    st.title("Test de Eneagrama")

    st.write("## Instrucciones")
    # ... tus instrucciones aquí

    for type_num, qs in questions.items():
        display_questions(type_num, qs)

    if st.button("Obtener Resultados"):
        # Encuentra el tipo principal
        main_type = max(scores, key=scores.get)
        
        # Encuentra el ala
        wing = find_wing(main_type)
        
        st.write(f"Tu tipo de eneagrama más probable es el Tipo {main_type} con ala en Tipo {wing}.")

if __name__ == "__main__":
    main()