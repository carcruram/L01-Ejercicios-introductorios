from calificaciones import*


def test_calcula_calificaciones():
    aciertos, errores, total_respuestas = datos()
    nota = calificaciones(aciertos, errores, total_respuestas)
    print(f'La nota de Ada es: {nota:.2f}')

def test_calcula_nota_cuatrimestre(parciales, proyectos, cuestionarios):
    nota_final = calcula_nota_cuatrimestre(parciales, proyectos, cuestionarios)
    print(f'La nota del cuatrimestre es: {nota_final:2f}')

def test_calcula_nota_cuatrimestre2(parciales, proyectos, cuestionarios):
    nota_final = calcula_nota_cuatrimestre2(parciales, proyectos, cuestionarios)
    print(f'La nota del cuatrimestre 2 es: {nota_final:2f}')

def test_calcula_nota_evaluacion_continua(parciales, proyectos, cuestionarios):
    nota_final = calcula_nota_evaluacion_continua(parciales, proyectos, cuestionarios)
    print(f'La nota de la evaluación continua es: {nota_final:2f}')

if __name__ == '__main__':
    test_calcula_calificaciones()
    parciales, proyectos, cuestionarios = lee_datos()
    test_calcula_nota_cuatrimestre(parciales, proyectos, cuestionarios)
    test_calcula_nota_cuatrimestre2(parciales, proyectos, cuestionarios)
    test_calcula_nota_evaluacion_continua(parciales, proyectos, cuestionarios)