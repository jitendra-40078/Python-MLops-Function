import wikipedia
import click

@click.command()
@click.option("--name", prompt = "wikipedia page to scrape", help = "web page we want to scrape")

def scrape(name, length = 1):
    result = wikipedia.summary("Microsoft", sentences = length)
    click.echo(click.style(f'{result}:',bg = 'white', fg = 'blue'))

if __name__ == '__main__':
    scrape()

