from shared.abstract_classes.Generator import Generator
import os

from ui.MenuItem import MenuItem
from ui.MenuBuilder import MenuBuilder

from shared.functions.artFunctions import getInput, changeSymbol, askToSaveArt, previewArt, scaleArt, draw_char,align_art

from shared.classes.artClasses.ArtSettings import ArtSettings

class ArtGeneratorNoLib(Generator):

    def __init__(self, settings):
       super().__init__(settings)

    def generate(self):
        user_input = getInput()

        art = draw_char(user_input)

        art = changeSymbol(art, self.settings.symbol)

        art = scaleArt(art, self.settings.width, self.settings.height)

        art = align_art(art, 175, self.settings.align)

        coloured_art = f"\033[{self.settings.color}m{art}\033[0m"

        file_path = os.path.join(self.folderToSave, '')

        previewArt(coloured_art)
        askToSaveArt(file_path, art)

    def menu(self):
        settings = ArtSettings()
        generator = ArtGeneratorNoLib(settings)
        menu_items = [
            MenuItem("1", "Art", generator.generate),
            MenuItem("2", "Art Settings", settings.menu),
            MenuItem("0", "Exit", exit),
        ]
        menu_builder = MenuBuilder(menu_items)
        while True:
            menu_builder.initialize()