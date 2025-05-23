from env_loader import load_env
from notion_client import fetch_notion_data
from response_parser import (
    extract_titles_from_response,
    extract_select_from_response,
    extract_titles_and_selects_from_response,
)

if __name__ == "__main__":
    api_key, db_id = load_env()
    data = fetch_notion_data(api_key, db_id)
    # title_text = extract_titles_from_response(data)
    select_text = extract_select_from_response(data)
    # title_and_select_text = extract_titles_and_selects_from_response(data)
    print(select_text)
