define abuela = Character(_("Ester"), color="#7c039a")
define pensamientoabuela = Character(_("Pensamientos de Ester"), color="#7c039a")

define hijo = Character(_("Lucas"), color="#2b00ff")
define hija = Character(_("Luciana"), color="#fbfbfbc6")

define esposa = Character(_("Ámbar"), color="#fd0065ff")
define nietomayordelhijo = Character(_("Facundo"), color="#00ff0dff")
define nietadelmediodelhijo = Character(_("Yamila"), color="#ff00e6ff")
define nietomenordelhijo = Character(_("Santino"), color="#00d9ffff")

define cachito = Character(_("Cachito"), color="#000000ff")

define policia = Character(_("Policía"), color="#ef1c5bff")

define doc = Character(_("Psiquiatra"), color="#d7ec82ff")

default confio_doctora = False
default acepta_medicacion = False

default text_box = 0
image textbox = ConditionSwitch(
    "text_box == 0", Image("gui/textbox.png", xalign = 0.5, xfill = True, yalign = gui.textbox_yalign, ysize = gui.textbox_height),
    "text_box == 1", Image("gui/thoughtbubble.png", xalign = 0.5, xfill = True, yalign = gui.textbox_yalign, ysize = gui.textbox_height),
    )

label start:

    play music "initiumfinis(startline).mp3"

    scene realliving

    show nona_busto:
        xalign 0
        yalign 1.0
    
    $ text_box = 1

    pensamientoabuela "El día había arribado. El tiempo pasó, de la noche a la mañana."
    pensamientoabuela "Los escucho, corriendo por los pasillos de la casa."
    pensamientoabuela "Están riendo."
    pensamientoabuela "Sonrío."
    pensamientoabuela "Mis hijos, los quiero."
    pensamientoabuela "¿Puedo abrazarlos?"
    pensamientoabuela "¿Dónde están?"

    $ text_box = 0
    
    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá, ¿cómo te sentís?"

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
    hijo "Sabés que podés confiar en mí para lo que sea."

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1

    pensamientoabuela "Algo me dice que puedo creerle, pero prefiero quedarme callada."

    #0 es caja de diálogo normal.
    $ text_box = 0

    hijo "No te preocupes si no podés contarme ahora." 
    hijo "Voy a ir a preparar el almuerzo."
    hijo "Andá a sentarte que ya viene tu hija."

    scene ventana_no_sombras
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    #1 es caja de diálogo pero como pensamiento de Ester.
    $ text_box = 1
    
    pensamientoabuela "Miro a la ventana."
    pensamientoabuela "¿Hija?"
    pensamientoabuela "¿Tenía una?"
    pensamientoabuela "¿No será mi amiga?"
    pensamientoabuela "Amiga…"
    pensamientoabuela "¿Seguirá viviendo al lado?"

    #0 es caja de diálogo normal.
    $ text_box = 0

    abuela "Mi amiga."
    abuela "¿La podrías llamar para que venga a comer también, por favor?"

    scene realliving

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

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
    
    pensamientoabuela "Lo observo suspirar."

    hijo "Debe ser confuso, ¿no?"
    hijo "Acá estoy para vos."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "¿Falleció?"
    pensamientoabuela "¿En serio?"
    pensamientoabuela "¿Cuándo pasó eso?"
    pensamientoabuela "¿Hace mucho?"

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela "Escucho las llaves sonar, seguro que es ella."

    show hija at center
    with dissolve

    hija "Mamá, hola. El tráfico estaba terrible. No pude llegar más rápido."
    abuela "Amiga. Te estaba esperando. Él está cocinando. Siéntate en tu silla favorita."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "¿Por qué mi Amiga me observa de esa manera?"
    pensamientoabuela "¿Cuál es el motivo por el cual sus ojos se llenan de lágrimas?"
    pensamientoabuela "¿Por qué parece frustrada?"
    pensamientoabuela "¿Hice algo mal?"

    show personaje_placeholder_blury at right
    with dissolve

    show hija at center
    with dissolve

    hija "¿Cómo? ¿Cómo que amiga? Yo soy tu hija."
    hija "¿Cómo no te acordás de mí?"
    hijo "Entiendo que estés agotada por el trabajo, hermana."
    hijo "Puedo comprender que toda esta situación te duela."
    hijo "Pero vos sabés que ella no lo hace a propósito."
    hijo "Te pediría que vayas a tomar algo de aire al balcón."
    hijo "Por favor."
    hija "No, estoy bien. Ya me relajé."
    hija "Mamá."

    pensamientoabuela "La observo desconcertada por el intercambio de palabras que acabo de ver."

    hija "Los chicos vendrán una vez que salgan del colegio y de la facultad."
    abuela "¿Cuándo... tuviste hijos, Amiga? No me avisaste."
    hija "Yo no soy tu amiga. ¿Cuántas veces más te lo tengo que decir?"
    hija "Soy tu hija."
    hija "Y desde hace 26 años tengo una hija."
    hija "¿No te podés acordar?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "La observo."

    play sound "audio/grandma breathing sfx.mp3"

    pensamientoabuela "Siento latir a mi corazón."
    pensamientoabuela "No entiendo."
    pensamientoabuela "El aire se empieza a escapar de mis pulmones."
    pensamientoabuela "¿Recordar?"
    pensamientoabuela "¿Qué cosa exactamente?"
    pensamientoabuela "¿Por qué me cuesta respirar?"

    jump Story1

