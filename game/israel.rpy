init:
    
    $ persistent.vi = False        #variable visitado israel
    
label israel:
    if persistent.finbolas==False:
        
        if persistent.vi == False:  #primera visita
            scene jerusalen
            p "Siempre quise visitar Tierra Santa, me encantan los fuegos artificiales."
            hide jerusalen
            scene jerus
            show mc at left
            show dj at right
            mc "¡Hola, hola, hola!"
            dj "¿Qué tal?"
            mc "Estábamos mi colega Dj Jerichó y yo ahí sentados, cuando he visto a un grupo de chicas guapas y nos hemos dicho:"
            dj "Vamos a acercarnos porque tienen una cara de turistas que no se las quita nadie."
            mc "Y aquí a los turistas les pueden pasar cosas malas si se meten donde no deben."
            dj "Seremos vuestros guías."
            p "Muy amables."
            mc "Aquí donde nos vemos, somos rappers."
            dj "Pero no uno de esos que insulta hasta a su abuela."
            mc "Nosotros hemos creado un nuevo subgénero:"
            dj "El villancico Rap. Hemos comenzado una gira aquí en Jerusalén para ponerlo de moda."
            carmoine2 "¿Un villancico rapeado?"
            carmoine2 "Eso tiene que sonar mal a la fuerza."
            dj "Deja que te cantemos algo."
            dj "Es nuestro primer trabajo: In the guetto born."
            dj "¡¡¡¡Vamos MC Josafat living from Jerusalem!!!!"
            mc "Ah, ah , ah , ah"
            mc "En esta tierra santa, donde están a la que salta,"
            mc "nació el niño dios, lo envolvieron en la manta."
            mc "A adorar a Jesús, el nombre del churumbel,"
            mc "llegaron mil pastores, llegaron por doquier."
            dj "Venimos a ver al rey de nuestro pueblo"
            dj "Y a ver si de paso, me cura este huevo."
            mc "Cállate blasfemo, no le hables así a un niño"
            mc "Como te coja dios, te va a dar un buen piño."
            dj "Que viva el nuevo rey, viva nuestro señor."
            dj "Siempre en estas fechas comeremos el turrón."
            mc "Cantaremos villancicos, este villancico rap,"
            dj "apto para los niños y para sus papás."
            sandrine2 "Nunca he escuchado nada igual."
            mc "¿Verdad que no?"
            dj "Esperamos dar el pelotazo pronto, pero mientras nos ganamos la vida como guías."
            dj "Y hablando de guías, pongámonos en marcha, ¿no?"
            mc "Lo típico es ir a ver primero el muro de las lamentaciones."
            p "Por mí, vale."
            hide dj
            hide mc
            hide jerus
            scene mezquita
            show mc at right
            show dj at left
            mc "Mira la mezquita, ahí la tienes bien cerquita."
            dj "Más no te acerques, o te romperán los dientes."
            mc "Estos musulmanes, son unos animales."
            dj "Tras un buen polvete, nos tiran sus cohetes."
            hide mc
            hide dj
            hide mezquita
            scene muroj
            hide muroj
            scene muroj with vpunch
            $ renpy.play("punchhard.wav")
            p "¿Quién me ha tirado una pedrada?"
            show mc at right
            show dj at left
            mc "Son esos palestinos de allí."
            dj "Es su deporte nacional, apedrear a la gente."
            p "¡¡¡¿Cómo queréis una tierra propia si me la estáis tirando toda encima?!!!"
            dj "No te molestes, no vale de nada."
            mc "Esos palestinos tiran con gran desatino"
            dj "aunque los jodios no le dan ni un poco al vino."
            mc "El JB es lo que le va a esa gente."
            dj "Beben a escondidas y si dicen no es que mienten."
            hide dj
            hide mc
            hide muroj
            scene muro
            show mc at left
            show dj at right
            mc "Y este es el muro. Te dejaremos solo para que la energía mística fluya por tu ser."
            dj "Si necesitas algo, por aquí estaremos."
            hide dj
            hide mc
            p "Es impresionante..."
            p "Mmm, aquí parece haber una inscripción."
            "\"Aqui estuvo Sir Daniel. Que estas inmortales piedras sean testigos por los siglos de mi amor incondicional y sincero por mi amada Lady Carme."
            p "Ah, al lado pone otra..."
            "\"Gamberro, no rayes el muro. ¡Como llame a los de la UNESCO te vas a enterar!\""
            jesus "psche"
            p "¿Quién me habla?"
            jesus "¿Quién va a ser, cojones? Soy YO. Verme a comprar un paquete de Ducados, pisha, que ninguno de estos me hace caso."
            p "Eh... creo que la pedrada en la cabeza de antes me afectó un poco."
            p "Creo que me iré lentamente..."
            $ persistent.vi = True
            if persistent.bolas == 3:   
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide muro
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide muro
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide muro
                jump map
        else:
            #terminado
            $ renpy.play ("atrapado.mp3")
            scene jerusalen
            radio "Buenos días, queridos oyentes."
            radio "Amanece de nuevo en la capital espiritual del mundo."
            radio "¿Qué nuevo altercado nos traerá este día?"
            radio "Para empezar, el tiempo: se prevén ventiscas de potencia moderada, con vientos capaces de apagar el cocktel Molotov más explosivo."
            radio "Así que no os molestéis en salir de casa."
            sandrine2 "¿Y si nos vamos a la fiesta del hotel Rey David?"
            sandrine2 "Me han dicho que hay barra libre."
            radio "A los que se dirijan al hotel Rey David, una mala noticia."
            radio "Ha ardido hasta los cimientos por un incendio provocado por un cocktel Molotov."
            carmoine2 "Pues nada, sigamos nuestro camino."
            p "Qué extraño, tengo la sensación de haber vivido esto antes."
            hide jerusalen
            jump map
        
    else: #saga bolas terminada  
        if persistent.vi2==False:
            if persistent.modelos==False:
                $ persistent.vi2=True
                scene calleisrael
                show jehov
                if persistent.hombre==False:
                    jehov "Perdone, hija de dios, ¿se ha parado a pensar alguna vez en la magnificencia de la obra de Jehova?"
                else:
                    jehov "Perdone, hijo de dios, ¿se ha parado a pensar alguna vez en la magnificencia de la obra de Jehova?"
                p "Oh no se molesten, yo también soy testigo de Jehova."
                jehov "¿Puede enseñarnos el carnet?"
                p "Esto... creo que me lo dejé en casa."
                jehov "Ve a por él, nosotros te esperamos."
                hide jehov
                p "Jim, recuérdame que no pasemos por aquí más."
                hide calleisrael
                jump map
            else:
                $ persistent.vi2=True
                scene muro
                p "¿Hola?"
                jesus "Hombre, tú por aquí."
                p "Pues sí, pasaba por aquí y bueno, hace un rato hablé con unas chicas muy simpáticas... y en fin..."
                jesus "Desembucha, no tengo todo el día, ¿sabes?"
                p "Verá, venía a pedirle un milagro."
                jesus "Hombre, solo se acuerdan del pobre Jesús, cuando quieren que su novia no salga huyendo el dia de la boda, cuando pasan la revisión de su 600 o cuando forman trios con gemelas..."
                jesus "¿Te acuerdas de lo del tabaco?"
                p "Si, claro."
                jesus "Pues ya sabes"
                p "¿Ducados, verdad?"
                jesus "Y sin filtro a ser posible."
                p "Voy a por ellos."
                $ persistent.muro=True
                if persistent.tabaco==False:
                    hide muro
                    jump map
                else:
                    scene muro
                    $ persistent.milagro=True
                    p "Son Celtas, espero que eso no influya."
                    jesus "Hombre, los hay mejores, pero bueno..."
                    jesus "Se agradece el gesto."
                    jesus "Tuyo es el milagro."
                    hide muro
                    jump map

        else:  #segunda visita o mas  #mirar
            if persistent.modelos==False: #no ha hablado con modelos
                scene calleb22
                "DJ Jericho y MC Josafat animan con escaso éxito a los transeuntes con sus rimas, a la espera de que les den una limosna."
                "Algo te dice que el villancico-rap tardará varios años en despegar."
                hide calleb22
                jump map
            else:  #hablo con modelos
                if persistent.tabaco==False:  #si no compro el tabaco, va a 
                    scene murow
                    "La gente se apiña en los aledaños del muro de las lamentaciones. Ninguno lleva un misero cigarrillo para el Mesías."
                    $ persistent.muro=True
                    hide murow
                    jump map
                else:  # ya ha vuelto, tiene el tabaco
                    scene muro
                    p "Aquí tienes, Dios."
                    $ persistent.milagro=True
                    p "Son Celtas, espero que eso no influya en lo del milagro."
                    jesus "Hombre, los hay mejores, pero bueno..."
                    jesus "La necesidad hace mucho."
                    jesus "Se agradece el gesto."
                    jesus "Tuyo es el milagro."
                    $ persistent.tabaco=False
                    hide muro
                    jump map
