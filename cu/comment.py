import requests
from cli_app import Command
from ._token import headers
from pprint import pprint as print


class Comment(Command):
    """
    Comment on a post
    """

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('task_id', type=str, help='Task ID')
        parser.add_argument('comment', type=str, help='Comment to be added', )
        parser.add_argument('-notify_all', '-n', type=bool, help='Notify all users', default=False)

    def run(self):
        body = {
            "comment_text": self.app.args.comment,
            "notify_all": self.app.args.notify_all
        }
        t_id = self.app.args.task_id
        res = requests.post(f"https://api.clickup.com/api/v2/task/{t_id}/comment",
                            headers=headers,
                            json=body)
        print("Commenting on task")
        print(res.json())
