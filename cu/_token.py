import os
import sys

token = os.environ.get("CUTOKEN", None)
if token is None:
    print("Token not found")
    sys.exit(1)

headers = {"Authorization": token}