label Lie:

    hijo "Que bueno."
    hijo "¿Pudiste descansar bien?"
    hijo "Te puedo preparar el almuerzo, si querés."
    abuela "No gracias, yo lo hago."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Mis pies se dirigen a la cocina."
    pensamientoabuela "¿Quedaba por acá?"
    pensamientoabuela "Sí, puede ser."
    pensamientoabuela "O, quizás... no sé."
    pensamientoabuela "En fin, mi marido debería estar por llegar."
    pensamientoabuela "Le debería cocinar algo."
    pensamientoabuela "¿Qué le gustaba al Viejo?"
    pensamientoabuela "Fideos, arroz, esa pasta amarilla. ¿Cómo se llamaba?"
    pensamientoabuela "Bah. Le haré eso mismo."

    scene cocina
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    play sound "audio/cooking sfx.mp3"

    hijo "¿Segura?"
    hijo "Mamá, ¿no recordás dónde dejaste los huevos?"
    abuela "¿Cómo no me voy a acordar?"
    abuela "Están en la heladera."
    hijo "¿Y por qué está buscando en la alacena?"
    abuela "Ah. Mi mente, no te preocupes."

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela "Escucho las llaves sonar, seguro que es el Viejo."
    pensamientoabuela "Habrá vuelto del viaje."
    pensamientoabuela "Estuvo seis meses afuera."
    pensamientoabuela "En el océano."
    pensamientoabuela "Donde la vida y la muerte conviven constantemente."
    pensamientoabuela "Espero que esté bien."

    show personaje_placeholder_blury at right
    with dissolve

    show hija at center
    with dissolve

    hija "Mamá, hola. El tráfico estaba terrible. No pude llegar más rápido."
    abuela "Viejo. ¡Tanto tiempo!"
    abuela "Te estoy preparando el almuerzo."
    hija "¿El Viejo?" 
    hija "Me parece que te equivocaste."
    hija "¿Me veo como él?"
    abuela "Eh... ¿no?"
    hija "¿No recuerdas que partió hace años?"
    abuela "¿A dón-?"
    hija "A las Bahamas. Falleció en alta mar."

    pensamientoabuela "¿Cómo?"
    pensamientoabuela "¿Falleció?"

    hija "En fin, te espero en el salón para cuando decidas recordarme."
    hijo "¡Hermana!"

    scene cocina
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Los observo moverse por el espacio."
    pensamientoabuela "Se van."
    pensamientoabuela "No tiene sentido lo que dice."
    pensamientoabuela "¿No era ese mi marido?"
    pensamientoabuela "¿Mi propio marido dijo que se murió?"
    pensamientoabuela "¿Es un fantasma?"
    pensamientoabuela "Qué miedo."
    pensamientoabuela "Menos mal que soy cristiana."
    pensamientoabuela "Me voy al salón que me duelen las piernas."

    play sound "audio/footsteps sfx.mp3"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    abuela "¡Ay! ¿En qué momento llegaste, hijo?"
    abuela "¿No estabas en el trabajo?"

    show personaje_placeholder_blury at right
    with dissolve

    pensamientoabuela "¿Y ahora por qué mi hijo me mira desconcertado?"

    hijo "No, estaba acá. En el salón, hablando algunas cosas con mi hermana."

    pensamientoabuela "Observo a mi... ¿marido? revolear los ojos."
    pensamientoabuela "¿Qué bicho le picó ahora?"

    hijo "Estábamos esperando a que termines de cocinar."

    pensamientoabuela "Cocinar."
    pensamientoabuela "¿Estaba cocinando?"
    pensamientoabuela "¿Qué estaba haciendo?"
    pensamientoabuela "¿Habrá sido algo importante?"

    abuela "Sí, sí. Ahora les traigo la comida."

    scene pasillo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "¿Dónde quedaba la cocina?"
    pensamientoabuela "¿Era por acá?"
    pensamientoabuela "¿Qué decía mi hijo?"
    pensamientoabuela "Carteles. ¡Eso!"
    pensamientoabuela "Que mire los papelitos que me dejaba."
    pensamientoabuela "Me recuerda las cartas que me mandaba el Viejo."

    scene pared_con_papelitos
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "A ver, este papel dice: Cocina."

    play sound "audio/footsteps sfx.mp3"

    scene cocina
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Supongo que será acá."
    pensamientoabuela "Bueno, ¿y ahora?"
    pensamientoabuela "¿Qué le gustaba al Viejo?"
    pensamientoabuela "Fideos, arroz, esa pasta amarilla. ¿Cómo se llamaba?"
    pensamientoabuela "Bah. Le haré eso mismo."
    pensamientoabuela "Agarro el paquete verde."
    pensamientoabuela "¿Esto venía con instrucciones?"
    pensamientoabuela "Mejor me fijo en el libro de recetas."
    pensamientoabuela "Me pongo los lentes..."
    pensamientoabuela "¿Dónde estaban?"
    pensamientoabuela "Ah, acá."

    scene receta
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/cooking sfx.mp3"

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

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Había un poema que escribí, que se lo dediqué a mi amado."
    pensamientoabuela "Tu imagen, en mis luceros se ha quedado."
    pensamientoabuela "La última vez que te vi, antes de que partieras, "
    pensamientoabuela "tus dedos se extendían para alcanzarme."
    pensamientoabuela "Tal como el agua que nos rodeaba, tu voz se despedía."
    pensamientoabuela "Y mi alma, había quedado ardiendo."
    pensamientoabuela "En fuego, quemando..."
    pensamientoabuela "¿Qué es ese olor?"

    abuela "¡Se quemó la comida!"

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Tranquila mamá, no pasa nada."
    hijo "Vamos a arreglarlo, juntos. ¿Te parece?"
    abuela "¿Qué me estará pasando hoy?"
    abuela "Esto no me solía suceder."
    hijo "Lo que importa en verdad es que estamos todos bien."
    hijo "Son cosas que le pueden pasar a cualquiera."

    jump Story2

label Story1:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela "De repente, escucho un sonido."
    pensamientoabuela "Es el ruido de la puerta nuevamente."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    with dissolve

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Abuela. Tanto tiempo."

    show hermana_del_medio:
        xalign 0.75
        yalign 1.0
    with dissolve

    nietadelmediodelhijo "Abue. Hoy mi día fue tan tedioso."

    show hermano_menor:
        xalign 0.25
        yalign 1.0
        xzoom -1.0
    with dissolve

    nietomenordelhijo "Estos dos son unos aburridos."
    nietomenordelhijo "Al menos yo me divertí en clase."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Son... demasiadas personas."
    pensamientoabuela "¿Debería preguntarles algo?"

    jump Story12


label Story2:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    pensamientoabuela "Después de haber comido el almuerzo con mi hijo, y mi... ¿marido?."

    play sound "audio/keys opening door sfx.mp3"

    pensamientoabuela "Escucho el ruido de la puerta."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    with dissolve

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Abuela. Tanto tiempo."

    show hermana_del_medio:
        xalign 0.75
        yalign 1.0
    with dissolve

    nietadelmediodelhijo "Abue. Hoy mi día fue tan tedioso."
    nietadelmediodelhijo "Se ve que comieron sin nosotros."

    show hermano_menor:
        xalign 0.25
        yalign 1.0
        xzoom -1.0
    with dissolve

    nietomenordelhijo "Estos dos son unos aburridos."
    nietomenordelhijo "Al menos yo me divertí en clase."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Son... demasiadas personas."
    pensamientoabuela "¿Debería preguntarles algo?"

    jump Story21

