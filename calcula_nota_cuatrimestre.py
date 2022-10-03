def datos():
    parc_1 = float(input('Nota del examen práctico 1: ')) 
    proy_1 = float(input('Nota del proyecto 1: '))
    cuest_1 = float(input('Nota del cuestionario 1: '))
    cuest_2 = float(input('Nota del cuestionario 2: '))
    cuest_3 = float(input('Nota del cuestionario 3: ')) 
    cuestionarios = (cuest_1, cuest_2, cuest_3)
    return(parc_1, proy_1, cuestionarios)

proy_1, parc_1, cuestionarios = datos() #Esto hay que ponerlo en el fichero que tiene que coger los datos

def cuatrimestre1(parc_1, proy_1, cuestionarios):
    if proy_1<5:
        cuatrimestre1 = 3.0
        print('La nota del cuatrimestre 1 es', end=': ')
        return(cuatrimestre1)
    else:
        cuatrimestre1 = 0.1*sum(cuestionarios)+0.6*parc_1+0.1*proy_1
        print('La nota del cuatrimestre 1 es', end=': ')
        return(cuatrimestre1)
print(cuatrimestre1(parc_1, proy_1, cuestionarios)) #Esto también