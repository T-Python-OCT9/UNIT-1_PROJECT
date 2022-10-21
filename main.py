from cli_view import CommandLineView

main_view = CommandLineView({
    'message': '\n\t\tWelcome to Tuwaiq HR System\n\n Type one of these commands to execute:\n\t(M) \t\t- Manager login.\n\t(E)\t\t- Employe login. \n\t(EXIT)\t\t- Exit the system. \n\n',
    'commands': ['m', 'e', 'exit']
})

command: str = main_view.commandLineListener()