label Story12:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    show hermano_menor:
        xalign 0.25
        yalign 1.0
        xzoom -1.0
    with dissolve

    nietomenordelhijo "¡No sabes el día que tuvimos!"
    nietomenordelhijo "Los profesores nos dejaron sin recreo."
    nietomenordelhijo "Y todo porque dos compañeros se pelearon en plena lección."
    nietomenordelhijo "Lo peor de todo es que teníamos clase previa al examen."
    nietomenordelhijo "No pudimos repasar nada."

    show hermana_del_medio:
        xalign 0.75
        yalign 1.0
    with dissolve

    nietadelmediodelhijo "¿Les sacaron el receso?"
    nietadelmediodelhijo "Siempre les pasa algo a ustedes, son re quilomberos."
    nietadelmediodelhijo "Nosotros tuvimos taller de música. Re aburrido."

    pensamientoabuela "Ni siquiera me dieron tiempo de poder contestar."
    pensamientoabuela "Pareciera que me conocen desde hace mucho."
    pensamientoabuela "¿Será que es así?"

    nietomenordelhijo "A todo esto, ¿podemos ir a la plaza?"
    nietomenordelhijo "Hace mucho no vamos con la abuela."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "No sé Santi. Es mejor que se quede en casa."

    show hija at center
    with dissolve

    hija "Lucas, no les dejás hacer nada."
    hija "El paseo le va a venir bien a mamá."
    hija "A ver si no se olvida de ellos también..."
    hijo "Luciana. Basta."
    hija "Vayan, chicos. Tienen mi permiso."
    hija "Me voy a quedar a hablar con su viejo."
    hijo "Agh. Pero tengan cuidado, ¿sí?."
    hijo "Si llega pasar algo o ven a alguien raro, por favor, llámenme."

    pensamientoabuela "No estoy entendiendo lo que sucede."
    pensamientoabuela "¿A dónde me quieren llevar?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Los niños se fueron ya. Los adultos se quedaron hablando."
    pensamientoabuela "Como si ni existiera en sus vidas."
    pensamientoabuela "Lo único que me queda es suspirar y seguir a los jóvenes."

    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Así que eso hago."

    scene calle
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Los sigo por calles que nunca vi antes."
    pensamientoabuela "La gente me saluda. Yo sigo de largo."

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "No corran chicos."
    nietomayordelhijo "Recuerden que estoy con la abuela."

    menu:
        pensamientoabuela "¿Debería dejar que este muchacho siga caminando a mi lado?"

        "Sí.":

            jump Yes

        "No.":

            jump No

label Story21:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (2nd chapter).mp3"

    show hermano_menor:
        xalign 0.25
        yalign 1.0
        xzoom -1.0
    with dissolve

    nietomenordelhijo "¡No sabes el día que tuvimos!"
    nietomenordelhijo "Los profesores nos dejaron sin recreo."
    nietomenordelhijo "Y todo porque dos compañeros se pelearon en plena lección."
    nietomenordelhijo "Lo peor de todo es que teníamos clase previa al examen."
    nietomenordelhijo "No pudimos repasar nada."

    show hermana_del_medio:
        xalign 0.75
        yalign 1.0
    with dissolve

    nietadelmediodelhijo "¿Les sacaron el receso?"
    nietadelmediodelhijo "Siempre les pasa algo a ustedes, son re quilomberos."
    nietadelmediodelhijo "Nosotros tuvimos taller de música. Re aburrido."

    pensamientoabuela "Ni siquiera me dieron tiempo de poder contestar."
    pensamientoabuela "Pareciera que me conocen desde hace mucho."
    pensamientoabuela "¿Será que es así?"

    nietomenordelhijo "A todo esto, ¿podemos ir a la plaza?"
    nietomenordelhijo "Hace mucho no vamos con la abuela."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "No sé Santi. Es mejor que se quede en casa."

    show hija at center
    with dissolve

    hija "Lucas, no les dejás hacer nada."
    hija "El paseo le va a venir bien a mamá."
    hija "A ver si no se olvida de ellos también..."
    hijo "Luciana. Basta."
    hija "Vayan, chicos. Tienen mi permiso."
    hija "Me voy a quedar a hablar con su viejo."
    hijo "Agh. Pero tengan cuidado, ¿sí?."
    hijo "Si llega pasar algo o ven a alguien raro, por favor, llámenme."

    pensamientoabuela "No estoy entendiendo lo que sucede."
    pensamientoabuela "¿A dónde me quieren llevar?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Los niños se fueron ya. Los adultos se quedaron hablando."
    pensamientoabuela "Como si ni existiera en sus vidas."
    pensamientoabuela "Lo único que me queda es suspirar y seguir a los jóvenes."
    
    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Así que eso hago."

    scene calle
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    pensamientoabuela "Los sigo por calles que nunca vi antes."
    pensamientoabuela "La gente me saluda. Yo sigo de largo."

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "No corran chicos."
    nietomayordelhijo "Recuerden que estoy con la abuela."

    menu:
        pensamientoabuela "¿Debería dejar que este muchacho siga caminando a mi lado?"

        "Sí.":

            jump Yes

        "No.":

            jump No

