from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    SECRET_ID = os.environ["NOTION_SECRET_ID"]
    DB_ID = os.environ["NOTION_DB_ID"]
    return SECRET_ID,DB_ID

if __name__ == "__main__":
    print(load_env())
