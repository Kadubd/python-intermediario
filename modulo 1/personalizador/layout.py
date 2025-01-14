from rich.console import Console
from rich.table import Table

console = Console()

def exibir_tabela(texto, isArquivo):
    """
    Exibe o texto como uma tabela.
    """
    if isArquivo:
        with open(texto, "r") as file:
            texto = file.read()
    table = Table(title="Tabela de Texto")
    table.add_column("Linha", style="bold")
    for linha in texto.splitlines():
        table.add_row(linha)
    console.print(table)

def exibir_mensagem(texto, isArquivo):
    """
    Exibe o texto como uma mensagem estilizada.
    """
    if isArquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(f"[bold green]{texto}[/bold green]")