label Yes:

    pensamientoabuela "Decido permitir que el joven me acompañe."

    scene plaza
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hermano_mayor at right
    with dissolve

    play sound "audio/footsteps on grass sfx.mp3"

    abuela "Gracias por llevarme afuera."
    abuela "No salía desde que mi amiga se mudó."
    abuela "Hace mucho que no hablamos."
    abuela "¿Estará bien?"
    abuela "Se veía molesta cuando me fui de la casa."
    nietomayordelhijo "¿Eran muy unidas ustedes?"
    abuela "Sí."
    abuela "Solíamos sentarnos en un banco a charlar."
    abuela "Y a ponernos al día."
    nietomayordelhijo "Ojalá tenga una amistad tan larga como la de ustedes."
    nietomayordelhijo "Con mis amigos discutimos por cualquier cosa."
    abuela "Siempre es bueno mantener amistades."
    abuela "Y más cuando uno pasa mucho tiempo solo."

    pensamientoabuela "El muchacho se queda pensando."
    pensamientoabuela "No sé por qué todos esquivan el tema cuando nombro a mi amiga."

    scene banco
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Este banco me resulta familiar."

    abuela "Me recuerdan a mis hijos."
    abuela "Les encantaba correr por esta plaza cuando eran chicos."

    pensamientoabuela "El muchacho sigue sin decir nada."
    pensamientoabuela "Extraño, ¿no?"

    show hermano_menor:
        xalign 0.25
        yalign 1.0
        xzoom -1.0
    with dissolve

    nietomenordelhijo "¡Vení a jugar con nosotros, abuela!"

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Es mejor que se quede sentada."
    nietomayordelhijo "Papá nos va a retar si le pasa algo."

    scene banco
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Los chicos vuelven a correr."
    pensamientoabuela "Los observo jugar."
    pensamientoabuela "Parecen felices."

    scene black
    with fade

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "¡Volvimos!"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "¿Está bien la abuela?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Sí, papá."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at center
    with dissolve

    hija "Te dije que no iba a pasar nada."
    abuela "¿El joven chico es tu hijo?"
    abuela "Me acompañó hasta la plaza."
    abuela "Muy educado."
    hija "Es tu nieto, mamá."
    hija "No sirvió de nada el paseo parece."

    pensamientoabuela "¿Por qué se enoja?"
    pensamientoabuela "¿Le hice algo malo?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show personaje_placeholder_blury at right
    with dissolve

    hijo "No seas así, Luciana."
    hijo "A pesar de que no estaba tan de acuerdo al principio, ahora entiendo."
    hijo "Le ayuda a despejarse."
    hijo "A sentirse acompañada."
    abuela "Les agradezco lo que hicieron por mí."
    abuela "Pero me puedo cuidar sola."

    show hija at center
    with dissolve

    hija "Bah. A ver si sirve esto."

    scene tv
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show hija at right
    with dissolve

    hija "Mirá."
    hija "¿Te acordás?"
    hija "Somos todos nosotros en la playa."
    hija "Era el día de tu cumpleaños."

    pensamientoabuela "Conozco esa playa."

    play sound "audio/children laughing sfx.mp3"

    pensamientoabuela "Conozco esas risas."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "No le muestres eso, tía."
    nietomayordelhijo "La vas a confundir más."

    show hija at center
    with dissolve

    hija "No te metas, Facundo."

    show hermana_del_medio:
        xalign 0.75
        yalign 1.0
    with dissolve

    nietadelmediodelhijo "Basta, tía."
    nietadelmediodelhijo "Ya entendimos que no confiás en nosotros."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Luciana."
    hijo "Escuchá a tus sobrinos."
    hijo "Así no la vas a ayudar."

    show hija at center
    with dissolve

    hija "Estoy tratando de que se acuerde de nosotros."
    hija "¿Por qué nadie me ayuda?"

    menu:

        pensamientoabuela "Las voces vuelven a subir de tono."

        "Voy a intentar calmar las aguas.":
            jump Intervene

        "Preferiría no meterme.":
            jump DoNotIntervene

label Intervene:

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Otra vez mis chicos pelean."

    abuela "Ya fue suficiente."
    abuela "No paro de escucharlos discutir."
    abuela "Siempre es lo mismo."
    abuela "Parece que volvieran a tener diez años."

    pensamientoabuela "La casa, de repente, quedó en silencio."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "¿Mamá?"

    show hija at center
    with dissolve

    hija "¿Te acordás de nosotros?"
    abuela "Estoy cansada de que discutan por todo."
    abuela "Vayan a su cuarto los dos."

    pensamientoabuela "Por fin, un poco de paz."

    jump Capitulo3_Casa

label DoNotIntervene:

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show personaje_placeholder_blury at right
    with dissolve
    
    hijo "¿No te quedó claro que no se va a acordar de nosotros?"
    hijo "Ya nos dijo el médico que no debemos forzarla."
    hijo "La puede estresar más."

    show hija at center
    with dissolve

    hija "Yo solo quiero que nos recuerde."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/running around sfx.mp3"

    pensamientoabuela "Observo el modo en el que la mujer se va al balcón de manera precipitada."

    show personaje_placeholder_blury at right
    with dissolve

    pensamientoabuela "Miro ahora al hombre que tengo en frente."

    abuela "¿Por qué discuten tanto, Luqui?"

    pensamientoabuela "Todos súbitamente se quedaron inmóviles."

    hijo "Hace muchísimo tiempo que no me decías así, mamá."

    pensamientoabuela "¿Dije algo raro?"

    scene ventana
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Noto cómo el hombre sale a buscar a la mujer."

    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Me aproximo a la ventana que da al balcón para oír su conversación."
    
    hijo "Lu."
    hijo "Mamá me acaba de decir Luqui."
    hija "¿Qué?"
    hija "Hace muchísimo que no te llamaba así."
    hijo "¿Viste?"
    hijo "Todavía recuerda algunas cosas."
    hija "Tal vez tengas razón."
    hijo "No sirve de nada discutir."
    hijo "Vení, vamos adentro."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Me alejo del balcón."
    pensamientoabuela "No entiendo el motivo por el que actúan así."

    jump Capitulo3_Casa

label No:

    pensamientoabuela "No necesito que me acompañen."

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "¿Te ayudo, abuela?"

    pensamientoabuela "Otra vez me dijo abuela."
    pensamientoabuela "¿Tengo nietos?"

    abuela "No, jovencito."
    abuela "Te agradezco, pero puedo cuidarme sola."
    nietomayordelhijo "Pero te acompaño hasta la plaza."
    abuela "No hace falta."
    abuela "Puedo sola."

    pensamientoabuela "El muchacho parece dudar."
    pensamientoabuela "Pero termina alejándose."

    scene calle
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Estoy caminando hace un rato ya."
    pensamientoabuela "¿Tan lejos estaba la plaza?"
    pensamientoabuela "No me suena este barrio."
    pensamientoabuela "Las calles no están donde las recuerdo."
    pensamientoabuela "¿Me habré equivocado?"

    show cachito at right
    with dissolve

    pensamientoabuela "Alguien se acerca."
    pensamientoabuela "Otra cara que no conozco."
    pensamientoabuela "¿Me podrá ayudar?"

    cachito "¿Necesita ayuda, doña?"
    abuela "No gracias, joven."
    abuela "Estoy de camino a la plaza."
    cachito "¿La plaza?"
    cachito "Por acá no hay ninguna."
    cachito "¿Quiere que la acompañe?"

    menu:

        pensamientoabuela "¿Debería confiar en él?"

        "Aceptar su ayuda.":
            jump CachitoYes

        "Seguir sola.":
            jump CachitoNo

