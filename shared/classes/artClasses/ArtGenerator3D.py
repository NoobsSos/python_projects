class ThreeDArtService:

    def __init__(self, height: int, color: int, direction: bool):
        self.color = color
        self.direction = direction

    def change_size(self):
        try:
            size = int(input("Enter new size (no less than 3): "))
            if size >= 3:
                self.side_a = size
            else:
                print("Size must be at least 3. Try again.")
                self.change_size()
        except ValueError:
            print("Invalid input. Please enter a valid integer for size.")
            self.change_size()

    def change_color(self, color: int):
        self.color = color

    def change_direction(self):
        self.direction = not self.direction
        print("Direction was successfully changed")

    def get_art(self) -> str:
        color_text = '\033[%dm%s\033[0m'
        if self.direction:
            art = self.art.get_three_d_art()
        else:
            art = self.art.get_three_d_inverted_art()

        return color_text % (self.color, art)

    def get_2d_art(self) -> str:
        color_text = '\033[%dm%s\033[0m'
        art = self.art.get_two_d_art()
        return color_text % (self.color, art)

    def print_art(self):
        print(self.get_art())

    def print_2d_art(self):
        print(self.get_2d_art())