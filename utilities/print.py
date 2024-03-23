from threading import Lock
from pystyle import Colors

lock = Lock()

"""Prints white colored text with timestamp and with the defined header separator and content."""
def _printw(header:str,content:str):
    lock.acquire()
    print(f'  {Colors.white} [{header}] {content}')
    lock.release()

"""Prints yellow colored text with timestamp and with the defined header separator and content."""
def _printy(header: str, content: str):
    lock.acquire()
    print(f'  {Colors.white} [{Colors.yellow}{header}{Colors.white}] {Colors.white}{content}')
    lock.release()

"""Prints green colored text with timestamp and with the defined header separator and content."""
def _printg(header:str,content:str):
    lock.acquire()
    print(f'  {Colors.white} [{Colors.light_green}{header}{Colors.white}] {Colors.white}{content}')
    lock.release()

"""Prints red colored text with timestamp and with the defined header separator and content."""
def _printr(header:str, content:str):
    lock.acquire()
    print(f'  {Colors.white} [{Colors.light_red}{header}{Colors.white}] {Colors.white}{content}')
    lock.release()