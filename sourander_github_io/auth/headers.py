import dotenv
import os

def get_github_headers():
    # Load the .env file
    dotenv.load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    assert token, "No GitHub token found! Use .evn file or set GITHUB_TOKEN environment variable."

    headers = {
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28"
    }

    return headers