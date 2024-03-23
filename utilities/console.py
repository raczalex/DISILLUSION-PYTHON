from sys import stdout
from os import name,system,get_terminal_size
from pystyle import Center,Colors,Colorate,Box
import math

def _clear():
    """Clear the console on every os."""
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

def _setTitle(title:str):
    """Sets the console title on every os."""
    if name == 'posix':
        stdout.write(f"\x1b]2;{title}\x07")
    elif name in ('ce', 'nt', 'dos'):
        system(f'title {title}')
    else:
        stdout.write(f"\x1b]2;{title}\x07")
        stdout.flush()

def _printThreeColumnsWithNumbers(data,terminal_width=82):
    items_per_column = len(data) // 3
    remainder = len(data) % 3

    max_width = 0
    for i in range(3):
        index = i * (items_per_column + min(1, remainder))
        if index < len(data):
            max_width += len(f"[{index + 1}] {data[index]}")

    offset = (terminal_width - max_width) // 2

    for i in range(items_per_column + min(1, remainder)):
        for j in range(3):
            index = i + j * (items_per_column + min(1, remainder))
            if index < len(data):
                print(f"{' ' * offset}{Colors.white}[{index + 1}] {Colors.light_green}{data[index]:<20}", end="")
        print()

def _visibleLength(text):
    escape_code_start = '\033['
    escape_code_end = 'm'

    visible_len = 0
    i = 0
    while i < len(text):
        if text[i:i + len(escape_code_start)] == escape_code_start:
            while i < len(text) and text[i] != escape_code_end:
                i += 1
            i += 1
        else:
            visible_len += 1
            i += 1

    return visible_len

def _printThreeColumnsWithNumbersColored(options):
    num_options = len(options)
    num_columns = 3

    max_index_length = len(f"[{num_options}]")
    max_option_length = max(map(len, options))
    max_column_width = max_index_length + max_option_length + 2

    rows = math.ceil(num_options / num_columns)
    terminal_width = get_terminal_size().columns
    if len(options) == 1:
        print(f'   {Colors.white}[1] {Colors.light_green}{options[0]}')
    elif len(options) == 2:
        print(f'   {Colors.white}[1] {Colors.light_green}{options[0]}  {Colors.white}[2] {Colors.light_green}{options[1]}')
    elif len(options) == 3:
        print(f'   {Colors.white}[1] {Colors.light_green}{options[0]}  {Colors.white}[2] {Colors.light_green}{options[1]}   {Colors.white}[3] {Colors.light_green}{options[2]}')
    else:
        for row in range(rows):
            row_text = ""
            for col in range(num_columns):
                index = row + col * rows
                if index < num_options:
                    option = options[index]
                    index_str = f"[{index + 1}]"
                    padding = max_column_width - len(index_str) - len(str(option))
                    colored_text = f"{Colors.white}{index_str} {Colors.light_green}{option}{Colors.reset}"
                    row_text += f"{colored_text}{padding * ' '}\t"

            row_text = row_text.rstrip('\t')

            remaining_space = terminal_width - len(row_text)
            center_padding = max(3, remaining_space // 2)
            print(' ' * center_padding + row_text)

def _printThreeColumnsDictWithNumbersColored(options):
    num_options = len(options)
    num_columns = 3

    max_index_length = len(f"[{num_options}]")
    max_option_length = max(map(lambda x: len(x['Name']), options))
    max_column_width = max_index_length + max_option_length + 2

    rows = math.ceil(num_options / num_columns)
    terminal_width = get_terminal_size().columns

    for row in range(rows):
        row_text = ""
        for col in range(num_columns):
            index = row + col * rows
            if index < num_options:
                option = options[index]['Name']
                index_str = f"[{index + 1}]"
                padding = max_column_width - len(index_str) - len(str(option))
                if option != "":
                    colored_text = f"{Colors.white}{index_str} {Colors.light_green}{option}{Colors.reset}"
                else:
                    colored_text = f"{Colors.light_green}{option}{Colors.reset}"
                row_text += f"{colored_text}{padding * ' '}\t"

        row_text = row_text.rstrip('\t')

        remaining_space = terminal_width - len(row_text)
        center_padding = max(3, remaining_space // 2)
        print(' ' * center_padding + row_text)

def _printBoxedData(*args):
    contact_info = " - ".join(args)
    formatted_contact = Colorate.Vertical(Colors.green_to_cyan, Center.XCenter(Box.DoubleCube(contact_info)))
    print(formatted_contact)
    print('')


def _initTitle(title:str):
    _setTitle(title)
    _clear()
    print(Colorate.Vertical(Colors.green_to_cyan,Center.XCenter("""
                                                                
████████▄   ▄█     ▄████████  ▄█   ▄█        ▄█       ███    █▄     ▄████████  ▄█   ▄██████▄  ███▄▄▄▄   
███   ▀███ ███    ███    ███ ███  ███       ███       ███    ███   ███    ███ ███  ███    ███ ███▀▀▀██▄ 
███    ███ ███▌   ███    █▀  ███▌ ███       ███       ███    ███   ███    █▀  ███▌ ███    ███ ███   ███ 
███    ███ ███▌   ███        ███▌ ███       ███       ███    ███   ███        ███▌ ███    ███ ███   ███ 
███    ███ ███▌ ▀███████████ ███▌ ███       ███       ███    ███ ▀███████████ ███▌ ███    ███ ███   ███ 
███    ███ ███           ███ ███  ███       ███       ███    ███          ███ ███  ███    ███ ███   ███ 
███   ▄███ ███     ▄█    ███ ███  ███▌    ▄ ███▌    ▄ ███    ███    ▄█    ███ ███  ███    ███ ███   ███ 
████████▀  █▀    ▄████████▀  █▀   █████▄▄██ █████▄▄██ ████████▀   ▄████████▀  █▀    ▀██████▀   ▀█   █▀  
                                  ▀         ▀                                                           
    """)))
    _printBoxedData('discord: racz.alex','email: raczalex@proton.me','github: raczalex')