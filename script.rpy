define abuela = Character(_("Ester"), color="#ee97f3", image = "ester")
define pensamientoabuela = Character(_("Pensamientos de Ester"), color="#ee97f3", image = "ester")

define hijo = Character(_("Lucas"), color="#377af8", image = "lucas")
define hija = Character(_("Luciana"), color="#fbfbfbc6", image = "hija")

define esposa = Character(_("Ámbar"), color="#c13e6f", image = "ambar")
define nietomayordelhijo = Character(_("Facundo"), color="#00ff0dff", image = "facundo")
define nietadelmediodelhijo = Character(_("Yamila"), color="#fc6accff", image = "yamila")
define nietomenordelhijo = Character(_("Santino"), color="#00d9ffff", image = "santino")

define cachito = Character(_("Cachito"), color="#000000ff", image = "cachito")

define policia = Character(_("Policía"), color="#fb399dc1", image = "policia")

define doc = Character(_("Psiquiatra"), color="#d7ec82ff", image = "psicologa")

define left_1 = Position(xalign = 0, yalign = 1.0)
define left_2 = Position(xalign = 0.15, yalign = 1.0)
define left_2B = Position(xalign = 0.25, yalign = 1.0)
define left_3 = Position(xalign = 0.3, yalign = 1.0)
define right_1 = Position(xalign = 1.0, yalign = 1.0)
define right_2 = Position(xalign = 0.85, yalign = 1.0)
define right_2B = Position(xalign = 0.8, yalign = 1.0)
define right_3 = Position(xalign = 0.6, yalign = 1.0)

default confio_doctora = False
default acepta_medicacion = False

default text_box = 0
image textbox = ConditionSwitch(
    "text_box == 0", Image("gui/textbox.png", xalign = 0.5, xfill = True, yalign = gui.textbox_yalign, ysize = gui.textbox_height),
    "text_box == 1", Image("gui/thoughtbubble.png", xalign = 0.5, xfill = True, yalign = gui.textbox_yalign, ysize = gui.textbox_height),
    "text_box == 2", Image("gui/sheetmaker.png", xalign = 0.5, xfill = True, yalign = gui.textbox_yalign, ysize = gui.textbox_height),
    )

label start:

    play music "initiumfinis(startline).mp3"

    scene realliving

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "El día había arribado. El tiempo pasó, de la noche a la mañana."
    pensamientoabuela "Los escucho, corriendo por los pasillos de la casa."
    pensamientoabuela "Están riendo."
    pensamientoabuela happy "Sonrío."
    pensamientoabuela "Mis hijos, los quiero."
    pensamientoabuela confused "¿Puedo abrazarlos?"
    pensamientoabuela "¿Dónde están?"

    #0 es caja de diálogo normal.
    $ text_box = 0
    
    show lucas normal at right_1
    with dissolve

    hijo "Mamá, ¿cómo te sentís?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:
        pensamientoabuela "¿Cómo me siento?"

        "No sé. Extraña.":

            jump Trust

        "Bien.":

            jump Lie

label Trust:

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¿Y eso? ¿Algo te molesta?"
    hijo @ happy"Sabés que podés confiar en mí para lo que sea."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "Algo me dice que puedo creerle, pero prefiero quedarme callada."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "No te preocupes si no podés contarme ahora." 
    hijo "Voy a ir a preparar el almuerzo."
    hijo "Andá a sentarte que ya viene tu hija."

    scene ventana_no_sombras
    with fade

    show ester normal at left_1
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Miro a la ventana."
    pensamientoabuela "¿Hija?"
    pensamientoabuela confused "¿Tenía una?"
    pensamientoabuela "¿No será mi amiga?"
    pensamientoabuela normal "Amiga…"
    pensamientoabuela "¿Seguirá viviendo al lado?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Mi amiga."
    abuela "¿La podrías llamar para que venga a comer también, por favor?"

    scene realliving

    show ester normal at left_1
    with dissolve

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Oh. Ella."
    hijo "¿Cómo te lo podría explicar? Ella ya no está acá."
    hijo "La querías mucho por todo lo que me solés contar."

    abuela "¿A qué te refieres?"
    abuela "Ella está allí, detrás de esa pared."
    abuela "Debe estar barriendo el piso."
    abuela "Siempre mueve todo los muebles cuando lo hace."
    abuela "Lo digo porque la escuché recién."

    hijo "No, Mamá. Ella ya no se halla entre nosotros."
    hijo "Tu amiga estuvo muy enferma durante un tiempo."
    hijo "Por lo que la tuvieron que internar."
    hijo "Los médicos nos dijeron que hicieron todo lo que pudieron."
    hijo "Lamentablemente, no hubo caso."
    hijo "Como no tenía familiares cercanos, la fuimos a enterrar en un hermoso prado."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Lo observo suspirar."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Debe ser confuso, ¿no?"
    hijo "Acá estoy para vos."

    hide lucas
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela confused "¿Falleció?"
    pensamientoabuela "¿En serio?"
    pensamientoabuela "¿Cuándo pasó eso?"
    pensamientoabuela "¿Hace mucho?"

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela normal "Escucho las llaves sonar, seguro que es ella."

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Mamá, hola. El tráfico estaba terrible. No pude llegar más rápido."
    abuela happy "Amiga. Te estaba esperando. Él está cocinando. Siéntate en tu silla favorita."
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "¿Por qué mi Amiga me observa de esa manera?"
    pensamientoabuela confused "¿Cuál es el motivo por el cual sus ojos se llenan de lágrimas?"
    pensamientoabuela "¿Por qué parece frustrada?"
    pensamientoabuela "¿Hice algo mal?"

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "¿Cómo? ¿Cómo que amiga? Yo soy tu hija."
    hija angry "¿Cómo no te acordás de mí?"
    hijo "Entiendo que estés agotada por el trabajo, hermana."
    hijo "Puedo comprender que toda esta situación te duela."
    hijo "Pero vos sabés que ella no lo hace a propósito."
    hijo "Te pediría que vayas a tomar algo de aire al balcón."
    hijo "Por favor."
    hija normal "No, estoy bien. Ya me relajé."
    hija "Mamá."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "La observo desconcertada por el intercambio de palabras que acabo de ver."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Los chicos vendrán una vez que salgan del colegio y de la facultad."
    abuela "¿Cuándo... tuviste hijos, Amiga? No me avisaste."
    hija angry "Yo no soy tu amiga. ¿Cuántas veces más te lo tengo que decir?"
    hija "Soy tu hija."
    hija "Y desde hace 26 años tengo una hija."
    hija normal "¿No te podés acordar?"

    hide hija
    with dissolve

    hide lucas
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "La observo."

    play sound "audio/grandma breathing sfx.mp3"

    pensamientoabuela "Siento latir a mi corazón."
    pensamientoabuela "No entiendo."
    pensamientoabuela "El aire se empieza a escapar de mis pulmones."
    pensamientoabuela confused "¿Recordar?"
    pensamientoabuela "¿Qué cosa exactamente?"
    pensamientoabuela "¿Por qué me cuesta respirar?"

    jump Story1

