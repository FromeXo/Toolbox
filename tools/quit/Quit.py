from sys import exit


class Quit:

    NAME = "Quit"
    DESC = "Exit out of the program."
    VERS = "1.0.0"

    def main():
        print("Bye.")
        exit()


if __name__ == "__main__":
    Quit.main()
