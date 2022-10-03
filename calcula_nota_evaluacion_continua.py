from calcula_nota_cuatrimestre import cuatrimestre1
def datos():
    parc_1 = float(input('Nota del examen práctico 1: '))
    parc_2 = float(input('Nota exámen práctica 2: '))
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
    cuestionarios2 = (cuest_1, cuest_2, cuest_3, cuest_4, cuest_5, cuest_6)
    return(parciales, proyectos, cuestionarios2)

parciales, proyectos, cuestionarios2 = datos()

def cuatrimestre2(parciales, proyectos, cuestionarios2):
    if proyectos[1]<5:
        cuatrimestre2 = 3
        print('La nota del cuatrimestre 2 es', end=': ')
        return(cuatrimestre2)
    else:
        print('La nota del cuatrimestre 2 es', end=': ')
        cuatrimestre2 = 0.1*sum(cuestionarios2)+0.6*parciales[1]+0.1*proyectos[1]
        return(cuatrimestre2)

print(cuatrimestre2(parciales, proyectos, cuestionarios2))

nota_primer_cuatrimestre = cuatrimestre1(parciales[0],proyectos[0], cuestionarios2[:3])
nota_segundo_cuatrimestre = cuatrimestre2(parciales[1], proyectos[1], cuestionarios2[3:])

def nota():
    if nota_primer_cuatrimestre<4 or nota_segundo_cuatrimestre<4:
        nota = 4
        print('La nota de la evaluación continua es', end=': ')
        return(nota)
    else:
        nota = (nota_primer_cuatrimestre + nota_segundo_cuatrimestre)/2
        print('La nota de la evaluación continua es', end=': ')
        return(nota)

print(nota())