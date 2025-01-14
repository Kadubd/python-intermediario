from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_painel_simples(texto, isArquivo):
    """Exibe um painel simples com o texto fornecido."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console.print(Panel(texto))

def exibir_painel_colorido(texto, isArquivo):
    """Exibe um painel colorido com o texto fornecido."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    console.print(Panel(texto, border_style="bold magenta"))
