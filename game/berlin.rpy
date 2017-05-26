init:   
    
    $ persistent.vberlin = False   #visitado berlin con persistent.nombre se consigue una variable que se guarda
    
label berlin:
    
    if persistent.finbolas==False: 
        if persistent.vberlin == False:
            scene riob
            sandrine2 "Mira, el río ese que pasa por Berlín, ya sabes..."
            hide riob
            scene berlinw
            p "¿Esto es el muro de Berlín?"
            sandrine2 "Eso parece."
            p "Pensaba que lo habían tirado abajo."
            anette2 "Han vuelto los Led Zeppelin, así que supongo que esto habrá vuelto también."
            carmoine2 "Un momento, creo que veo una inscripción."
            extend "\"Ni siquiera los gruesos muros de piedra, lograrán separarme de tí, Lady Carme...\""
            anette2 "¿Quién la escribiría?"
            sandrine2 "Alguien que estaba en el lado contrario del muro."
            scene germanc
            $ renpy.pause(0.5)
            show rudiger
            rudiger "Una lismona para un pobre pintor."
            carmoine2 "Qué kitsch, un artista callejero, como los del rastro."
            rudiger "Más o menos, solo que yo no pinto falsificaciones."
            rudiger "Me llamo Rudiger y soy austríaco."
            p "¿El de los mundos de Yupi?"
            rudiger "Déjame que te enseñe mis obras."
            hide rudiger
            scene espinete
            $ renpy.pause(0.5)
            rudiger "Este fue mi primer trabajo."
            p "Bueno..."
            rudiger "Lo sé, es infame, pero sirve para ver mi evolución."
            scene churchill
            $ renpy.pause(1.0)
            rudiger "De este estoy más orgulloso. Las curvas imprimieron al dibujo de un volumen que hasta entonces me era dificil captar."
            carmoine2 "Está muy conseguido."
            hide churchill
            scene pitufo
            $ renpy.pause(1.0)
            rudiger "No hace falta que lo presente, ¿verdad?"
            sandrine2 "Si Gargamel estuviera aquí, se lo comería."
            rudiger "Notad el detalle de que está realizado a escala"
            extend "con la dificultad que ello implica."
            hide pitufo
            scene sabrina
            $ renpy.play(1.0)
            rudiger "Este en particular me lo quitan de las manos."
            anette2 "Uy, yo quiero uno"
            rudiger "Lo he visto colgado en la carlinga de más de un camionero..."
            hide sabrina
            scene ursula
            $ renpy.play(1.0)
            rudiger "Mi última creación."
            rudiger "El dolor que se deduce de su mueca desgarrada llega a lo más hondo."
            hide ursula
            scene hitler
            $ renpy.play(1.0)
            rudiger "Y para terminar, un clásico del lugar."
            p "..."
            rudiger "Lo suelo vender más cuando está todo oscuro."
            hide hitler
            scene germanc
            show rudiger
            p "Me gustaria comprarte alguno pero no llevo nada suelto."
            rudiger "Oh"
            p "Tenemos que irnos, lo siento."
            rudiger "Volved cuando tengáis dinero, por favor."
            rudiger "Necesito dinero para alimentar a mis tres mujeres."
            hide rudiger
            $ persistent.vberlin = True
            if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide germanc
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide germanc
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide germanc
                jump map

        else:  # la visitas mas veces
            scene germanc
            "Rudiger continúa intentando vender alguna de sus vanguardistas obras a los transeúntes, pero ni siquiera la de Sabrina logra llamar la atención."
            hide germanc
            jump map
    else:
        if persistent.fotos==False:
            scene parking
            show garganta
            gp  "¿Todavia no las tienes?"  #pinguino garganta profunda
            if persistent.xman:
                p "Sí, aquí tengo algunas."
                $ persistent.xman=False
                scene marco
                show expression Text("Por el bien de los estómagos de los lectores le ahorraremos el visionar dichas fotos.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(3.5)
                hide text
                scene parking
                show garganta
                gp "\"¿Estas fotos me quieres dar?\" ¡¡Pero si parece un secuestro con tanta mujer atada!!"
            gp "Anda, sigue buscando, que tienes el gusto en la punta de..."
            gp "Lo que sea que tengas."
            hide garganta
            hide parking
            jump map
        else:
            jump antartida