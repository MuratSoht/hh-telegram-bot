from dataclasses import dataclass
from typing import List

from hh_telegram.domain.entities.vacancy_id import VacancyId

@dataclass(slots=True)
class QuerySearchVacancies:
    query_text: str
    per_page: int
    period: int
    industry: int 
    shedule: str
    experience: List[str]
    search_field: str

@dataclass(slots=True)
class QuerySearchVacancy:
    id: VacancyId
