init: 
    
    $ persistent.vsm = False               #variable visitado san marino
    $ persistent.vsm2=False
    
label marino:
    if persistent.finbolas==False:
        if persistent.vsm==False:
            scene marino
            p "El ambiente prebélico se puede cortar con un cuchillo."
            jim2 "Mis datos históricos no dan cuenta de ningún conflicto en ese lugar del continente."
            p "Le preguntaré a ese joven que viene por allí."
            soldado2 "Alto, ¿quién vive?"
            p "¿Viva el GUA?"
            hide marino
            scene soldier
            soldado2 "¿El GUA?"
            soldado2 "No me suena. ¿Es una facción del miniejército rojo de San Marino?"
            p "Si te digo que sí, ¿me dejarás pasar?"
            soldado2 "Por supuesto, con un kilo de plomo en tu estómago."
            jim2 "Aquí sí que saben dar la bienvenida."
            p "Entonces no, no."
            p "Somos de tu bando."
            soldado2 "Aun así no puedes pasar si no eres de aquí."
            p "¿Yo? De toda la vida."
            soldado2 "Mmmmm"
            soldado2 "¿De qué parte de San Marino eres?"
            p "De la de la casa amarilla."
            soldado2 "Puedes pasar."
            scene marinoc
            $ renpy.pause(1.0)
            megafonia "Atención, mensaje de nuestro comandante en jefe Dwight D. Eisenhower."
            ike "Ciudadanos libres de San Marino: durante años, los comunistas del PCSM han gobernado con mano de hierro estas tierras."
            ike "Mucho hemos combatido contra su tiranía, con la esperanza de que la luz de la libertad iluminara la senda de nuestro futuro."
            ike "Hoy, ese momento está más cerca que nunca."
            ike "En vuestros hombros, soldados del Frente de Liberación de San Marino, reposa el destino de toda una nación."
            ike "Solo puedo prometeros la victoria total, la aniquilación de nuestros enemigos y la gloria eterna."
            ike "Eso es todo."
            jim2 "Parece que no hemos venido en buen momento."
            show sargento at Position(ypos=500)
            sargento "¿Qué haces aquí pedazo de escoria?"
            if persistent.hombre==False:
                sargento "¿Acaso la señorita no quiere mezclarse con la gentuza que va a derramar su sangre por el derecho a decir lo que se piensa?"
            else:
                sargento "¿Acaso el señorito no quiere mezclarse con la gentuza que va a derramar su sangre por el derecho a decir lo que se piensa?"
            p "Yo..."
            sargento "¡¡¡¡¡Corre gusano si no quieres que apague mi puro en tu culo y luego te lo haga comer!!!!!"
            scene base
            $ renpy.play("marching.wav")
            soldados "¡Me cago en esta puta guerra!"
            soldados "¡Con lo bien que estaría mi menda de juerga!"
            soldados "1... 2..."
            soldados "¿Qué somos?"
            soldados "¡Los San Marino Killers!"
            soldados "3... 4...."
            soldados "¿Y qué hacemos?"
            soldados "¡Matar, matar, matar, comer, matar, matar, cenar y dormir!"
            $ renpy.sound.stop(0,2)
            show sargento at Position(ypos=500)
            sargento "¿Veis al enemigo?"
            sargento "Esos que están a escasos veinte metros de nosotros son el miniejército rojo de San Marino:"
            extend " Los cabrones más grandes que ha parido una perra."
            sargento "¿De dónde eres recluta?"
            $ lugar = renpy.input (prompt)
            sargento "En %(lugar)s solo hay vacas y maricones; y no veo que tengas ningún CD de Barbra Streisand, así que debes de ser una vaca."
            p "..."
            sargento "Así que es eso, has venido aquí a que te ordeñe."
            if persistent.hombre==False:
                sargento "Apuesto a que eso te pone cachonda."
                p "La verdad es que sí."
                sargento "Con esas ubres no llenarías ni medio vaso de leche."
                sargento "No quiero mujeres cerca de mí. Y mucho menos en mi ejército."
                sargento "¡Fuera de mi vista, gusano!"
            else:
                sargento "Apuesto a que eso te pone cachondo."
                p "La verdad es que sí."
                $ renpy.play(2.0)
                sargento "Después de todo no eres una vaca..."
                $ renpy.play(1.0)
                sargento "Fuera de mi ejército. Quiero tener mi retaguardia bien cubierta, pero no de \"esa\" manera."  
            hide sargento
            jim2 "Fue una suerte que te dejaran salir, parece que se esté preparando una buena."
            p "Y que lo digas, será mejor que siga con mis investigaciones."
            $ persistent.vsm=True
            if persistent.bolas == 3:  
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide base
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide base
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide base
                jump map
        else:
            #terminado
            scene marino
            p "Será mejor que vuelva en otra ocasión, se están entrenando en lucha muy cuerpo a cuerpo."
            hide marino
            jump map
    
    else:  #saga fin bolas terminada
        if persistent.vsm2==False:
            scene despacho2
            show ike
            p "Hola, quienquiera que este debajo de ese rostro."
            p "Métase esto, por favor."
            ike "Guardias, guardias, ¡¡¡intenta matarme!!!"
            p "No sea paranóico."
            p "Solo intento volverlo a su estado normal"
            ike "Yo he sido siempre asi, bueno de joven tenia pelo,pero la edad no perdona"
            p "¡¡¡Usted no es Eisenhower!!!"
            ike "¿Qué le hace pensar eso?"
            p "¡¡¡Que lleva más de cuarenta años muerto!!!"
            show ike at right with move
            show guardiap at left
            guardia "¿Qué ocurre, señor?"
            if persistent.hombre==False:
                ike "Esa loca ha intentado meterme... meterme... ¡¡¡ESO!!!"
            else:
                ike "Ese loco ha intentado meterme... meterme... ¡¡¡ESO!!!"
            if persistent.hombre==False:
                ike "¡¡¡Aporreadla!!!"
                guardia "Señor, a una mujer no se le levanta la mano."
                ike "Pues rompedle entonces todo su vestuario."
                guardia "Señor, eso es asquerosamente machista."
                ike "¿Despeinadla?"
                guardia "¿Usted no tiene madre, señor?"
                ike "Algo tendremos que hacer. No podemos dejar este intento de... "
                extend " ¡Hay que castigarla!"
                guardia "Señor, podríamos..."
                guardia "Bsss, bsss, bssss."
                ike "Muy buena idea."
                ike "Señorita, le ofrezco la posibilidad de redimirse de su afrenta comandando una misión suic..." 
                extend " muy difícil."
            else:
                ike "Dadle una paliza."
                guardia "Señor, está escuchimizado, sería como pegarle a un niño."
                ike "Pues métele un dedo en el ojo."
                guardia "Tiene gafas, señor."
                ike "Algo tendremos que hacer. No podemos dejar este intento de... "
                ike "Hay que castigarlo."
                guardia "Señor, podríamos..."
                guardia "Bsss, bsss, bssss."
                ike "Muy buena idea."
                ike "Señor, le ofrezco la posibilidad de redimirse de su afrenta comandando una misión suic... muy difícil"
            p "Lo que sea con tal de largarme de aquí."
            ike "Veo que es usted razonable."
            ike "Ayer desapareció está mujer mientras realizaba un servicio."
            hide guardiap
            hide ike
            show elvira2
            p "Me puedo hacer una idea de qué tipo de servicio se trataba"
            ike "Pues se equivoca."
            ike "Se llama Elvira. Creemos que ha sido secuestrada por el Miniejército Rojo de San Marino."
            ike "Aunque no tenemos información muy precisa, creemos que la mantienen retenida en Venecia."
            hide elvira2
            show ike
            ike "Por supuesto, de ser así, contarían con la complicidad absoluta de las autoridades italianas; lo que nos llevaría a contestar con una represalía."
            ike "Así pues deberá viajar hasta la ciudad de los canales, comprobar si se encuentra allí y en caso afirmativo, traerla de vuelta."
            ike "Es de vital importancia para la moral de las tropas."
            show ike at left with move
            show sargenta at right
            ike "Para asegurarnos de que no escapará en cuanto cruce la puerta, irá acompañada por la sargento Sanchez, aquí presente."
            sargenta "Más bien me acompañará a mí."
            p "Mucho gusto."
            ike "Partirán en media hora."
            hide sargenta
            hide ike
            hide despacho2
            scene marco
            show expression Text("Venecia, prostíbulo de Europa venido a menos...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text
            scene venecia1
            show sargenta at right
            sargenta "Ahí la tienes, la ciudad sobre las aguas."
            sargenta "Inteligencia naval cree que Elvira puede estar retenida en ese edificio de la izquierda."
            p "¿Cómo entraremos?"
            sargenta "Este es el plan:"
            extend " Tú escalarás por la pared norte hasta la última planta. Lo más probable es que la retengan allí."
            sargenta "Mientras, yo entraré por la puerta principal y acabaré con quien esté dentro creando una distracción que te hará las cosas más fáciles."
            p "Me parece un buen plan."
            sargenta "¡Adelante!"
            scene alturas
            p "Desde abajo no parecía tan grande."
            p "Qué alto está esto."
            p "Sabía que debía haberme pedido entrar por la puerta."
            p "Si ni siquiera podía subirme al taburete del bar."
            p "Oh dios mío, las fuerzas me fallan, voy a caer." 
            p "Aquí se terminan mis días como espía y la novela visual."
            p "Adiós, mundo cruel..."
            scene ardilla
            ardilla "¡Rápido!"
            ardilla "¡Cógete a mi mano!"
            p "¿De donde sales tú?"
            ardilla "Me envía el señor de las bestias, para que veas que no te guarda rencor por haberle plagiado el título."
            p "Gracias, amiga ardilla."
            ardilla "Bueno yo me voy. Ah , y soy un hamster."
            hide ardilla
            scene sala
            show sargenta 
            p "¿Qué tal te fue?"
            sargenta "Me enfrenté a libidinosos hombres pulpo, zombis, asesinos maníacos y un par de perros."
            sargenta "¿Y a tí?"
            p "Me salvó la vida una ardilla."
            $ renpy.play("silla.mp3")
            $ renpy.pause(2.0)
            sargenta "A cubierto, he oído algo."
            scene guitarra
            $ renpy.pause(2.0)
            p "Es muy buena, se ha mimetizado en una guitarra, que a su vez se ha mimetizado con el suelo."
            p "Me esconderé detrás de ella."
            $ renpy.pause(2.5)
            hide guitarra
            scene sala
            show sargenta
            sargenta "Parece que fue una falsa alarma."
            p "Habrá sido el hamster de antes."
            sargenta "Entra en la habitación, yo me quedo aquí cubriendo la retaguardia."
            hide sargenta
            hide sala
            show elvira at Zoom((800, 600), (0, 0, 800, 600), (506, 376, 92,64), 3.0)
            p "Qué ojos más bonitos tienes."
            elvira "¿Ah sí? ¿Y de qué color son?"
            p "Rosa chicle"
            elvira "Ejem..."
            show elvira at Zoom((800, 600), (506, 376, 92, 64), (0, 0, 800,600), 3.0)
            elvira "No me molesta que me mires las tetas, de hecho si las enseño son para algo, pero no me gusta que me babeen encima."
            p "Lo siento, fue un acto reflejo."
            elvira "¿Podemos irnos ya?"
            hide elvira
            scene marco
            show expression Text("La huida del edificio no fue fácil. Tuvieron que luchar contra la reencarnación de Al Lowe y sus mujeres piratas, con erótico resultado. Pero al final, lograron llegar sanos y salvos a la seguridad de San Marino.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text
            scene despacho2
            show ike
            ike "El pueblo libre de San Marino agradece sus servicios." 
            ike "Ya ajustaremos cuentas con los italianos, pero ahora no."
            ike "Dentro de poco, tendremos que atacar al enemigo."
            ike "Le invito a contemplar la ofensiva conmigo."
            $ persistent.vsm2=True
            jump map
        else:
            if persistent.finguerra==False:
                if persistent.vfg==False:  # vuelta antes de terminar la guerra
                    jump guerramarino
                else:
                    scene despacho2
                    show ike
                    ike "Seguimos buscando juez."
                    hide ike
                    hide despacho2
                    jump map
            else:
                scene marino
                show ike 
                ike "Estamos reconstruyendo un nuevo futuro bajo la premisa de que todas las personas son libres para gastar el dinero que nos dan los americanos."
                ike "Y usted es en parte responsable de ello."
                ike "Gracias de corazón."
                hide ike
                hide marino
                jump map
            
    # cantico: si en la guerra hay que luchar, antes yo quiero follar


    
label guerramarino:
    scene despacho2
    show ike at Position(ypos=550)
    ike "Ah, usted por aquí de nuevo."
    ike "Con Elvira de vuelta, la moral de los muchachos subió como la espuma justo cuando vamos a atacar."
    p "Apuesto a que subió más cosas."
    ike "Venga a mi sala de mando."
    ike "Seguiremos el combate desde allí."
    hide despacho2
    scene despacho3
    show ike at Position(ypos=540)
    ike "Es hora de atacar. Espero que los americanos nos apoyen."
    "Según su embajador, nos apoyan al 100 por 100."
    ike "Espero que intervengan si tenemos problemas."
    hide despacho3
    scene barco
    show expression Text("Mientras tanto en el portaaviones USS Eisenhower (paradojas de la vida) buque insignia de la 6ª flota en el Mediterráneo...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(4.5)
    hide text
    almirante "Alférez, el otro día estuve en el mando espacial del CONUS y me ofreció un bocata de tortilla cojonudo."
    alferez "Debió de estar delicioso, señor."
    almirante "Hazme tu otro. Como no te salga igual de bien, te paso por la quilla."
    hide barco with fade
    scene despacho3
    ike "Pondré la radio, a ver qué tal van las tropas."
    $ renpy.play("marcha.mp3")
    $ renpy.pause(5.0)
    sold "Mi capitán, ¿por qué toca el gaitero si nosotros somos italianos como quien dice?"
    cap "Cállate soldado y sigue marchando."
    $ renpy.play("interferencia.wav")
    $ renpy.pause(3.0)
    ike "Subteniente, quiero imágenes desde el satelite, ¡ya!"
    $ renpy.sound.stop(0,2)
    satel "¿Qué canal? ¿Spice channel? No, ese quebró, ¿Playboy TV? ¿VIVA? ¿TV Mozambique? Creo que ahí dan el Barça..."
    ike "Inepto, quiero imágenes del campo de batalla, ¡¡¡¡YA!!!!"
    scene telv
    $ renpy.play("hy.mp3")
    ike "Aquí no se ve una mierda."
    satel "Un segundo, señor."
    $ renpy.sound.stop(0,2)
    scene capitol
    p "Uau, parece que hay fuego intenso en el centro de la capital."
    hide capitol
    scene guer
    p "Parece que a la aviación le están dando duro."
    scene nuclear
    p "Oh oh, parece que alguien la cagó."
    ike "Deje de mirar la Playstation y venga aquí."
    scene campb
    ike "A ver si terminan de jugar..."
    ike "Como San Marino es tan pequeño, tenemos que alquilar ese estadio a Suiza para poder combatir a nuestras anchas."
    ike "Nuestro tanque no podría moverse en las calles tan estrechas de nuestro país."
    $ renpy.play("tank.wav")
    $ renpy.pause(1.0)
    ike "Ah, ahí llega."
    ike "Vamos a borrar su recuerdo de las páginas del libro de la historia."
    $ renpy.pause(1.0)
    scene marco
    show expression Text("Durante horas los dos bandos lucharon con furia suicida hasta que finalmente decidieron darse un respiro ante la ausencia de avances significativos por las dos partes.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(7.0)
    hide text with dissolve
    $ renpy.pause(0.25)
    scene despacho3
    show ike at Position(ypos=550)
    ike "Joder, nos han jodido el jodido tanque con una jodida mina."
    ike "La situación está estancada."
    p "No soy militar, pero creo que deberían resolver la situación de otra forma."
    ike "Oh sí, y ¿cómo?"
    ike "Vamos donde están ellos y les decimos \"por favor señores rojos, ¿pueden rendirse?, de lo contrario le dedicaremos una ácida crítica en el periódico universitario."
    ike "Que por cierto es una mierda, solo habla de Ismael Serrano."
    p "Ya que habla de un cantante, ¿qué le parece un concurso de canciones?"
    ike "Mmm, es una idea tan absurda que podría funcionar."
    ike "Pero necesitamos a alguien imparcial."
    ike "¿Dónde podríamos encontrar a alguien intachable para que ejerza de juez?"
    p "¿En la ONU?"
    ike "He dicho alguien intachable."
    $ persistent.guerra=True
    $ persistent.vfg=True
    hide ike
    hide despacho3
    jump map
    
