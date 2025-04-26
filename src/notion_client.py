import requests


def fetch_notion_data(notion_api_key, database_id):
    NOTION_API_KEY = notion_api_key
    DATABASE_ID = database_id

    url = "https://api.notion.com/v1/databases/" + DATABASE_ID + "/query"

    headers = {
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers)
    json_dict = response.json()

    return json_dict