label CachitoYes:

    abuela "Bueno."
    cachito "¿Por dónde vive?"

    pensamientoabuela "¿Dónde vivo?"
    pensamientoabuela "¿Cómo era mi casa?"

    abuela "Por Sarmiento."
    abuela "Una casa con rejas celestes."
    cachito "Tranquila."
    cachito "La vamos a encontrar."

    scene frente_de_casa
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "¡Ahí está mamá!"

    show hija at center
    with dissolve

    hija "Por fin apareció."
    hija "¿Y vos quién sos?"

    scene frente_de_casa
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show cachito at right
    with dissolve

    cachito "La encontré caminando sola."
    cachito "Parecía perdida."
    abuela "Muchas gracias por acompañarme, buen hombre."

    show personaje_placeholder_blury at center
    with dissolve

    hijo "De verdad, muchísimas gracias."
    hijo "Estábamos muy preocupados."
    cachito "No hacía falta agradecer."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Todos parecen más tranquilos."

    show hija at center
    with dissolve

    hija "Ay mamá."
    hija "Gracias a Dios estás bien."

    jump Capitulo3_Perdida

label CachitoNo:

    abuela "Gracias."
    abuela "Pero puedo cuidarme sola."

    pensamientoabuela "Prosigo con mi camino."

    scene calle
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Sigo sin reconocer nada."

    show policia at right
    with dissolve

    policia "¿Ester?"

    pensamientoabuela "¿Cómo sabe mi nombre?"

    policia "Su familia la está buscando."

    scene frente_de_casa
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at center
    with dissolve

    hija "Mamá."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Gracias, Oficial."

    scene frente_de_casa
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show policia at right
    with dissolve

    policia "Por su seguridad les recomendamos que no salga sola."
    policia "También sería importante que lleve alguna identificación."
    policia "Y reforzar las medidas de acompañamiento."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at center
    with dissolve

    hija "Gracias a Dios estás bien."

    pensamientoabuela "No entiendo por qué todos estaban tan preocupados."

    jump Capitulo3_Perdida

label Capitulo3_Casa:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"

    scene realliving
    with fade
    
    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "La casa se siente distinta cuando todos hablan al mismo tiempo."
    pensamientoabuela "A veces pienso que están contentos."
    pensamientoabuela "Otras veces, que están por pelearse otra vez." 

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá... ¿estás cansada?"
    abuela "Un poco."
    abuela "Pero el aire de la plaza me hizo bien."

    show hija at center
    with dissolve

    hija "Te dije que salir un rato le iba a hacer bien."
    hijo "Sí, bueno."
    hijo "Capaz esta vez sí."
    hija "Mamá."
    hija "Perdón por cómo te hablé antes."
    hija "A veces me gana la desesperación."

    abuela "¿Desesperación por qué, querida?"
    hija "Porque..."
    hija "Porque siento que te perdemos un poquito más cada día."

    play sound "audio/luciana crying sfx.mp3"

    pensamientoabuela "Tiene la misma cara que cuando era chica y rompía algo sin querer."
    pensamientoabuela "Esa mezcla de culpa y tristeza."
    pensamientoabuela "¿Será mi hija de verdad?"

    abuela "No llores, hija."
    abuela "No me gusta cuando lloran en esta casa."
    hija "Perdón, mamá."
    hijo "Bueno, ya está."
    hijo "Lo importante es que hoy salió todo bien."

    jump EntradaAmbar

label Capitulo3_Perdida:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show hija at center
    with dissolve

    hija "Mamá, no podés volver a hacer algo así."
    abuela "¿Algo como qué?"
    abuela "Solo estaba caminando."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá."
    hijo "Te perdimos por dos horas."
    hija "¡Dos horas!"

    pensamientoabuela "¿Dos horas?"
    pensamientoabuela "No puede ser."
    pensamientoabuela "Para mí fue apenas un ratito."

    abuela "No exageren."
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

    pensamientoabuela "Me están mirando."
    pensamientoabuela "Pero siento que hablan de otra persona."

    abuela "No hablen como si yo no estuviera acá."
    hija "¿Y cuándo sería momento de hablar?"
    hija "¿Cuando no reconozca más a ninguno?"

    hijo "No digas eso."
    hija "¡Hay que internarla, Lucas!"

    pensamientoabuela "¿Internarme?"
    pensamientoabuela "¿A mí?"
    pensamientoabuela "¿Por qué quieren hacerme esto?"
    pensamientoabuela "¿Qué les pasa?"

    abuela "¿Internar a quién?"

    jump EntradaAmbar

label EntradaAmbar:

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    play sound "audio/doorbell sfx.mp3"

    pensamientoabuela "Escucho el timbre."

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Voy."

    scene realliving
    with fade

    play sound "audio/keys opening door sfx.mp3"

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show ambar at right
    with dissolve

    esposa "Buenas noches, familia."

    pensamientoabuela "Esa mujer."
    pensamientoabuela "Me resulta familiar."

    esposa "¿Llegué en mal momento?"

    show hija at center
    with dissolve

    hija "No."
    hija "Bueno, más o menos."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Llegaste justo."

    show ambar at center
    with dissolve

    esposa "Hola, Ester."

    pensamientoabuela "No. Me habré confundido."
    pensamientoabuela "No recuerdo quién es."
    pensamientoabuela "Pero, me transmite calma."

    abuela "Hola..."
    esposa "Lucas."
    esposa "Luciana."
    esposa "¿Por qué no van a hablar tranquilos a otro lado?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Sí."

    show hija at center
    with dissolve

    hija "Dale."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Los veo alejarse."

    show ambar at right
    with dissolve

    esposa "Chicos."
    esposa "¿Por qué no van a jugar un rato?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show ambar at right
    with dissolve

    play sound "audio/footsteps sfx.mp3"

    pensamientoabuela "Distingo a los chicos irse de igual modo."
    pensamientoabuela "Sin realizar queja alguna."
    pensamientoabuela "Sorprendente."

    esposa "Ester..."
    esposa "¿Querés ayudarme con la cena?"
    abuela "¿Quién sos?"
    esposa "Una vieja amiga."

    pensamientoabuela "Vieja amiga."
    pensamientoabuela "Me guiñó el ojo."
    pensamientoabuela "Tal vez, pueda serlo."

    abuela "Bueno."
    abuela "Quedarme quieta me pone nerviosa."

    jump CocinaAmbar

