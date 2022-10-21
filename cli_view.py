import os


class CommandLineView:
    def __init__(self, the_view: dict) -> None:
        interrupt: str = ''
        self.__message = the_view['message']
        self.__commands = the_view['commands']
        self.__interrupt = interrupt

    def commandLineListener(self):
        while not self.__interrupt in self.__commands:
            os.system('clear')
            self.__interrupt = input(f"{self.__message}\n > ")
        return self.__interrupt