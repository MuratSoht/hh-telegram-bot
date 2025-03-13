from dataclasses import dataclass, asdict
from src.hh_telegram.domain.entities.vacancy_id import VacancyId
from typing import List

@dataclass(slots=True)
class Vacancy:
    id: VacancyId
    title: str
    published_date: str
    salary: str
    work_format: str
    city: str
    experience: str
    skills_keys: List[str]
    descriptions: str
    url: str
    is_archive: bool

    def get_vacancy(self):
        return asdict(self)