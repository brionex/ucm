from auto.cli import cli


def main():
    """
    Función principal, ejecuta las acciones del CLI de desarrollo.
    """
    try:
        cli()
    except Exception as e:
        print(f"Error al ejecutar el CLI: {e}")


if __name__ == "__main__":
    main()
