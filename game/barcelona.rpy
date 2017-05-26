init:
    $ persistent.visitadobarcelona = False                 #cada ciudad debe de tener su variable de visitado
    $ persistent.visitadobarcelona2 = False 
    
label barcelona:
    if persistent.finbolas == False:
        if persistent.visitadobarcelona == False:  #continuación
            scene barna5
            "Este espacio estaba dedicado a los independentistas que venden banderas en Las Ramblas, pero se cogieron el puente de la Constitución y nadie los ha vuelto a ver."
            hide barna5
            scene barna3
            show carmoine
            carmoine "Entremos a preguntar a esa cafetería, los camareros siempre suelen estar al tanto de quién entra y quién sale,"
            extend "Y una chica como Tigara no pasa desapercibida."
            hide carmoine
            hide barna3
            scene cafeteria
            show jackie
            jackie "Bienvenido al Café de los 90, donde cada día se arruina una punto com."
            jackie "Les recomiendo uno de nuestros cafés Clinton."
            jackie "El Bill Clinton, con extra de crema,"
            extend "O el Hillary Clinton, solo con pimienta."
            sandrine2 "¿Quién se supone que eres tú?"
            jackie "Jackie Chan"
            sandrine2 "¿En los 90?"
            jackie "Jackie Chan es un personaje atemporal gracias al bótox, aunque sus mejores películas datan de los 90, sí."
            jackie "Yo preferia el disfraz de Kurt Cobain, pero la gente me confundía con el de Perdidos, y no era buen negocio."
            jackie "¿Qué vais a tomar?"
            carmoine2 "En realidad nada, solo queríamos saber si has visto a una chica con los brazos en alto."
            jackie "No sé nada."
            jackie "Largo de aquí, no nos gustan los gorrones."
            hide jackie
            hide cafeteria
            scene barna3
            sandrine2 "Conocemos muy bien estas calles, no creo que anden por aquí."
            $ persistent.visitadobarcelona=True
            if persistent.bolas == 3:   # si se tienen todas las bolas, se saltadonde se cuenta como da con el pinguino, adios de las angeles
                if persistent.vsm and persistent.vparis and persistent.vm and persistent.vberlin and persistent.visitadobarcelona and persistent.vi:
                    hide barna3
                    jump enlace
                else:
                    "Aún debo visitar el resto de ciudades de Europa."
                    hide barna3
                    jump map
            else:
                "Aún debo visitar el resto de ciudades de Europa."
                hide barna3
                jump map
            
            jump map
        else:
            scene barna2
            "Aquí no hay nada, mejor que vayas a otra parte."
            hide barna2
            jump map

        
    else:  #saga bolas terminada
        if persistent.visitadobarcelona2==False:
            scene barna3
            show abril
            p "¿Sabe que es uno de mis iconos sexuales de juventud?"
            abril "¿Un dibujo?"
            abril "¿Qué eres, uno de esos frikis de viruete.com?"
            abril "¿Y además pretendes meterme esas bolas?"
            abril "¿Pero qué te has creido, degenerado?"
            abril "Corre antes de que te parta el bastón del maestro Astilla en la cabeza."
            hide abril
            hide barna3
            scene barna
            p "Esta zona de la ciudad la veo demasiado oriental."
            jim2 "Debe de ser el barrio chino."
            show kirai 
            kirai "¡Konichi wa!"
            kirai "Mira tío, una uva que adivina tu cumpleaños y te canta el cumpleaños feliz."
            kirai "No te pierdas una pequeña tienda escondida en lo más profundo del barrio Akiba en la ciudad de Honshu, prefectura de Hokkaido."
            p "¿Y que venden?"
            kirai "Ni puta idea, pero tienes que ir, tío. Es total. Además tengo aqui el plano, hecho con migas de dorayaki."
            kirai "¡¡Sayonara!!"
            hide kirai
            jim2 "¿Qué fue eso?"
            p "Ni idea, no he entendido una palabra."
            hide barna
            $ persistent.visitadobarcelona2=True
            jump map
        else:
            scene barna4
            "Barcelona, la ciudad que a todo el mundo acoge."
            "Motor económico y cultural del pais."
            "Una gota de modernidad en un mar de atraso."
            "Visita Barcelona"
            "Spot patrocinado por la Generalitat de Catalunya."
            "Recaudamos tu dinero para financiar a las empresas de peaje."
            hide barna4
            jump map
