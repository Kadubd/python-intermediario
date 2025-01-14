from rich.progress import Progress

def barra_progresso_simples(texto, isArquivo):
    """Exibe uma barra de progresso enquanto mostra o texto."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    with Progress() as progress:
        task = progress.add_task(texto, total=100)
        for _ in range(100):
            progress.update(task, advance=1)

def barra_progresso_personalizada(texto, isArquivo):
    """Exibe uma barra de progresso personalizada."""
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    with Progress(transient=True) as progress:
        task = progress.add_task(f"[green]{texto}", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
