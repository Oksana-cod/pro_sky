import json
from pprint import pprint as pp
from candid import DATA


def _load_data(path=DATA):
    """считывает всех кондидатов"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def candidates_get_all():
    """получает данные всех кандидатов"""
    data = _load_data()
    return data


def candi_pk(id):
    """получаем кондидата по его id"""
    candidates = _load_data()
    for candidate in candidates:
        if candidate["id"] == id:
            return candidate


def candi_skill(skill_name):
    """получаем кондидата по навыкам"""

    skilled_candidates = []
    skill_name_lower = skill_name.lower()

    candidates = _load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue

    return skilled_candidates


#pp(candi_skill("go"))