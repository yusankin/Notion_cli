def extract_titles_from_response(json_dict):
    titles = []
    for index_json_dict, value_json_dict in enumerate(json_dict["results"]):
        for index_title, value_title in enumerate(
            json_dict["results"][index_json_dict]["properties"]["Name"]["title"]
        ):
            titles.append(value_title["plain_text"])

    return titles
