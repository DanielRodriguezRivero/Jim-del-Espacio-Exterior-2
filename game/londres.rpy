init:
    
    $ persistent.visitado = False
    $ persistent.visitado2 = False
    
label londres: 
    
 if persistent.finbolas == False:
    if persistent.visitado == False:         #si no has visitado la ciudad
        scene londres1
        show sandrine
        sandrine "Ya estamos en la Gran Bretaña."
        sandrine "¿Se te ocurre donde podríamos comenzar a buscar?"
        p "Vosotras sois las profesionales..."
        "¡¡¡¡Notting Hill español!!!!"
        carmoine2 "Mira hacia allí, estudiantes españoles."
        anette2 "Deben ser Erasmus, están destrozando el mobiliario público."
        sandrine2 "Puede que sepan algo, no perdemos nada por interrogarles."
        hide londres1
        scene londres4
        p "Hola, perdona..."
        show borracho
        p "¿Qué estudias?"
        borracho "Pues no me acuerdo, ni siquiera recuerdo mi nombre."
        borracho "Lo único que sé, es que soy español, porque no entiendo ni papa de lo que me dicen los ingleses."
        borracho "Y es raro, porque en otras cogorzas sabía hablar hasta japonés."
        borracho "Debo de estar madurando."
        hide borracho
        carmoine2 "Mejor preguntemos a otro."
        show borracha
        p "¿Por casualidad no habréis visto unas bolas chinas azules verdad?"
        borracha "Uy, anoche me metí cuatro, déjame ver."
        anette2 "Tú y yo seríamos buenas amigas."
        borracha "Pues no, lo siento, pero lo que sí que he encontrado son las llaves de casa."
        hide borracha
        p "Había que intentarlo."
        show borracha
        borracha "Nos vamos al cementerio a apedrear la tumba del Dr. Who."
        borracha "¿Os venís?"
        p "No, gracias, tenemos asuntos que requieren nuestra atención."
        hide borracha
        show carmoine
        carmoine "Me he quedado sin ideas. Paseemos un rato. Eso nos despejará."
        hide carmoine
        scene londonc
        p "Aún recuerdo mi estancia en Irlanda como Erasmus."
        p "El último día, me sacaron a hombros del pub \"El unicornio negro.\""
        p "Y no me extraña, le pagué los estudios al hijo del tabernero."
        p "De vez en cuando me envia una postal contándome qué tal le va."
        hide londonc
        if persistent.entrada == False:
            # se llega hasta la puerta pero el bobby no deja entrar
            scene pakis
            carmoine2 "Mira que monos los inglesitos, cómo ven la tele embobados ante de la hora del té."
            sandrine2 "Eh, mirad esa tele de la izquierda."
            sandrine2 "¿Qué es eso que lleva la Reina en la mano?"
            anette2 "Un bolso monísimo de Mandarina Duck."
            carmoine2 "Color granate, mi preferido."
            sandrine2 "No, no, eso redondo y azulón."
            p "¡¡¡Una de las bolas del antídoto!!!"
            p "Tenemos que cogerla como sea."
            sandrine2 "¿Estás loco? ¿Sabes el dispositivo de seguridad que tiene la Reina a su alrededor?"
            carmoine2 "SSShh, están diciendo que se celebra una recepción en el Palacio de Buckingham."
            carmoine2 "Puede que sea nuestra oportunidad."
            p "¿Y cómo se va?"
            anette2 "..."
            sandrine2 "..."
            carmoine2 "..."
            p "Deberíamos pensar seriamente en comprar un mapa."
            p "O mejor aún, un GPS."
            $ renpy.play("banda.mp3")
            scene londres2
            $ renpy.pause(3.5)
            carmoine2 "Sigamos a la banda, seguro que nos llevan al palacio."
            p "O igual vienen de allí y vuelven a su cuartel."
            carmoine2 "Correremos el riesgo."
            scene guardia
            gu "Entrada, por favor."
            p "No tenemos, pero como usted no se puede mover, vamos a pasar de todas formas."
            $ renpy.play("punch.wav")
            scene guardia with vpunch
            $ renpy.pause(1.0)
            gu "Para no permitir la entrada de capullos sí que nos podemos mover."
            gu "Y mucho, además."
            p "Habrá que conseguir esa dichosa entrada..."
            show sandrine at left
            sandrine "Venga hombre, ¿voy a tener que enseñar los pechos para que este se anime?"
            gu "A mi no me molestaría."
            gu "Se sorprendería la de chicas que lo hacen."
            gu "Ahí mi compañero tiene en la garita unas doscientas fotos."
            gu "Las guardias nocturnas pueden llegar a ser muy aburridas."
            gu "Pero aún así debo negarme a dejarles pasar."
            p "Iremos a otra parte mientras."
            $ persistent.visitado=True
            jump map
        else:
            # lo mismo de arriba, solo que sigue con la trama
            scene pakis
            carmoine2 "Mira que monos los inglesitos, cómo ven la tele embobados."
            sandrine2 "Eh, mirad esa tele de la izquierda."
            sandrine2 "¿Qué es eso que lleva la Reina en la mano?"
            anette2 "Un bolso monísimo de Mandarina Duck."
            carmoine2 "Color granate, mi preferido."
            sandrine2 "No, no, eso redondo y azulón."
            p "¡¡¡Una de las bolas del antídoto!!!"
            p "Tenemos que cogerla como sea."
            sandrine2 "¿Estás loco? ¿Sabes el dispositivo de seguridad que tiene la Reina a su alrededor?"
            carmoine2 "SSShh, están diciendo que se celebra una recepción en el Palacio de Buckingham."
            carmoine2 "Puede que sea nuestra oportunidad."
            p "¿Y cómo se va?"
            anette2 "..."
            sandrine2 "..."
            carmoine2 "..."
            p "Deberíamos pensar seriamente en comprar un mapa."
            p "O mejor aún, un GPS."
            $ renpy.play("banda.mp3")
            scene londres2
            $ renpy.pause(3.5)
            carmoine2 "Sigamos a la banda, seguro que nos lleva al palacio."
            scene guardia
            gu "Entrada, por favor."
            show entrada at Position(ypos=400, yanchor=1.0)
            p "Aquí tiene."
            gu "Puede pasar." 
            gu "Disfrute de la fiesta."
            hide guardia
            scene trono
            show chambelan
            chambelan "El famoso escritor Spencer Fitzgerald y acompañantes."
            hide chambelan
            show doncella 
            reina "Esperábamos vuestra llegada."
            reina "Vuestro virtuosismo con las letras es famosa en toda la corte."
            reina "¿Seríais tan amable de recitar algún verso que nos encumbre a la cima de la lírica?"
            p "Por supuesto."
            #sonido de tos
            p "Majestad, está usted tan buena que la mataría a polvos en mitad de la calle y ningún jurado del mundo me encontraría culpable."
            $ renpy.play("grillos.mp3")
            $ renpy.pause(3.0)
            $ renpy.sound.stop(0,2)
            sandrine "Pst, esa no es la Reina."
            hide doncella
            $ renpy.pause(2.0)
            sandrine "Es esa."
            show reina at Position(ypos=540)
            $ renpy.pause(2.0)
            if persistent.hombre==False:
                reina "¡Hola guapa!"
            else:
                reina "¡Hola guapo!"
            p "Oh"
            "..."
            p "Pues lo mismo para usted, majestad."
            hide reina
            show chambelan
            chambelan "La Reina desea que visite sus aposentos privados más tarde."
            sandrine2 "Es tu oportunidad para hacerte con la bola."
            p "Preferiría que me encerraran en la torre de Londres con el hombre de la máscara de hierro."
            jim2 "Si no consigues esa bola, es lo que te haré."
            hide chambelan
            hide trono
            scene marco
            show expression Text("Lo que a continuación pasó, solo pueden imaginarlo las mentes más enfermas.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(2.5)
            hide text with dissolve
            $ renpy.pause(0.25)
            scene trono
            p "Conseguí la bola, pero necesitaré una aspiradora para quitarme tanto pelo de la boca."
            p "Alguien va a tener que pagarme mucho dinero por esto."
            $ persistent.visitado = True
            $ persistent.bolas += 1
            $ persistent.entrada=False
            if persistent.bolas == 3:   
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide trono
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide trono
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide trono
                jump map


    else:     # ya has visitado la ciudad
        if persistent.entrada==False:
            scene guardia
            "El guardia te sigue mirando raro, será mejor que vuelvas cuando tengas la entrada."
            hide guardia
            jump map
        else:
            scene guardia
            p "Ahora sí que nos dejará entrar ese estirado de guardia real."
            gu "Entrada, por favor."
            show entrada at Position(ypos=400, yanchor=1.0)
            gu "Gracias, puede pasar."
            hide entrada
            gu "Disfrute de la fiesta."
            hide guardia
            scene trono
            show chambelan
            chambelan "El famoso escritor Spencer Fitzgerald y acompañantes."
            hide chambelan
            show doncella 
            reina "Vuestro virtuosismo con las letras ha llegado a oídos de la corte."
            reina "¿Seríais tan amable de recitar algun verso que nos encumbre a la cima de la lírica?"
            p "Será un honor para mí."
            p "Majestad, está usted tan buena que la mataría a polvos en mitad de la calle y ningún jurado del mundo me encontraria culpable."
            $ renpy.play("grillos.mp3")
            $ renpy.pause(3.0)
            p "Majestad, está usted tan buena que la mataria a polvos en mitad de la calle y ningún jurado del mundo me encontraria culpable."
            sandrine "Pst, esa no es la Reina."
            hide doncella
            $ renpy.pause(2.0)
            sandrine "Es esa."
            show reina
            $ renpy.pause(3.0)
            if persistent.hombre==False:
                reina "¡Hola guapa!"
            else:
                reina "¡Hola guapo!"
                
            p "Oh"
            "..."
            p "Pues lo mismo para usted, majestad."
            hide reina
            show chambelan
            chambelan "La Reina desea que visite sus aposentos privados."
            sandrine2 "Es tu oportunidad para hacerte con la bola."
            p "Preferiría que me encerraran en la torre de Londres con el hombre de la mascara de hierro."
            jim2 "Si no consigues esa bola es lo que te haré."
            hide chambelan
            hide trono
            scene marco
            show expression Text("Lo que a continuación pasó, solo pueden imaginarlo las mentes más enfermas.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(2.5)
            hide text with dissolve
            $ renpy.pause(0.25)
            scene trono
            p "Consegui la bola, pero necesitaré una aspiradora para quitarme tanto pelo de la boca."
            #no debi morder la almohada
            p "Alguien va a tener que pagarme mucho dinero por esto."
            $ persistent.entrada=False  #para que se vuelva al a descripcion generica de antes
            $ persistent.bolas += 1
            if persistent.bolas == 3:   
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide trono
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide trono
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide trono
                jump map

            
 else:   # saga de bolas terminada
     
    if persistent.visitado2 == False:  
        $ persistent.visitado2 = True
        scene londresno
        sandrine2 "¿Crees que encontraremos por aquí a alguien afectado por el falo de la risa?"
        p "Por mirar no perdemos nada."
        anette2 "¿Por qué no vamos a ver qué están haciendo los erasmus?"
        p "Estaban por el cementerio, ¿no?"
        anette2 "Creo que sí."
        p "Supongo que será más alegre que esto..."
        hide londresno
        scene cementerio
        $ renpy.pause(1.0)
        p "Esto está muy desierto."
        p "No hay ni rastro de los estudiantes."
        jim2 "Se los habrá tragado la tierra."
        jim2 "O se habrán caido en una fosa recien cavada, con el ciego que llevaban no me extrañaría..."
        #scene bg black
        $ renpy.play ("under.mp3")
        $ renpy.pause(6.0)
        hide cementerio
        scene bg black with Fade(.25, 0, .75, color="#fff") 
        scene cementerio
        show undertaker
        $ renpy.pause(3.0)
        enterrador "Pablito, ¿eres tú?"
        p "S..s...sí, soy yo."
        if persistent.hombre==True:
            enterrador "Tienes la voz demasiado grave."
            p "Es que estoy resfriado."
        enterrador "¿Por qué te fuiste de mi lado?"
        p "Estaba en el médico."
        enterrador "Vino un tipo llamado Batista a meterse conmigo."
        enterrador "Pero el muy estúpido no sabía lo que hacía." 
        enterrador "Le quité el título."
        enterrador "Le quité el alma."
        enterrador "Sus entrañas."
        enterrador "Su casa en la playa."
        enterrador "Su colección de muñecos de Star Wars, con el de \"Friki matando a Jar Jar Binks\" incluido."
        enterrador "Su novia."
        enterrador "Sus ganas de vivir."
        enterrador "Y su pasión por las flores."
        enterrador "No me quedó nada más por quitarle, así que me echaron de la WWF, la NWO, NWC, WWE..."
        enterrador "De la lucha libre en general."
        p "To...t...tómate estas píldoras, y verás cómo te vuelven a llamar."
        enterrador "Confío en tí, pablito."
        enterrador "Porque como no me llamen..."
        enterrador "Bailaré sobre tu tumba."
        $ renpy.play(0.5)
        enterrador "Otra vez."
        p "Tienes que buscarte otras aficiones."
        p "Salir con los amigos a tomar unas cervezas, cosas así."
        $ renpy.pause(2.0)
        hide undertaker
        p "Por un momento pensé que no funcionaría."
        p "De los chicos sigue sin haber rastro, debe de habérselos comido el tipo este."
        jim2 "O puede que se cansaran de sus pueriles gamberradas y volvieran a casa."
        $ renpy.sound.stop(0,2)
        hide cementerio
        jump map

    else:       
        # terminado
        scene londres3
        "Como un episodio de Benny Hill, cuyo inicio preludiaba la aparición del puente de Westminster, se puede calificar tu aventura."
        "Solo que no has perseguido a ninguna rubia, ni un viejo disfrazado de policía ha querido darte con su porra."
        "Qué triste..."
        show erizo at Position(ypos=450)
        erizo "¡¡¡Dinsdale!!!"
        hide erizo
        hide londres3
        jump map