label CocinaAmbar:

    scene cocina
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Esta cocina sí la conozco."

    show ambar at right
    with dissolve

    esposa "Ester."
    esposa "¿Los cubiertos dónde están?"
    abuela "En ese cajón."

    pensamientoabuela "Abro el cajón."

    esposa "Ese no."
    esposa "El de más abajo."
    abuela "Ah."
    abuela "Ya sabía."
    esposa "Sí."
    esposa "Ya sé."
    esposa "A todos nos pasa."
    abuela "Sos buena para mentir sin que se note."
    esposa "Y vos siempre fuiste buena para darte cuenta."

    pensamientoabuela "Esa frase la conozco."
    pensamientoabuela "La escuché antes."

    esposa "¿Te acordás cuando nos quedábamos hablando?"
    esposa "Mientras los chicos corrían por toda la casa."
    abuela "Lucas siempre corría con medias."
    abuela "Se resbalaba y lloraba."
    esposa "Sí."
    esposa "¿Y Luciana se enojaba porque tocaba sus cosas?"
    abuela "Sí."
    abuela "Tiene carácter fuerte."
    esposa "Pero te quiere mucho."
    abuela "Ya lo sé."

    pensamientoabuela "Cuando me mira apretando la boca."
    pensamientoabuela "Me doy cuenta."

    esposa "Está cansada."
    esposa "No enojada con vos."
    esposa "A veces la tristeza sale como enojo."

    pensamientoabuela "Tristeza..."
    pensamientoabuela "Eso sí lo entiendo."
    pensamientoabuela "Hay días en que siento que me falta algo."
    pensamientoabuela "Aunque no sepa qué."

    esposa "¿Querés cortar el pan?"
    abuela "Sí."
    esposa "Dale."
    esposa "Con cuidado."

    pensamientoabuela "¿Lo estoy haciendo demasiado lento?"
    pensamientoabuela "No lo sé."
    pensamientoabuela "Luego de un tiempo, termino de cortar."

    abuela "Ahí está."
    esposa "¡Qué perfección, Ester!"
    esposa "Estás para abrir una panadería."

    pensamientoabuela "Me hace reír."

    esposa "Bueno."
    esposa "Vamos a llevar la comida."
    abuela "Dale."

    jump CenaFamiliar

label CenaFamiliar:

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Todos vuelven a sentarse juntos."

    show hermano_menor at right
    with dissolve

    nietomenordelhijo "¿Puedo servirle agua a la abuela?"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve
    
    hijo "Sí."
    hijo "Despacio."
    abuela "Gracias, querido."

    pensamientoabuela "Qué amable es este chico."
    pensamientoabuela "Hay un silencio extraño."

    hijo "Mamá..."
    hijo "Queríamos hablar con vos de algo importante."

    show hija at center
    with dissolve

    hija "Lucas."

    pensamientoabuela "¿Estará mal cortado el pan?"
    pensamientoabuela "Todos tienen caras raras."

    hijo "Tenés derecho a saberlo."
    abuela "Me están asustando."
    abuela "Decilo de una vez."
    hijo "Creemos que sería bueno que hables con una profesional."
    hijo "Una psicóloga."
    hijo "O una psiquiatra."
    hijo "Alguien que pueda ayudarte a entender mejor lo que te está pasando."
    hija "Y que nos ayude a nosotros a acompañarte."

    pensamientoabuela "Ayuda."
    pensamientoabuela "Otra vez esa palabra."

    abuela "¿Estoy tan mal?"
    hijo "No se trata de eso."
    hijo "Se trata de que no estés sola."
    hija "Y de no esperar a que pase algo peor."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show ambar at right
    with dissolve

    esposa "Nadie te está castigando, Ester."
    esposa "Solo quieren cuidarte."

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

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    abuela "No me gusta la idea."
    abuela "Pero menos me gusta verlos así."

    pensamientoabuela "Observo el modo en el que el hombre baja la mirada."

    abuela "Si de verdad creen que me va a hacer bien..."
    abuela "Voy a ir."

    show hija at center
    with dissolve

    hija "¿En serio?"
    abuela "Sí."
    abuela "Pero no me hablen como si ya no entendiera nada."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Nunca haríamos eso."
    hija "Gracias, mamá."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show ambar at center
    with dissolve

    esposa "Entonces mañana vemos cómo organizarlo."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Vamos a ir con vos."
    abuela "Bueno."
    abuela "Pero ahora quiero dormir."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show hija at center
    with dissolve

    hija "¿Querés que te acompañe al cuarto?"
    abuela "Sí."
    abuela "Vení."

    jump Capitulo4

label Cap3Negar:

    $ renpy.music.stop(fadeout=2.0)

    play music "initium finis (3rd chapter).mp3"
    
    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    abuela "No."
    abuela "No voy a ir a ningún lado."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá..."
    abuela "¡No!"
    abuela "Ya escuché demasiado por hoy."

    show hija at center
    with dissolve

    hija "No es un ataque."
    abuela "Entonces dejá de mirarme como si estuviera mal."
    hija "Nadie piensa eso."
    abuela "Vos sí."

    pensamientoabuela "La veo bajar la mirada."

    hijo "Mamá."
    hijo "Por favor."
    abuela "¡No me digas que me tranquilice!"
    abuela "¡Estoy en mi casa!"

    play sound "audio/grandma breathing sfx.mp3"

    pensamientoabuela "El pecho me aprieta."
    pensamientoabuela "Las voces se mezclan."
    pensamientoabuela "Ya no entiendo quién está hablando."

    hija "Mamá, sentate."
    abuela "¡No me toques!"

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show ambar at center
    with dissolve

    esposa "Lucas."
    esposa "Traé agua."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Ya voy."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show ambar at center
    with dissolve

    esposa "Ester."
    esposa "Mirame."
    esposa "Nadie te va a sacar de tu casa."
    esposa "Respirá conmigo."

    play sound "audio/breathing sfx.mp3"

    pensamientoabuela "Intento hacerlo."

    play sound "audio/grandma breathing sfx.mp3"

    show personaje_placeholder_blury at right
    with dissolve

    hijo "No vamos a seguir discutiendo ahora."
    hijo "Pero tenemos que buscar ayuda profesional."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at right
    with dissolve

    hija "Aunque te enojes con nosotros."

    pensamientoabuela "Su voz se quiebra."
    pensamientoabuela "Quisiera consolarla."

    show ambar at center
    with dissolve

    esposa "Basta por hoy."
    esposa "Ester necesita descansar."
    abuela "Quiero irme a dormir."
    abuela "Sola."
    esposa "Te acompaño hasta la puerta."

    pensamientoabuela "Me está costando levantarme."

    jump Capitulo4

