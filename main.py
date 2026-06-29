import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer()
console = Console()

@app.callback()
def main():
    """📦 TeleVault"""

@app.command()
def version():
    """عرض إصدار البرنامج"""
    console.print(
        Panel.fit(
            "[bold cyan]TeleVault[/bold cyan]\nVersion: 0.1.0",
            title="Information",
        )
    )

if __name__ == "__main__":
    app()
