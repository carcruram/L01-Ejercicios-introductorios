from calificaciones import*
aciertos, errores, total_respuestas = datos()
nota = calificaciones(aciertos, errores, total_respuestas)
print(f'La nota de Ada es: {nota:.2f}')


cuestionarios = datos(cuestionarios)
parciales = datoçs(parciales)
proyectos = datos(proyectos)


nota_ev_continua = nota()