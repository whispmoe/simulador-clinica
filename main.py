from rich import print
from rich.text import Text
from rich.panel import Panel

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator

PACIENTES_ESPERA = []
PACIENTES_ATENDIDOS = []

NOMBRE_CLINICA = "Clínica Pavas"


def registrar_paciente():
    nombre = inquirer.text(
        message="Nombre del paciente:",
        validate=EmptyInputValidator(message="El nombre no puede estar vacío"),
    ).execute()

    prioridad = inquirer.select(
        message="Prioridad del paciente:",
        choices=[
            Choice("n", "Normal"),
            Choice("u", "Urgente"),
        ],
    ).execute()

    paciente = {
        "nombre": nombre,
        "prioridad": prioridad
    }
    globals()["paciente"] = paciente
    PACIENTES_ESPERA.append(paciente)


def atender_siguiente_paciente():
    if not PACIENTES_ESPERA:
        print("No hay pacientes en espera")
        return
    for p in enumerate(PACIENTES_ESPERA):
        p = paciente.get('prioridad') == 'u'
    nombre = paciente.get('nombre')
    print(f"Atendiendo a {nombre}")
    PACIENTES_ATENDIDOS.append(nombre)
    for i, pacientes in enumerate(PACIENTES_ESPERA):
        if PACIENTES_ESPERA.get("nombre") == nombre:
            del PACIENTES_ESPERA[i]
            break
    """ for i, e in enumerate(PACIENTES_ESPERA):
        if paciente.get("nombre") == nombre:
            paciente.remove(i) """
    pass


def ver_estado_cola():
    if not PACIENTES_ESPERA:
        print("No hay personas en cola")
    print (PACIENTES_ESPERA)
    pass


def ver_pacientes_atendidos():
    if not PACIENTES_ATENDIDOS:
        print("No hay pacientes atendidos por el momento")
    else:
        print(PACIENTES_ATENDIDOS)
    pass


def calcular_tiempo_promedio():
    # Implementación pendiente
    pass


def main():
    print(
        Panel.fit(
            f"[bold]{NOMBRE_CLINICA}[/bold] ~ [cyan]Gestión de Pacientes[/cyan]",
        )
    )

    while True:
        seleccion = inquirer.select(
            message="Elija una opción:",
            choices=[
                Choice("registrar", "Registrar paciente"),
                Choice("atender", "Atender siguiente paciente"),
                Choice("ver_cola", "Ver estado de la cola"),
                Choice("ver_pacientes", "Ver pacientes atendidos"),
                Choice("tiempo_promedio", "Calcular tiempo promedio de atención"),
                Choice(None, "Salir"),
            ],
            default="registrar",
        ).execute()

        if seleccion == "registrar":
            registrar_paciente()
        elif seleccion == "atender":
            atender_siguiente_paciente()
        elif seleccion == "ver_cola":
            ver_estado_cola()
        elif seleccion == "ver_pacientes":
            ver_pacientes_atendidos()
        elif seleccion == "tiempo_promedio":
            calcular_tiempo_promedio()

        elif seleccion is None:
            print(f"[bold green]Saliendo del programa, hasta pronto![/bold green]")
            print()
            break

        else:
            print(f"[bold red]Selección no valida[/bold red]")

        print()


if __name__ == "__main__":
    main()
