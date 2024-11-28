import os
from pyfiglet import Figlet

from shared.abstract_classes.Generator import Generator
from shared.functions.artFunctions import getInput, changeSymbol, askToSaveArt, previewArt, scaleArt

from shared.classes.artClasses.ArtSettings import ArtSettings

from ui.MenuItem import MenuItem
from ui.MenuBuilder import MenuBuilder

class ArtGenerator(Generator):
    def __init__(self, settings):
        super().__init__(settings)

    def generate(self):
        user_input = getInput()

        art = Figlet(font=self.settings.font, width=800)
        art = art.renderText(user_input)

        art = changeSymbol(art, self.settings.symbol)

        art = scaleArt(art, self.settings.width, self.settings.height)

        coloured_art = f"\033[33m{art}\033[0m"

        file_path = os.path.join(self.folderToSave, '')

        previewArt(coloured_art)
        askToSaveArt(file_path, art)

    def menu(self):
        settings = ArtSettings()
        generator = ArtGenerator(settings)

        menu_items = [
            MenuItem("1", "Art", generator.generate),
            MenuItem("2", "Art settings", settings.menu),
            MenuItem("0", "Вийти", exit),
        ]

        menu_lab = MenuBuilder(menu_items)
        while True:
            menu_lab.initialize()

