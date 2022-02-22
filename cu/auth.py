import requests
from cli_app import Command
from ._token import headers
from pprint import pprint as print


class GetUser(Command):
    """Get user information"""

    def run(self):
        """
        Get user information
        :return: None
        """
        print("Getting user information...")
        print(requests.get("https://api.clickup.com/api/v2/user", headers=headers).json())
