
import math
class Proceso:
    def __init__(self):
        self.nombre = ""
        self.llegada = 0
        self.cpu = 0
        self.instante = 0
        self.t_fin = 0
        self.t_e = 0
        self.t_r = 0
        self.penalizacion = 0.0

# Función de comparación para sorted
def comparar_procesos(proceso):
    return (proceso.llegada, proceso.nombre)

def main():
    print("+------------------------------------------------------+")
    print("|     Programa de Planificación de Procesos (PEPS)      |")
    print("+------------------------------------------------------+")

    num_procesos = int(input("Ingrese el número de procesos: "))

    procesos = []

    # Ingresar información de los procesos
    for i in range(num_procesos):
        proceso = Proceso()
        proceso.nombre = chr(ord('A') + i)
        proceso.llegada = int(input(f"Ingrese la hora de llegada del proceso {proceso.nombre}: "))
        proceso.cpu = int(input(f"Ingrese la duración del proceso {proceso.nombre}: "))
        procesos.append(proceso)

    # Ordenar procesos usando sorted con la función de comparación personalizada
    procesos.sort(key=comparar_procesos)

    # Calcular los valores de la tabla y la penalización
    tiempo_actual = 0
    penalizacion_total = 0.0

    # Crear una lista de cadenas de caracteres para almacenar las filas de valores
    filas_por_nombre = []

    for proceso in procesos:
        proceso.instante = tiempo_actual
        proceso.t_fin = proceso.instante + proceso.cpu
        proceso.t_e = proceso.instante - proceso.llegada
        proceso.t_r = proceso.t_e + proceso.cpu

        # Evitar división por 0
        if proceso.t_e == 0:
            proceso.penalizacion = 0
        else:
            proceso.penalizacion = proceso.t_r / proceso.t_e

        # Reemplazar "INF" con 0
        if math.isnan(proceso.penalizacion):
            proceso.penalizacion = 0

        penalizacion_total += proceso.penalizacion
        tiempo_actual = proceso.t_fin

        # Crear la fila de valores para este proceso
        fila = f"|    {proceso.nombre}    |    {proceso.llegada:2d}   |  {proceso.cpu:2d} |    {proceso.instante:2d}    |  {proceso.t_fin:3d}  |  {proceso.t_e:2d}  |  {proceso.t_r:3d}  |     {proceso.penalizacion:.8f}   |"
        filas_por_nombre.append(fila)

    # Ordenar las filas de valores por nombre
    filas_por_nombre.sort()

    print("+---------+---------+-----+----------+-------+------+-------+--------------+")
    print("| proceso | llegada | cpu | instante | t.fin | t.e  |  t.r  | penalizacion |")
    print("+---------+---------+-----+----------+-------+------+-------+--------------+")

    # Imprimir las filas de valores en orden alfabético
    for fila in filas_por_nombre:
        print(fila)

    print("+---------+---------+-----+----------+-------+------+-------+--------------+")

    # Calcular y mostrar el promedio de penalización
    promedio_penalizacion = penalizacion_total / num_procesos

    # Reemplazar "INF" en el promedio con 0
    if math.isnan(promedio_penalizacion):
        promedio_penalizacion = 0

    print(f"Promedio de penalización: {promedio_penalizacion:.8f}")

if __name__ == "__main__":
    main()
