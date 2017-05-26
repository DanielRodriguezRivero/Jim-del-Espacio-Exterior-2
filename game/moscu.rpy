init:
    
    $ persistent.vm = False      #variable visitado moscu
    $ persistent.vm2 = False  
    $ persistent.leones=False
    $ persistent.oso=False
    $ persistent.zorras=False
    
label moscu:
    if persistent.finbolas==False:
        if persistent.vm == False:  #primera visita
            #descripcion, gag, referencia al vodka
            scene moscow
            show sandrine
            p "¿Qué sabéis de Rusia?"
            sandrine "Es un país muy grande, hace mucho frío y beben vodka en lugar de agua."
            p "¿Solo eso?"
            sandrine "¿Hace falta saber más?"
            p "Supongo que no."
            p "Sigamos investigando."
            hide sandrine
            hide moscow
            scene ivan
            sandrine2 "Qué colores más apagados tiene este parque, casi parece un cuadro."
            carmoine2 "Yo diría más, juraría que es un cuadro de Korovin, pero es solo una suposición."
            anette2 "¿Y si la realidad no existiera como tal?"
            anette2 "¿Y si vivieramos dentro de un programa de computador?"
            sandrine2 "Cállate Anette y ponte en marcha, debemos seguir buscando."
            $ persistent.vm = True
            if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide ivan
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide ivan
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide ivan
                jump map
                
        else:
            scene plazaroja
            show nieve with dissolve
            "Un campesino de Minsk recorre las calles bajo una nevada intensa. Pretende llegar al ministerio de agricultura para pedir de rodillas al ministro que invierta dinero en las plantaciones de trigo."
            "Pero antes de llegar, muere de frío bajo la implacable nieve."
            "No importa, detrás suya, le sigue otro campesino."
            "Aún debo visitar el resto de ciudades de Europa."
            hide nieve
            hide plazaroja
            jump map
    else:
        if persistent.vm2 == False: #primera visita
            if persistent.modelos == False: # si no hablo con las modelos
                scene moscuc
                show misha with fade
                p "Yo te conozco."
                p "Eres el Oso Misha, la mascota de Moscú 80."
                oso "Sí, veo que aún me recuerda la gente."
                p "¿Pero qué pasó contigo?"
                p "Al terminar las olimpiadas desapareciste."
                oso "Es una historia larga y triste, para un breve resumen te recomiendo el post de Fin del juego: \"Anoche fui... el chollo.\""
                oso "Después de escapar de la isla, decidimos volver a la Rodina."
                oso "Echaba de menos a mis familiares y deseaba obtener una venganza justa contra quienes me desterraron en esa prisión."
                oso "Nada más cruzar la frontera, los guardias comenzaron a perseguirnos."
                oso "Pensaban que seguía siendo un agente doble."
                oso "No me dejaron explicarme."
                oso "La huida fue larga y dura. Al principio tuvimos éxito, pero una noche..."
                p "¿Qué pasó?"
                oso "Una noche, una ráfaga de viento lanzó por los aires la chistera de mi camarada Chollo."
                oso "Decidió retroceder para recuperarla..."
                extend " y entonces esos perros del KGB lo mataron."
                oso "Que no te engañe mi sonriente rostro, perpetuo gracias a un trabajador de Kemerovo."
                oso "Por dentro las lágrimas inundan mi alma."
                oso "El chollo murió a las afueras de Minsk por mi culpa."
                oso "Por no querer acompañarle a buscar el sombrero."
                oso "Ahora mi venganza es contra el gobierno ruso también."
                oso "Porque si estoy perseguido es debido a Putin, cogió un trauma cuando no le saludé durante las olimpiadas."
                oso "Y por eso me la tiene jurada."
                p "¿Ahora a qué te dedicas?"
                oso "Al contrabando, camarada." 
                oso "Contrabando de Vodka Putinka."
                p "¿No es algo contradictorio?"
                oso "Busco financiación para mi plan de venganza."
                oso "De hecho ya la tengo, solo necesito un objeto: es un juego para MSX llamado Rescate Atlantida."
                p "Qué casualidad, justo hace poco lo compre en un mercadillo."
                hide moscuc
                scene rescate
                oso "¡Sí!, ¡sí! Eso es, ¡al fin podré vengarme!"
                hide rescate
                scene moscuc
                show misha
                oso "Pero necesito tiempo para prepararlo todo."
                hide misha
                hide moscuc
                $ persistent.vm2 =True
                jump map
            else: #hablo con las modelos, pero no conoce a misha todavia
                scene moscuc
                show misha with fade
                p "Yo te conozco."
                p "Eres el Oso Misha, la mascota de Moscú 80."
                oso "Sí, veo que aún me recuerda la gente."
                p "¿Pero qué pasó contigo?"
                p "Al terminar las olimpiadas desapareciste."
                oso "Es una historia larga y triste, para un breve resumen te recomiendo el post de Fin del juego: \"Anoche fui... el chollo.\""
                oso "Después de escapar de la isla, decidimos volver a la Rodina."
                oso "Echaba de menos a mis familiares y deseaba obtener una venganza justa contra quienes me desterraron en esa prisión."
                oso "Nada más cruzar la frontera, los guardias comenzaron a perseguirnos."
                oso "Pensaban que seguía siendo un agente doble."
                oso "No me dejaron explicarme."
                oso "La huida fue larga y dura. Al principio tuvimos éxito, pero una noche..."
                p "¿Qué pasó?"
                oso "Una noche, una ráfaga de viento lanzó por los aires la chistera de mi camarada Chollo."
                oso "Decidió retroceder para recuperarla..."
                extend " y entonces esos perros del KGB lo mataron."
                oso "Que no te engañe mi sonriente rostro, perpetuo gracias a un trabajador de Kemerovo."
                oso "Por dentro las lágrimas inundan mi alma."
                oso "El chollo murió a las afueras de Minsk por mi culpa."
                oso "Por no querer acompañarle a buscar el sombrero."
                oso "Ahora mi venganza es contra el gobierno ruso también."
                oso "Porque si estoy perseguido es debido a Putin, cogió un trauma cuando no le saludé durante las Olimpiadas."
                oso "Y por eso me la tiene jurada."
                p "¿Ahora a qué te dedicas?"
                oso "Al contrabando camarada. Busco financiación para mi plan de venganza."
                oso "De hecho ya la tengo, solo necesito un objeto para desbaratar los sistemas de seguridad."
                oso "Es un juego para MSX, llamado Rescate Atlantida."
                p "Qué casualidad, justo hace poco lo compré en un mercadillo."
                hide moscuc
                scene rescate
                oso2 "¡Sí!, ¡sí! Eso es, ¡al fin podre vengarme!"
                hide rescate
                scene moscuc
                show misha
                oso "Asaltaremos el Kremlin e introduciremos un virus en sus ordenadores que sumirá la ciudad en el caos."
                p "Pues yo necesito vodka, ¿me daréis un poco si os acompaño?"
                oso "Claro, aunque es un trabajo peligroso, solo iremos nosotros dos."
                oso "Es la hora. ¡Vamos al ataque!"
                hide misha
                hide moscuc
                scene moscun
                show misha
                p "¿Cómo entraremos? Debe estar repleto de guardias."
                oso "Conozco una entrada secreta."
                oso "Pagué mucho dinero por los planos del Kremlin. Espero que haya merecido la pena."
                hide misha
                hide moscun
                scene corredor1
                p "Jo, que pasillo más raro."
                oso2 "Putin se aficionó al sudoku durante un viaje oficial a Japón y mandó empapelar varias habitaciones así para poder jugar cuando quisiera."
                hide corredor1
                scene sr
                oso2 "Bien, conecta el MSX al servidor central."
                show msx at Position(ypos=500)
                p "Un segundito..."
                p "Listo"
                scene msx1
                p "Mmmm, voy a probar a ver."
                p "color 1,2"
                hide msx1
                scene msx2
                p "Qué recuerdos..."
                oso2 "No tenemos tiempo para la nostalgia, venga, carga el juego."
                p "Load \"cas:\" , r"
                hide msx2
                $ renpy.play("bso1.mp3")
                scene rescate2
                $ renpy.pause(4.5)
                $ renpy.sound.stop(0,2)
                hide rescate2
                scene sr
                show misha
                oso "Jajaja, lo conseguí. Al fin he transferido los planes de Putin y he anulado las alarmas de seguridad."
                oso "Llegó la hora de la verdad."
                scene corredor2
                p "Este no es el camino de salida."
                oso2 "No vamos hacia la salida."
                oso2 "¡¡¡Vamos hacia la retribución!!!"
                hide corredor2
                scene habitacion2 with hpunch
                p "Auch, ¿dónde hemos caido?"
                oso2 "Qué sitio más extraño. Mira esas puertas y esos números..."
                p "Hey, aquí en esta pared parece haber un cartel."
                $ result = renpy.imagemap("wall.jpg", "wall.jpg", [ (314, 172, 496, 316, "cartel"),  
                ], focus="imagemap")
                if result=="cartel":
                    jump cartel
        else: #segunda visita
            if persistent.modelos == False:
                scene moscuc
                show misha
                oso "Todavía necesito un poco mas de tiempo."
                oso "Como decía mi abuelo Piotr:"
                oso "La caida de una oligarquia no se ejecuta en un día."
                hide misha
                scene moscuc
                jump map
            else:
                if persistent.vodka==True:  # ya se hizo lo de la habitación, esto se ve siempre hasta el final
                    scene kremlin
                    "Las coloreadas bóvedas del Kremlin refulgen como diamantes bajo el cielo moscovita."
                    hide kremlin
                    jump map
                else:
                    scene moscuc
                    show misha
                    oso "Ah, amigo, de nuevo aquí. Está todo listo. Me acompañarás al Kremlin y compartirás mi gloria."
                    p "¿Me darás un poco de vodka?"
                    oso "Por supuesto, camarada."
                    p "En marcha entonces."
                    oso "Esperaremos hasta el anochecer y caeremos sobre ellos como halcones."
                    oso "Asaltaremos sus servidores y con tu juego corromperemos el sistema, sumiendo al caos a la ciudad."
                    hide misha
                    hide moscun
                    scene moscun
                    show misha
                    p "¿Cómo entraremos? Debe estar repleto de guardias."
                    oso "Conozco una entrada secreta."
                    oso "Pagué mucho dinero por los planos del Kremlin. Espero que haya merecido la pena."
                    hide moscun
                    scene corredor1
                    p "Jo, que pasillo más raro."
                    oso2 "Putin se aficionó al sudoku durante un viaje oficial a Japón y mandó empapelar varias habitaciones así para poder jugar cuando quisiera."
                    hide corredor1
                    scene sr
                    oso2 "Bien, conecta el MSX al servidor central."
                    show msx at Position(ypos=500)
                    p "Un segundito..."
                    p "Listo"
                    scene msx1
                    p "Mmmm, voy a probar a ver"
                    p "color 1,2"
                    hide msx1
                    scene msx2
                    p "Qué recuerdos..."
                    oso2 "No tenemos tiempo para la nostalgia. Venga, carga el juego."
                    p "Load \"cas:\" , r"
                    hide msx2
                    $ renpy.play("bso1.mp3")
                    scene rescate2
                    $ renpy.pause(4.0)
                    $ renpy.sound.stop(0,2)
                    hide rescate2
                    scene sr
                    show misha
                    oso "Jajaja, lo conseguí. Al fin he transferido los planes de Putin y he anulado las alarmas de seguridad."
                    oso "Llegó la hora de la verdad."
                    scene corredor2
                    p "Este no es el camino de salida."
                    oso2 "No vamos hacia la salida."
                    oso2 "¡¡¡Vamos hacia la retribución!!!"
                    hide corredor2
                    scene habitacion2 with hpunch
                    p "Auch, ¿dónde hemos caido?"
                    oso2 "Qué sitio más extraño. Mira esas puertas y esos números..."
                    p "Hey, aquí en esta pared parece haber un cartel."
                    $ result = renpy.imagemap("wall.jpg", "wall.jpg", [ (314, 172, 496, 316, "cartel"),  #coordenadas para los boliches, etc
                    ], focus="imagemap")
                    if result=="cartel":
                        jump cartel
                