label Lie:

    #0 es caja de diálogo normal.
    $ text_box = 0

    show ester normal

    hijo @ happy "Que bueno."
    hijo "¿Pudiste descansar bien?"
    hijo "Te puedo preparar el almuerzo, si querés."
    abuela "No gracias, yo lo hago."

    hide lucas
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Mis pies se dirigen a la cocina."
    pensamientoabuela "¿Quedaba por acá?"
    pensamientoabuela "Sí, puede ser."
    pensamientoabuela @ confused "O, quizás... no sé."
    pensamientoabuela "En fin, mi marido debería estar por llegar."
    pensamientoabuela "Le debería cocinar algo."
    pensamientoabuela "¿Qué le gustaba al Viejo?"
    pensamientoabuela "Fideos, arroz, esa pasta amarilla. ¿Cómo se llamaba?"
    pensamientoabuela "Bah. Le haré eso mismo."

    scene cocina
    with fade

    show ester normal at left_1
    with dissolve

    show lucas normal at right_1
    with dissolve

    play sound "audio/cooking sfx.mp3"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¿Segura?"
    hijo "Mamá, ¿no recordás dónde dejaste los huevos?"
    abuela "¿Cómo no me voy a acordar?"
    abuela "Están en la heladera."
    hijo "¿Y por qué está buscando en la alacena?"
    abuela "Ah. Mi mente, no te preocupes."

    play sound "audio/keys opening door sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Escucho las llaves sonar, seguro que es el Viejo."
    pensamientoabuela "Habrá vuelto del viaje."
    pensamientoabuela "Estuvo seis meses afuera."
    pensamientoabuela "En el océano."
    pensamientoabuela "Donde la vida y la muerte conviven constantemente."
    pensamientoabuela "Espero que esté bien."

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Mamá, hola. El tráfico estaba terrible. No pude llegar más rápido."
    abuela "Viejo. ¡Tanto tiempo!"
    abuela "Te estoy preparando el almuerzo."
    hija "¿El Viejo?" 
    hija "Me parece que te equivocaste."
    hija "¿Me veo como él?"
    abuela confused "Eh... ¿no?"
    hija "¿No recuerdas que partió hace años?"
    abuela "¿A dón-?"
    hija "A las Bahamas. Falleció en alta mar."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Cómo?"
    pensamientoabuela "¿Falleció?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "En fin, te espero en el salón para cuando decidas recordarme."
    hijo @ angry "¡Hermana!"

    hide lucas
    with dissolve

    hide hija
    with dissolve

    show ester normal at left_1
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los observo moverse por el espacio."
    pensamientoabuela "Se van."
    pensamientoabuela "No tiene sentido lo que dice."
    pensamientoabuela confused "¿No era ese mi marido?"
    pensamientoabuela "¿Mi propio marido dijo que se murió?"
    pensamientoabuela "¿Es un fantasma?"
    pensamientoabuela "Qué miedo."
    pensamientoabuela normal "Menos mal que soy cristiana."
    pensamientoabuela "Me voy al salón que me duelen las piernas."

    play sound "audio/footsteps sfx.mp3"

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¡Ay! ¿En qué momento llegaste, hijo?"
    abuela "¿No estabas en el trabajo?"

    show lucas normal at right
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Y ahora por qué mi hijo me mira desconcertado?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "No, estaba acá. En el salón, hablando algunas cosas con mi hermana."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Observo a mi... ¿marido? revolear los ojos."
    pensamientoabuela "¿Qué bicho le picó ahora?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Estábamos esperando a que termines de cocinar."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Cocinar."
    pensamientoabuela confused "¿Estaba cocinando?"
    pensamientoabuela "¿Qué estaba haciendo?"
    pensamientoabuela "¿Habrá sido algo importante?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela normal "Sí, sí. Ahora les traigo la comida."

    scene pasillo
    with fade

    show ester normal at left_1
    with dissolve
    
    play sound "audio/footsteps sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela confused "¿Dónde quedaba la cocina?"
    pensamientoabuela "¿Era por acá?"
    pensamientoabuela "¿Qué decía mi hijo?"
    pensamientoabuela normal "Carteles. ¡Eso!"
    pensamientoabuela "Que mire los papelitos que me dejaba."
    pensamientoabuela "Me recuerda las cartas que me mandaba el Viejo."

    scene pared_con_papelitos
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "A ver, este papel dice: Cocina."

    play sound "audio/footsteps sfx.mp3"

    scene cocina
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Supongo que será acá."
    pensamientoabuela "Bueno, ¿y ahora?"
    pensamientoabuela "¿Qué le gustaba al Viejo?"
    pensamientoabuela "Fideos, arroz, esa pasta amarilla. ¿Cómo se llamaba?"
    pensamientoabuela "Bah. Le haré eso mismo."
    pensamientoabuela "Agarro el paquete verde."
    pensamientoabuela "¿Esto venía con instrucciones?"
    pensamientoabuela "Mejor me fijo en el libro de recetas."
    pensamientoabuela "Me pongo los lentes..."
    pensamientoabuela @ confused "¿Dónde estaban?"
    pensamientoabuela "Ah, acá."

    scene receta
    with fade

    show ester normal at left_1
    with dissolve
    
    play sound "audio/cooking sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "...Hervir 570 ml de agua y agregar una cucharada sopera de aceite de girasol."
    pensamientoabuela "Bien. ¿Qué sigue?"
    pensamientoabuela "...Retirar la olla del fuego y añadir 180 ml de leche descremada fría."
    pensamientoabuela "¿Leche descremada? Qué raro."
    pensamientoabuela "¿Qué más?" 
    pensamientoabuela "...Verter el contenido del sobre de una sola vez y dejar reposar un minuto."
    pensamientoabuela "¿Y...? Terminó la receta."
    pensamientoabuela "Supongo que ahora quedará esperar."

    scene cocina
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Había un poema que escribí, que se lo dediqué a mi amado."
    pensamientoabuela happy "Tu imagen, en mis luceros se ha quedado."
    pensamientoabuela "La última vez que te vi, antes de que partieras, "
    pensamientoabuela "tus dedos se extendían para alcanzarme."
    pensamientoabuela "Tal como el agua que nos rodeaba, tu voz se despedía."
    pensamientoabuela "Y mi alma, había quedado ardiendo."
    pensamientoabuela "En fuego, quemando..."
    pensamientoabuela confused "¿Qué es ese olor?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¡Se quemó la comida!"

    show lucas normal at right
    with dissolve

    hijo "Tranquila mamá, no pasa nada."
    hijo @ happy "Vamos a arreglarlo, juntos. ¿Te parece?"
    abuela normal "¿Qué me estará pasando hoy?"
    abuela "Esto no me solía suceder."
    hijo "Lo que importa en verdad es que estamos todos bien."
    hijo "Son cosas que le pueden pasar a cualquiera."

    jump Story2

