import click
import requests


class PublicationCLI:
    def __init__(self, url):
        self.url = url
        self.cache = None

    def _get_publications(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            click.echo(f"An error occurred: {e}")
            return None

    def _get_publication(self, id):
        try:
            response = requests.get(f"{self.url}/{id}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            click.echo(f"An error occurred: {e}")
            return None

    def _print_publication(self, publication):
        click.echo(f"Title: {publication['title']}")
        click.echo(f"URL: {publication['url']}")
        click.echo(f"Note: {publication['note']}")

    def show_ids(self):
        publications = self._get_publications()
        if publications is None:
            click.echo("Failed to retrieve publications.")
            return
        for i, publication in enumerate(publications):
            click.echo(f"id: {i}, title: {publication['title']}")

    def show_all(self):
        publications = self._get_publications()
        if publications is None:
            click.echo("Failed to retrieve publications.")
            return
        for publication in publications:
            self._print_publication(publication)
            click.echo()

    def show_single(self, id):
        if self.cache is None:
            self.cache = self._get_publications()
            if self.cache is None:
                click.echo("Failed to retrieve publications.")
                return
        if id >= len(self.cache):
            click.echo("Publication not found")
        elif id < 0:
            click.echo("Invalid publication ID.")
        else:
            publication = self.cache[id]
            self._print_publication(publication)
