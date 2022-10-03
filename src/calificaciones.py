def datos():
    aciertos = int(input('¿Cuál es el número de aciertos: '))
    errores = int(input('¿Cuál es el número de errores?: '))
    total_respuestas = int(input('¿Cuál es el número total de respuestas?: '))
    return (aciertos, errores, total_respuestas)

def calificaciones(aciertos, errores, total_respuestas):
    nota = aciertos*10/total_respuestas-(errores*10/(50-total_respuestas))
    nota = max(0, nota)
    return (nota)