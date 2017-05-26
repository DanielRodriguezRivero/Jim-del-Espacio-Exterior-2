init:
    
    $ persistent.vb = False        
    $ persistent.vb2 = False 
    
label boliches:
    if persistent.finbolas == False:
        if persistent.vb==False:
            scene calleb2
            p "Hay algo en esta ciudad que me resulta familiar."
            carmoine2 "Debe de ser su aire limpio, sus magníficas playas, la hospitalidad de la gente..."
            #ruido gentio
            if persistent.hombre==False:
                p "Oh, un mercadillo. Cuando era pequeña solía ir todos los domingos a comprar tebeos de Mortadelo."
            else:
                p "Oh, un mercadillo. Cuando era pequeño solía ir todos los domingos a comprar muñecas."
            p "¿Podemos ir?"
            p "¡¡¡Por fa, por fa!!!"
            anette2 "Bueno vale, pero solo a mirar, ¿eh? No me empieces a pedir cosas en cada puesto, que el dinero cuesta mucho de ganarlo."
            hide calleb2
            scene rastro
            p "Ooooh, ¡¡el Rescate Atlantida!!"
            p "Uau, llevo buscando este juego desde hace siglos (literalmente)."
            p "De pequeño lo tenía y desapareció de mi habitación misteriosamente, justo el día en que vino a visitarme un primo del pueblo."
            p "¿Puedo comprarlo?"
            p "Venga, venga."
            p "¡¡¡Por favoooooooooooooooooooooooooooooooooooooooooooooooooooor!!!"
            anette2 "No sé cómo, pero siempre me acabas convenciendo."
            p "¡¡¡Bieeeeen. Eres la mejor!!!"
            "Los mafiosos retienen a [p] y le endosan una bomba."
            tigara "¿No tendrían un reposabrazos de titanio por casualidad?"
            p "¡¡Por fin!! Reconocería esa voz entre un millón, y esos pechos entre cuarenta millones."
            show tigara
            if persistent.hombre==False:
                tigara "Volvemos a encontrarnos, señora perdedora."
            else:
                tigara "Volvemos a encontrarnos, señor perdedor."
            p "Un respeto. Es triste de jugar, pero más triste es de robar."
            if persistent.hombre==False:
                tigara "Si insinúas que te robé, estás completamente equivocada."
            else:
                tigara "Si insinúas que te robé, estás completamente equivocado."
            tigara "Simplemente tomé una compensación por los gastos de juego que ocasionaste."
            p "Ahora vendrás conmigo."
            tigara "No, vosotros vendréis conmigo."
            tigara "Otto, acompaña a los señores a la limusina."
            show tigara at left with move
            show otto at right
            otto "Como mandes, Reina."
            p "Es uno y escuchimizado. Nosotros somos tres."
            otto "Y uno de ellos no sabe contar."
            otto "Somos yo, Smith and Wesson."
            tigara "Llévalos a nuestro piso franco."
            tigara "Yo iré en cuanto encuentre ese dichoso reposabrazos."
            scene marco
            show expression Text("En vista de que poco podían hacer, se dejaron llevar mansamente al piso franco,muy bien decorado por otra parte, donde estuvieron esperando media hora...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(4.5)
            hide text
            scene habibol
            show otto
            p "¿Y en verano no huele aquello?"
            otto "No le digas que te lo he dicho yo, pero cuando llega el mes de julio, no le hace falta pistola para matar a alguien."
            show tigara at left
            show otto at right with move
            tigara "Al fin estoy aquí, y con las manos vacías."
            p "Será un decir, ¿no?"
            tigara "Bien %(name)s, creo saber por qué me estás buscando."
            p "Desde luego porque me enamoré de la finura de tus manos, no, desde luego."
            if persistent.bolas>1:
                tigara "Como supongo ya sabrás, partí las bolas en varios trozos. Así podia sacar un mejor precio por ellas."
            else:
                tigara "Dividí las bolas chinas en varios trozos para poder sacar un mejor precio por ellas."
            p "¿Por unas bolas chinas?"
            tigara "¿Acaso un diamante con forma de clítoris pierde su valor?"
            tigara "Poco después de robártelas, mandé analizarlas. En su composición había sustancias que no se encuentran en esta galaxia."
            tigara "Lo que las convertía en algo muy valioso."
            tigara "Por ahora solo he vendido un pedazo. El otro lo retengo en espera de otro vendedor, con el que por cierto he quedado dentro de media hora."
            tigara "Lo cual me pone en una difícil disyuntiva."
            tigara "¿Qué hago con vosotros?"
            anette2 "¿Volarnos por los aires?"
            tigara "Sí, eso es lo que haré."
            tigara "Otto, ve a por el coche."
            hide otto
            show hamilton at right
            hamilton "Jefa, ¿puedo conducir yo?"
            tigara "Ni hablar, tú quedate aquí y asegurate de que no se muevan mientras armo la bomba."
            hide tigara
            show hamilton at Position(ypos=350, yanchor=1.0)
            hamilton "Tranquila jefa, no lo harán."
            p "Me voy a mover ahora mismo."
            $ renpy.play("arma.mp3")
            $ renpy.pause(1.0)
            hamilton "Vamos hazlo, alégrame el día."
            tigara "Hamilton, sube al coche."
            hide hamilton
            show tigara 
            tigara "Es hora de despedirnos, %(name)s"
            tigara "No llegamos a conocernos lo suficiente como para considerarte mi archienemigo, pero al menos has ascendido a la categoría de grano en el culo."
            p "Es un honor."
            hide tigara
            sandrine2 "¿Y ahora, quién podrá defendernos?"
            $ renpy.play("puerta.wav")
            $ renpy.play("puerta.wav")
            $ renpy.pause(1.0)
            hide habibol
            scene luigi
            luigi "¿Llego en mal momento?"
            p "¡Te quiero, Luigi!"
            luigi "Y yo a tí %(name)s, desde la primera vez que me elegiste en el Mario Kart, cuando todos escogían al chulo de mi hermano."
            p "Liberanos para que podamos vivir el resto de nuestros días juntos."
            hide luigi
            scene habibol
            show sandrine at left
            show carmoine at center
            show anette at right
            sandrine "¿Qué hay entre tú y ese fontanero?"
            p "No hay tiempo para cotilleos, intentad detener a Tigara y sus compinches. Yo desactivaré la bomba. No puedo dejar que estalle."
            hide sandrine 
            hide carmoine
            hide anette
            scene bomba
            jim2 "Suerte que la bomba es muy rudimentaria."
            p "Y tan rudimentaria, como que solo son tres cables. No veo explosivos ni detonador. Hasta un niño de tres años hubiera hecho una bomba mejor."
            p "¿Cual corto?"
            jim2 "Hagas lo que hagas, no cortes el rojo."
            p "Pero ¿por qué?"
            jim2 "Tú hazme caso, el rojo no."
            p "Pero..."
            jim2 "¿Qué te he dicho? Deja al rojo tranquilo."
            hide bomba
            $ result = renpy.imagemap("bomba.png", "bomba.png", [
            (126, 20, 186, 582, "rojo2"),  #coordenadas para los boliches, etc
            (307, 20, 372, 581, "amarillo2"),   #explosion
            (530, 21, 657, 583, "verde2"),
            ], focus="imagemap")
    
    
            if result == "rojo2":
                #esconder la imagen de europa con alguna transicion chula
                jump rojo2
            if result == "amarillo2":
                jump amarillo2
            if result == "verde2":
                jump verde2
        else:
            scene callesb
            "Centenares de jubilados se dirigen a las playas en una marcha solo comparable a la de los elefantes que se internan en la sabana, en busca de un buen lugar donde morir."
            hide callesb
            jump map

    else:
        if persistent.vb2 ==False:
            if persistent.guerra==False:
                scene playa2
                show roger
                roger "Hola preciosidad, ¿te apetece un Martini?"
                p "Sería un placer."
                roger "Se lo preguntaba a la morena."
                show roger at left with move
                show sandrine at right
                sandrine "Con mucho gusto."
                roger "Pero... "
                sandrine "Soy rubia de bote."
                hide playa2
                $ persistent.vb2=True
                jump map
            else:
                scene playa2
                jim2 "Roger Moore sería un perfecto juez para el concurso de San Marino."
                p "Estoy de acuerdo."
                show roger
                p "Señor Moore, el mundo libre le necesita."
                roger "¿Y cuándo no?"
                if persistent.hombre==False:
                    roger "Voy contigo, cariño."
                else:
                    roger "Voy contigo, hijo."
                hide roger
                hide playa2
                scene escenario
                show presentadora
                presentadora "Señoras y señores, bienvenidos al primer festival de cánticos militares de San Marino."
                presentadora "El de hoy, es un evento muy especial donde se decidirá el futuro de este gran país."
                presentadora "Antes de comenzar, damos las gracias a la Fundación \"Bill Gates por la paz mundial y la instalación de Windows\""
                presentadora "por cedernos amablemente este auditorio."
                presentadora "Después del festival, quienes lo deseen podrán quedarse a una conferencia donde un montón de empollones podrán charlar sobre sus cosas sin que los cubran de brea y los tiren al río."
                presentadora "Demos comienzo pues a la velada."
                presentadora "La noche la abrirán..."
                publico "¿Y quién te abrirá a ti, morena?"
                $ renpy.play("risas.wav")
                $ renpy.pause(4.0)
                presentadora "Como les decía, abrirán la competición los muchachos del Pelotón Baker, de la resistencia de San Marino."
                $ renpy.play("aplausos.ogg")
                hide presentadora
                $ renpy.pause(2.0)
                # voces
                soldados "El sargento Furillo tiene la picha corta. Eso nos ha dicho en privado su esposa."
                $ renpy.pause(0.5)
                roger2 "A mí también me lo dijo hace unos meses, y por lo que pude ver, es cierto."
                $ renpy.pause(0.5)
                soldados "En la guerra hay que luchar, aunque yo prefiero follar. De todas formas el enemigo es muy feo, ni con la cara tapada le metía yo un dedo."
                $ renpy.pause(0.5)
                roger2 "Hablando de dedos, chicas, tengo diez..."
                $ renpy.pause(0.5)
                soldados "Jesucristo dijo amaos los unos a los otros, y al que no ame palos a cascoporro."
                $ renpy.pause(0.5)
                roger "Ese debe ser el capellán del cuerpo."
                $ renpy.pause(0.5)
                soldados "Los del Miniejército Rojo son unos iletrados, ni las gafas de ver tienen el graduado."
                $ renpy.play("aplausos.ogg")
                roger2 "Será mejor entonces que lleven lentillas."
                show presentadora
                presentadora "Bien, a continuación es el turno del coro glorioso Miniejército Rojo de San Marino, liderado por Stalisnav Petrov, famoso músico local."
                publico "Ese no es de aquí, ayer hice una fiesta para todos los habitantes y no le ví en mi salón."
                presentadora "Adelante, por favor."
                hide presentadora
                soldados2 "El coño de mi novia está muy bien amueblado. Metí mi polla y a vivir se ha quedado."
                $ renpy.pause(1.0)
                roger2 "Tal y como está la vivienda hoy día, creo que todos deberíamos imitar a ese miembro viril."
                roger2 "Ya sabéis jóvenes, buscad un agujero caliente, y meteos en él."
                $ renpy.pause(0.5)
                soldados2 "Mi rifle no dispara balas de fogueo. Ahí te quedas, en nueve meses te veo."
                $ renpy.pause(0.5)
                roger2 "Es curioso, el otro día conocí a un chaval, Giuseppe se llamaba, sus padres renegaban de él, pobrecillo."
                roger2 "Una gran letra que encierra un problema endémico en la juventud, poneos forros, jóvenes."
                $ renpy.pause(0.5)
                soldados2 "En Laponia se folla poco, para no calentar el globo."
                roger2 "Loable acción por parte de los esquimales, que, siento decirlo, no vale para nada mientras yo siga en activo."
                $ renpy.pause(1.0)
                show presentadora
                presentadora "Con este último cántico, se dan por finalizadas las actuaciones."
                presentadora "El jurado está reunido en estos momentos, y cuando tomen su decisión, se procederá a hacerla pública."
                publico "¿Y cuándo te vas a hacer tú \"pública\"?"
                $ renpy.play("risas.wav")
                $ renpy.pause(2.0)
                hide presentadora
                $ renpy.pause(3.0)
                show roger
                roger "Ciudadanos de San Marino, mentiría si dijera que este es el concurso más estrambótico en el que he participado."
                roger "En mis años mozos fui concursante en un certamen de aplastar calabazas con el trasero."
                roger "Al finalizar el día, tenia más puntos en el culo que el Real Madrid jugando en la liga de Andorra"
                roger "Lo que es innegable, es que habéis dado un ejemplo impagable a todas las naciones del planeta, que miran a San Marino como modelo a seguir en el futuro."
                roger "El mundo iría mejor si los conflictos se resolvieran con cánticos ofensivos."
                roger "Al menos habría menos muertos."
                $ renpy.pause(0.5)
                roger "Antes de dar mi veredicto, recuerden que lo importante es participar."
                $ renpy.pause(0.5)
                publico "Si es en un menage a trois con la presentadora, yo me apunto."
                $ renpy.play ("tiros.wav")
                roger "El subcampeón recibirá un contrato por dos años con Vale Music, para grabar tres discos."
                $ renpy.play ("aplausos.ogg")
                $ renpy.pause(3.0)
                roger "Y el campeón, ganará este país."
                roger "Por favor, el sobre."
                show azafata2 at right
                show roger at left with move
                roger "Gracias nena, ten mi número."
                hide azafata2
                show roger at center with move
                roger "And the winner is..."
                roger "El Frente para la liberación de San Marino por..."
                roger "Jesucristo dijo amaos los unos a los otros, y al que no ame palos a cascoporro."
                $ renpy.play("aplausos.ogg")
                $ renpy.pause(3.0)
                hide roger
                show ike
                ike "Jajajajaj"
                ike "Victoria"
                ike "¡¡¡All your country are belong to us!!!"
                scene marco
                show expression Text("Perdido el concurso, los comunistas cogieron sus bártulos y se fueron a casa tranquilamente.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(2.5)
                hide text with dissolve
                hide marco
                scene despacho2
                show roger
                roger "Bien caballeros, me vuelvo a Los Boliches."
                roger "No me gusta estar tanto tiempo lejos del paraíso."
                ike "Gracias por darnos la victoria."
                roger "No me las de."
                roger "Tenía un buen par de razones."
                hide roger
                show roger2
                roger "Vámonos chicas."
                hide roger2
                scene victoria
                show expression Text("Y así fue cómo los hijos de San Marino ganaron su libertad.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(2.5)
                hide text with dissolve
                hide victoria   
                scene bg black
                show expression Text("Libre ya el paso a Roma, hacia allí se dirigieron nuestros héroes...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(4.5)
                hide text with dissolve
                scene trevi
                show kirai
                kirai "Hombre, tú por aquí."
                kirai "¿Probaste el mapa hecho de dorayakis? Estaba bueno, ¿verdad?"
                jim2 "Hay que tener mucha hambre para comerse eso."
                kirai "Tío, qué reloj más guapo. ¿Lo has sacado de una tienda de Akihabara?"
                p "Sí, sí. El caso es que necesitaría un favor."
                kirai "Por alguien que es poseedor de tecnología punta, hago lo que sea."
                p "Verás, tú tienes mucha mano con los orientales por lo que veo."
                kirai "Como son pequeños y manejables..."
                p "A eso iba, verás, necesito una cámara de fotos para..."
                p "Bueno, para un asuntillo."
                kirai "Va dilo, si es la última moda en Japón. Tú quieres fotografiarte desnudo."
                p "Eso mismo, lo malo es que no tengo un duro y claro, por aquí hay tanto japonés con cámara..."
                kirai "Sé donde quieres llegar."
                kirai "Déjame que elija a nuestra \"victima.\""
                hide kirai
                show turista
                kirai "Qué guapa es."
                kirai "Déjamela a mí."
                show turista at right with move
                show kirai at left
                kirai "Hola, ¿cómo va eso?"
                turista "¿Sexo?"
                turista "¡¡¡Todos los latinos sois iguales!!!"
                turista "Ni siquiera sabes mi nombre. Has visto un cuerpo trabajado e irresistible acompañado por un rostro angelical y has dicho:"
                turista "Voy a entrarle a saco"
                turista "¿Sabes lo que te digo?"
                turista "Vámonos al callejón de atrás que yo he venido a este país a tirarme a un italiano."
                kirai "Io sonno tu homme."
                kirai "Arrivederci %(name)s"
                p "Tráeme la cámara cuando termines, ¿eh?"
                scene marco
                show expression Text("Treinta segundos después...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(2.5)
                hide text with dissolve
                scene trevi
                kirai "Aquí tienes %(name)s Espero haberte servido de ayuda."
                p "Muchas gracias, es todo lo que necesitaba."
                kirai "Me vuelvo al callejón que la he dejado desnudándose."
                kirai "¡¡¡¡¡¡¡Banzaiiiiii!!!!!!!"
                $ persistent.camara=True
                $ persistent.finguerra=True
                $ persistent.guerra=False
                $ persistent.vroma2=True
                $ persistent.vb2=True
                jump map
        else:
            if persistent.guerra==False:
                scene beach
                "Roger Moore toma el sol despreocupado en la playa, rodeado de decenas de atractivas mujeres en bikini."
                "Una agradable sensación de bienestar flota en el aire."
                "Ahora que el final parece tan cerca, te apena la posibilidad de no volver a ver este pueblo que siempre permanecerá en tu corazón."
                hide beach
                jump map
            else:
                scene playa2
                jim2 "Roger Moore sería un perfecto juez para el concurso de San Marino."
                p "Estoy de acuerdo."
                show roger
                p "Señor Moore, el mundo libre le necesita."
                if persistent.hombre==False:
                    roger "Voy contigo, cariño."
                else:
                    roger "Voy contigo, hijo."
                hide roger
                hide playa2
                scene escenario
                show presentadora
                presentadora "Señoras y señores, bienvenidos al primer festival de cánticos militares de San Marino."
                presentadora "El de hoy, es un evento muy especial, donde se decidirá el futuro de este gran pais."
                presentadora "Antes de comenzar, damos las gracias a la Fundación \"Bill Gates por la paz mundial y la instalación de Windows\""
                presentadora "por cedernos amablemente este auditorio"
                presentadora "Despues del festival, quienes lo deseen podrán quedarse a una conferencia donde un montón de empollones podrán charlar sobre sus cosas sin que los cubran de brea y los tiren al río."
                presentadora "Demos comienzo pues a la velada."
                presentadora "La noche la abrirán..."
                publico "¿Y quién te abrirá a ti, morena?"
                $ renpy.play("risas.wav")
                $ renpy.pause(4.0)
                presentadora "Como les decía, abrirán la competición los muchachos del Pelotón Baker, de la resistencia de San Marino."
                $ renpy.play("aplausos.ogg")
                hide presentadora
                $ renpy.pause(2.0)
                # voces
                soldados "El sargento Furillo tiene la picha corta. Eso nos ha dicho en privado su esposa."
                roger "A mí también me lo dijo hace unos meses, y por lo que pude ver, es cierto."
                $ renpy.pause(1.0)
                soldados "En la guerra hay que luchar, aunque yo prefiero follar. De todas formas el enemigo es muy feo, ni con la cara tapada le metia yo un dedo"
                roger2 "Hablando de dedos, chicas, tengo diez..."
                $ renpy.pause(0.5)
                soldados "Los del Miniejército Rojo son unos iletrados, ni las gafas de ver tienen el graduado."
                roger2 "Será mejor que lleven lentillas entonces."
                $ renpy.pause(0.5)
                soldados "Jesucristo dijo amaos los unos a los otros, y al que no ame palos a cascoporro."
                $ renpy.pause(0.5)
                roger "Ese debe ser el capellán del cuerpo."
                $ renpy.pause(0.5)
                $ renpy.play("aplausos.ogg")
                $ renpy.pause(2.0)
                show presentadora
                presentadora "Bien, a continuación, es el turno del coro glorioso Miniejército Rojo de San Marino, liderado por Stalisnav Petrov, famoso músico local."
                publico "Ese no es de aquí, ayer hice una fiesta para todos los habitantes y no le vi en mi salón."
                presentadora "Adelante, por favor."
                hide presentadora
                $ renpy.pause(1.0)
                soldados2 "El coño de mi novia está muy bien amueblado. Metí mi polla allí y a vivir se ha quedado."
                roger2 "Tal y como está la vivienda hoy día, creo que todos deberíamos imitar a ese miembro viril."
                roger2 "Ya sabéis jovenes, buscad un agujero caliente y meteos en él."
                $ renpy.pause(0.5)
                soldados2 "Mi rifle no dispara balas de fogueo. Ahí te quedas, en nueve meses te veo."
                roger2 "Es curioso, el otro día conocí a un chaval, Giuseppe se llamaba, sus padres renegaban de él, pobrecillo."
                roger2 "Una gran letra que encierra un problema endémico en la juventud, poneos forros, jóvenes."
                $ renpy.pause(0.5)
                soldados2 "En Laponia se folla poco, para no calentar el globo."
                roger "Una iniciativa loable por parte de los esquimales, pero que siento decir, no vale para nada mientras yo esté en activo."
                $ renpy.pause(0.5)
                show presentadora
                presentadora "Con este último cántico, se dan por finalizadas las actuaciones."
                presentadora "El jurado está reunido en estos momentos, y cuando tomen su decisión, se procederá a hacerla pública."
                publico "¿Y cuando te vas a hacer tú \"pública\"?"
                $ renpy.play("risas.wav")
                $ renpy.pause(2.0)
                hide presentadora
                $ renpy.pause(2.0)
                show roger
                $ renpy.pause(1.0)
                roger "Ciudadanos de San Marino, mentiría si dijera que este es el concurso más estrambótico en el que he participado."
                roger "En mis años mozos fui concursante en un certamen de aplastar calabazas con el trasero."
                roger "Lo que es innegable, es que habéis dado un ejemplo impagable a todas las naciones del planeta, que miran a San Marino como modelo a seguir en el futuro."
                roger "El mundo iría mejor si los conflictos se resolvieran con cánticos ofensivos."
                roger "Al menos habría menos muertos."
                $ renpy.pause(0.5)
                roger "Antes de dar mi veredicto, recuerden que lo importante es participar."
                $ renpy.pause(0.5)
                publico "Si es en un menage a trois con la presentadora, yo me apunto."
                $ renpy.play ("tiros.wav")
                presentadora "Gilipollas"
                $ renpy.pause(2.0)
                roger "El subcampeón recibirá un contrato por dos años con Vale Music, para grabar tres discos."
                $ renpy.play ("aplausos.ogg")
                $ renpy.pause(3.0)
                roger "Y el campeón, ganará este país."
                roger "Por favor, el sobre."
                $ renpy.pause(2.0)
                show azafata2 at right
                show roger at left with move
                roger "Gracias nena, ten mi número."
                hide azafata2
                show roger at center with move
                roger "And the winner is..."
                roger "El Frente para la liberación de San Marino por..."
                roger "Jesucristo dijo amaos los unos a los otros, y al que no ame palos a cascoporro."
                $ renpy.play("aplausos.ogg")
                $ renpy.pause(3.0)
                hide roger
                show ike
                ike "Jajajajaj"
                ike "Victoria"
                ike "¡¡¡All your country are belong to us!!!"
                scene marco
                show expression Text("Perdido el concurso, los comunistas cogieron sus bártulos y se fueron a casa tranquilamente.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(4.5)
                hide text with dissolve
                hide marco
                scene despacho2
                show roger
                roger "Bien caballeros, me vuelvo a Los Boliches."
                roger "No me gusta estar tanto tiempo lejos del paraíso."
                ike "Gracias por elegirnos ganadores."
                roger "Tenía un buen par de razones."
                hide roger
                show roger2
                roger "Vámonos, chicas."
                hide roger2
                scene victoria
                show expression Text("Y así fue cómo los hijos de San Marino ganaron su libertad.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(2.5)
                hide text with dissolve
                hide victoria
                #luego ir a roma a por camara con kirai"
                scene marco
                show expression Text("Libre ya el paso a Roma, hacia allí se dirigieron nuestros héroes...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(4.5)
                hide text with dissolve
                hide marco
                scene trevi
                show kirai
                kirai "Hombre, tú por aquí."
                kirai "¿Probaste el mapa hecho de dorayakis? Estaba bueno, ¿verdad?"
                jim2 "Hay que tener mucha hambre para comerse eso."
                kirai "Tío, qué reloj más guapo ¿Lo has sacado de una tienda de Akihabara?"
                p "Sí, sí. El caso es que necesitaria un favor."
                kirai "Por alguien que es poseedor de tecnología punta, hago lo que sea."
                p "Verás, tú tienes mucha mano con los orientales por lo que veo."
                kirai "Como son pequeños y manejables..."
                p "A eso iba, verás, necesito una cámara de fotos para..."
                p "Bueno, para un asuntillo."
                kirai "Va dilo, si es la última moda en Japón. Tú quieres fotografiarte desnudo."
                p "Sí, eso mismo. Lo malo es que no tengo un duro y claro, por aquí hay tanto japonés con cámara..."
                kirai "Sé dónde quieres llegar."
                kirai "Déjame que elija a nuestra \"victima\""
                hide kirai
                show turista
                kirai "Qué guapa es."
                kirai "Déjamela a mí."
                show turista at right with move
                show kirai at left
                kirai "Hola, ¿cómo va eso?"
                turista "¿Sexo?"
                turista "¡¡¡Todos los latinos sois iguales!!!"
                turista "Ni siquiera sabes mi nombre. Has visto un cuerpo trabajado e irresistible acompañado por un rostro angelical y has dicho:"
                turista "Voy a entrarle a saco."
                turista "¿Sabes lo que te digo?"
                turista "Vámonos al callejón de atrás que yo he venido a este país a tirarme a un italiano."
                kirai "Io sonno tu homme."
                kirai "Arrivederci %(name)s"
                p "Traeme la cámara cuando termines, ¿eh?"
                scene marco
                show expression Text("Treinta segundos después...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
                $ renpy.pause(2.5)
                hide text with dissolve
                scene trevi
                show kirai
                kirai "Aquí tienes %(name)s Espero haberte servido de ayuda."
                p "Muchas gracias, es todo lo que necesitaba."
                kirai "Me vuelvo al callejón que la he dejado desnudandose."
                kirai "¡¡¡¡¡¡¡Banzaiiiiii!!!!!!!"
                $ persistent.camara=True
                $ persistent.finguerra=True
                $ persistent.guerra=False
                $ persistent.vb2=True
                $ persistent.vb2=True
                jump map
                
label rojo2:
    
    $ renpy.play("error.wav")
    scene pantalla
    $ renpy.pause(2.5)
    jim2 "Te dije que no lo cortaras."
    hide pantalla with dissolve
    scene habibol
    jim2 "Por suerte se trataba de un error leve y podemos seguir jugando."
    p "Menos mal, qué susto."
    jim2 "Qué suerte no estar en uno de esos juegos de Sierra."
    jim2 "¿Te imaginas leer todo el rollazo de antes de nuevo?"
    hide habibol
    jump bolichesfin
    

label verde2:
    show explosion
    $ renpy.play("explosion.mp3")
    $ renpy.pause (4.5)
    hide explosion with fade
    $ renpy.sound.stop(0,1)
    show bg black
    $ renpy.pause(3.0)
    show vutroi
    "¡¡Vutroi!! ¡¡Vutroi!! Tenemos uno nuevo."
    $ renpy.pause(2.0)
    "Parece que Vutroi está ocupado."
    p "¿Quién eres?"
    if persistent.hombre==False:
        "¿Quién voy a ser, muchacha?"
    else:
        "¿Quién voy a ser, muchacho?"
    "Soy yo."
    p "Ah, ya me ha quedado claro."
    "Que estropicio has formado ahí abajo, ¿no?"
    "Suele pasar mucho. La gente tiene una preferencia enfermiza a cortar los cables verdes."
    "Color esperanza dicen... el color de la muerte, eso es lo que es."
    if persistent.hombre==False:
        "Si permites que te de un consejo, a lo único verde que puedes acercarte es a un activista de Greenpeace que esté bueno."
        "Pero claro, son todos unos empollones poco amigos del agua."
    else:
        "Si permites que te dé un consejo, a lo único verde que puedes acercarte es a una activista de Greenpeace que esté buena."
        "Pero claro, son todas unas empollonas poco amigas del agua."
    "Bueno, te devolvere a la Tierra después de haber desactivado la bomba."
    "Después de todo, el cielo puede esperar otro día."
    "Además, bastante tengo con tener que soportar a Vutroi."
    "Y recuerda, no te toques."
    "Y si lo haces, cierra la puerta que no tengo por qué verte."
    hide vutroi
    jump bolichesfin
    
label amarillo2:
    scene bomba2
    jim2 "Lo has conseguido. ¡¡El reloj se ha parado!!"
    $ renpy.play("explosion.ogg")  #sonido golpe fuerte
    scene bg black
    $ renpy.pause(3.0)
    scene pradera
    p "¿Es esto el paraíso?"
    jim2 "No, es un wallpaper del Windows."
    jim2 "Se cayó un portatil de la estantería que está sobre ti y te cayó en la cabeza."
    jump bolichesfin

label bolichesfin:
    scene habibol
    jim2 "Rápido, salgamos fuera."
    scene www
    show anette
    anette "Los tenemos %(name)s. La mala noticia es que Tigara consiguió escapar."
    anette "Cuando nos vieron salir, se sorprendieron mucho."
    anette "Hamilton tomó el volante, pero se le caló el coche."
    p "Se haría un lío con la palanca de cambios, como solo tiene 4 dedos..."
    show anette at left with move
    show sandrine
    sandrine "Cuando Tigara comprendió que íbamos a cogerla, saltó del coche y salió huyendo."
    sandrine "No pudimos alcanzarla."
    show sandrine at right with move
    show carmoine
    carmoine "Quién se iba a imaginar que se puede correr con tanta rapidez con las manos en la cabeza..."
    p "Lo importante es que tenemos su parte del antídoto."
    p "Esto tenemos que celebrarlo..."
    $ persistent.vb=True
    $ persistent.bolas += 1
    if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
        if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
            hide www
            jump enlace
        else:
            "Aún debo visitar el resto de ciudades de Europa."
            hide www
            jump map
    else:
        "Aún debo visitar el resto de ciudades de Europa."
        hide www
        jump map