label cartel:
    show cartel
    p "¿Qué dice ahí?"
    oso2 "Veamos..."
    oso2 "Creo que los números se corresponden con las puertas."
    oso2 "En la 1, hay leones muertos de hambre."
    oso2 "En la 2, unas zorras salidas."
    oso2 "En la 3, John Locke."
    oso2 "En la 4, un oso polar."
    p "Pues cogemos la 2, ¿no?"
    oso2 "Habrá que meditarlo bien. Estas cosas suelen tener trampa."
    hide cartel
    $ persistent.vodka=True
    jump habitacion  #habitacion del kremlin

label habitacion:
    $ result = renpy.imagemap("habitacion2.png", "habitacion2.png", [
    (302, 16, 377, 41, "puerta1"),  #coordenadas para los boliches, etc
    (29, 229, 53, 309, "puerta2"), 
    (385, 560, 461, 584, "puerta3"),
    (753, 228, 771, 295, "puerta4"),
    ], focus="imagemap")
    if result == "puerta1":
        #esconder la imagen de europa con alguna transicion chula
        jump puerta1
    if result == "puerta2":
        jump puerta2
    if result == "puerta3":
        jump puerta3
    if result == "puerta4":
        jump puerta4
        
label puerta1:
    if persistent.leones==False:
        scene bg black
        p "No me gusta nada esto. Está muy oscuro."
        oso "Tonterías, el Chollo sí que lo vio todo negro aquella noche de octubre..."
        $ renpy.play("leon.mp3")
        $ renpy.pause(2.0)
        p "¿Qué ha sido eso?"
        oso "¿El chollo pidiendo venganza desde ultratumba?"
        $ renpy.play("leon.mp3")
        show leon
        $ renpy.pause(2.0)
        p "No corras, puede oler tu miedo."
        oso "Yo creo que está oliendo otra cosa..."
        p "Así, despacio. Ya veo la puerta."
        $ renpy.play("puerta.mp3")
        scene habitacion
        oso "Nos hemos librado por un pelo."
        hide habitacion
        $ persistent.leones=True
        jump habitacion
    else:
        scene habitacion
        p "Ser la cena de un león no entra dentro de mis planes."
        hide habitacion
        jump habitacion
