from rich.console import Console
from rich.prompt import Prompt

# Create a Console object
console = Console()

# Use the Prompt.ask method to get user input
name = Prompt.ask("What's your name?", console=console)

# Print a greeting using the Console object
console.print(f'Hello, [bold green]{name}[/bold green]!')