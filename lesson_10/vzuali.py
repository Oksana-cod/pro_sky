def function_1(candidate):
    """формирует HTML код для вывода 1 кандидата"""
    code_for_candidate = ""
    code_for_candidate += f"<img src=\"{candidate['picture']}\">\n"
    code_for_candidate += f"{candidate['name']}\n"
    code_for_candidate += f"{candidate['skills']}\n"
    code_for_candidate += f"{candidate['position']}\n"
    code_for_candidate += "\n"

    return "<pre>" + code_for_candidate + "<pre>"


def function_2(candidates):
    """ HTML для нескольких кандитатов"""
    list_of_candidates = ""

    for candidate in candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += "\n"

    return "<pre>" + list_of_candidates + "</pre>"