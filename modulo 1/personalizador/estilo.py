from rich.console import Console
from rich.text import Text

console = Console()

def exibir_texto_estilizado(texto, isArquivo):
    """Exibe texto estilizado."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    styled_text = Text(texto, style="bold green")
    console.print(styled_text)

def exibir_texto_destacado(texto, isArquivo):
    """Exibe texto destacado."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    highlighted_text = Text(texto, style="bold red on yellow")
    console.print(highlighted_text)