label Story1:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    play sound "audio/keys opening door sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "De repente, escucho un sonido."
    pensamientoabuela "Es el ruido de la puerta nuevamente."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "Abuela. Tanto tiempo."

    show yamila normal at right_2
    with dissolve

    nietadelmediodelhijo "Abue. Hoy mi día fue tan tedioso."

    show santino normal at right_3
    with dissolve

    nietomenordelhijo "Estos dos son unos aburridos."
    nietomenordelhijo @ happy "Al menos yo me divertí en clase."

    hide facundo
    with dissolve

    hide yamila
    with dissolve

    hide santino
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Son... demasiadas personas."
    pensamientoabuela "¿Debería preguntarles algo?"

    jump Story12


label Story2:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Después de haber comido el almuerzo con mi hijo, y mi... ¿marido?."

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela "Escucho el ruido de la puerta."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "Abuela. Tanto tiempo."

    show yamila normal at right_2
    with dissolve

    nietadelmediodelhijo "Abue. Hoy mi día fue tan tedioso."
    nietadelmediodelhijo "Se ve que comieron sin nosotros."

    show santino normal at right_3
    with dissolve

    nietomenordelhijo "Estos dos son unos aburridos."
    nietomenordelhijo "Al menos yo me divertí en clase."

    hide facundo
    with dissolve

    hide yamila
    with dissolve

    hide santino
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Son... demasiadas personas."
    pensamientoabuela "¿Debería preguntarles algo?"

    jump Story21

label Story12:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    show santino normal at right_3
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo happy "¡No sabes el día que tuvimos!"
    nietomenordelhijo normal "Los profesores nos dejaron sin recreo."
    nietomenordelhijo "Y todo porque dos compañeros se pelearon en plena lección."
    nietomenordelhijo "Lo peor de todo es que teníamos clase previa al examen."
    nietomenordelhijo "No pudimos repasar nada."

    show yamila normal at right_2
    with dissolve

    nietadelmediodelhijo "¿Les sacaron el receso?"
    nietadelmediodelhijo "Siempre les pasa algo a ustedes, son re quilomberos."
    nietadelmediodelhijo "Nosotros tuvimos taller de música. Re aburrido."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Ni siquiera me dieron tiempo de poder contestar."
    pensamientoabuela "Pareciera que me conocen desde hace mucho."
    pensamientoabuela @ confused "¿Será que es así?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo "A todo esto, ¿podemos ir a la plaza?"
    nietomenordelhijo "Hace mucho no vamos con la abuela."

    show lucas normal at right_1
    with dissolve

    hijo "No sé Santi. Es mejor que se quede en casa."

    show hija normal at left_3
    with dissolve

    hija "Lucas, no les dejás hacer nada."
    hija "El paseo le va a venir bien a mamá."
    hija "A ver si no se olvida de ellos también..."
    hijo @ angry "Luciana. Basta."
    hija @ happy "Vayan, chicos. Tienen mi permiso."
    hija "Me voy a quedar a hablar con su viejo."
    hijo "Agh. Pero tengan cuidado, ¿sí?."
    hijo "Si llega pasar algo o ven a alguien raro, por favor, llámenme."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No estoy entendiendo lo que sucede."
    pensamientoabuela @ confused "¿A dónde me quieren llevar?"

    scene realliving
    with fade

    show ester normal at left_1

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los niños se fueron ya. Los adultos se quedaron hablando."
    pensamientoabuela "Como si ni existiera en sus vidas."
    pensamientoabuela "Lo único que me queda es suspirar y seguir a los jóvenes."

    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Así que eso hago."

    scene calle
    with fade

    show ester normal at left_1
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los sigo por calles que nunca vi antes."
    pensamientoabuela "La gente me saluda. Yo sigo de largo."

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "No corran chicos."
    nietomayordelhijo "Recuerden que estoy con la abuela."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:
        pensamientoabuela "¿Debería dejar que este muchacho siga caminando a mi lado?"

        "Sí.":

            jump Yes

        "No.":

            jump No

label Story21:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    show santino normal at right_3
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo @ happy "¡No sabes el día que tuvimos!"
    nietomenordelhijo "Los profesores nos dejaron sin recreo."
    nietomenordelhijo "Y todo porque dos compañeros se pelearon en plena lección."
    nietomenordelhijo "Lo peor de todo es que teníamos clase previa al examen."
    nietomenordelhijo "No pudimos repasar nada."

    show yamila normal at right_2
    with dissolve

    nietadelmediodelhijo "¿Les sacaron el receso?"
    nietadelmediodelhijo "Siempre les pasa algo a ustedes, son re quilomberos."
    nietadelmediodelhijo "Nosotros tuvimos taller de música. Re aburrido."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Ni siquiera me dieron tiempo de poder contestar."
    pensamientoabuela "Pareciera que me conocen desde hace mucho."
    pensamientoabuela "¿Será que es así?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo "A todo esto, ¿podemos ir a la plaza?"
    nietomenordelhijo "Hace mucho no vamos con la abuela."

    show lucas normal at right_1
    with dissolve

    hijo "No sé Santi. Es mejor que se quede en casa."

    show hija normal at left_3
    with dissolve

    hija "Lucas, no les dejás hacer nada."
    hija "El paseo le va a venir bien a mamá."
    hija "A ver si no se olvida de ellos también..."
    hijo @ angry "Luciana. Basta."
    hija @ happy "Vayan, chicos. Tienen mi permiso."
    hija "Me voy a quedar a hablar con su viejo."
    hijo "Agh. Pero tengan cuidado, ¿sí?."
    hijo "Si llega pasar algo o ven a alguien raro, por favor, llámenme."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No estoy entendiendo lo que sucede."
    pensamientoabuela "¿A dónde me quieren llevar?"

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los niños se fueron ya. Los adultos se quedaron hablando."
    pensamientoabuela "Como si ni existiera en sus vidas."
    pensamientoabuela "Lo único que me queda es suspirar y seguir a los jóvenes."
    
    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Así que eso hago."

    scene calle
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Los sigo por calles que nunca vi antes."
    pensamientoabuela "La gente me saluda. Yo sigo de largo."

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "No corran chicos."
    nietomayordelhijo "Recuerden que estoy con la abuela."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:
        pensamientoabuela "¿Debería dejar que este muchacho siga caminando a mi lado?"

        "Sí.":

            jump Yes

        "No.":

            jump No

