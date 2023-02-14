import os
import time
import random

def print_colored_typing(text, color, typing_speed=0.03):
    for letter in text:
        print(f'\033[{color}m{letter}\033[0m', end='', flush=True)
        time.sleep(typing_speed)
    print()

def process_file(file):
    if not os.path.exists(file):
        print_colored_typing(f'The file "{file}" does not exist.', 31)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored_typing(f'File: "{file}"', 34)
        print_colored_typing('------------------------------', 33)
        print_colored_typing('1. Read', 32)
        print_colored_typing('2. Write', 32)
        print_colored_typing('3. Remove', 32)
        print_colored_typing('------------------------------', 33)
        option = input('Enter your option:\n')
        if option == '1':
            os.system(f'exiftool "{file}"')
        elif option == '2':
            copywrite = input('Enter the custom copyright notice: ')
            os.system(f'exiftool -overwrite_original -rights="{copywrite}" -CopyrightNotice="{copywrite}" "{file}"')
        elif option == '3':
            os.system(f'exiftool -all= -overwrite_original "{file}"')
        else:
            print_colored_typing('Invalid option.', 31)
        input('Press Enter to continue...')

def process_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            process_file(full_path)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_colored_typing('Enter the file names or folder path (separated by comma):', 33)
    files = input().split(',')
    for item in map(str.strip, files):
        if os.path.isdir(item):
            process_folder(item)
        else:
            process_file(item)
    print_colored_typing('Do you want to process more files or folders? (y/n)', 33)
    choice = input()
    if choice.lower() != 'y':
        break
