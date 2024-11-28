from shared.classes.artClasses.ArtGenerator import ArtGenerator
from shared.classes.artClasses.ArtSettings import ArtSettings

class Lab3:
    def run(self):
        artSettings = ArtSettings()
        generator = ArtGenerator(artSettings)

        generator.menu()