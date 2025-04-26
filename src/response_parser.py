import select


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
