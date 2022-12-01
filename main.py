from PyInquirer import prompt
from terminal_style import style
from validators import EmptyValidator
from pyfiglet import Figlet
import user
from dotenv import load_dotenv
import os
import sys


def main() -> None:
    load_dotenv()
    print(Figlet(font=os.getenv('FigletFont')).renderText('TikTok Tools'))
    menu = [
        {
            "type": "list",
            "name": "menu",
            "message": "Choose the option: ",
            "choices": [
                "Download Profile Picture",
                "Download Video",
                "Show all video liked by user",
                "Exit"
            ]
        }
    ]
    ans = prompt(menu, style=style)
    if ans['menu'] == "Download Profile Picture":
        get_username = [
            {
                "type": "input",
                "name": "username",
                "message": "Enter username: ",
                "validate": EmptyValidator
            }
        ]
        answer = prompt(get_username, style=style)
        user.profile_picture_user(username=answer['username'])

    elif ans['menu'] == "Download Video":
        get_username = [
            {
                "type": "input",
                "name": "username",
                "message": "Enter username: ",
                "validate": EmptyValidator
            }
        ]
        answer = prompt(get_username, style=style)
        user.video_from_user(username=answer['username'])
    elif ans['menu'] == "Show all video liked by user":
        pass
    elif ans['menu'] == "Exit":
        exit_confirm = [
            {
                "type": "confirm",
                "message": "Do you want to exit?",
                "name": "exit",
                "defult": False
            }
        ]
        answer = prompt(exit_confirm, style=style)
        if answer['exit']:
            sys.exit(0)
        else:
            main()
    else:
        print("Bad choose!.")
        main()


if __name__ == "__main__":
    main()

