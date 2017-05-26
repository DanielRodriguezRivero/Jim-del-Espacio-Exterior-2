init:
    
    $ persistent.va = False       #variable visitado atenas
    $ persistent.atenas2=False
label atenas:
    if persistent.finbolas == False:
        if persistent.va == False:
            $ persistent.va = True
            scene acantilado
            p "Tendremos que quejarnos al dueño del mapa. Nos ha dejado a las afueras de la ciudad."
            p "Ahí hay un cartel, a ver si pone algo de hacia dónde debemos ir."
            hide acantilado
            scene cartel2
            $ renpy.pause(4.0)
            hide cartel2
            scene acantilado
            p "Volvería a casa si pudiera."
            $ renpy.play("llorar.wav")
            $ renpy.pause(1.5)
            anette2 "¿No escucháis a alguien llorar?"
            anette2 "Creo que viene de lo alto de esa colina."
            hide acantilado
            scene atenas2
            show dragon
            dragon "Pobre de mí, pobre de mi existencia."
            dragon "Primero a la sombra del enchufado de Seiya, que pegó el braguetazo del siglo."
            dragon "Y ahora relegado a segundón por ese aficionado a las letras de Mr Roboto."
            p "¿Qué te ocurre?"
            dragon "O perdonad, dejad que enjuague mis lágrimas por la suerte que me ha tocado vivir."
            carmoine2 "Vamos, anímate, seguro que tu problema tiene solución."
            dragon "Ojala, pero a no ser que podáis convencer a Mr Roboto de que me dé más protagonismo en esta historia, me temo que persistiré en mi depresión."
            carmoine2 "¿Has hablado con él? ¿Le has pedido explicaciones de por qué no te da más peso en la novela?"
            dragon "Sí, me contestó que mi higiene personal dejaba que desear."
            sandrine2 "La verdad es que tienes el pelo hecho un asco, además recogido con esa cuerdecilla."
            p "!!!Es la cuerda de las bolas!!!"
            p "Tenemos que conseguirlas como sea."
            hide atenas2
            if persistent.champu==False: # si no lo tienes
                scene atenas2
                show dragon
                p "Intentaremos ayudarte, pero tendrás que darnos algo a cambio."
                dragon "Pedid lo que queráis."
                p "Ese coletero que llevas."
                dragon "Cuando me deis una solución a mi problema, vuestro será."
                punto "A ver si encuentro un caballero del zodiaco por aquí."
                hide dragon 
                hide atenas2
                jump map
            else:
                $ persistent.segunda=True
                scene atenas2
                anette2 "%(name)s ¿recuerdas nuestra última visita a Roma?"
                p "¡¡¡Es verdad!!! Lo intentaré"
                p "Hombre, por casualidad tengo esta bolsita de champú que seguro que te viene de perlas."
                p "Con el pelo limpio, seguro que Mr Roboto recapacita."
                dragon "Por la inexistente ropa interior de Atenea, es el mejor regalo que me han hecho."
                dragon "Tomad mi coletero, mientras limpio mi castigada cabellera."
                dragon "Con el pelo sedoso y brillante como el de una colegiala, seguro que Roboto me da un papel protagonista."
                p "Otra para el bote, chicas."
                $ persistent.bolas +=1
                if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                    if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                        hide atenas2
                        jump enlace
                    else:
                        "Aún debo visitar el resto de ciudades de Europa."
                        hide atenas2
                        jump map
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide atenas2
                    jump map
        else:
            if persistent.champu==False:
                if persistent.segunda==False:
                    scene atenas3
                    "Puedes ver al caballero del zodiaco sentado junto a la fuente."
                    show dragon 
                    dragon "Pobre de mí, pobre de mí, que ya se han acabao las fiestas de San Fermín y sigo siendo un segundón." 
                    hide dragon
                    hide atenas3
                    jump map
                else: # ha vuelto ya despues de  darle el champu
                    scene atenas1
                    "Puedes ver a Shiryu junto al río, con la cabeza metida en el agua. Le llevará horas lavarse el pelo."
                    "Lo que no sabe, es que Mr Roboto ya ha terminado de escribir la historia y va a pasar a la posteridad como el tío que se lavó la cabeza."
                    hide atenas1
                    jump map
                    
            else:
                scene atenas2
                anette2 "%(name)s ¿recuerdas nuestra última visita a Roma?"
                p "¡¡¡Es verdad!!! Lo intentaré."
                show dragon
                p "Hombre, por casualidad tengo esta bolsita de champú, que seguro que te viene de perlas."
                p "Con el pelo limpio seguro que Mr Roboto recapacita."
                dragon "Por la inexistente ropa interior de Atenea, es el mejor regalo que me han hecho."
                dragon "Tomad mi coletero mientras limpio mi castigada cabellera."
                dragon "Con el pelo sedoso y brillante como el de una colegiala seguro que Roboto me dá un papel protagonista."
                p "Otra para el bote, chicas."
                hide dragon
                hide atenas2
                $ persistent.bolas += 1
                $ persistent.champu=False
                $ persistent.segunda=True
                if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                    if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                        hide atenas2
                        jump enlace
                    else:
                        "Aún debo visitar el resto de ciudades de Europa."
                        hide atenas2
                        jump map
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide atenas2
                    jump map
                    
    else:  # saga de bolas terminada
        if persistent.atenas2==False:
            $ persistent.xman=True
            scene atenasv
            p "Si los griegos no fueran tan salvajes, podría vivir aqui."
            show xman at Position(ypos=550)
            xman "¿He escuchado salvaje?"
            xman "Xman, rey del porno, es el más salvaje en la cama."
            p "Es bueno saberlo."
            xman "Con mi ojo biónico puedo ver todo el porno que me ponen por delante en segundos."
            xman "Y mi mano, también biónica... Ya te imaginarás lo que hace."
            p "Por casualidad no tendrás unas cuantas fotos de esas guarras de sobra, ¿no?"
            p "Porque tú tienes muchas de esas, ¿no?"
            xman "Oh sí, tengo millones."
            xman "Señálame una mujer y encontraré en mi archivo una foto suya en pelotas."
            xman "Mmmm, tengo por aquí unas..."
            p "Las que sean, acepto cualquier cosa."
            xman "¿Sabes qué es el BDSM?"
            hide xman
            hide atenasv
            scene marco
            show expression Text("Atonitos contemplaron el desfile de imagenes de cuero, cera derretida y posiciones humillantes...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text
            p "Me serán de mucha ayuda."
            p "Por cierto, ¿qué te parece esto?"
            show bolas at left 
            show xman at right with move
            xman "Un maravilloso objeto para mi colección."
            p "Y saben a fresa."
            xman "Quiero probarlo."
            hide xman
            p "Hemos librado al mundo de un pornógrafo más."
            $ persistent.atenas2=True
            hide atenasv
            jump map
        else:
            scene atenasc
            p "Oh no, es el niño ese repelente."
            p "Salgamos de aquí a toda prisa."
            hide atenasc
            jump map