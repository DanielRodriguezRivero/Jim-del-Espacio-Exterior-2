init: 
    
    $ persistent.vc = False
    $ persistent.vc2 = False       #variable visitado cairo
    
label cairo:
    if persistent.finbolas==False:
        if persistent.vc == False:
            scene marco
            show expression Text("El Cairo, capital de la que antaño fue la civilización más avanzada de la historia.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text with dissolve
            show expression Text("Hogar de la primera delegación extranjera del Ministerio de Andares Ridículos.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text with dissolve
            show expression Text("Aficionados a perder guerras...", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(3.5)
            hide text with dissolve
            scene egipt
            show egip
            if persistent.hombre==False:
                egip "¿Hola marinera infiel, te apetece pasar un buen rato con una reina egipcia?"
            else:
                egip "¿Hola marinero infiel, te apetece pasar un buen rato con una reina egipcia?"
            p "No, gracias"
            egip "Que un áspid se retuerza en tus entrañas hasta el final de tus días."
            anette "Yo probé eso una vez, pero no me gustó."
            anette "Al principio sí, se notaba el subidón, pero luego te acostumbras."
            sandrine2 "Hay cosas que no se deberían decir, Anette."
            hide egip
            $ renpy.pause(1.0)
            sandrine2 "Tenía una bonita nariz."
            p "Sí, pero parecía una momia."
            hide egipt
            scene palmera
            sandrine2 "¿Véis aquella palmera de allí?"
            sandrine2 "Hay alguien sentado bajo ella, ¿verdad?"
            p "Si, eso parece."
            anette2 "Voy a ver qué le pasa."
            show poeta
            poeta "Pero por favor, permitidme que me presente."
            poeta "Me llamo Spencer Fitzgerald y quiero ser un poeta."
            sandrine2 "Con lo que me gustan a mí."
            sandrine2 "Podrías recitarme algo."
            poeta "Oh bella silfide, mal momento escogéis para que os demuestre mi arte."
            poeta "He perdido la inspiración."
            poeta "Las musas me han abandonado como al marido que traiciona la fidelidad de su pareja."
            anette2 "A veces pasa."
            poeta "Pero es el peor momento para que mi mente se marchite en el desierto de la ignorancia."
            poeta "Pues no solo es el dolor de un escritor por ver como su espíritu creativo se diluye entre las brisas del atardecer..."
            anette2 "Seguro que hay una mujer por medio."
            anette2 "Siempre la hay."
            poeta "Sí, la más bella mujer que los incontables siglos de las pirámides hayan contemplado."
            poeta "Y mañana por la mañana, partirá a la lejana Australia, lejos de mis intenciones y de mis recursos."
            poeta "Necesito seducirla al precio que sea, mas no se me ocurre nada."
            anette2 "Tal vez pudiera ayudarte."
            carmoine2 "Ayudémosle, el amor debe triunfar siempre."
            poeta "¿Acaso seríais mi Cyrano, y ayudaríais a mi lengua a dar forma a los sentimientos que mi corazón alberga?"
            p "Claro que sí."
            poeta "Oh, gracias, gracias."
            if persistent.hombre==False:
                poeta "Que Apolo bendiga la varita de tu novio por los años venideros."
            else:
                poeta "Que Apolo bendiga tu varita por los años venideros."
            poeta "¿Por dónde empezamos?"
            p "Tranquilo, tengo un plan."
            hide palmera
            scene marco
            show expression Text("Anochece en la capital cairota.", xpos=0.5,ypos=0.5,xanchor="center", yanchor="center", drop_shadow=(2, 2)) as text with dissolve
            $ renpy.pause(2.0)
            hide text with dissolve
            $ renpy.pause(0.25)
            scene bg black
            rachid "¡¡Dame la cartera o te envío al infierno con 30 suegras virgenes!!"
            atracado "Solo llevo encima dos cabras."
            rachid "Con eso bastará."
            scene balcon
            show poeta at left 
            poeta "¡¡Lady Regina!!"
            show amada at right
            amada "¿Eres tú, François?"
            poeta "No"
            amada "¿Arturo?"
            poeta "... No"
            amada "¿Pierce?"
            poeta "Pues no."
            amada "¿%(name)s?"
            poeta "Por supuesto que no"
            poeta "Soy Spencer, el poeta inglés que anhela vuestro corazón y por lo visto el único de la colonia extranjera del Cairo que no ha sentido el calor de vuestras sábanas en su desnudo cuerpo."
            amada "Oh, no penséis mal de mí."
            amada "Solo me acuesto con ellos, pero mi corazón lo reservo al hombre que consiga derribar las marmoreas puertas que conducen a su interior."
            poeta "He aquí pues mi ariete."
            amada "Me gustaría verlo."
            scene balcon
            p "Bien, ahora tenemos que ayudarle a elegir los mejores versos."
            carmoine "De acuerdo."
            show poeta at left
            show amada at right
            poeta "Eres tú, amada mía..."
            menu:
                "más dulce que la ambrosía.":
                    poeta "Más dulce que la ambrosía."
                "melodiosa cuan sinfonía.":
                    poeta "melodiosa cuan sinfonía."
            menu:
                "Amarte me gustaría":
                    poeta "Amarte me gustaría"
                "Por ti la luna saltaría":
                    poeta "Por ti la luna saltaría"
            menu:
                "hasta el final de los días.":
                    poeta "hasta el final de los días."
                "hasta que despuntara el día.":
                    poeta "hasta que despuntara el día."
            menu:
                "Dejadme subir al balcón y ":
                    poeta "Dejadme subir al balcón y "
                "Cojamos mi camión y ":
                    poeta "Cojamos mi camión y "
            menu:
                "a la luz de la luna, hagamos el amor.":
                    poeta "a la luz de la luna, hagamos el amor."
                "déjame declararte mi amor.":
                    poeta "déjame declararte mi amor."
            amada "Aunque sea un simple bosquejo, me agrada vuestro cortejo."
            amada "Subid apuesto poeta, id bajándoos la bragueta."
            hide amada
            show poeta at center with move
            poeta "Miles de gracias, por todo, tened esta entrada como agradecimiento."
            show entrada at Position(ypos=400, yanchor=1.0)
            poeta "Es para la recepción que concederá la Reina de Inglaterra en su palacio."
            sandrine "¿Donde está el sello real?"
            poeta "Por el otro lado."
            poeta "Adios amigos, el placer me espera."
            hide entrada
            hide poeta
            sandrine2 "Lo conseguimos, el amor ha triunfado."
            p "Me encanta que los planes salgan bien."
            anette2 "No creo que Tigara y sus secuaces hayan pasado por aquí. Será mejor buscar en otro sitio."
            $ persistent.entrada= True
            $ persistent.vc = True
            if persistent.bolas == 3:   
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                        hide balcon
                        jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide balcon
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide balcon
                jump map
            

        else:
            scene palmera
            show poeta
            poeta2 "Los largos sollozos de los violines de otoño"
            extend "hieren mi corazón con monótona languidez."
            carmoine2 "¿Nos acercamos a ver qué tal le fue con su amada?"
            p "Déjalo, seguro que bien."
            hide poeta
            hide palmera
            scene desierto
            "Las misteriosas arenas del desierto guardan muchos más secretos en sus entrañas a la espera del aventurero adecuado para mostrarse."
            hide desierto
            jump map
            
    else:  #saga bolas fin
        if persistent.vc2 == False:
            if persistent.muro == False:
                scene tabac
                jim "¿Sabías que El Cairo es el primero productor de tabaco de África?"
                p "Precisamente ese dato no lo había leído."
                hide tabac
                $ persistent.vc2=True
                jump map
            else:
                if persistent.modelos==True:
                    scene tabacalera
                    p "Que suerte, un estanco en el centro del Cairo, y además en español."
                    p "Podría aprovechar y comprarle el tabaco a Dios."
                    show tendero
                    tendero "Buenos días, ¿qué quiere?"
                    p "Tabaco, por favor."
                    tendero "Aquí tiene."
                    p "Oiga, esto es un petardo."
                    tendero "Oh, perdón, perdón"
                    tendero "Tome."
                    p "Me ha vuelto a dar un porro."
                    tendero "Disculpe, lo malentendí."
                    p "Mi tabaco, por favor."
                    tendero "Aquí tiene, pero tenga en cuenta que el tabaco mata."
                    p "No creo que al que se lo llevó le importe eso."
                    hide tendero
                    hide tabacalera
                    $ persistent.tabaco= True
                    $ persistent.vc2=True
                    jump map
                else:
                    scene piramides
                    p "No podría mirar a la cara a mi madre si le dijera que he ido a Egipto y no he visitado las pirámides."
                    hide piramides
                    jump map
        else:
            scene tabacalera
            p "Es curioso cómo han diversificado su negocio las empresas españolas."
            jim2 "Curioso a la par que interesante."
            if persistent.tabaco == False:  # si es verdad, solo sale lo de arriba
                p "Entremos a comprar tabaco."
                jim2 "¿Por qué?"
                p "¿Acaso hace falta un motivo para disfrutar de un buen cohiba? ¿O de un aromático cigarrillo rubio?"
                $ persistent.tabaco = True
                show tendero
                tendero "Buenos días, ¿qué quiere?"
                p "Tabaco, por favor."
                tendero "Aquí tiene."
                p "Oiga, esto es un petardo."
                tendero "Oh, perdón, perdón."
                tendero "Tome."
                p "Me ha vuelto a dar un porro."
                tendero "Disculpe, lo malentendí."
                p "Mi tabaco, por favor."
                tendero "Aquí tiene, pero tenga en cuenta que el tabaco mata."
                p "No creo que al que se lo llevó le importe eso."
                hide tendero
                hide tabacalera
                jump map
            hide tabacalera
            jump map