label Yes:

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Decido permitir que el joven me acompañe."

    scene plaza
    with fade

    show ester normal:
        xalign 0.0
        yalign 1.0
    with dissolve

    show facundo normal at right_1
    with dissolve

    play sound "audio/footsteps on grass sfx.mp3"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela @ happy "Gracias por llevarme afuera."
    abuela "No salía desde que mi amiga se mudó."
    abuela "Hace mucho que no hablamos."
    abuela "¿Estará bien?"
    abuela "Se veía molesta cuando me fui de la casa."
    nietomayordelhijo "¿Eran muy unidas ustedes?"
    abuela "Sí."
    abuela @ happy "Solíamos sentarnos en un banco a charlar."
    abuela "Y a ponernos al día."
    nietomayordelhijo @ happy "Ojalá tenga una amistad tan larga como la de ustedes."
    nietomayordelhijo "Con mis amigos discutimos por cualquier cosa."
    abuela @ happy "Siempre es bueno mantener amistades."
    abuela "Y más cuando uno pasa mucho tiempo solo."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "El muchacho se queda pensando."
    pensamientoabuela "No sé por qué todos esquivan el tema cuando nombro a mi amiga."

    scene banco
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Este banco me resulta familiar."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Me recuerdan a mis hijos."
    abuela "Les encantaba correr por esta plaza cuando eran chicos."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "El muchacho sigue sin decir nada."
    pensamientoabuela "Extraño, ¿no?"

    show santino normal at right_3
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo @ happy "¡Vení a jugar con nosotros, abuela!"

    show facundo normal at right_1
    with dissolve

    nietomayordelhijo "Es mejor que se quede sentada."
    nietomayordelhijo "Papá nos va a retar si le pasa algo."

    hide facundo
    with dissolve

    hide santino
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los chicos vuelven a correr."
    pensamientoabuela "Los observo jugar."
    pensamientoabuela "Parecen felices."

    scene black
    with fade

    scene realliving
    with fade

    show facundo normal at left_2:
        xzoom -1.0
    with dissolve

    show ester normal at left_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "¡Volvimos!"

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¿Está bien la abuela?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "Sí, papá."

    hide facundo
    with dissolve

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Te dije que no iba a pasar nada."
    abuela "¿El joven chico es tu hijo?"
    abuela "Me acompañó hasta la plaza."
    abuela @ happy "Muy educado."
    hija "Es tu nieto, mamá."
    hija @ angry "No sirvió de nada el paseo parece."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela confused "¿Por qué se enoja?"
    pensamientoabuela "¿Le hice algo malo?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo @ angry "No seas así, Luciana."
    hijo "A pesar de que no estaba tan de acuerdo al principio, ahora entiendo."
    hijo "Le ayuda a despejarse."
    hijo "A sentirse acompañada."
    abuela @ happy "Les agradezco lo que hicieron por mí."
    abuela "Pero me puedo cuidar sola."

    hija @ angry "Bah. A ver si sirve esto."

    scene tv
    with fade

    show ester normal at left_1
    with dissolve
    
    show hija normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Mirá."
    hija "¿Te acordás?"
    hija happy "Somos todos nosotros en la playa."
    hija "Era el día de tu cumpleaños."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Conozco esa playa."

    play sound "audio/children laughing sfx.mp3"

    pensamientoabuela @ happy "Conozco esas risas."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve

    show hija normal at center
    with dissolve
    
    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "No le muestres eso, tía."
    nietomayordelhijo "La vas a confundir más."

    hija @ angry "No te metas, Facundo."

    show yamila normal at right_2
    with dissolve

    nietadelmediodelhijo "Basta, tía."
    nietadelmediodelhijo "Ya entendimos que no confiás en nosotros."

    hide yamila normal
    with dissolve

    hide facundo
    with dissolve

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Luciana."
    hijo "Escuchá a tus sobrinos."
    hijo "Así no la vas a ayudar."

    hija "Estoy tratando de que se acuerde de nosotros."
    hija "¿Por qué nadie me ayuda?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:

        pensamientoabuela "Las voces vuelven a subir de tono."

        "Voy a intentar calmar las aguas.":
            jump Intervene

        "Preferiría no meterme.":
            jump DoNotIntervene

label Intervene:
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Otra vez mis chicos pelean."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Ya fue suficiente."
    abuela angry "No paro de escucharlos discutir."
    abuela "Siempre es lo mismo."
    abuela "Parece que volvieran a tener diez años."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "La casa, de repente, quedó en silencio."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¿Mamá?"

    hija "¿Te acordás de nosotros?"
    abuela "Estoy cansada de que discutan por todo."
    abuela "Vayan a su cuarto los dos."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "Por fin, un poco de paz."

    jump Capitulo3_Casa

label DoNotIntervene:

    #0 es caja de diálogo normal.
    $ text_box = 0
    
    hijo angry "¿No te quedó claro que no se va a acordar de nosotros?"
    hijo "Ya nos dijo el médico que no debemos forzarla."
    hijo "La puede estresar más."

    hija @ sad "Yo solo quiero que nos recuerde."

    hide hija 
    with dissolve
    
    play sound "audio/running around sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Observo el modo en el que la mujer se va al balcón de manera precipitada."

    pensamientoabuela "Miro ahora al hombre que tengo en frente."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¿Por qué discuten tanto, Luqui?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Todos súbitamente se quedaron inmóviles."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Hace muchísimo tiempo que no me decías así, mamá."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Dije algo raro?"

    scene ventana
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Noto cómo el hombre sale a buscar a la mujer."

    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Me aproximo a la ventana que da al balcón para oír su conversación."

    #0 es caja de diálogo normal.
    $ text_box = 0
    
    hijo "Lu."
    hijo @ happy "Mamá me acaba de decir Luqui."
    hija "¿Qué?"
    hija "Hace muchísimo que no te llamaba así."
    hijo "¿Viste?"
    hijo "Todavía recuerda algunas cosas."
    hija @ happy "Tal vez tengas razón."
    hijo "No sirve de nada discutir."
    hijo "Vení, vamos adentro."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    play sound "audio/footsteps sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Me alejo del balcón."
    pensamientoabuela "No entiendo el motivo por el que actúan así."

    jump Capitulo3_Casa

label No:

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No necesito que me acompañen."

    nietomayordelhijo "¿Te ayudo, abuela?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Otra vez me dijo abuela."
    pensamientoabuela @ confused "¿Tengo nietos?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "No, jovencito."
    abuela "Te agradezco, pero puedo cuidarme sola."
    nietomayordelhijo "Pero te acompaño hasta la plaza."
    abuela "No hace falta."
    abuela "Puedo sola."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "El muchacho parece dudar."
    pensamientoabuela "Pero termina alejándose."

    hide facundo
    with dissolve

    scene calle
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Estoy caminando hace un rato ya."
    pensamientoabuela confused "¿Tan lejos estaba la plaza?"
    pensamientoabuela "No me suena este barrio."
    pensamientoabuela "Las calles no están donde las recuerdo."
    pensamientoabuela "¿Me habré equivocado?"

    show cachito normal at right_1
    with dissolve

    pensamientoabuela normal "Alguien se acerca."
    pensamientoabuela "Otra cara que no conozco."
    pensamientoabuela "¿Me podrá ayudar?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    cachito "¿Necesita ayuda, doña?"
    abuela "No gracias, joven."
    abuela "Estoy de camino a la plaza."
    cachito "¿La plaza?"
    cachito "Por acá no hay ninguna."
    cachito "¿Quiere que la acompañe?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:

        pensamientoabuela "¿Debería confiar en él?"

        "Aceptar su ayuda.":
            jump CachitoYes

        "Seguir sola.":
            jump CachitoNo

