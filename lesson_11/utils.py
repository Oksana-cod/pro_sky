import json
from pprint import pprint as pp
from candid import DATA


def load_candidates_from_json(path=DATA):
    """считывает всех кондидатов"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_all_candidates():
    """возвращает список всех кандидатов"""
    candidates = load_candidates_from_json()
    return candidates


def get_candidate_by_id(id):
    """возвращает одного кандидата по его id"""
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate["id"] == id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    name_cand = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            name_cand.append(candidate)
    return name_cand


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    skill_name = skill_name.lower()
    candidates_found = []
    candidates = load_candidates_from_json()

    for candidate in candidates:
        skills = candidate.get("skills")
        list_of_skills = skills.lower().split(", ")
        if skill_name in list_of_skills:
            candidates_found.append(candidate)
    return candidates_found


#pp(get_all_candidates())