label Capitulo4:

    scene sala_de_espera
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Este lugar huele a nuevo."
    pensamientoabuela "¿Por qué me trajeron acá?"
    pensamientoabuela "Todos me miran como si fuera a romperme."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Viste mamá, está lindo el lugar."
    abuela "No me gustan los hospitales así."

    show hija at center
    with dissolve

    hija "No es un hospital, es un centro de ayuda."
    abuela "Es lo mismo."

    scene sala_de_espera
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show ambar at center
    with dissolve

    esposa "Bueno, el propósito es que te sientas más cómoda."

    scene sala_de_espera
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Escucho que llaman mi nombre."
    pensamientoabuela "Distingo el modo en el que todos se levantan."

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    pensamientoabuela "Entramos a una oficina tranquila."

    show psicologa at right
    with dissolve

    doc "¿Son ustedes los familiares de Ester?"

    show personaje_placeholder_bluryl at center
    with dissolve

    hijo "Así es."
    doc "Muy bien, entonces, les pido amablemente que se retiren."
    doc "Me gustaría hablar a solas con Ester."

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    play sound "audio/closed door sfx.mp3"

    pensamientoabuela "Observo el modo en el que se van de la sala."

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show psicologa at right
    with dissolve

    doc "Hola Ester, ¿cómo llegó hasta acá?"
    abuela "Me trajeron."

    pensamientoabuela "Observo a la mujer sonreír."

    doc "¿Y usted quería venir?"

    menu:

        pensamientoabuela "¿Debería confiar en esta mujer?"

        "Confiar.":
            jump Cap4Confiar

        "Mantener distancia.":
            jump Cap4NoConfiar

label Cap4Confiar:

    $ confio_doctora = True

    abuela "La verdad que no."
    abuela "Pero entiendo que mi situación no mejora con el tiempo."
    abuela "Veo a mucha gente pero no recuerdo a nadie."
    abuela "Me visitan constantemente pero me siento sola."
    doc "¿Y cómo le cae eso?"

    pensamientoabuela "Me quedo en silencio un tiempo."

    abuela "Mal."
    abuela "Me cae muy mal."
    doc "Tiene sentido que le caiga mal."

    pensamientoabuela "No me dijo que no me preocupara."
    pensamientoabuela "Solo dijo que tiene sentido."
    pensamientoabuela "Hace cuánto no me decían eso."

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

    pensamientoabuela "Miro mis manos."

    abuela "A veces siento que me observan y ven a otra persona."
    abuela "Una que necesita ayuda para todo."
    doc "¿Y usted qué ve cuando se mira?"

    pensamientoabuela "Qué pregunta difícil."
    pensamientoabuela "A veces la misma de siempre."

    abuela "Depende del día."
    doc "Eso es muy honesto, Ester."
    doc "¿Le gustaría volver la semana que viene?"

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show psicologa at right
    with dissolve

    pensamientoabuela "No sé si quiero."
    pensamientoabuela "Pero tampoco me disgustó."

    abuela "Puede ser."
    abuela "Veremos."

    jump Cap4Conexion

label Cap4NoConfiar:

    $ confio_doctora = False

    abuela "Me trajeron."
    abuela "Vine para que se quedaran tranquilos."
    doc "Entiendo."
    doc "¿Y usted está tranquila?"
    abuela "Estoy bien."
    doc "¿Qué es estar bien para usted?"

    pensamientoabuela "Qué pregunta rara."

    abuela "Estar en mi casa."
    abuela "Con mi gente."
    doc "¿Y acá no se siente así?"
    abuela "Acá no conozco a nadie."
    doc "Es la primera vez que nos vemos."

    scene cuadro_del_psicologo
    with fade

    pensamientoabuela "Miro un cuadro."

    doc "¿Qué está mirando?"
    abuela "Esa pintura."
    abuela "Mi hijo tiene uno parecido."
    doc "¿Cómo se llama su hijo?"

    pensamientoabuela "Lo sé."
    pensamientoabuela "Lo sé perfectamente."
    pensamientoabuela "¿Por qué no me sale?"

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show psicologa at right
    with dissolve

    abuela "Eso no le importa a usted."
    doc "Tiene razón."
    doc "Perdón."

    pensamientoabuela "Esperaba que insistiera."

    abuela "Lucas."
    abuela "Se llama Lucas."
    doc "¿Y cómo es Lucas?"
    abuela "Cabeza dura."
    abuela "Pero buen chico."
    doc "¿Se parece a usted?"
    abuela "En cabeza dura, sí."

    pensamientoabuela "No le voy a contar nada importante."
    pensamientoabuela "Pero tampoco me lo está exigiendo."
    pensamientoabuela "Qué extraña esta mujer."

    doc "Ester, gracias por venir."
    doc "La puerta queda abierta si algún día quiere volver."
    abuela "Ya veremos."

    pensamientoabuela "¿La puerta queda abierta?"
    pensamientoabuela "Nadie me había dicho eso en mucho tiempo."

    jump Cap4Conexion

label Cap4Conexion:

    scene sala_de_espera
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at center
    with dissolve

    hija "¿Cómo te fue? ¿Qué te dijo? ¿Estuvo bien?"
    abuela "No me apures, por favor."

    pensamientoabuela "Miro el modo en el que aquella señora sale de la oficina."
    pensamientoabuela "Y la forma en la que ambos adultos se apresuran hacia ella."
    
    scene sala_de_espera
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show ambar at center
    with dissolve

    esposa "¿Cómo estás?"
    abuela "Fatigada."
    abuela "Hablar cansa."
    esposa "Sí."
    esposa "Pero lo hiciste igual."

    pensamientoabuela "Sí."
    pensamientoabuela "Lo hice igual."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show hija at center
    with dissolve

    hija "¿Querés tomar algo, mamá?"
    abuela "Un té está bien."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show personaje_placeholder_blury at right
    with dissolve

    hijo "¿No querés descansar?"
    abuela "Primero el té."

    pensamientoabuela "No me pregunta nada."

    abuela "¿No querés saber cómo me fue?"
    hijo "Solo si vos querés contarme."

    pensamientoabuela "Ahí está."
    pensamientoabuela "Aprendió algo."

    abuela "Fue bien."
    abuela "La doctora es rara."
    abuela "Pero no molesta."
    hijo "Algo es algo."

    scene black
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Sentí la manera en la que el tiempo pasó."

    scene psicologo
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    pensamientoabuela "Los chicos me consultan cosas que sé responder."
    pensamientoabuela "No sé si lo hacen a propósito."
    pensamientoabuela "Pero me gusta."
    pensamientoabuela "Además, el cuadro de la oficina ya lo conozco."
    pensamientoabuela "La señora de recepción se llama Mirta."
    pensamientoabuela "Hoy no tuve que preguntar dónde sentarme."
    pensamientoabuela "Y vine acompañada, también."

    show hija at center
    with dissolve

    show personaje_placeholder_bluryl:
        xalign 0.75
        yalign 1.0
    with dissolve

    show psicologa at right
    with dissolve

    doc "Ester, estos últimos encuentros me ayudaron a entenderla mejor."
    doc "Y quiero ser honesta."

    pensamientoabuela "Cuando alguien dice eso."
    pensamientoabuela "Viene algo difícil de oír."

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

    pensamientoabuela "Una pastilla para el cerebro."
    pensamientoabuela "Como si fuera un reloj al que le faltara cuerda."
    pensamientoabuela "¿Y si no funciona?"
    pensamientoabuela "¿Y si sí funciona y me vuelvo otra?"

    abuela "¿Y si no quiero tomarla?"
    doc "Es su decisión."
    doc "Nadie la obliga, Ester."
    doc "Me gustaría saber qué es lo que le genera malestar de todo esto."

    menu:

        pensamientoabuela "¿Aceptar la medicación?"

        "Aceptar.":
            jump MedicacionSi

        "Pensarlo más.":
            jump MedicacionNo

