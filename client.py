import click
import requests
from publication_cli import PublicationCLI


@click.command()
@click.option("--url",
              default="http://127.0.0.1:5000/publications",
              help="URL of the publications API")
def cli(url):
    publication_cli = PublicationCLI(url)

    while True:
        click.echo("0 - Exit the program")
        click.echo("1 - Show all available publications id and title")
        click.echo("2 - Print all publications")
        click.echo("3 - Print a single publication")

        try:
            status = int(click.prompt("Please enter your selection"))
        except ValueError:
            click.echo("Invalid input")
            continue

        if status == 0:
            break
        elif status == 1:
            publication_cli.show_ids()
        elif status == 2:
            publication_cli.show_all()
        elif status == 3:
            try:
                id = int(click.prompt("Please enter publication's id"))
            except ValueError:
                click.echo("Invalid input")
                continue
            publication_cli.show_single(id)
        else:
            click.echo("Invalid selection")


if __name__ == "__main__":
    cli()
