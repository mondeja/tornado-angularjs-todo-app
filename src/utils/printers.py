#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Back, Fore, Style, init
init(autoreset=True)

def fail(msg):  # Error message
    print(Back.LIGHTRED_EX + Fore.YELLOW + Style.BRIGHT + " %s " % msg)

def success(msg): # Success message
    print(Fore.GREEN + Style.BRIGHT + " %s " % msg)

def warning(msg): # Warning message
    print(Back.LIGHTYELLOW_EX + Fore.RED + Style.BRIGHT + " %s " % msg)

def verboser(msg): # Info message
    print(Fore.BLUE + Style.BRIGHT + " %s " % msg)