label CachitoYes:

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Bueno."
    cachito "¿Por dónde vive?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Dónde vivo?"
    pensamientoabuela "¿Cómo era mi casa?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Por Sarmiento."
    abuela "Una casa con rejas celestes."
    cachito @ happy "Tranquila."
    cachito "La vamos a encontrar."

    scene frente_de_casa
    with fade

    show ester normal at left_1
    with dissolve

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¡Ahí está mamá!"

    show hija normal at right_2
    with dissolve

    hija "Por fin apareció."
    hija "¿Y vos quién sos?"

    show cachito normal at left_3:
        xzoom -1.0
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    cachito "La encontré caminando sola."
    cachito "Parecía perdida."
    abuela @ happy "Muchas gracias por acompañarme, buen hombre."

    hijo @ happy "De verdad, muchísimas gracias."
    hijo "Estábamos muy preocupados."
    cachito @ happy "No hacía falta agradecer."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Todos parecen más tranquilos."

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Ay mamá."
    hija @ happy "Gracias a Dios estás bien."

    jump Capitulo3_Perdida

label CachitoNo:

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Gracias."
    abuela "Pero puedo cuidarme sola."

    hide cachito
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Prosigo con mi camino."

    scene calle
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Sigo sin reconocer nada."

    show policia at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    policia "¿Ester?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Cómo sabe mi nombre?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    policia "Su familia la está buscando."

    scene frente_de_casa
    with fade

    show ester normal at left_1
    with dissolve

    show policia at left_3:
        xzoom -1.0
    with dissolve

    show hija normal at right_2
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Mamá."

    show lucas normal at right_1
    with dissolve

    hijo "Gracias, Oficial."

    #0 es caja de diálogo normal.
    $ text_box = 0

    policia "Por su seguridad les recomendamos que no salga sola."
    policia "También sería importante que lleve alguna identificación."
    policia "Y reforzar las medidas de acompañamiento."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "Gracias a Dios estás bien."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No entiendo por qué todos estaban tan preocupados."

    jump Capitulo3_Perdida

label Capitulo3_Casa:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"

    scene realliving
    with fade
    
    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "La casa se siente distinta cuando todos hablan al mismo tiempo."
    pensamientoabuela "A veces pienso que están contentos."
    pensamientoabuela "Otras veces, que están por pelearse otra vez." 

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Mamá... ¿estás cansada?"
    abuela "Un poco."
    abuela "Pero el aire de la plaza me hizo bien."

    show hija normal at center
    with dissolve

    hija "Te dije que salir un rato le iba a hacer bien."
    hijo "Sí, bueno."
    hijo "Capaz esta vez sí."
    hija "Mamá."
    hija "Perdón por cómo te hablé antes."
    hija "A veces me gana la desesperación."

    abuela @ confused "¿Desesperación por qué, querida?"
    hija "Porque..."
    hija sad "Porque siento que te perdemos un poquito más cada día."

    play sound "audio/luciana crying sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Tiene la misma cara que cuando era chica y rompía algo sin querer."
    pensamientoabuela "Esa mezcla de culpa y tristeza."
    pensamientoabuela @ confused "¿Será mi hija de verdad?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela @ happy "No llores, hija."
    abuela "No me gusta cuando lloran en esta casa."
    hija normal "Perdón, mamá."
    hijo "Bueno, ya está."
    hijo "Lo importante es que hoy salió todo bien."

    jump EntradaAmbar

label Capitulo3_Perdida:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija @ angry "Mamá, no podés volver a hacer algo así."
    abuela "¿Algo como qué?"
    abuela "Solo estaba caminando."

    show lucas normal at right_1
    with dissolve

    hijo "Mamá."
    hijo "Te perdimos por dos horas."
    hija angry "¡Dos horas!"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela confused "¿Dos horas?"
    pensamientoabuela "No puede ser."
    pensamientoabuela "Para mí fue apenas un ratito."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela normal "No exageren."
    abuela "Yo sabía lo que hacía."
    hija "¡No!"
    hija "Ni siquiera sabías volver a casa."
    hijo "Luciana, basta."
    hija "¿Cómo que basta?"
    hija "¿No entendés la gravedad de esto?"
    hija "Hoy apareció."
    hija "Mañana capaz no."
    hijo "Ya entendí."
    hijo "Pero no grites."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Me están mirando."
    pensamientoabuela "Pero siento que hablan de otra persona."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "No hablen como si yo no estuviera acá."
    hija "¿Y cuándo sería momento de hablar?"
    hija "¿Cuando no reconozca más a ninguno?"

    hijo @ angry "No digas eso."
    hija "¡Hay que internarla, Lucas!"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela confused "¿Internarme?"
    pensamientoabuela "¿A mí?"
    pensamientoabuela "¿Por qué quieren hacerme esto?"
    pensamientoabuela "¿Qué les pasa?"

    abuela "¿Internar a quién?"

    jump EntradaAmbar

label EntradaAmbar:

    scene realliving
    with fade

    show ester normal at left_1

    play sound "audio/doorbell sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Escucho el timbre."

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "Voy."

    hide facundo
    with dissolve

    play sound "audio/keys opening door sfx.mp3"
    
    show ambar normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa @ happy "Buenas noches, familia."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Esa mujer."
    pensamientoabuela "Me resulta familiar."

    #0 es caja de diálogo normal.
    $ text_box = 0

    show ambar normal at center:
        xzoom -1.0

    esposa "¿Llegué en mal momento?"

    show hija normal at right_2
    with dissolve

    hija "No."
    hija "Bueno, más o menos."

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Llegaste justo."

    show ambar normal at center:
        xzoom 1.0

    esposa @ happy "Hola, Ester."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No. Me habré confundido."
    pensamientoabuela "No recuerdo quién es."
    pensamientoabuela @ happy "Pero, me transmite calma."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Hola..."

    show ambar normal at center:
        xzoom -1.0

    esposa "Lucas."
    esposa "Luciana."
    esposa "¿Por qué no van a hablar tranquilos a otro lado?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Sí."

    hija "Dale."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    play sound "audio/footsteps sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Los veo alejarse."

    show ambar normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Chicos."
    esposa "¿Por qué no van a jugar un rato?"

    play sound "audio/footsteps sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Distingo a los chicos irse de igual modo."
    pensamientoabuela "Sin realizar queja alguna."
    pensamientoabuela "Sorprendente."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Ester..."
    esposa "¿Querés ayudarme con la cena?"
    abuela "¿Quién sos?"
    esposa @ happy "Una vieja amiga."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Vieja amiga."
    pensamientoabuela "Me guiñó el ojo."
    pensamientoabuela "Tal vez, pueda serlo."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Bueno."
    abuela "Quedarme quieta me pone nerviosa."

    jump CocinaAmbar

