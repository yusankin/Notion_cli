from dotenv import load_dotenv
import os


def load_env():
    load_dotenv()
    notion_api_key = os.environ["NOTION_SECRET_ID"]
    database_id = os.environ["NOTION_DB_ID"]
    return notion_api_key, database_id
