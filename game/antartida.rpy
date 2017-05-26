init:
    $ prueba=False
label antartida:
    $ renpy.sound.stop(0,2)
    scene parking
    p "¡¿Garganta?!"
    p "¿¡¡Lindaaaaa!!?"
    gp "Estoy aquí."
    show garganta
    p "Ya tengo las fotos que me dijiste."
    $ renpy.pause(1.5)
    gp "Mmmmm"
    gp "Creo que valdrán."
    p "Con lo que me ha costado conseguirlas, más vale que sí."
    gp "Bien, gracias por todo %(name)s"
    gp "Hasta la próxima vez, que espero no se vuelva a dar."
    p "Un momento, ¿qué hay de la información sobre Fetch que me iba a dar?"
    p "¿Cómo sabías de su existencia?"
    p "¿Dónde está?"
    p "Y por encima de todo, ¿quién diablos eres?"
    gp "Esas son preguntas que no tendrán respuesta para usted, excepto la última."
    gp "Creo que es hora de desvelar mi rostro."
    p "Hace dos días que tendrían que haberme cambiado las vendas."
    hide garganta
    $ renpy.pause(1.0)
    show schultz
    p "¡¡¡Una nazi!!!"
    jim2 "Y está buenísima."
    p "Pensaba que solo existían en las películas."
    gp "En efecto, Oberleutenant Schultz, a tus pies."
    gp "O mejor dicho, tú a los míos."
    $ renpy.play("punch.wav")
    $ renpy.pause(0.5)
    scene bg black
    $ renpy.pause(2.0)
    scene parking
    $ renpy.pause(1.5)
    scene bg black
    $ renpy.pause(1.5)
    scene parking
    p "Ouch, eso dolió."
    p "Maldición, no está."
    p "Habrá escapado en submarino, como todos los nazis."
    jim2 "O puede que nadando."
    p "Sí, pero ¿hacia donde?"
    p "Mmmm"
    p "¿Dónde podrían quedar nazis hoy día?"
    extend " en esta época, quiero decir."
    jim2 "¿En sudamérica?"
    p "No, demasiado fácil de encontrar."
    jim2 "¿En España?"
    p "No lo creo, eso metería en graves problemas al autor de esta novela visual..."
    p "Se me ocurre..."
    extend " recuerdo una antigua historia sobre una base nazi secreta que fue descubierta tras el final de la guerra."
    p "¡Ya me acuerdo!" 
    p "Vi un documental hace... en su día, sobre el tema. Recuerdo que había muchos pinguinos por allí. No recuerdo el lugar exacto..."
    jim2 "¿En el polo Sur?"
    p "¡Eso! Pero en el juego no está implementado, no podemos ir a pie o en AVE como hasta ahora."
    jim2 "Seguro que hay otro método."
    show lara
    lara "Hola, chicos."
    lara "¿Alguien ha pedido una atractiva arqueóloga?"
    jim2 "Yo, hace cinco años." 
    jim2 "Una fría noche de invierno, cuando la soledad arrinconaba mi esperanza, oprimiendo mi pecho..."
    lara "Al fin os encontré."
    p "¿Pero cómo?"
    lara "Es una larga historia, preferís oirla o verme saltar?"
    jim2 "¡¡¡Saltar, saltar!!!"
    lara "Es broma, me enviaron las chicas. Pensaron que podrías necesitar mi ayuda."
    lara "Y tenían razón."
    lara "Recuerdos de Anette, me dijo que te preguntara algo sobre unas bolas demasiado usadas o algo así."
    lara "No la pude entender entre tanto gemido."
    p "Toda ayuda es poca."
    p "No sabrás de algún modo de ir a la Antártida, ¿no?"
    lara "Por esas casualidades de la vida, sí que lo conozco."
    lara "Al menos sé que existe un paso bajo la tierra, que conduce hasta el Polo Sur."
    lara "De lo que no tengo ni idea es dónde está exactamente."
    lara "Con toda probabilidad, por la Hélade."
    p "Bien, vayamos allí de inmediato-"
    lara "No es tan fácil, podríamos pasarnos meses buscando la entrada."
    lara "Sin embargo, se dice que en un templo subterraneo, perdido en lo más profundo del valle de los Reyes, se encuentran las indicaciones exactas."
    p "Voy a acabar de El Cairo hasta los mismísimos..."
    lara "¡En marcha!"
    scene marco
    show expression Text("Tras un viaje sin complicaciones en el que, por mucho que espió a Lara, no consiguió verla desnuda...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(3.0)
    hide text
    scene valler
    show lara
    lara "Espero que los turistas no interfieran en nuestra búsqueda."
    lara "El templo que buscamos está a doscientos kilómetros al norte."
    hide valler
    scene abus
    lara "Aquí perdí a un buen amigo."
    lara "Le cayó un peñasco en la cabeza, creyó que había sido yo, y desde entonces no me habla."
    hide abus
    scene templo
    show lara
    lara "Ya hemos llegado."
    lara "Desde lo alto de esas piedras, una cámara de vigilancia te contempla."
    lara "Así que nada de sacar fotos o dar de comer a los camellos"
    extend " por muy buen precio que te hagan."
    scene marco
    show expression Text("Si has pillado esta chanza recuerda: Los ganadores no consumen drogas (toman sustancias prohibidas)", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(3.5)
    hide text with dissolve
    scene pasilloc
    lara "Los jeroglíficos de este recinto son impresionantes."
    lara "En ellos está plasmada la historia del país."
    p "¿Qué pone ahí?"
    show jero2  #juntar jerogilifcos
    $ renpy.pause(2.0)
    lara "Nefertiti puta."
    $ renpy.pause(1.0)
    p "Así que era ella."
    p "Yo que pensaba que era Cleopatra..."
    scene interiort
    $ renpy.pause(0.5)
    p "Juraría que estás mazmorras las vi en Lady Halcón."
    show templario
    templario "No te equivocas, se la quité a Rutger Hauer mientras se comía un bocadillo durante un descanso del rodaje."
    $ renpy.pause(1.0)
    show lara at left
    show templario at right with move
    lara "Saludos, anciano templario, venimos a por el mapa Neptunio."
    templario "Queréis adentraros en el Hades, ¿verdad?"
    templario "Antes deberéis revivir la famosa escena de Indiana Jones y la última cruzada y elegir cuál es el cáliz de la última cena."
    hide templario
    hide lara
    $ renpy.pause(2.0)
    p "Está la cosa difícil..."
    $ renpy.pause(1.0)
    show caliz at Position(ypos=550)
    p "Este es el cáliz del hijo de un carpintero."
    lara "Pues por lo que me cobró uno del gremio por hacerme una puerta, podría haberse permitido uno mejor."
    hide caliz
    show templario
    templario "¿De qué hijo de carpintero hablas?"
    templario "Yo me refería al de mi última cena, la de anoche, que comí fabes con tomate y no me sentó nada bien, por cierto."
    templario "Pero quién lo diría, habéis acertado de igual forma."
    templario "Elige tu premio."
    menu:
        "Un perrito piloto":
            templario "Tú lo que quieres es el mapa."
            templario "Ahí lo tienes."
        "Un karaoke":
            templario "Tú lo que quieres es el mapa."
            templario "Tú directamente eres tonto, coge el mapa."
        "Un televisor portátil en blanco y negro":
            templario "Tú lo que quieres es el mapa."
            templario "Deberías ponerte al día un poco, ten el mapa."
        "Mapa de la entrada al Hades":
            templario "Aquí tienes."
    lara "Es un mapa muy antiguo."
    p "En perfecto castellano. Esos griegos sabían lo que se hacían."
    hide templario
    hide interiort
    scene map2
    p "La X marca el lugar."
    hide map2
    scene marco
    show expression Text("Y así, tras decir adiós al ajado caballero templario, los modernos émulos de Indiana Jones, cogieron un avión en dirección a la X...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(3.0)
    hide text
    hide marco
    $ renpy.pause(1.0)
    scene cueva1
    p "Parece que hay alguien ahí."
    $ renpy.pause(1.0)
    p "Perdone, si se aparta a un lado se lo agradeceríamos."
    show esfinge
    esfinge "Eso no será posible."
    esfinge "Si queréis entrar, un terrible acertijo deberéis acertar."
    p "¿Y si fallamos?"
    esfinge "Acabaréis en mi estómago."
    p "..."
    p "Perdóneme si lo dudo."
    esfinge "Que no os engañe mi aspecto."
    esfinge "Antes era una terrible esfinge. Los niños del lugar se lo hacían encima con solo escuchar mi nombre."
    esfinge "Pero entonces llegó un tío muy raro y me lanzó una especie de rayo que me convirtió en esto."
    esfinge "Pagaré mi rabia con vosotros, pero antes contestadme:"
    esfinge "Este banco está ocupado por un padre y por un hijo. El nombre del padre es Juan, el del hijo, ya te lo he dicho."
    esfinge "¿Cómo se llama el hijo?"
    p "Bah, es muy fácil: Esteban."
    esfinge "Nooooo jajaja. Se llama Antonio."
    esfinge "La explicación es muy larga así que iros desnudandoos que no me gusta comer fibras sintéticas."
    p "¿A quién quiere engañar?"
    p "Si se le cae la dentadura cada vez que abre la boca."
    jim2 "Parece que al menos algo bueno hizo Fetch."
    esfinge "Sí, así se llamaba el rufián causante de mis males."
    esfinge "¿Lo conocéis?"
    p "Queremos capturarle y llevarlo a la justicia."
    esfinge "En ese caso os dejo pasar. Dadle una buena por mí."
    hide esfinge
    show lara
    lara "Un momento, un momento."
    lara "Yo ahí no entro."
    p "¿Cómo que no?"
    lara "¿Sabes lo que simboliza entrar en un túnel?"
    p "¿Qué tienes claustrofobia?"
    lara "No"
    p "¿Miedo a la oscuridad?"
    lara "Algo mucho peor..."
    lara "¡¡El coito!!"
    p "Eso no tiene nada de malo."
    lara "Es una costumbre falocentrista, ideada para recordar a las mujeres que si quieren llegar a algún lado, tienen que ser penetradas."
    p "Es una forma diferente de verlo."
    lara "Deberían estar prohibidos los túneles, las cuevas, la ceremonia de iniciación de Arborea, el champán, las pajitas..."
    p "¿Qué tienen de malo las pajitas?"
    if persistent.hombre==False:
        lara "Chica, hay que explicártelo todo."
    else:
        lara "Chico, hay que explicártelo todo."
    p "Para ir tan descocada eres un poco..."
    lara "Soy casta y pura por mucho que os la ponga dura."
    p "No, si a mí no..."
    lara "No te preocupes, sé quién puede acompañaros por esos peligrosos túneles."
    lara "El guía de El desfiladero."
    hide cueva1
    scene tavern
    show lara
    lara "El desfiladero es el antro más infecto de toda Atenas."
    p "Pues está bastante limpio."
    lara "Ni siquiera los piratas se atreven a entrar solos."
    lara "Es tan sórdido, que venden alcohol a niños."
    p "Entonces nuestro hombre debe ser más fiero que un pirata."
    p "Más sigiloso que un ninja."
    p "Más astuto que el representante de..."
    lara "En realidad es el hijo del dueño."
    lara "Aunque tiene mucha experiencia como guía."
    lara "Ha organizado expediciones al Kilimanjaro, Eurodisney, Marina d´or y la casa del terror."
    show lara at left with move
    show guia at right
    guia "En realidad lo de la casa del terror sólo lo coorganicé. Contraté a un guía local."
    lara "Hola Pahmuk, ¿Qué tal va todo?"
    guia "No me puedo quejar, sigo viviendo al día."
    lara "¿Estás disponible para un trabajito?"
    lara "Para ti estoy disponible siempre, ya lo sabes."
    guia "¿Habrá atracciones peligrosas, centros de esparcimiento y/o desfiles de carrozas?"
    lara "Por supuesto."
    guia "Entonces me apunto."
    guia "Pero ya sabes que mis honorarios son altos."
    lara "Pagaremos el precio."
    hide guia
    show lara at center with move
    lara "No tendrás 3.000 dólares de Miki por casualidad, ¿verdad?"
    p "Justo ayer me toco esa cantidad en la lotería."
    show lara at left with move
    show guia at right
    lara "Ten, cuéntalo si quieres."
    guia "No hará falta."
    guia "¿Dónde vamos?"
    hide tavern
    scene bg black
    show expression Text("Provistos ya de guía, Lara se despidió, pues nuevas aventuras la esperaban en las cataratas de la mansión Playboy.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(4.5)
    hide text
    scene marco
    show expression Text("Pahmuk resultó ser tan buen guía que ni siquiera le hizo falta echar un vistazo para llegar a la entrada del Hades.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(5.0)
    hide text
    scene cueva2
    p "Pahmuk, esta no es la entrada."
    guia "Tranquilo, yo controlo."
    hide cueva2
    scene bg black
    $ renpy.play("step.wav")
    $ renpy.play("step.wav")
    guia "Mmm, esto está muy oscuro."
    $ renpy.play("step.wav")
    guia "Yo esperaba encontrar unas lucecitas en las paredes de la cueva y un cordón de terciopelo."
    guia "Todas las entradas a parques de atracciones las tienen."
    $ renpy.play("step.wav")
    p "Andemos un poco más."
    guia "Auch"
    p "Perdón, fue sin querer."
    guia "Necesitamos luz, ya."
    p "Me descargué la aplicación de linterna para móvil, pero no alumbra nada."
    p "Por aquí creo que tengo un misto."
    $ renpy.play("llama.wav")
    $ renpy.pause(0.5)
    scene cueva3
    guia "Se ve luz al final del túnel, debemos de estar cerca."
    $ renpy.sound.stop(0,2)
    hide cueva3
    scene centro
    $ renpy.pause(0.5)
    p "Me da que nos hemos equivocado."
    guia "Sí, hace demasiado calor para ser el polo sur."
    rubia "¿Queréis ir a la Antártida?"
    p "Eso teníamos pensado. Llevamos no sé cuánto tiempo dando vueltas por estos túneles."
    rubia "Por aquí no es, volved por donde habéis venido y en la primera bifurcación"
    extend " girad por el túnel de la derecha y llegaréis a vuestro destino."
    p "Le estaré eternamente agradecido."
    p "No puedo pagarle con dinero, pero sí con mi cuerpo."
    guia "Y si aún así no es suficiente todavía para saldar la deuda, yo también me ofrezco a pagar, ¿eh?"
    rubio "¿Veis este pico que tengo en la mano?"
    p "Sí."
    rubio "¿Y veis al viejo colgado de la cuerda?"
    guia "tambien"
    rubio "Pues estaba intentando huir antes de que le clavara el pico en la espalda por haberle tocado el culo a mi chica."
    p "Nosotros nos vamos yendo ya."
    p "Gracias de nuevo."
    scene bg black
    $ renpy.play("step.wav")
    guia "La piedra está más fría, debemos estar llegando."
    p "Sí, yo también lo noto."
    scene bg black with Fade(.25, 0, .75, color="#fff") 
    $ renpy.sound.stop(0,2)
    scene antartida1
    show nieve with dissolve
    p "Debimos coger ropa de abrigo."
    show hans
    punto "No den un paso más, caballerros."
    guia "Anda un pinguino, qué mono, bailate algo."   
    $ renpy.play("disparo.ogg")
    $ renpy.pause(0.5)
    $ renpy.play("caida.wav")
    punto "Bien, un gracioso menos."
    punto  "No se mueva %(name)s"
    p "Me está apuntando un pinguino con un revolver."
    p "Jamás se me ocurriría moverme."
    punto "No me llame pinguino si no quierre que le agujerree la entrepierrna."
    punto "Soy el Oberstumgruppenfuhrer Hans."
    p "Te llamaré Pingu."
    hans "Debió quedarrse en la acogedorra Alemania, su vida se hubierra visto prrolongada y tal vez alguna humana hubierra sentido lástima por usted."
    p "Es que tengo muy mal perder."
    hans "Acompáñeme, porr favorr."
    p "Vale, vale." 
    hide antartida1
    scene hielo2
    p "Oye, ¿de qué va todo esto? Es la primera vez que escucho a un pinguino con acento alemán."
    hans "Es una larga historia que resumiré con tres palabras."
    hans "Somos pinguinos nazis."
    p "Fascinante..."
    hans "Poco antes de la guerra, los alemanes mandarron una expedición a estas tierras."
    hans "El estallido de la contienda les aisló aquí y nos legaron la cultura y el ideario nacionalsocialista."
    hans "Nosotros somos los continuadores del gran Reich."
    p "Sois unos dignos sucesores."
    hans "Gracias."
    p "Y pilláis las ironías a la primera."
    hans "Por algo somos medio germanos."
    scene hielo
    $ renpy.pause(2.0)
    hans "Ya hemos llegado."
    hans "¡Jájá Fuhrer!"
    show hans at left with move
    show meyer at right
    meyer "Buen trabajo, Hans."
    meyer "Vuelve a tu puesto."
    hide hans
    p "No sé qué me da menos confianza, si el acento alemán, o ese estúpido bigote."
    schultz "Volvemos a encontrarnos %(name)s"
    show schultz at left
    p "¡¡Tú!!"
    p "¿Qué hace una chica tan guapa como tú con estos pinguinos, por muy nazis que sean?"
    schultz "Jajaja, veo que no entiendes nada."
    schultz "Yo soy uno de esos pinguinos, como usted los llama despectivamente."
    p "Eso es imposible, la evolución no puede actuar tan rápido."
    p "Aunque eso explicaría el fuerte olor a pescado..."
    schultz "Va desencaminado, el causante de mi forma actual es Fetch."
    p "¿Lo conocen?"
    meyer "Sabemos muchas cosas %(name)s"
    schultz "Estaba en Berlín en una conferencia con los camaradas, cuando yendo camino del acuario."
    extend " el rayo transmutador me dio de lleno."
    schultz "Daba la casualidad de que en ese momento tenía el póster de la chica que tiene ante sus ojos, justo enfrente."
    schultz "Y no hace falta que le explique qué sucedió después..."
    meyer "Rápidamente un equipo de nuestros científicos se dirigió a la ciudad alemana para investigar lo sucedido."
    meyer "Fue así como dimos con el paradero de Fetch. Tras una amistosa charla, descubrimos la utilidad de ese rayo."
    schultz "Una noche lo secuestramos y lo trajimos a nuestra base."
    schultz "Teniamos grandes planes para ese aparato, pero nos surgió un problema. Los pinguinos solo pensamos en otros pinguinos o en pescado."
    schultz "Hicimos innumerables pruebas, pero no sirvieron de nada. Sólo obteniamos nuevos pinguinos"
    meyer "Entonces, en uno de sus paseos por Berlín, Hans comprobó que los hombres quedaban prendados de su cuerpo."
    meyer "Vimos la oportunidad de usar un ejército de atractivas mujeres para dominar a los humanos e instaurar de nuevo el IV Reich."
    schultz "Yo personalmente recorrí el continente en busca de fotos de mujeres, pero los resultados fueron desalentadores."
    hide schultz
    hide meyer
    hide hielo
    scene fea1
    schultz "Yo no le veo nada raro a esta, pero fuí al zoo y uno de los cuidadores insistió violentamente en que regresara a la jaula de los loros."
    hide fea2
    scene fea2
    schultz "Con esta, sin embargo, tuvimos un éxito espectacular con las mujeres, aunque los hombres huían de ella."
    hide fea2
    scene hielo
    show meyer at right
    show schultz at left
    meyer "El resto para qué se las vamos a enseñar..."
    schultz "Y entonces supimos que vendrías, además con el antídoto que podría echar por tierra nuestros planes."
    schultz "Contratamos a Tigara para que se lo robara, pero nos traicionó y lo vendió en el mercado negro."
    p "¿Cómo supieron de mi existencia?"
    jim2 "Juro que no lo publiqué en mi blog."
    meyer "Nos descargamos el juego desde la página de Mr Roboto."
    schultz "Y además descubrimos en sus posts datos interesantes sobre su persona."
    schultz "¿Sabias que es tan asiduo del Club Momentos, que le hacen el 50 por ciento de descuento?"
    p "No tenía ni idea."
    schultz "Me lo acabo de inventar, pero a que estaría bien, ¿eh?"
    schultz "Como iba diciendo, seguimos sus pasos durante su búsqueda de las bolas."
    meyer "E intentamos evitar que las recuperara."
    schultz "Pero cuando fue evidente que te librabas de todas, decidimos usarte."
    p "Y entonces montásteis el montaje de las fotos."
    schultz "En efecto."
    meyer "Una vez que le hemos puesto en antecedentes, es hora de que acabemos con usted."
    meyer "Pero antes, vea como se construye el nuevo mundo desde sus cimientos."
    p "¿Cómo espera que los gobiernos mundiales se rindan ante este puñado de pájaros?"
    meyer "Nos subestima."
    meyer "Mire una muestra de mi poder y del fanatismo con el que mis soldados me seguirán hasta el fín."
    meyer "¡Walter!"
    pingu2 "Ja mein Fuhrer."
    meyer "Salta al precipio."
    scene salto
    $ renpy.pause (1.0)
    $ renpy.play("falling.wav")
    $ renpy.play("inmersion.ogg")
    $ renpy.pause(6.0)
    scene hielo
    p "Pero eso no vale, ha saltado al agua."
    meyer "¿Cómo que no vale?"
    meyer "Un buen nazi no se tira al mar, el agua le arruga el uniforme."
    p "Pero él no lleva..."
    meyer "¡A callar!"
    pingu2 "Ya estoy de vuelta, Fuhrer."
    meyer "Vuélvete a tirar y enseña cómo obedece un pinguino alemán."
    pingu2 "¡Jawohl!"
    scene pingus2
    meyer "Traedlo."
    hide pingus2
    scene pingus
    show meyer
    meyer "¡¡Pinguinos!!"
    meyer "Durante décadas, los malvados capitalistas y los cerdos comunistas se han reído de nosotros."
    meyer "Han elevado a la categoría de burla nuestras accidentadas caídas."
    meyer "Han ridiculizado nuestro aspecto." 
    meyer "¡¡¡A los que visten frac les llaman pinguinos!!!"
    ping "¡¡Qué hijos de puta!!"
    meyer "Y para colmo, les parece cómica nuestra forma de caminar."
    extend " ¡Pero eso se va a acabar!"
    meyer "Hemos desarrollado una nueva arma maravillosa que dará un vuelco a nuestra situación."
    meyer "Contemplad el inicio de una nueva era de dominio pinguinil."
    meyer "Adelante, Schultz."
    scene bg black with Fade(.25, 0, .75, color="#fff") 
    scene hielo
    show hans2
    meyer "¡¡¡Jajaja, funciona!!!"
    meyer "Aunque tengo algo de frío..."
    pingu1 "Mein Gott, ¡¡vaya madonna!!"
    pingu2 "Ja, aunque tiene los melones un poco caídos."
    meyer "Vamos soldados, a la cámara de conversión."
    meyer "Vosotros, llevadlo a la celda con Fetch."
    hide hans2
    scene celda
    show hans
    pingu1 "Primate, mira qué te traigo."
    fetch "¿Otro plato de sushi?"
    show hans at left with move
    show fetch2 at right
    pingu1 "Mucho mejor, un miembro de tu especie."
    pingu1 "Ahora podrás aparearte."
    hide hans
    show fetch2 at center with move
    fetch "Son unos cabritos adorables, ¿no es cierto?"
    fetch "No le malinterprete, es que no saben distinguir entre sexos"
    p "¿Fetch?"
    fetch "El mismo."
    p "No eres como en la foto."
    fetch "Siempre te sacan feo en las fotos criminales."
    fetch "A nadie le gustaría arrestar a alguien hermoso como yo."
    p "¿Por qué no cambias de postura?"
    fetch "Es que estoy feliz de ver a una persona normal por primera vez en tanto tiempo."
    $ renpy.play("cerrojo.mp3")
    pingu1 "Acompáñenme."
    p "¿Qué crees que querrán de nosotros?"
    fetch "¿Que le digamos cómo cocinar el pescado?"
    scene lava
    show meyer at left
    meyer "Caballeros, gracias por su ayuda."
    meyer "Puede que los libros de historia que escribamos hablen de ustedes, ya lo pensaremos."
    meyer "Mientras tanto, ya saben que para formar parte de la posteridad, es condición necesaria morir."
    meyer "Colgadlos sobre el pozo de lava que compramos en el IKEA maligno, hace una semana."
    p "¿Es que hay alguno bueno?"
    meyer "Jajá, caballeros."
    hide meyer
    fetch "Qué inhumanos, quieren cocinarnos como a dos cochinillos, con lo fácil que sería tirarnos al pozo."
    if persistent.hombre==False:
        hijo "!!Máma, Máma!!"
    else:
        hijo "!!Pápa, Pápa!!"
    show hijo2
    p "¡¡¡¡¡Hijo mío!!!!!"
    hijo "Estuve buscandote por todo el orbe."
    hijo "¿Ma que cosa hace colgado ahí como una longaniza?"
    p "Un pinguino malo me quiere hacer daño, Giuseppe."
    hijo "¡Qué terribile!"
    if persistent.hombre==False:
        p "Anda, ven y libera a tu máma."
    else:
        p "Anda, ven y libera a tu pápa."
    hijo "Ah, che ahora sonno el tuo fillo, ¿eh?"
    if persistent.hombre==False:
        hijo "Cuando Giuseppe dice tú eres máma, tú no crees a Giuseppe"
    else:
        hijo "Cuando Giuseppe dice tú eres pápa, tú no crees a Giuseppe"
    fetch "Eres de lo peor, si tiene tus mismos ojos."
    p "Tú callate."
    p "Perdona hijo, es que estaba algo cansado y no te ví bien."
    hijo "Te perdono. Io no sonno reconroso."
    p "Muchas gracias, Giuseppe."
    p "Ahora tenemos que ir a por esos pinguinos."
    p "Tú vete a casa, cuando termine con esto, me iré contigo."
    if persistent.hombre==False:
        hijo "Arrivederci Máma."
    else:
        hijo "Arrivederci pápa."
    hide hijo2
    show fetch2
    p "Vamos, tenemos que patear unos cuantos traseros fríos."
    p "Y cambia de postura ya."
    fetch "¡¡¡¡Es que estoy muy contento por habernos librado de morir!!!!"
    hide fetch2
    hide lava
    scene cuevahp
    fetch "Vaya juerga que se han montado aquí, ¿no?"
    p "Jamás en mis... años vi algo parecido."
    scene marco
    show expression Text("En solidaridad con las personas invidentes, no mostraré la escena: Un continuo mar de pechos inflamados por la cirugia y la bondad extrema de la naturaleza.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(5.5)
    hide text with dissolve
    scene marco
    show expression Text("Una masa compacta de pezón contra pezón, aureola contra aureola, desde la base hasta el techo de la cueva, aprisionados por su propia voluptuosidad.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(5.5)
    hide text with dissolve
    scene marco
    show expression Text("Sin poder desplazarse un solo centimetro hasta el final de los tiempos o hasta que explote algún pecho de silicona...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
    $ renpy.pause(5.5)
    hide text with dissolve
    hide marco
    scene cuevahp
    p "Ya lo dice el refrán:"   # al llenarse la cueva de tias
    extend " En tetas, como en bravura, la mesura es buena cura."
    show fetch2 
    fetch "Mira, junto a esa roca tienes el consolador transformador."
    fetch "Lo cogí para cumplir un sueño, hecho realidad ante mis ojos."
    scene tetasp
    fetch "Cógelo y vete, yo voy a ver si puedo colarme entre esos cuerpos y morir cómo siempre quise:"
    extend " De un tetazo"
    hide fetch2
    #zoom hacia el interior de los pechos
    hide tetasp
    scene cuevahp
    p "Qué magnífico valor..."
    p "Ni en la muerte cambió de postura."
    p "Debía de estar contento de morir así..."
    hide cuevahp
    jump final
    