label CocinaAmbar:

    scene cocina
    with fade

    show ester normal at left_1
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Esta cocina sí la conozco."

    show ambar normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Ester."
    esposa "¿Los cubiertos dónde están?"
    abuela "En este cajón."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Abro el cajón."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Ese no."
    esposa "El de más abajo."
    abuela "Ah."
    abuela "Ya sabía."
    esposa "Sí."
    esposa "Ya sé."
    esposa "A todos nos pasa."
    abuela "Sos buena para mentir sin que se note."
    esposa @ happy "Y vos siempre fuiste buena para darte cuenta."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Esa frase la conozco."
    pensamientoabuela "La escuché antes."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¿Te acordás cuando nos quedábamos hablando?"
    esposa "Mientras los chicos corrían por toda la casa."
    abuela "Lucas siempre corría con medias."
    abuela "Se resbalaba y lloraba."
    esposa "Sí."
    esposa "¿Y Luciana se enojaba porque tocaba sus cosas?"
    abuela "Sí."
    abuela "Tiene carácter fuerte."
    esposa @ happy "Pero te quiere mucho."
    abuela "Ya lo sé."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Cuando me mira apretando la boca."
    pensamientoabuela "Me doy cuenta."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Está cansada."
    esposa "No enojada con vos."
    esposa "A veces la tristeza sale como enojo."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Tristeza..."
    pensamientoabuela "Eso sí lo entiendo."
    pensamientoabuela "Hay días en que siento que me falta algo."
    pensamientoabuela "Aunque no sepa qué."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¿Querés cortar el pan?"
    abuela "Sí."
    esposa "Dale."
    esposa "Con cuidado."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Lo estoy haciendo demasiado lento?"
    pensamientoabuela "No lo sé."
    pensamientoabuela "Luego de un tiempo, termino de cortar."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Ahí está."
    esposa happy "¡Qué perfección, Ester!"
    esposa "Estás para abrir una panadería."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela @ happy "Me hace reír."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa normal "Bueno."
    esposa "Vamos a llevar la comida."
    abuela "Dale."

    jump CenaFamiliar

label CenaFamiliar:

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Todos vuelven a sentarse juntos."

    show santino normal at right_3
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomenordelhijo "¿Puedo servirle agua a la abuela?"

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0
    
    hijo "Sí."
    hijo "Despacio."
    abuela happy "Gracias, querido."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Qué amable es este chico."
    pensamientoabuela normal "Hay un silencio extraño."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hide santino
    with dissolve

    hijo "Mamá..."
    hijo "Queríamos hablar con vos de algo importante."

    show hija normal at center
    with dissolve

    hija "Lucas."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Estará mal cortado el pan?"
    pensamientoabuela "Todos tienen caras raras."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Tenés derecho a saberlo."
    abuela "Me están asustando."
    abuela "Decilo de una vez."
    hijo "Creemos que sería bueno que hables con una profesional."
    hijo "Una psicóloga."
    hijo "O una psiquiatra."
    hijo "Alguien que pueda ayudarte a entender mejor lo que te está pasando."
    hija @ happy "Y que nos ayude a nosotros a acompañarte."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Ayuda."
    pensamientoabuela "Otra vez esa palabra."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¿Estoy tan mal?"
    hijo "No se trata de eso."
    hijo "Se trata de que no estés sola."
    hija "Y de no esperar a que pase algo peor."

    show ambar normal at right_2B
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Nadie te está castigando, Ester."
    esposa "Solo quieren cuidarte."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Cuidarme..."
    pensamientoabuela "Antes era yo quien cuidaba a todos."

    menu:

        pensamientoabuela "¿Debería aceptar?"

        "Aceptar la ayuda.":
            jump Cap3Aceptar

        "Negarme.":
            jump Cap3Negar

label Cap3Aceptar:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "No me gusta la idea."
    abuela "Pero menos me gusta verlos así."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Observo el modo en el que el hombre baja la mirada."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Si de verdad creen que me va a hacer bien..."
    abuela "Voy a ir."

    hija "¿En serio?"
    abuela "Sí."
    abuela @ angry "Pero no me hablen como si ya no entendiera nada."

    hijo "Nunca haríamos eso."
    hija @ happy "Gracias, mamá."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Entonces mañana vemos cómo organizarlo."

    hijo "Vamos a ir con vos."
    abuela "Bueno."
    abuela "Pero ahora quiero dormir."

    hide lucas
    with dissolve

    hide ambar
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "¿Querés que te acompañe al cuarto?"
    abuela "Sí."
    abuela "Vení."

    jump Capitulo4

label Cap3Negar:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"
    
    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "No."
    abuela "No voy a ir a ningún lado."

    hijo "Mamá..."
    abuela angry "¡No!"
    abuela "Ya escuché demasiado por hoy."

    hija "No es un ataque."
    abuela "Entonces dejá de mirarme como si estuviera mal."
    hija "Nadie piensa eso."
    abuela "Vos sí."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "La veo bajar la mirada."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Mamá."
    hijo "Por favor."
    abuela "¡No me digas que me tranquilice!"
    abuela "¡Estoy en mi casa!"

    play sound "audio/grandma breathing sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "El pecho me aprieta."
    pensamientoabuela confused "Las voces se mezclan."
    pensamientoabuela "Ya no entiendo quién está hablando."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija @ angry "Mamá, sentate."
    abuela angry "¡No me toques!"

    hide hija
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    show ambar:
        xzoom -1.0 

    esposa "Lucas."
    esposa "Traé agua."

    hijo "Ya voy."

    hide lucas
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    show ambar:
        xzoom 1.0 

    esposa "Ester."
    esposa "Mirame."
    esposa "Nadie te va a sacar de tu casa."
    esposa "Respirá conmigo."

    play sound "audio/breathing sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela normal "Intento hacerlo."

    play sound "audio/grandma breathing sfx.mp3"

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "No vamos a seguir discutiendo ahora."
    hijo "Pero tenemos que buscar ayuda profesional."

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija sad "Aunque te enojes con nosotros."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Su voz se quiebra."
    pensamientoabuela "Quisiera consolarla."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Basta por hoy."
    esposa "Ester necesita descansar."
    abuela "Quiero irme a dormir."
    abuela "Sola."
    esposa "Te acompaño hasta la puerta."

    hide lucas
    with dissolve

    hide hija
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Me está costando levantarme."

    jump Capitulo4

label Capitulo4:

    scene black
    with fade

    show ester normal at left_1

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Ya es mañana."

    scene sala_de_espera
    with fade

    show ester normal at left_1
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Y este lugar huele a nuevo."
    pensamientoabuela "¿Por qué me trajeron acá?"
    pensamientoabuela "Todos me miran como si fuera a romperme."

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "Viste mamá, está lindo el lugar."
    abuela "No me gustan los hospitales así."

    show hija normal at center
    with dissolve

    hija "No es un hospital, es un centro de ayuda."
    abuela "Es lo mismo."

    hide lucas
    with dissolve

    hide hija with dissolve
    
    show ambar normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Bueno, el propósito es que te sientas más cómoda."

    scene sala_de_espera
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Escucho que llaman mi nombre."
    pensamientoabuela "Distingo el modo en el que todos se levantan."

    scene psicologo
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Entramos a una oficina tranquila."

    show psicologa normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "¿Son ustedes los familiares de Ester?"

    show lucas normal at left_3:
        xzoom -1.0
    with dissolve

    hijo "Así es."
    doc "Muy bien, entonces, les pido amablemente que se retiren."
    doc "Me gustaría hablar a solas con Ester."

    hide lucas
    with dissolve
    
    play sound "audio/closed door sfx.mp3"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Observo el modo en el que se van de la sala."

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "Hola Ester, ¿cómo llegó hasta acá?"
    abuela "Me trajeron."

    show psicologa happy

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Observo a la mujer sonreír."

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc normal "¿Y usted quería venir?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:

        pensamientoabuela "¿Debería confiar en esta mujer?"

        "Confiar.":
            jump Cap4Confiar

        "Mantener distancia.":
            jump Cap4NoConfiar

