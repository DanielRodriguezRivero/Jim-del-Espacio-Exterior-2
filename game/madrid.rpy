init:
    $ madrid= 0
label madrid:  
    
    scene madrid at Pan((0, 0), (0, 300), 14.0)
    jim2 "Madrid, capital del mundo."
    p "¿Tú eres de aquí, verdad?"
    jim2 "¿Cómo lo has sabido?"
    p "Por nada, por nada."
    jim2 "Es hora de que comiences tu investigación."
    jim2 "Ve preguntando por ahí o hazlo como tú veas."
    jim2 "Recuerda que nuestro futuro está en tus manos."
    p "Tranquilo, no os fallaré."
    jim2 "Lo sé. Te hemos colocado un chip en la sangre."
    jim2 "A la mínima que metas la pata, te freiremos los..."
    p "Entendido"
    jim2 "Recuerda que puedes ponerte en contacto conmigo por medio del reloj."
    p "Ok"
    jim2 "Corto y cierro."
    p "Juas juas, qué pringao. Suerte que tengo esto."
    show almanaque at Position(ypos=300, yanchor=1.0)
    p "Con este libro de apuestas que le birlé a Jim, voy a hacerme de oro."
    p "Mmm, aprovecharé que estoy cerca del Bernabeu para acercarme a ver qué encuentro."
    hide almanaque
    scene marco
    show expression Text("Tras diez minutos de caminata a través de zanjas, basuras, lating kings y orcos de Mordor...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(3.5)
    hide text with dissolve
    scene bernabeu
    $ renpy.play ("gentio.ogg")
    $ renpy.pause(2.0)
    p "Qué suerte, hoy hay partido."
    show reventa with dissolve
    reventa "Psss"
    p "¿Es a mí?"
    reventa "¿Le interesa unas entradas para el partido a muy buen precio?"
    reventa "Solo el doble de lo que le cuestan en taquilla."
    p "No, gracias, no me gusta el fútbol."
    p "..."
    p "¿Usted es de aquí?"
    reventa "Sí señor, de toda la vida."
    reventa "Desde antes de que se construyera la ciudad."
    reventa "Cuando el primer fulano pensó en asentarse en este solar, antes de poner la primera piedra, me tuvo que pedir permiso."
    reventa "\" La pondré si me sale de los cojones\" le dije."
    p "Y le salió por lo que veo."
    reventa "Es que tenia un palo muy grande."
    reventa "Luego me hizo bailar sobre la piedra, así inventé el chotis."
    p "Eso está muy bien, pero me preguntaba si sabría de algún sitio dónde apostar."
    reventa "Por supuesto, amigo."
    reventa "¿Conoce la calle Alcona? Pues dos calles más atrás encontrarás una tienda llamada \"El rincón del Bebé\""
    reventa "Es una tapadera, tranquilo."
    reventa "Dile a la dependienta que vas de parte de \"Pérdidas\" Te atenderán bien."
    p "¿Pérdidas?"
    reventa "Sí, ese es mi nombre."
    p "Muchas gracias, amable estafador."
    $ renpy.sound.stop(0,2)
    hide reventa with dissolve
    scene callem
    p "Qué simpático el tal Pérdidas. Si yo me llamara así sería un amargado."
    hide callem
    scene escaparate
    p "Aquí es."
    jim2 "O lo de \"bebé\" es un eufemismo, o la dueña de esto es una feminista de cuidado."
    hide callem
    scene mostrador
    show dependienta with dissolve
    dependienta "Buenos dias, ¿qué desea?"
    p "Pérdidas"
    dependienta "Ah, necesita pañales."
    dependienta "Me temo que de su talla no tenemos."
    p "Oh no no, vengo de parte de Pérdidas, el reventa, ya sabe."
    dependienta "Haberlo dicho antes."
    dependienta "Sígame al almacén."
    scene cuartucho
    show dependienta at left
    dependienta "Tigara, aquí tienes a uno nuevo."
    show tigara at right
    tigara "Muchas gracias querida, vuelve al mostrador. Yo me ocupo."
    hide dependienta with dissolve
    show tigara at center with move
    tigara "Así que estás dispuesto a jugar, ¿eh?"
    p "Así es, el dinero me quema en el bolsillo."
    tigara "Pues a juzgar por el bulto de tus pantalones, está a punto de explotar."
    if persistent.hombre==False:
        p "Oh, es una linterna, lo siento."
    tigara "Déjalo en mis manos, cariño."
    tigara "¿Dónde quieres apostar primero?"
    p "Déme un minuto para pensarlo."
    hide tigara with fade
    show almanaque at Position(ypos=350, yanchor=1.0)
    p "¡¡Maldición no se abre!!"
    hide almanaque
    show tigara with fade
    tigara "Lo siento cariño, no tengo todo el día. Decídete ya."
    p "Estoooo, verá, he decidido echarme atrás."
    tigara "No puedes, cariño, podrías salir muy mal parado."
    tigara "El último que se negó a jugar, va a todos lados a pie..."
    p "Eso no está tan mal, es bueno para la salud."
    tigara "... en sueños"
    show tigara at left with move
    show goliath at right
    tigara "A Goliath no les gusta los que se rajan, ¿verdad?"
    go "Goliath odia, Goliath aplasta."
    go "¡¡Matar!! ¡¡Matar!!"
    p "¡¡¡Tranquilo!!!! Apuesto 50.000$ a que gana el Madrid."
    tigara "Eso me gusta más."
    tigara "Siéntate, el partido está a punto de comenzar."
    scene marco
    show expression Text("Dos tensas horas de confraternización con Goliath después...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(4.5)
    hide text with dissolve
    scene cuartucho
    show tigara with fade
    tigara "Qué pena, has perdido."
    p "..."
    tigara "Ahora, paga."
    p "Un momento, dame una oportunidad, juguemos al poker."
    p "Doble o nada."
    tigara "Mmm, de acuerdo. Hoy me siento generosa."
    tigara "¿Reglas de Las Vegas o las tradicionales?"
    p "¿Es que hay más de una forma de jugar?"
    tigara "Uy, esto me va a gustar mucho."
    jim2 "%(name)s ¿estás ahí? Me preocupaba el no recibir noticias tuyas."
    tigara "Pon los 50.000 $ sobre la mesa mientras Goliath reparte."
    jim2 "¿Cómo?"
    jim2 "¿Vas a jugar con alguien capaz de no bajar los brazos en horas para que te distraigas con sus pechos?"
    p "Cállate ya."
    scene black
    $ renpy.pause(1.0)
    jim2 "¿Hola?"
    jim2 "¿%(name)s???"
    jim2 "¡¡Esto está muy oscuro!!"
    scene cuartucho
    show tigara
    tigara "Es la primera vez que veo perder a alguien tan rápido."
    tigara "Y ahora si me das el resto del dinero..."
    p "Verás..."
    p "Es que no tengo el dinero..."
    tigara "Goliath... Aplasta."
    show tigara at right with move
    show goliath at left
    go "Salgamos a la calle."
    hide tigara
    hide goliath
    scene callejon 
    $ renpy.pause(1.5)
    $ renpy.play("punch.wav")
    scene callejon with vpunch
    scene bg black 
    $ renpy.pause(2.0)
    $ renpy.play("disparo.wav")
    $ renpy.pause(0.5)
    $ renpy.play("punch.wav")
    $ renpy.pause(0.5)
    scene bg black with hpunch
    $ renpy.play("punch.wav")
    $ renpy.play("explosion.ogg")
    $ renpy.play("punch.wav")
    $ renpy.pause(2.0)
    scene callejon
    $ renpy.pause(2.0)
    jim2 "No puede ser."
    $ renpy.music.play("protegido.mp3", 7, False, 2)
    $ renpy.pause(2.5)
    jim2 "¡Sigue en pie!"
    p "Aunque como si me hubiera pasado por encima una mole de 150 kilos."
    jim2 "Sí, creo que algo así te pasó"
    $ renpy.sound.stop(0,2)
    jim2 "¿Cómo se te ocurrió la brillante idea de apostar con esa gente?"
    p "La culpa es de tu maldito almanaque deportivo."
    show almanaque at Position(ypos=350, yanchor=1.0)
    if persistent.hombre==False:
        jim2 "No puedo creer que seas tan estúpida."
    else:
        jim2 "No puedo creer que seas tan estúpido."
    jim2 "Ese almanaque es un elemento de atrezo de \"Regreso al futuro II\""
    hide almanaque
    jim2 "Me sorprende que no te dieras cuenta."
    p "Digamos que me dejé llevar por la avaricia."
    jim2 "Eso te servirá de lección para no andarte con tonterías."
    p "Eh, eh, un momento."
    p "Creí que sólo podía hablar contigo si te llamaba."
    p "¿Qué es eso de aparecer de improviso? No me habías dicho nada."
    jim2 "Hay muchas cosas que no te digo."
    jim2 "¿Te he dicho que mi suegra me pilló la semana pasada con su hija en la cama?"
    p "No"
    jim2 "¿Y sabes por qué?"
    p "¿Porque no me interesa?"
    jim2 "No, porque es mentira."
    jim2 "Además no te quejes, ya es la segunda vez que te lo hago."
    jim2 "Ahora sigue con la investigación."
    p "Hay un problema Jim..."
    p "Me han robado el antídoto."
    jim2 "Debió de quedárselo Tigara. Tenía una cara de viciosa..."
    p "Ah, pero, ¿le miraste a la cara?"
    if persistent.hombre==False:
        jim2 "No me quedó otra, es lo único que tenía en mi campo de visión, Doña \"me luxo el brazo con la más mínima brisa.\""
    else:
        jim2 "No me quedó otra, es lo único que tenía en mi campo de visión, Don \"me luxo el brazo con la más mínima brisa.\""
    p "¿Y ahora qué hacemos?"
    jim2 "Lo primero, recuperar el antídoto. No podemos arriesgarnos a que te disparen con el rayo y no lo tengas a mano para volver a tu forma normal."
    jim2 "No quiero ni imaginar lo que ronda por tu cabeza."
    p "¿Alguna sugerencia de por dónde comenzar a buscar?"
    jim2 "En vista de tu fracaso, necesitarás ayuda profesional."
    jim2 "En Barcelona se encuentra una famosa agencia de detectives. No es la mejor, pero son los únicos que creerán nuestra historia."
    p "Cogeremos el tren entonces. Es lo más rápido."
    scene marco
    show expression Text("Una semana después...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(4.5)
    hide text with dissolve
    scene hq
    jim2 "Bonito edificio, ¿eh?"
    jim2 "No es como mi torre de la libertad, pero para un grupito de detectives no está nada mal."
    show sandrine
    sandrine "¿Quién ha dicho eso?"
    p "No he escuchado nada."
    sandrine "Juraría que le he visto hablar con su muñeca."
    p "Es que le tengo mucho aprecio."
    p "Son muchas noches juntos..."
    sandrine "¿Se le ofrece algo?"
    p "Venía a contratar los servicios de unos detectives."
    sandrine "Ha venido al sitio indicado, acompáñeme."
    scene angeles
    show sandrine at left
    sandrine "Yo soy Sandrine."
    show carmoine at center
    carmoine "Yo, carmoine."
    show anette at right
    anette "Y yo Anette, para servirte a ti y a un equipo de fútbol si hace falta."
    carmoine "Somos algo así como los ángeles de Charlie, pero sin un viejo baboso que nos ordene lo que tenemos que hacer."
    carmoine "Cuénteme, ¿en qué podemos ayudarle?"
    p "Por favor, tuteadme."
    p "La verdad es que es un trabajo algo..."
    p "Me tomaréis por un chiflado."
    p "Es necesario encontrar un objeto que no creeríais que existe."
    carmoine "Tranquilo, trabajamos por horas. Cuanto más increible sea ese objeto mejor para nosotras."
    carmoine "¿Qué hay que buscar?: la espada del Rey Arturo, el cuerno de un unicornio..."
    p "Unas bolas chinas"
    carmoine "..."
    sandrine "..."
    anette "Oye, yo tengo el carnet de socio del sex shop de abajo. Te lo dejo si quieres y te compras unas nuevas."
    p "Es que las mías son algo especiales."
    anette "Te entiendo, al final se les coge cariño de tanto usarlas."
    p "Veréis..."
    scene marco
    show expression Text("Con infinita paciencia, les explicó todo. Desde que despertó del sueño criogénico, hasta cuando le tocó el culo a Sandrine y le echó las culpas a Carmoine, justo antes de sentarse a explicarles la historia...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(6.5)
    scene angeles
    show sandrine
    sandrine "Desde luego no es algo que pase todos los días, pero necesitamos el dinero..."
    sandrine "Además nos vendrá bien viajar un poco, mañana vienen a cobrar el alquiler."
    hide sandrine
    show anette
    anette "Tenemos que registrar el local donde te robaron."
    anette "Con suerte habrán dejado alguna pista."
    hide anette

    hide angeles
    scene marco
    show expression Text("De vuelta en Madrid...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(2.5)
    hide text with dissolve
    $ renpy.pause(0.25)
    scene cuartucho
    show carmoine
    carmoine "Chicas, registradlo todo minuciosamente."
    hide carmoine
    show anette
    anette "Aquí hay una foto de Tigara."
    p "Qué tía. También aparece con los brazos sobre la cabeza."
    anette "Yo creo que es bracicorta y para que no se le note, no los baja."
    sandrine2 "Más bien es tetas gordas."
    hide anette
    show carmoine
    carmoine "No hay nadie"
    carmoine "Pero he encontrado en un cajón resguardos de billetes de avión para toda Europa."
    carmoine "¿Qué se propondrá hacer con ellos?"
    anette2 "¿Turismo?"
    hide carmoine
    p "Qué curioso. Parece que quisiera que la siguiéramos."
    sandrine2 "Si eso quiere, eso es lo que haremos."
    hide cuartucho
    scene mapa2
    sandrine2 "En una de estas ciudades europeas se esconde esa fulana con las bolas."
    p "Sin una pista fiable, tendremos que visitarlas todas."
    p "Suerte que tenemos este mapa mágico que ha aparecido de pronto entre mis manos y que nos permite teletransportanos a cualquier parte."
    hide map2
    jump map