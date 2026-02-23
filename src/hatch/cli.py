import typer
from pathlib import Path
from .templates import *

app = typer.Typer()

class Hatch:
    
    @staticmethod
    @app.command()
    def script(
        name: str = typer.Argument(..., help="Script name"), 
        directory: bool = typer.Option(
            None, 
            "--directory",
            "-d",            
            help="Directory to create script in"
        ),
        comments: bool = typer.Option(
            False, 
            "--comments",
            "-c",            
            help="Include template comments"
        )
    ):
        """
        Create a new Hatch script file.
        """
    
        name = name[0].upper() + name[1:]
        file_name = f"{name}.hsl"
        
        if comments:
            content = SCRIPT_TEMPLATE_COMMENTS.format(classname=name)
        else:
            content = SCRIPT_TEMPLATE.format(classname=name)
            
        if directory:
            path = Path(directory)
            path.mkdir(parents=True, exist_ok=True)
            file_path = path / file_name
        else:
            file_path = Path(file_name)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        typer.echo(f"Created script '{file_path}' successfully.")
    
    @staticmethod
    @app.command()
    def project(
        game_title: str = typer.Option("Hatch Project", "--game-title", "-g", help="Game title"),
        developer: str = typer.Option("Developer", "--developer", "-d", help="Game title")
    ):
        """
        Create a new Hatch project.
        """
        
        root = Path(game_title)
        
        if root.exists():
            typer.echo(f"Directory '{game_title}' already exists.")
            raise typer.Exit(code=1)
            
        root.mkdir()
        
        resources = root / "Resources"
        subfolders = [
            "Scenes",
            "Sprites",
            "Music",
            "Images",
            "SoundFX",
            "Game",
            "Shaders",
            "Palettes",
            "Models",
            "Fonts",
        ]
        
        for folder in subfolders:
            (resources / folder).mkdir(parents=True)
            
        config_content = GAME_CONFIG_TEMPLATE.format(
            game_title=game_title,
            short_title=game_title.replace(" ", ""),
            developer=developer
        )
        
        (resources / "GameConfig.xml").write_text(config_content, "utf-8")
        
        scripts = root / "Scripts"
        scripts.mkdir()
        
        (scripts / "Static.hsl").write_text(STATIC_TEMPLATE, "utf-8")
        
        typer.echo(f"Created Hatch project '{game_title}' successfully.")