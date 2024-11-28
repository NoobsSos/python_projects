from shared.classes.artClasses.ArtGeneratorNoLib import ArtGeneratorNoLib
from shared.classes.artClasses.ArtSettings import ArtSettings

class Lab4:
    def run(self):
        artSettings = ArtSettings()
        generator = ArtGeneratorNoLib(artSettings)

        generator.menu()