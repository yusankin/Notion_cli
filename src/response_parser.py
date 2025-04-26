def extract_titles_from_response(json_dict):
    titles = []
    for value_json_dict in json_dict["results"]:
        for value_title in value_json_dict["properties"]["Name"]["title"]:
            titles.append(value_title["plain_text"])
    return titles


def extract_select_from_response(json_dict):
    selects = []
    for value_json_dict in json_dict["results"]:
        value_selects = value_json_dict["properties"]["セレクト"]["select"]
        selects.append(value_selects["name"])

    return selects


def extract_titles_and_selects_from_response(json_dict):
    titles_and_selects = []
    for result in json_dict["results"]:
        try:
            title = result["properties"]["Name"]["title"][0]["plain_text"]
        except (KeyError, IndexError, TypeError):
            title = ""
        try:
            select = result["properties"]["セレクト"]["select"]["name"]
        except (KeyError, TypeError):
            select = ""

        titles_and_selects.append({"title": title, "select": select})

    return titles_and_selects