label MedicacionSi:

    $ acepta_medicacion = True

    abuela "Me da miedo no ser yo."
    doc "La medicación no busca cambiarla."
    doc "Busca ayudarla a seguir siendo usted durante más tiempo."

    pensamientoabuela "Quizás sí..."

    abuela "Está bien."
    abuela "La voy a tomar."
    hija "Gracias, mamá."

    pensamientoabuela "No lo hice por ella."
    pensamientoabuela "Lo hice por mí."

    jump CentroMemoria

label MedicacionNo:

    $ acepta_medicacion = False

    abuela "Todavía no."
    abuela "Necesito pensarlo."

    doc "Muy bien."
    doc "No hay apuro."
    doc "Seguimos con las sesiones y cuando esté lista, se habla de nuevo."
    hija "Mamá..."
    hijo "Lu."
    hijo "Ya escuchaste a la doctora."

    pensamientoabuela "Lucas me defendió."
    pensamientoabuela "No me esperaba eso."

    jump CentroMemoria

label CentroMemoria:

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

    pensamientoabuela "¿Otras personas como yo?"

    hija "¿Qué opinás, mamá?"
    abuela "¿Y qué talleres hay?"
    doc "De música, manualidades, lectura, cocina."
    doc "Depende del día."
    doc "Usted eligiría a cuál ir."

    pensamientoabuela "Cocina."
    pensamientoabuela "Eso sí sé hacerlo."

    abuela "¿Puedo ir a mirar primero?"
    doc "Por supuesto."
    doc "De hecho, se lo recomiendo."

    scene pieza_ester
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    show ambar at right
    with dissolve

    esposa "¿Cómo estás?"
    abuela "Pensando."
    esposa "¿En qué?"
    abuela "En si la gente de ese centro será buena."
    esposa "¿Y qué dice tu instinto?"
    abuela "Que vaya a ver."
    abuela "Y que si no me gusta, me vuelva."
    esposa "Eso siempre fue tuyo, Ester."
    esposa "Saber cuándo quedarte o irte."

    pensamientoabuela "Sí."
    pensamientoabuela "Eso todavía lo sé."
    pensamientoabuela "Quizás no todo se fue."
    pensamientoabuela "Observo a la mujer irse."

    scene pieza_ester_no_luz
    with fade

    play sound "audio/closed door sfx.mp3"

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Mañana voy a ver ese lugar."
    pensamientoabuela "Sola no. Pero voy."

    scene black
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Ha pasado un año ya."

    if confio_doctora and acepta_medicacion:
        jump EpilogoBueno
    else:
        jump EpilogoMalo

label EpilogoBueno:

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0

    pensamientoabuela "Todavía voy al centro de ayuda."
    pensamientoabuela "Y sigo viendo a la psiquiatra."
    pensamientoabuela "Hay días mejores."
    pensamientoabuela "Y otros más difíciles."

    abuela "¡Buenas!"

    show hija at center
    with dissolve

    hija "Mamá, ¿cómo te sentís?"

    abuela "Bien."
    abuela "Creo que dormí bastante."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "En un rato llega Ámbar con los chicos."

    pensamientoabuela "No siempre recuerdo quién viene."
    pensamientoabuela "Pero me gusta cuando la casa se llena."

    scene realliving
    with fade

    show nona_busto:
        xalign 0
        yalign 1.0
    
    show ambar at right
    with dissolve

    esposa "¡Llegamos!"

    show hermano_menor:
        xalign 0.25
        yalign 1.0
    with dissolve

    nietomenordelhijo "¡Hola, abuela!"

    pensamientoabuela "Me siento tranquila."

    esposa "¿Cómo estás, Ester?"
    abuela "Bien."
    abuela "Y con hambre."
    esposa "Perfecto."
    esposa "Porque justo trajimos algo para merendar."

    show hija at center
    with dissolve

    hija "Vamos a la mesa."

    pensamientoabuela "No recuerdo todo."
    pensamientoabuela "Probablemente nunca vuelva a hacerlo."
    pensamientoabuela "Pero ya no me siento sola."

    scene black
    with fade

    "Fin."

    return

label EpilogoMalo:

    scene hospital
    with fade
    
    show psicologal at left
    with dissolve

    doc "Ester, tiene visitas."
    doc "Pueden pasar."

    show personaje_placeholder_blury at right
    with dissolve

    hijo "Mamá."
    hijo "Somos nosotros."
    
    show hija:
        xalign 0.75
        yalign 1.0
    with dissolve

    hija "Quizás ya no nos reconoce."
    hijo "Vinieron los chicos también."

    scene hospital
    with fade

    show psicologal at left
    with dissolve

    show hermano_mayor at right
    with dissolve

    nietomayordelhijo "Abu."

    doc "Ester no habla con nadie desde hace días."

    scene hospital
    with fade

    show psicologal at left
    with dissolve
    
    show personaje_placeholder_blury:
        xalign 0.75
        yalign 1.0
    with dissolve

    show hija at right
    with dissolve

    hija "No sé para qué seguimos viniendo."
    hijo "Porque sigue siendo nuestra mamá."

    scene hospital
    with fade

    show psicologal at left
    with dissolve
    
    show ambar at right
    with dissolve

    esposa "Es mejor dejarla descansar."
    esposa "Volvemos otro día."

    scene hospital
    with fade
    
    pensamientoabuela "Esperen..."

    scene black
    with fade

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









    





















