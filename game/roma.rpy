init:
    $ persistent.vroma = False
    $ persistent.vroma2 = False
label roma:
    if persistent.finbolas==False:
        
        if persistent.vroma == False:
        # se conoce a los japoneses
            scene rome3
            $ persistent.vroma = True
            jim2 "Italia, los franceses del Eje."
            jim2 "Mussolini mandó fusilar a las señales de tráfico durante su mandato, lo que se ha traducido en un caos circulatorio continuo."
            p "Pues a los japoneses que hay por aquí no deben de importarles mucho los accidentes de tráfico."
            p "Están fotografiando todo lo que se mueve y lo que lleva parado desde hace más de dos mil años."
            jim2 "No te distraigas con las japonesas y sigue con la investigación."
            p "Mira, una tienda de Massimo Dutti."
            p "¿Quieres que te compre una camiseta?"
            jim2 "No, gracias."
            anette2 "Hey %(name)s mira allí. Hay una cola enorme."
            p "Seguro que regalan algo."
            show vendedora at left
            vendedora "Por favor guarde la cola, aunque recomiendo que vuelva usted mas tarde."
            carmoine2 "¿Qué es lo que dan?"
            vendedora "Una bolsita de champú."
            p "¿Por una bolsita de champú? Ni de coña vuelvo."
            vendedora "¡¡Recuerde que es gratis!!"
            hide vendedora
            if persistent.hombre==False:
                hijo "¡¡Máma!! ¡¡Máma!!"
            else:
                hijo "¡¡Pápa!! ¡¡Pápa!!"
            show hijo
            p "¿Te has perdido, niño?"
            if persistent.hombre==False:
                hijo "No máma, tú te perdiste, pero al final te encontré."
            else:
                hijo "No pápa, tú te perdiste pero al final te encontré."
            p "¿Ma qué dice bambino? Io sonno espagnol."
            p "¿Cómo es que hablo italiano?"
            carmoine2 "¿Es tu hijo?"
            p "No digas tonterías, por supuesto que no."
            carmoine2 "¿Cómo te llamas, cielo?"
            hijo "Giuseppe"
            p "Qué nombre más feo..."
            hijo "¡¡Me lo pusiste tú!!"
            p "Nunca le pondría a mi hijo Giuseppe."
            p "Antes me tiraría por un barranco."
            if persistent.hombre==False:
                hijo "¿Es por eso que te fuiste de casa, Máma?"
                hijo "¿No querías al pobre Giuseppe y por eso le dijiste al Pápa que te ibas a comprar tabaco?"
            else:
                hijo "¿Es por eso que te fuiste de casa, Pápa?"
                hijo "¿No querías al pobre Giuseppe y por eso le dijiste a la Máma que te ibas a comprar tabaco?"
            sandrine2 "Eres un monstruo."
            if persistent.hombre==False:
                p "¿Y quién se supone que es tu padre?"
                hijo "Un zíngaro."
            else:
                p "¿Y quién se supone que es tu madre?"
                hijo "Una zingara."
            sandrine2 "Pensé que se habían extinguido cuando murió Sissi."
            p "¿Pero cómo va a ser mi hijo si acabo de llegar del futuro? Por no hablar de que ni siquiera se parece a mí."
            hijo "Ma yo tengo dos ojos, dos piernas, dos manos..."
            anette "Sí, sí, empiezo a verle el parecido..."
            p "¡¡Basta ya!! Es fisiológicamente imposible"
            anette "Sí, ya..."
            if persistent.hombre==False:
                show hijo at left with move
                show anette at right
                anette "Ahora dirás que eres virgen..."
                anette "A mi no me engañas que he visto la forma en que miras a los hombres por la calle."
                anette "Lo raro es que solo hayas tenido uno."
                hide anette
            else:
                show hijo at left with move
                show sandrine at right
                sandrine "Típico de los hombres:"
                sandrine "\"No importa si no tenemos preservativos, yo sería un buen padre.\""
                sandrine "Y luego, \"El niño no es mío hasta que no me obliguen a hacerme un test de ADN\""
                sandrine "Y aun así, \"antes tendréis que encontrarme.\""
                hide sandrine
            show hijo at center with move
            p "Mira niño, toma estos veinte euros y vete a dar una vuelta mientras resuelvo unos asuntos."
            hijo "¿Estarás aquí cuando vuelva?"
            p "Claro, claro."
            hide hijo
            p "Rápido, vámonos."
            if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide rome3
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide rome3
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide rome3
                jump map
            
            
        else:
            scene rome2
            p "Vámonos de aquí antes de que vuelva el niño psicópata ese."
            show vendedora at left
            vendedora "¡¡¡Un momento!!!"
            vendedora "Tenga, su bolsita de champú."
            p "Gracias, simpática."
            $ persistent.champu=True
            hide vendedora
            hide rome2
            jump map
    else:  #saga fin bolas terminada
        if persistent.vroma2==False:
            scene carreterac
            "La carretera está cortada por la guerra en San Marino."
            hide carreterac
            jump map
        else:
            scene rome1
            "Kirai debe estar todavía en el callejón"
            hide rome1
            jump map
