from save_content import SaveContent
from cli_commands import CLICommands
from generating_content import GeneratingContent

# Main function that starts the application
def main():

    cli = CLICommands(generate=GeneratingContent() , storge=SaveContent())
    cli.welcome_message()
    cli.start_ai()

# Run the app if this file is executed directly
if __name__ == "__main__":
    main()
