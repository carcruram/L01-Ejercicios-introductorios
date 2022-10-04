def datos():
    aciertos = int(input('¿Cuál es el número de aciertos: '))
    errores = int(input('¿Cuál es el número de errores?: '))
    total_respuestas = int(input('¿Cuál es el número total de respuestas?: '))
    return (aciertos, errores, total_respuestas)

def calificaciones(aciertos, errores, total_respuestas):
    nota = aciertos*10/total_respuestas-(errores*10/(50-total_respuestas))
    nota = max(0, nota)
    return (nota)


def lee_datos():
    parc_1 = float(input('Nota del examen práctico 1: ')) 
    parc_2 = float(input('Nota del examen práctico 2: '))
    parciales = (parc_1, parc_2)
    proy_1 = float(input('Nota del proyecto 1: '))
    proy_2 = float(input('Nota del proyecto 2: '))
    proyectos = (proy_1, proy_2)
    cuest_1 = float(input('Nota del cuestionario 1: '))
    cuest_2 = float(input('Nota del cuestionario 2: '))
    cuest_3 = float(input('Nota del cuestionario 3: ')) 
    cuest_4 = float(input('Nota del cuestionario 4: '))
    cuest_5 = float(input('Nota del cuestionario 5: '))
    cuest_6 = float(input('Nota del cuestionario 6: ')) 
    cuestionarios = (cuest_1, cuest_2, cuest_3, cuest_4, cuest_5, cuest_6)
    return(parciales, proyectos, cuestionarios)


#parciales, proyectos, cuestionarios = lee_datos() #Esto hay que ponerlo en el fichero que tiene que coger los datos

def calcula_nota_cuatrimestre(parciales, proyectos, cuestionarios):
    if proyectos[0]<5:
        calcula_nota_cuatrimestre = 3.0
        return(calcula_nota_cuatrimestre)
    else:
        calcula_nota_cuatrimestre = 0.6*parciales[0]+0.1*proyectos[0]+0.1*sum(cuestionarios[:3])
        return(calcula_nota_cuatrimestre)

#print(calcula_nota_cuatrimestre(parciales, proyectos, cuestionarios)) #Esto también

def calcula_nota_cuatrimestre2(parciales, proyectos, cuestionarios):
    if proyectos[1]<5:
        calcula_nota_cuatrimestre2 = 3.0
        return(calcula_nota_cuatrimestre2)
    else:
        calcula_nota_cuatrimestre2 = 0.6*parciales[1]+0.1*proyectos[1]+0.1*sum(cuestionarios[3:])
        return(calcula_nota_cuatrimestre2)

#print(calcula_nota_cuatrimestre2(parciales, proyectos, cuestionarios))

def calcula_nota_evaluacion_continua(parciales, proyectos, cuestionarios):
    if proyectos[0]<5 or proyectos[1]<5:
        nota_evaluacion_continua = 4
    else:
        nota_1_cuatrimestre = 0.6*parciales[0]+0.1*proyectos[0]+0.1*sum(cuestionarios[:3])
        nota_2_cuatrimestre = 0.6*parciales[1]+0.1*proyectos[1]+0.1*sum(cuestionarios[3:])
        
        if nota_1_cuatrimestre<4 or nota_2_cuatrimestre<4:
            nota_evaluacion_continua = 4
        else:
            nota_evaluacion_continua = (nota_1_cuatrimestre+nota_2_cuatrimestre)/2
    return (nota_evaluacion_continua)

#print(calcula_nota_evaluacion_continua(parciales, proyectos, cuestionarios))