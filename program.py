import fileHandler
import calculate
import tkinter
from tkinter import filedialog


def main():
    print_header()
    run_every_loop()


def print_header():
    print('-----------------------')
    print('     Sudoko Solver     ')
    print('-----------------------')


def run_every_loop():
    print('What do you want to do with this Sudoko Solver?')
    cmd = 'EMPTY'
    sudoku_name = 'default'

    while cmd != 'x' and cmd:
        cmd = input('[C]alculate a new Sudoko, [L]ist previously solved Sudokos, [E]xit')
        cmd = cmd.lower().strip()
        if cmd == 'c':
            root = tkinter.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            print(file_path)


if __name__ == '__main__':
    main()