label Cap4Confiar:

    $ confio_doctora = True

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "La verdad que no."
    abuela "Pero entiendo que mi situación no mejora con el tiempo."
    abuela "Veo a mucha gente pero no recuerdo a nadie."
    abuela "Me visitan constantemente pero me siento sola."
    doc "¿Y cómo le cae eso?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Me quedo en silencio un tiempo."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Mal."
    abuela "Me cae muy mal."
    doc "Tiene sentido que le caiga mal."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No me dijo que no me preocupara."
    pensamientoabuela "Solo dijo que tiene sentido."
    pensamientoabuela "Hace cuánto no me decían eso."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Todos en casa me hablan como si fuera de vidrio."
    doc "¿Y cómo preferiría que le hablen?"
    abuela "Como siempre."
    abuela "Como cuando yo era la que resolvía las cosas."
    doc "¿Qué tipo de cosas resolvía?"
    abuela "Todo."
    abuela "Los líos de mis hijos."
    abuela "La casa."
    abuela "Las peleas."
    doc "¿Y ahora siente que le sacaron ese lugar?"

    scene focos_manos
    with fade

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Miro mis manos."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "A veces siento que me observan y ven a otra persona."
    abuela "Una que necesita ayuda para todo."
    doc "¿Y usted qué ve cuando se mira?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Qué pregunta difícil."
    pensamientoabuela "A veces la misma de siempre."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Depende del día."
    doc "Eso es muy honesto, Ester."
    doc "¿Le gustaría volver la semana que viene?"

    scene psicologo
    with fade

    show ester normal at left_1

    show psicologa normal at right_1
    with dissolve

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No sé si quiero."
    pensamientoabuela "Pero tampoco me disgustó."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Puede ser."
    abuela "Veremos."

    jump Cap4Conexion

label Cap4NoConfiar:

    $ confio_doctora = False

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Me trajeron."
    abuela "Vine para que se quedaran tranquilos."
    doc "Entiendo."
    doc "¿Y usted está tranquila?"
    abuela "Estoy bien."
    doc "¿Qué es estar bien para usted?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Qué pregunta rara."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Estar en mi casa."
    abuela "Con mi gente."
    doc "¿Y acá no se siente así?"
    abuela "Acá no conozco a nadie."
    doc "Es la primera vez que nos vemos."

    scene cuadro_del_psicologo
    with fade

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Miro un cuadro."

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "¿Qué está mirando?"
    abuela "Esa pintura."
    abuela "Mi hijo tiene uno parecido."
    doc "¿Cómo se llama su hijo?"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Lo sé."
    pensamientoabuela "Lo sé perfectamente."
    pensamientoabuela "¿Por qué no me sale?"

    scene psicologo
    with fade

    show ester normal at left_1
    with dissolve

    show psicologa normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Eso no le importa a usted."
    doc "Tiene razón."
    doc "Perdón."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Esperaba que insistiera."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Lucas."
    abuela "Se llama Lucas."
    doc "¿Y cómo es Lucas?"
    abuela "Cabeza dura."
    abuela @ happy "Pero buen chico."
    doc "¿Se parece a usted?"
    abuela "En cabeza dura, sí."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No le voy a contar nada importante."
    pensamientoabuela "Pero tampoco me lo está exigiendo."
    pensamientoabuela "Qué extraña esta mujer."

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc @ happy "Ester, gracias por venir."
    doc "La puerta queda abierta si algún día quiere volver."
    abuela "Ya veremos."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿La puerta queda abierta?"
    pensamientoabuela "Nadie me había dicho eso en mucho tiempo."

    jump Cap4Conexion

label Cap4Conexion:

    scene sala_de_espera
    with fade

    show ester normal at left_1
    with dissolve

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "¿Cómo te fue? ¿Qué te dijo? ¿Estuvo bien?"
    abuela "No me apures, por favor."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Miro el modo en el que aquella señora sale de la oficina."
    pensamientoabuela "Y la forma en la que ambos adultos se apresuran hacia ella."

    show ambar normal at right_2

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¿Cómo estás?"
    abuela "Fatigada."
    abuela "Hablar cansa."
    esposa "Sí."
    esposa @ happy "Pero lo hiciste igual."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Sí."
    pensamientoabuela "Lo hice igual."

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve

    show hija normal at center
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "¿Querés tomar algo, mamá?"
    abuela "Un té está bien."

    hide hija
    with dissolve

    show lucas normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "¿No querés descansar?"
    abuela "Primero el té."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No me pregunta nada."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¿No querés saber cómo me fue?"
    hijo "Solo si vos querés contarme."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Ahí está."
    pensamientoabuela "Aprendió algo."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela @ happy "Fue bien."
    abuela "La doctora es rara."
    abuela @ happy "Pero no molesta."
    hijo "Algo es algo."

    scene black
    with fade

    show ester normal at left_1

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Sentí la manera en la que el tiempo pasó."

    scene psicologo
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Los chicos me consultan cosas que sé responder."
    pensamientoabuela "No sé si lo hacen a propósito."
    pensamientoabuela @ happy "Pero me gusta."
    pensamientoabuela "Además, el cuadro de la oficina ya lo conozco."
    pensamientoabuela "La señora de recepción se llama Mirta."
    pensamientoabuela "Hoy no tuve que preguntar dónde sentarme."
    pensamientoabuela "Y vine acompañada, también."

    show hija normal at center
    with dissolve

    show lucas normal at left_2B:
        xzoom -1.0
    with dissolve

    show psicologa normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "Ester, estos últimos encuentros me ayudaron a entenderla mejor."
    doc "Y quiero ser honesta."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Cuando alguien dice eso."
    pensamientoabuela "Viene algo difícil de oír."

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "Lo que está atravesando necesita un acompañamiento más completo."
    doc "Junto con el médico que la atiende, queremos incorporar medicación."
    hija "¿De qué tipo?"
    doc "Medicamentos,"
    doc "que pueden ayudar a mantener algunas funciones cognitivas,"
    doc "durante más tiempo."
    doc "No son una cura."
    hijo "¿Tiene efectos secundarios?"
    doc "Como cualquier medicamento."
    doc "Por eso, vamos a empezar con una dosis baja."
    doc "Lo que facilitará controlar su respuesta ante ellos."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Una pastilla para el cerebro."
    pensamientoabuela "Como si fuera un reloj al que le faltara cuerda."
    pensamientoabuela confused "¿Y si no funciona?"
    pensamientoabuela "¿Y si sí funciona y me vuelvo otra?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela normal "¿Y si no quiero tomarla?"
    doc "Es su decisión."
    doc "Nadie la obliga, Ester."
    doc "Me gustaría saber qué es lo que le genera malestar de todo esto."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    menu:

        pensamientoabuela "¿Aceptar la medicación?"

        "Aceptar.":
            jump MedicacionSi

        "Pensarlo más.":
            jump MedicacionNo

