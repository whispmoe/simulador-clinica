# Aqui importamos las librerias.
import random

from rich import print
from rich.text import Text
from rich.panel import Panel

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator

PACIENTES_ESPERA = []
PACIENTES_ATENDIDOS = []

NOMBRE_CLINICA = "Clínica Pavas"
tiempo = 0.0


def registrar_paciente():
    # Le pedimos al usuario que ingrese su nombre.
    # El nombre que el usuario ponga quedaria guardado en la variable nombre.
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

    # Con el append agregamos una variable a la lista.
    PACIENTES_ESPERA.append(paciente)


def atender_siguiente_paciente():
    global tiempo

    if not PACIENTES_ESPERA:
        print("[bold red]No hay pacientes en espera[/bold red]")
        return

    tiempo = round(random.uniform(0.5, 2.0), 2)
    for i, paciente in enumerate(PACIENTES_ESPERA):
        if paciente.get('prioridad') == 'u':
            nombre = paciente.get('nombre')
            PACIENTES_ATENDIDOS.append(nombre)
            print(f"[bold]Atendiendo a [cyan]{nombre}[/cyan][/bold]")

            # Eliminar el paciente de la lista
            PACIENTES_ESPERA.pop(i)
            return

    for i, paciente in enumerate(PACIENTES_ESPERA):
        if paciente.get('prioridad') == 'n':
            nombre = paciente.get('nombre')
            PACIENTES_ATENDIDOS.append(nombre)
            print(f"[bold]Atendiendo a [cyan]{nombre}[/cyan][/bold]")

            # Eliminar el paciente de la lista
            PACIENTES_ESPERA.pop(i)
            return


def ver_estado_cola():
    if not PACIENTES_ESPERA:
        print("[bold red]No hay personas en cola[/bold red]")

    for i, paciente in enumerate(PACIENTES_ESPERA, start=1):
        print(
            f"{i}. [bold cyan]{paciente.get('nombre')}[/bold cyan] "
            f"[dim](Prioridad: {'Urgente' if paciente.get('prioridad') == 'u' else 'Normal'})[/dim]"
        )


def ver_pacientes_atendidos():
    if not PACIENTES_ATENDIDOS:
        print("[bold red]No hay pacientes atendidos por el momento[/bold red]")
    else:
        for i, nombre in enumerate(PACIENTES_ATENDIDOS, start=1):
            print(f"{i}. [bold green]{nombre}[/bold green]")


def calcular_tiempo_promedio():
    if not PACIENTES_ATENDIDOS:
        print(
            "[bold red]No hay pacientes atendidos para calcular el tiempo promedio[/bold red]")
        return

    tiempo_str = f"{int(tiempo)}" if tiempo.is_integer() else f"{tiempo}"

    print(
        f"El tiempo promedio de atención es de [bold]{tiempo_str} horas[/bold]")


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
