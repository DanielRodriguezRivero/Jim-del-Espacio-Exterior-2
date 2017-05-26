init: 
    $ persistent.vparis = False
    $ persistent.vparis2 = False
label paris:
    if persistent.finbolas==False:
        if persistent.vparis==False:
            $ persistent.vparis=True
            scene notre
            carmoine2 "Oh mirad, el Senna."
            carmoine2 "Qué romántico, cómo me gustaría montar en un bateaux bus."
            sandrine2 "A mí también me gustaria."
            anette2 "Y a mí."
            p "Bueno, vale, vosotras ganáis."
            hide notre 
            scene barco2
            punto "... qué pequeño el muuuundo es..."
            sandrine2 "¿Qué es ese ruido?"
            punto "...it´s a little small world..."
            p "Viene de allí, junto a la Torre Eiffel."
            hide barco2
            scene paris2
            anette2 "Uy, un enano."
            show jacques
            jacques "De enano nada, señorita. \"No tan alto como los demás.\""
            jacques "Mi nombre es Jacques."
            anette2 "¿Es verdad lo que se dice de los \"no tan altos\"?"
            jacques "Bueno, se dicen muchas cosas..."
            jacques "Si me disculpan, déjenme seguir cantando."
            carmoine2 "¿Acepta peticiones?"
            jacques "¿Es que acaso existe una canción mejor que It´s a small world?"
            jacques "Si la hay, no quiero saberlo."
            jacques "It´s a small world aaaafter all..."
            p "Será mejor que nos vayamos."
            hide jacques
            show carmoine
            carmoine "Esperad, miremos este panel de anuncios antes."
            carmoine "Puede que encontremos algo útil."
            "\"Busco la verguenza, la perdi hace dos noches con una chica y sus primas, creo que alguna de ellas busca su virginidad también.\""
            "\"Caballero blanco soltero, busca princesa morena con buenos atributos y cinturón de castidad con cerradura universal.\""
            carmoine "Nada de interés."
            anette "Lo dirás por ti, yo tengo la virginidad de unos cuantos, podría venderlas a buen precio."
            p "Será mejor continuar buscando por otro lado."
            hide carmoine
            if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide paris2
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide paris2
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide paris2
                jump map
        else:
            scene torre
            "Jacques sigue deleitando a los presentes con innumerables interpretaciones de la misma canción."
            "Sin embargo su animado espectáculo no consigue dar calidez a unas calles frías y egoistas, a las que solo dan vida las parejas que demuestran su amor bajo las farolas."
            hide torre
            jump map
    
    else:
        if persistent.vparis2==False:
            scene arco
            show cp
            p "Tú eres el Capitán América."
            cp "Oui, c´est moi."
            cp "Me odio a mí mismo, si pudiera me tiraría al Senna."
            cp "La gente me odia, piensan que soy el verdadero."
            cp "Yo les digo:"
            cp "Non, je suis Philippe."
            cp "Desayuno croissants con mantequilla."
            cp "Nunca salgo de casa sin una baguette bajo el brazo."
            cp "Corro el Tour de France y me gusta Truffaut."
            p "¿Y que hacen ellos?"
            cp "Me pegan más fuerte porque aquí todo el mundo lo odia a él también."
            cp "¿Podrías tirarme el escudo contra la cabeza?"
            cp "He intentado hacerlo a ver si así termino con mi sufrimiento, pero siempre termino cogiéndolo automáticamente."
            p "No hará falta, tengo una cosa mejor que te devolverá la forma anterior."
            show bolas at Position(ypos=370, xanchor=0.5, yanchor=1.0)
            cp "C´est superb. Así mato dos pajaros de un tiro. Siempre quise probarlo."
            cp "Ahora no tengo excusa. Mejor dicho, sí la tengo por si me preguntan."
            hide cp
            hide arco
            scene calleparis
            show anun
            anunciante "Hola, ¿le interesa una invitación para el Festival Erótico de París?"
            anunciante "Es nuestro primer año en esta ciudad y queremos invitar a lo más selecto de la sociedad local."
            anunciante "Por desgracia no quieren venir, así que estamos repartiendo entradas por aquí."
            p "Deme una."
            anunciante "Ten, un chubasquero de regalo."
            p "¿Para qué?"
            anunciante "Sí, la primera vez siempre sorprende..."
            anunciante "Nos encontramos en el Moulin Rouge."
            hide anun
            hide calleparis
            scene paris1
            p "En las películas sale más grande."
            hide paris1
            scene ficeb1
            p "Hay tantas chicas que no sé donde mirar."
            jim2 "Tú mira donde quieras pero asegurate de llevar el brazo siempre en alto."
            megafonia "En el stand de la izquierda, están a punto de comenzar el show lésbico más caliente de la feria:"
            megafonia "Teta Suvari y Maria unpajote"
            megafonia "Un fuerte aplauso, por favor."
            p "Mmmm, este sería un buen lugar para sacar las fotos."
            jim2 "Maria unpajote tiene pinta de dejarse hacer lo que sea."
            jim2 "Aunque creo que más que que le saquen, le va lo de que le metan."
            p "No seré yo el que se meta en esa turba ansiosa de tocar partes blandas. Ya encontraremos otras."
            hide ficeb1
            show ficeb
            show acpor1 at left
            show acpor2 at right
            acpor1 "Y entonces le dije: \"¿Todo eso me quieres meter?\"? ¿Te has pensado que soy un buzón de correos o qué?"
            acpor2 "Chica, es que no puedes dejar que un hombre te dé de comer, siempre cogen montones enormes de comida."
            acpor2 "Lo sé, pero en ese momento le estaba dando el pecho al pequeño Rocky."
            p "Ejem"
            acpor1 "Lo siento, el espectáculo terminó hace un rato."
            p "Oh no, no, no me interesa ver cómo hacen el amor."
            p "Bueno, en realidad sí, pero eso no es lo que me ha traido aquí."
            acpor2 "Te habrán traido tus piernas, supongo jajajaj."
            acpor1 "Discúlpala, es muy chistosa."
            p "Yo quería... Bueno... quería saber si podría hacerles unas fotos."
            acpor2 "Ni borracha, bueno, borracha puede."
            acpor1 "Te haría falta un milagro para que posáramos gratis para ti."
            acpor1 "Además, con qué quieres fotografiarnos, ¿con la retina?"
            acpor1 "Vete y no vuelvas por aquí, ¡¡¡SALIDO!!!"
            hide acpor1
            hide acpor2
            hide ficeb1 
            $ persistent.modelos=True
            $ persistent.vparis2=True
            jump map

        else:
            if persistent.milagro and persistent.camara and persistent.vodka:
                scene ficeb
                show acpor1 at left
                acpor1 "Mira, me has pillado en un buen día, haré las fotos"
                show acpor2 at right
                acpor2 "El vodka tan rico que me has traído no tiene nada que ver ¿eh?"
                acpor2 "Es solo que queremos demostrarte lo generosas que podemos ser las estrellas del porno."
                p "¿Qué tal una sesión privada?"
                acpor1 "Todavía nos podemos arrepentir."
                hide acpor1
                hide acpor2
                hide ficeb
                $ renpy.play("abierto.mp3")
                scene por1 at Pan((0, 0), (100, 0), 14.0) #movimiento horizontal
                $ renpy.pause(9.0)
                hide por1
                scene por2 at Pan((0, 0), (100, 0), 14.0)
                $ renpy.pause(9.0)
                hide por2
                scene por3 at Pan((0, 0), (0,300), 14.0)  #movimiento vertical
                $ renpy.pause(12.0)
                hide por3
                scene por4 at Pan((0, 0), (100, 0), 14.0)
                $ renpy.pause(8.0)
                hide por4
                scene por5 at Pan((0, 0), (0,300), 14.0)
                $ renpy.pause(8.0)
                hide por5
                scene por6 at Pan((0, 0), (0,300), 14.0)
                $ renpy.pause(8.0)
                hide por6
                scene por7 at Pan((0, 0), (0,300), 14.0)
                $ renpy.pause(8.0)
                hide por7
                scene por8 at Pan((0, 0), (0,300), 14.0)
                $ renpy.pause(8.0)
                hide por8
                $ renpy.sound.stop(0,2)
                scene ficeb
                p "Al final se enrollaron las chicas. Por desgracia, no entre ellas."
                scene pelea
                jim2 "Ahora solo tenemos que llevar esas fotos a nuestro contacto y nos dirá el paradero de Fetch."
                punto "No tan rápido."
                p "¿Quién ha dicho eso?"
                show burro2
                #show burro at Position(ypos=530, xanchor=0.5, yanchor=1.0)  # para la pelea
                burro "Yo: Edonka, el burro del Emule."
                p "¡Pero tú eres bueno!"
                p "Gracias a tí no tuve que pagar un duro por ver bodrios infumables, ni despilfarré mis ingresos en un pésimo disco."
                p "Hiciste más por mi economía que el Euro."
                burro "Son tiempos duros. Ahora impera la ley de la selva."
                burro "Nadie daba un duro por mí. Todo el mundo se aprovechaba de mis servicios y pocos eran los que me daban las gracias."
                p "Pero tiene su explicación, yo pensaba que eras solo un dibujo."
                burro "Eso me dicen todos."
                burro "En cualquier caso tomé una decisión y ahora trabajo para ellos."
                burro "Todo aquel que infringe los derechos de autor, se las ve conmigo más temprano que tarde."
                p "¡Eres un traidor!"
                burro "Simplemente son negocios. El pienso se ha puesto muy caro con eso de los biocombustibles. Y pagan bastante bien."
                p "¿Qué quieres de mí?"
                burro "Esas fotos. No puedo consentir que las publiques en Internet y que mis jefes pierdan un dinero que les corresponde."
                p "¡¡¡Si las fotos las hice yo, y las chicas me dieron su consentimiento!!!"
                if persistent.hombre==False:
                    burro "Mira hija, no me hagas las cosas más difíciles."
                    burro "¿Sabes a cuántas niñatas que no quisieron cumplir la ley me como para desayunar?"
                    burro "Estoy harto de sus patéticos lamentos."
                    burro "¡¡Mamá, el señor burro me ha roto los DVD´s de los Lunnis!!"
                    burro "Lo que no dicen a su mamá es que esos CD´s se los grabó su padre, el muy hijo de..."
                else:
                    burro "Mira hijo, no me hagas las cosas más difíciles."
                    burro "¿Sabes a cuántos niñatos que no quisieron cumplir la ley me como para desayunar?"
                    burro "Estoy harto de sus patéticos lamentos."
                    burro "¡¡Mamá, el señor burro me ha roto los DVD´s de los Lunnis!!"
                    burro "Lo que no le dicen a su mamá es que esos CD´s se los grabó su padre, el muy hijo de..."
                burro "Pero bueno, ya hemos hablado suficiente."
                burro "¿Me las vas a dar o no?"
                p "Antes prefiero la muerte, equino deficiente."
                burro "Tú lo has querido."
                burro "Nadie se mete con el burro del Emule y sale con vida."
                hide burro2
                $ renpy.play("kill2.mp3")
                burro "Prepárate a morder el polvo."
                $ renpy.pause(4.5)
                if persistent.hombre == False:
                    show burro at right with move
                    show prota2 at left
                else:
                    show burro at right with move
                    show prota at left
                    burro "¿Es necesario que te pongas en calzoncillos para pelear?"
                    p "¿Acaso tienes miedo?"
                    burro "Sí, de que se escape tu pajarito y me salte un ojo."
                    burro "Por suerte estoy a más de 5 centímetros de ti."
                menu:
                    "Intentas huir como un soldado francés":
                        "El campo es muy grande, intentas correr por donde viniste pero Edonka no te deja escapar"
                        "Con un acrobático salto, se coloca delante de ti y te muerde en la mano."
                        show btext1 at Position(xpos=138, ypos=58)  #encima del tio  x=626 y =58 encima del burro
                        $ renpy.pause(2.0)
                        hide btext1
                    "Le das un puñetazo":
                        "Los de PETA se te echan encima antes de que llegues a alcanzarlo."
                        "Te dan una paliza de muerte para enseñarte que no hay que hacer daño a los animales."
                        "Una vez que lo piensas friamente, te das cuenta de que la paliza fue un halago por su parte."
                        $ renpy.play("burro.wav")
                        show btext2 at Position(xpos=138, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext2
                menu:
                    "Te limitas a ignorarlo":
                        "Lo malo es que él no te ignora a ti y te da una coz."
                        "Algo cruje en tu interior: un par de nueces que llevabas en el bolsillo desde la última nochevieja."
                        show btext4 at Position(xpos=138, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext4
                    "Le colocas una bandera de los USA":
                        "Aparece un terrorista islámico para volarlo en pedazos."
                        terrorista "¡¡¡¡Muerte al infiel!!!!"
                        terrorista "Un momento, es un infiel demócrata."
                        terrorista "..."
                        terrorista "Qué dilema..."
                        p "Psss, se está meando en tu pierna."
                        $ renpy.play("explosion.mp3")
                        $ renpy.pause(1.0)
                        $ persistent.puntos +=1
                        show btext3 at Position(xpos=626, ypos=58) #sobre el burro
                        $ renpy.pause(2.0)
                        hide btext3
                menu:
                    "Le rocias de balas con una uzi":
                        "El burro tiene chaleco antibalas."
                        "Una rebota y te da en la pierna."
                        show btext5 at Position(xpos=138, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext5
                    "Tu eres cola yo pegamento":
                        p "Tu eres cola yo..."
                        "Antes de que termines la frase, el burro se lanza sobre ti y te da un cabezazo en la entrepierna que te deja sin aliento (y gracias)."
                        "Por suerte él se hace daño con la hebilla de tu cinturón."
                        show btext6 at Position(xpos=138, ypos=58)
                        show btext7 at Position(xpos=626, ypos=58) #sobre burror
                        $ renpy.pause(2.0)
                        hide btext7
                menu:
                    "Le lanzas un kame ha me ha":
                        $ renpy.play("kamehameha.wav")
                        p "Kame ha me ha"
                        scene bg black with Fade(.25, 0, .75, color="#fff")
                        hide bg black
                        $ renpy.pause(1.0)
                        scene pelea
                        "Por desgracia el burro lo esquiva con la transmisión instantánea."
                        show vegeta1 
                        vegeta "Me parecio sentir el aura de Kakarot."
                        p "No está aquí, lo siento, fui yo el que lanzó la Onda Vital."
                        vegeta "¿Tú? Ahora te enseñaré a no imitar a un saiyajin."
                        hide vegeta1 
                        show vegeta2
                        $ renpy.play ("finalflash.wav")
                        vegeta "Final flash"
                        $ renpy.pause(5.0)
                        scene bg black with Fade(.25, 0, .75, color="#fff")
                        hide vegeta2
                        $ renpy.pause(2.0)
                        scene pelea
                        show vegeta1
                        vegeta "Uh, guerrero de baja categoría."
                        hide vegeta1 with slideawayup
                        show btext8 at Position(xpos=138, ypos=58)
                        if persistent.hombre == False:
                            show burro at right
                            show prota2 at left
                        else:
                            show burro at right 
                            show prota at left
                        $ renpy.pause(2.0)
                        hide btext8
                    "Invocas a Tux el pinguino gigante":
                        "Aparece con cientos de frikis colgando de sus pies, declarándole su amor."
                        "Aparece un extraño robot con un cañón, dispara al burro y este aumenta de tamaño."
                        "Es la lucha más surrealista que has visto nunca."
                        "Cuando el burro acaba con Tux de un derechazo, su cuerpo inerme cae a plomo sobre la caterva de seguidores."
                        "Al día siguiente, las ofertas de empleo para los informáticos se disparan hasta cotas inalcanzables."
                        $ renpy.pause(2.0)
                        
                scene pelea
                if persistent.hombre == False:
                    show burro at right
                    show prota2 at left
                else:
                    show burro at right 
                    show prota at left
                menu:
                    "Invocas a Ted Dibiase":
                        hide burro
                        if persistent.hombre == False:
                            hide prota2
                        else:
                            hide prota
                        $ renpy.play("money.mp3")
                        $ renpy.pause(3.5)
                        show ted with vpunch
                        ted "Espero que sea importante."
                        ted "Estaba haciéndole el amor a 150.000$."
                        p "¿Y eso cómo se hace?"
                        ted "Contratando una puta de alto standing."
                        ted "¿A quién tengo que dar una paliza?"
                        ted "¿Jake Snake Roberts?"
                        ted "¿Macho Man?"
                        ted "Por favor, decidme que no es Virgil."
                        p "Lo tienes justo frente a ti."
                        ted "¿Qué? ¿Me has llamado para que le pegue a un burro?"
                        ted "¿Tienes idea de entre las piernas de quién estaba?"
                        $ renpy.play("punch.wav")
                        hide ted
                        $ persistent.puntos +=1
                        show btext9 at Position(xpos=138, ypos=58)
                        if persistent.hombre == False:
                            show burro at right
                            show prota2 at left
                        else:
                            show burro at right 
                            show prota at left
                        $ renpy.pause(2.0)
                        hide btext9
                    "Le tiras una oveja explosiva":
                        "Por desgracia eran amigas desde los tiempos en que vivían juntos en la granja y se vuelve contra ti."
                        show btext10 at Position(xpos=626, ypos=58)
                        "Mientras la oveja te apalea, Edonka invoca un hechizo de curación."
                        show btext12 at Position(xpos=626, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext12
                menu:
                    "Tiras un peso de 1 tonelada marca ACME sobre él":
                        scene pelea
                        show peso with slidedown
                        #peso cayendo hacia abajo, que se mueva hacia abajo
                        $ renpy.play("correcaminos.mp3")
                        scene pelea with vpunch
                        $ renpy.pause (2.0)
                        "El burro lo esquiva, pero el correcaminos es aplastado."
                        show coyote
                        coyote "Tantos años queriendo pillar a ese pajarraco..."
                        coyote "Y ahora viene un aficionado y me arrebata la gloria."
                        coyote "¡¡¡¿QUIÉN HA SIDO?!!!"
                        p "Ha sido el burro."
                        "El coyote apalea al burro con furia."
                        scene pelea with hpunch
                        $ renpy.play("punch.wav")
                        $ renpy.play("punch.wav")
                        scene pelea with vpunch
                        $ renpy.play("fight.wav")
                        $ renpy.pause(3.0)
                        show coyote
                        coyote "Eso te enseñará a no meterte en los intentos de asesinato ajenos."
                        p "Se lo agradezco."
                        hide coyote
                        if persistent.hombre==False:
                            show prota2 at left
                        else:
                            show prota at left
                        show burro at right
                        show btext11 at Position(xpos=626, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext11
                        hide burro
                    "Te rindes":
                        scene pelea
                        if persistent.hombre==False:
                            show prota2 at left
                        else:
                            show prota at left
                        show burro at right
                        p "Te he atacado con todo lo que tenía y no tienes un solo rasguño."
                        p "Me rindo, toma las fotos."
                        burro "Te lo advertí, muchacho. Deberías estar contento, has sobrevivido a un poder al que muchos temen."
                        burro "Venga, dame el carrete."
                        jv "No tan rápido, amigo equino."
                        burro "No, no puede ser."
                        burro "Te vi caer por el precipicio."
                        show jv at Position(ypos=550)
                        jv "Muchos mulos me han dado por muerto, pero siempre vuelvo..."
                        burro "No volveré a trabajar contigo."
                        burro "¡¡¡NO VOLVERÉ A TRABAJAR EN ESE INFIERNO!!!"
                        "Edonka corre frenético hacia un barranco, y salta sin pensárselo un segundo."
                        show btext11 at Position(xpos=626, ypos=58)
                        $ renpy.pause(2.0)
                        hide btext11
                        hide burro
                        jv "Pobre burro, hubiera sido un buen transportista de café."
                        hide jv
                        $ renpy.pause(2.0)
                scene pelea
                if persistent.hombre == False:
                    show prota2 at left
                else:
                    show prota at left
                show muerto at Position(xpos=579, ypos=436)  #imagen del burro muerto
                p "Descanse en paz, señor burro."
                p "Y ahora, rumbo a Alemania."
                if persistent.hombre == False:
                    hide prota2
                else:
                    hide prota 
                hide muerto 
                jump antartida
            else:
                scene ficeb
                show acpor1
                acpor1"Aún te falta mucho para que mueva los labios siquiera."
                p "Pero si ya los estás moviendo."
                acpor1 "No me refiero a esos labios."
                hide acpor1
                hide ficeb
                jump map
                
                
                
                

