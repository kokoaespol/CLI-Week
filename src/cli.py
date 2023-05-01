import os
import click
import requests
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

TEXTCORTEX_API_KEY = os.getenv('TEXTCORTEX_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

CODES = 'https://api.textcortex.com/v1/codes'


@click.group()
def cli():
    pass


languages = {
    "py": 'python',
    "java": 'java',
    "js": 'javascript',
    "go": 'go',
    "php": 'php'
}


@click.command()
@click.option('-l', '--language', default=languages['py'], help='The language you want to use', required=False)
@click.argument('text', type=click.STRING, required=True)
def code(language, text):
    """Chatgpt will transform your nl prompt into code"""
    payload = {
        "max_tokens": 256,
        "mode": languages[language],
        "model": "icortex-1",
        "n": 1,
        "temperature": 0,
        "text": text
    }
    headers = {
        "Authorization": f"Bearer {TEXTCORTEX_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(CODES, json=payload, headers=headers)
    data = response.json()

    text = data['data']['outputs'][0]['text']

    click.echo(text)

@click.command()
@click.option('-l', '--language', default='en', help='The language you want to use', required=False)
@click.option('-c', '--country', default='ec', help='The country you want to use', required=False)
@click.argument('query', type=click.STRING, required=True)
def search(language, country, query):
    """Search in the internet for info, and get a summerized answer"""
    params = {
        "q": query,
        "hl": language,
        "gl": country,
        "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    snippet = results['organic_results'][0]['snippet']
    click.echo(snippet)


@click.command()
@click.option('-p', '--path', required=True, help='The path to the file you want to open')
@click.option('-l', '--lines', required=True, help='The lines where the problem is, format start:end')
@click.argument('statement', type=click.STRING, required=True)
@click.pass_context
def solve(ctx, path, lines, statement):
    """Open a file, address a problem, and get a solution"""
    with open(path, 'r') as f:
        start = int(lines[:lines.index(':')])
        end = int(lines[lines.index(':')+1:])
        text = f.read().splitlines()[start-1: end]
        text = '\n'.join(text)
    
    file_extension = path.split('.')[-1]
    ctx.invoke(code, language=file_extension, text=f"Problem: {statement}\nCode: {text}")

cli.add_command(code)
cli.add_command(search)
cli.add_command(solve)

if __name__ == "__main__":
    cli()