label puerta2:
    if persistent.zorras==False:
        scene bg black
        p "¿No escuchas algo como un jadeo?"
        oso2 "Sí, sí, sí"
        oso2 "Venid nenas a mí, soy blandito, pero cuando se me toca en..."
        oso2 "Au, me ha mordido alguien."
        p "Deben estar con el celo."
        oso2 "Oye, que esto no son mujeres salidas, ¡¡¡son zorros!!! ¡¡¡Pero de los que no tienen rabo!!!"
        oso2 "Sal echando leches."
        scene habitacion
        oso2 "Menos mal que en aquella fábrica de Petropaulovks no me hicieron ese agujero..."
        hide habitacion
        $ persistent.zorras=True
        jump habitacion
    else:
        scene habitacion
        p "Respeto a los sodomitas, pero los sodomitas zoófilos no tienen perdón de Dios."
        oso2 "No te metas con Ivenka."
        p "¿Quién es?"
        p "Déjalo, no quiero saberlo."
        hide habitacion
        jump habitacion
label puerta3:
    scene playa
    show locke at Position(ypos=550)
    locke "Compañeros, bienvenidos a la isla."
    p "¿La isla?, si estabamos en el Kremlin."
    locke "La isla es misteriosa,tan pronto estás aquí, como estás más allá."
    locke "Y no solo eso, también tiene otros poderes."
    locke "Antes de llegar aquí, tenía fimosis, pero ya no."
    hide locke
    show locke2
    locke "La isla me curó."
    locke "Me llevó a una sala brillante donde un cirujano me cortó lo que sobraba."
    locke "A la media hora ya podía caminar."
    p "Es magia eso."
    locke "Ya te digo"
    locke "También tenía halitosis, pero froté mi boca con un extraño palo que terminaba en suaves fibras que me dio la isla, y se me pasó."
    oso2 "los del hospital La isla deben de ser cojonudos."
    oso2 "Psss %(name)s tendríamos que irnos ya, ¿no?"
    p "Sí, tienes razón."
    p "Eh John, detrás de ti. ¡¡Jacob!!"
    locke "Imposible, ¿tú también puedes verlo?"
    p "¡Corre Misha!"
    scene puerta3
    show misha
    oso "Esta es la última puerta que me separa de mi venganza."
    oso "Es hora de que sigas tu camino. Toma este salvoconducto."
    oso "Acude mañana a la calle Checksnaya, mis hombres estarán allí y te darán el vodka."
    p "Gracias, camarada."
    oso "No hay por qué darlas."
    oso "Y ahora vete."
    hide misha
    $ renpy.pause(1.5)
    hide puerta3
    scene vladimir
    $ renpy.play(0.5)
    oso "Volvemos a encontrarnos Vladimir."
    hide vladimir
    scene bg black with fade
    $ persistent.puntos +=1
    jump continuacion
label puerta4:
    if persistent.oso==False:
        scene habitacion
        oso2 "Entremos por esta, yo me entiendo con los osos."
        p "¡¡Pero si eres un peluche!!"
        oso2 "¿Eso qué más da?"
        oso2 "Además, en el este no hay osos polares, están todos en el Sur."
        scene bg black
        $ persistent.oso=True
        $ renpy.play("polar.wav")
        $ renpy.pause(1.0)
        scene osob
        p "¡Huyamos!"
        hide osob
        jump habitacion
    else:
        p "Habría que estar muy loco para volver a vérselas con ese horrible oso."
        jump habitacion
    
        
label continuacion:
        $ persistent.vm2 = True
       # $ persistent.modelos = False #ponerlo a falso por si vuelvo de nuevo a moscu, salte a la descripcion general
        scene callejon2
        p "Aquí están las cajas de vodka."
        p "Con un par de botellas fijo que consigo que alguna de las actrices caiga rendida a mis pies."
        p "Lo probaré a ver qué tal..."
        #sonido de beber
        p "¡Por el camarada Misha!"
        $ persistent.vodka=True
        p "Espero que hallara la paz de espíritu."
        hide callejon2
        jump map