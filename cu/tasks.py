from cli_app import Command
from ._token import headers
import requests
from pprint import pprint as pp


class Team(Command):
    """
    Get all Teams
    """

    def run(self):
        teams = requests.get("https://api.clickup.com/api/v2/team", headers=headers).json()['teams']
        for team in teams:
            print(f"Team: {team['name']} \t ID: {team['id']}")


class Space(Command):
    """
    Get all Spaces
    """

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('team_id', type=str, help='Team ID')
        parser.add_argument('-all', '-a', type=bool, help='All of em', default=False)

    def run(self):
        spaces = \
            requests.get(
                f"https://api.clickup.com/api/v2/team/{self.app.args.team_id}/space?archived={self.app.args.all}",
                headers=headers).json()['spaces']
        for space in spaces:
            print(f"Space: {space['name']} \t ID: {space['id']}")


class Folder(Command):
    """
    Get all Folders
    """

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('space_id', type=str, help='Space ID')
        parser.add_argument('-all', '-a', type=bool, help='All of em', default=False)

    def run(self):
        folders = requests.get(
            f"https://api.clickup.com/api/v2/space/{self.app.args.space_id}/folder?archived={self.app.args.all}",
            headers=headers).json()['folders']
        for folder in folders:
            print(f"Folder: {folder['name']} \t ID: {folder['id']}")


class List(Command):
    """
    Get all Lists
    """

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('folder_id', type=str, help='Folder ID')
        parser.add_argument('-all', '-a', type=bool, help='All of em', default=False)

    def run(self):
        lists = requests.get(
            f"https://api.clickup.com/api/v2/folder/{self.app.args.folder_id}/list?archived={self.app.args.all}",
            headers=headers).json()['lists']
        for list in lists:
            print(f"List: {list['name']} \t ID: {list['id']}")


class Tasks(Command):
    """
    Get all Tasks
    """

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('team_id', type=str, help='List ID')
        parser.add_argument('-m', '--me', action='store_true')
        parser.add_argument('-a', '--all', action='store_true')

    def run(self):
        url = f"https://api.clickup.com/api/v2/team/{self.app.args.team_id}/task?"

        if self.app.args.me:
            uid = requests.get("https://api.clickup.com/api/v2/user", headers=headers).json()["user"]["id"]
            url = f"{url}assignees%5B%5D={uid}&"

        if self.app.args.all:
            url = f"{url}archived=false&"

        print(url)

        tasks = requests.get(
            url,
            headers=headers).json()['tasks']
        for task in tasks:
            print(f"Task: {task['name']} \t ID: {task['id']}")
