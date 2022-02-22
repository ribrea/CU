from cli_app import App
from dotenv import load_dotenv

from cu import GetUser, Comment, Team, Space, Folder, List, Tasks

load_dotenv()


class CU(App):
    """
    CU, Click up CLI app
    """

    def register_commands(self):
        self.add_command('me', GetUser)
        self.add_command('comment', Comment)
        self.add_command('team', Team)
        self.add_command('space', Space)
        self.add_command('folder', Folder)
        self.add_command('list', List)
        self.add_command('task', Tasks)


def main():
    CU().run()


if __name__ == '__main__':
    app = CU()
    app.run()
