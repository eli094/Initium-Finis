# Declaración de los personajes.
# A cada uno le asigno una letra que sirve para el código, 
# el nombre con el que se los ve en la novela
# y un color.

define abuela = Character(_("Abuela"), color="#f90101")

define hijo = Character(_("Hijo"), color="#ff00e6")
define hija = Character(_("Hija"), color="#00d5ff")

define nietomayordelhijo = Character(_("Nieto Mayor de la Abuela, del Hijo Mayor"), color="#ff00e68f")
define nietadelmediodelhijo = Character(_("Nieta del Medio de la Abuela, del Hijo Mayor"), color="#ff00e655")
define nietomenordelhijo = Character(_("Nieto Menor de la Abuela, del Hijo Mayor"), color="#ff00e649")
define nietadelahija = Character(_("Nieta de la Abuela, de la Hija Menor"), color="#00d5ffaf")

define amigaabuela = Character(_("Amiga de la Abuela"), color="#01f93f")


label start: # Acá empieza

    # play music "illurock.opus" 
    # Esta es la forma para reproducir sonidos/música.

    # Muestra una imagen de fondo: 
    # es posible añadir un archivo en el directorio 'images' con el nombre "bg room.png" o "bg room.jpg"/etc. para que se muestre.

    scene back_ground_ # Carga las imágenes de fondo.
    # with fade -> Agrega un efecto.

    show nona_busto: # Muestra a los personajes.
        xpos 100
        ypos 700

    "El día había arribado. El tiempo pasó, de la noche a la mañana."
    "Los escucho, corriendo por los pasillos de la casa."
    "Están riendo."
    "Sonrío."
    "Mis hijos, los quiero."
    "¿Puedo abrazarlos?"
    "¿Dónde están?"

    # Esto es para poner el texto que aparece y el poner adelante
    # el nombre del personaje (que declaré arriba).

    
    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá, ¿cómo te sientes?."

    menu:
        "¿Cómo me siento?"

        "No sé. Extraña.":

            jump Trust

        "Bien.":

            jump Lie

label Trust:

    hijo "¿Y eso? ¿No se siente cómoda?" 
    hijo "Le tendré que avisar a su hija. Seguro que ella se hace cargo." 
    hijo "Déjeme que le prepare el almuerzo."
    
    "Miro a la ventana."
    "¿Hija?"
    "¿Tenía alguna?"
    "¿No será mi amiga?"
    "Amiga…"
    "¿Seguirá viviendo al lado?"

    abuela "Mi amiga."
    abuela "¿La podrías llamar para que venga a comer también, por favor?"

    hijo "Oh. Ella."
    hijo "¿Cómo se lo podría explicar? Su alma se encuentra en otro plano."

    abuela "¿Otro plano? ¿A qué se refiere?"
    abuela "Ella está allí, detrás de esa pared."

    hijo "Falleció hace un tiempo."

    "¿Falleció?"
    "¿En serio?"
    "¿Cuándo pasó eso?"
    "¿Fue ayer?"
    "Escucho las llaves sonar, seguro que es ella."

    hija "Mamá. El tráfico estaba terrible. No pude llegar más rápido. Hola."
    abuela "Amiga. Te estaba esperando. Él está cocinando. Siéntate en tu silla favorita."

    "¿Por qué mi Amiga me observa de esa manera?"
    "¿Cuál es el motivo por el cual sus ojos se llenan de lágrimas?"
    "¿Hice algo mal?"

    hija "Los chicos vendrán una vez que salgan del colegio y de la facultad."
    abuela "¿Cuándo tuviste hijos, Amiga? No me avisaste."
    hija "Es- él tiene tres. Yo tengo una hija. ¿No te acuerdas?"

    "La observo."
    "No entiendo."
    "¿Recordar?"
    "¿Qué cosa exactamente?"

    jump Story

label Lie:

    hijo "Que bueno." 
    hijo "¿Pudo descansar bien?"
    hijo "Le puedo preparar el almuerzo, si quiere."
    abuela "No gracias, yo lo hago."

    "Mis pies se dirigen a la cocina."
    "¿Quedaba por acá?"
    "Sí, puede ser."
    "O, quizás... no-sé."
    "En fin, mi marido debería estar por llegar."
    "Le debería cocinar algo."
    "¿Qué le gustaba al Viejo?"
    "Fideos, arroz, esa pasta amarilla. ¿Cómo se llamaba? ¿Puré?"
    "Eso mismo."

    hijo "¿Segura?"
    hijo "Mamá, ¿no recuerda dónde dejó los huevos?"
    abuela "¿Cómo no me voy a acordar?"
    abuela "Están en la heladera."
    hijo "¿Y por qué está buscando en la alacena?"
    abuela "Ah. Mi mente, no te preocupes."

    "Escucho las llaves sonar, seguro que es el Viejo."
    "Habrá vuelto del viaje."
    "Estuvo seis meses afuera."
    "En el océano."
    "Donde la vida y la muerte conviven constantemente."
    "Espero que esté bien."

    hija "Mamá. El tráfico estaba terrible. No pude llegar más rápido. Hola."
    abuela "Viejo. ¡Tanto tiempo!"
    hijo "¿El Viejo? Murió hace años, mientras estaba de viaje por las Bahamas."

    jump Story

label Story:

    "Los nietos llegan a la casa de la abuela. Le cuentan cómo les fue el día."

    #hide Sirve para esconder a los personajes.

    return   # Finaliza el videojuego.
