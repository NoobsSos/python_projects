import os
import pyfiglet

from assets.font import chars

def getInput():
    user_input = input('Enter the phrase: ')

    return user_input

def changeSymbol(art, symbol):
    for char in art:
        if char != '\n' and char != ' ':
            art = art.replace(char, symbol)

    return art

def askToSaveArt(folderToSave, art):
    isArtToSave = input('Do you want to save your art? (y/n): ')

    if isArtToSave == 'y':
        saveArt(folderToSave, art)
    else:
        pass

def saveArt(folderToSave, art):
    file_name = input('Give a file name: ')
    formated_file_name = folderToSave + file_name + '.txt'

    with open(formated_file_name, 'w') as file:
        file.write(art)

def previewArt(art):
    print(art)


def scaleArt(ascii_art, width_factor, height_factor):
    width_factor = int(width_factor)
    height_factor = int(height_factor)

    scaled_lines = []
    for line in ascii_art.splitlines():
        scaled_line = "".join(char * width_factor for char in line)
        for _ in range(height_factor):
            scaled_lines.append(scaled_line)
    return "\n".join(scaled_lines)

def draw_char(text):
    result = [""] * 6

    for char in text.upper():
        if char in chars:
            for i in range(6):
                result[i] += chars[char][i] + "  "

    return "\n".join(result)

def align_art(ascii_art, width, alignment):
    aligned_lines = []
    for line in ascii_art.splitlines():
        if alignment == "left":
            aligned_lines.append(line.ljust(width))
        elif alignment == "center":
            aligned_lines.append(line.center(width))
        elif alignment == "right":
            aligned_lines.append(line.rjust(width))
        else:
            aligned_lines.append(line)
    return "\n".join(aligned_lines)