label MedicacionSi:

    $ acepta_medicacion = True

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Me da miedo no ser yo."
    doc "La medicación no busca cambiarla."
    doc "Busca ayudarla a seguir siendo usted durante más tiempo."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Quizás sí..."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Está bien."
    abuela "La voy a tomar."
    hija happy "Gracias, mamá."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No lo hice por ella."
    pensamientoabuela "Lo hice por mí."

    jump CentroMemoria

label MedicacionNo:

    $ acepta_medicacion = False

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Todavía no."
    abuela "Necesito pensarlo."

    doc "Muy bien."
    doc "No hay apuro."
    doc "Seguimos con las sesiones y cuando esté lista, se habla de nuevo."
    hija "Mamá..."
    hijo "Lu."
    hijo "Ya escuchaste a la doctora."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Lucas me defendió."
    pensamientoabuela "No me esperaba eso."

    jump CentroMemoria

label CentroMemoria:

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc "Hay algo más que me gustaría compartir."
    doc "Existe otro centro."
    doc "Al que me gustaría que Ester vaya algunas mañanas por semana."
    doc "Se llama Centro de Ayuda a la Memoria."
    hijo "¿Qué hacen ahí?"
    doc "Actividades grupales."
    doc "Talleres."
    doc "Ejercicios cognitivos."
    doc "No es una internación ni nada similar."
    doc "Es un espacio donde se puede estar con otras personas."
    doc "Las cuales están atravesando algo semejante."
    doc "Y donde se sigue estimulando la mente de manera activa."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "¿Otras personas como yo?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "¿Qué opinás, mamá?"
    abuela "¿Y qué talleres hay?"
    doc "De música, manualidades, lectura, cocina."
    doc "Depende del día."
    doc "Usted eligiría a cuál ir."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Cocina."
    pensamientoabuela @ happy "Eso sí sé hacerlo."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¿Puedo ir a mirar primero?"
    doc happy "Por supuesto."
    doc "De hecho, se lo recomiendo."

    scene pieza_ester
    with fade

    show ester normal at left_1
    with dissolve

    show ambar normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¿Cómo estás?"
    abuela "Pensando."
    esposa "¿En qué?"
    abuela "En si la gente de ese centro será buena."
    esposa "¿Y qué dice tu instinto?"
    abuela "Que vaya a ver."
    abuela "Y que si no me gusta, me vuelva."
    esposa "Eso siempre fue tuyo, Ester."
    esposa "Saber cuándo quedarte o irte."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Sí."
    pensamientoabuela "Eso todavía lo sé."
    pensamientoabuela "Quizás no todo se fue."
    pensamientoabuela "Observo a la mujer irse."

    scene pieza_ester_no_luz
    with fade

    play sound "audio/closed door sfx.mp3"

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Mañana voy a ver ese lugar."
    pensamientoabuela "Sola no. Pero voy."

    scene black
    with fade
    
    #2 es caja de diálogo de papel "moderno".
    $ text_box = 2

    "Ha pasado un año ya."

    if confio_doctora and acepta_medicacion:
        jump EpilogoBueno
    else:
        jump EpilogoMalo

label EpilogoBueno:

    scene realliving
    with fade

    show ester normal at left_1
    with dissolve
    
    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Todavía voy al centro de ayuda."
    pensamientoabuela "Y sigo viendo a la psiquiatra."
    pensamientoabuela @ happy "Hay días mejores."
    pensamientoabuela "Y otros más difíciles."

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "¡Buenas!"

    show hija normal at center
    with dissolve

    hija "Mamá, ¿cómo te sentís?"

    abuela "Bien."
    abuela "Creo que dormí bastante."

    show lucas normal at right_1
    with dissolve

    hijo "En un rato llega Ámbar con los chicos."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No siempre recuerdo quién viene."
    pensamientoabuela @ happy "Pero me gusta cuando la casa se llena."
    
    hide lucas
    with dissolve

    hide hija
    with dissolve

    show ambar normal at right_2
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¡Llegamos!"

    show santino normal at right_3
    with dissolve

    nietomenordelhijo @ happy "¡Hola, abuela!"

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Me siento tranquila."

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "¿Cómo estás, Ester?"
    abuela @ happy "Bien."
    abuela "Y con hambre."
    esposa @ happy "Perfecto."
    esposa "Porque justo trajimos algo para merendar."

    hide santino
    with dissolve

    show hija normal at center
    with dissolve

    hija "Vamos a la mesa."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "No recuerdo todo."
    pensamientoabuela "Probablemente nunca vuelva a hacerlo."
    pensamientoabuela @ happy "Pero ya no me siento sola."

    scene black
    with fade

    #2 es caja de diálogo final.
    $ text_box = 2

    "Fin."

    return

label EpilogoMalo:

    scene hospital
    with fade
    
    show psicologa normal:
        xalign 0.0
        yalign 1.0
        xzoom -1.0
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    doc @ happy "Ester, tiene visitas."
    doc "Pueden pasar."

    show lucas normal at right_1
    with dissolve

    hijo "Mamá."
    hijo "Somos nosotros."
    
    show hija sad at right_2
    with dissolve

    hija "Quizás ya no nos reconoce."
    hijo "Vinieron los chicos también."

    hide lucas
    with dissolve

    hide hija
    with dissolve

    show facundo normal at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    nietomayordelhijo "Abu."

    doc "Ester no habla con nadie desde hace días."

    hide facundo
    with dissolve
    
    show lucas normal at right_2
    with dissolve

    show hija sad at right_1
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    hija "No sé para qué seguimos viniendo."
    hijo "Porque sigue siendo nuestra mamá."
    
    show ambar normal at right_3
    with dissolve

    #0 es caja de diálogo normal.
    $ text_box = 0

    esposa "Es mejor dejarla descansar."
    esposa "Volvemos otro día."

    scene hospital
    with fade

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Esperen..."

    scene black
    with fade

    #2 es caja de diálogo final.
    $ text_box = 2

    "Con el tiempo, Ester perdió la capacidad de moverse."
    "Pasa su tiempo, acostada."
    "Lucas es el único que continúa visitándola una vez por semana."
    "El Alzheimer afecta a cada persona de manera diferente."
    "La detección temprana,"
    "el acompañamiento familiar y"
    "el tratamiento adecuado,"
    "pueden mejorar significativamente la calidad de vida de las personas."
    
    "Fin."

    return