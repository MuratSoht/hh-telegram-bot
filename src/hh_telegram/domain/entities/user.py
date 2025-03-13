from dataclasses import dataclass
from hh_telegram.domain.entities.query import QuerySearchVacancies
from typing import List

@dataclass(slots=True)
class User:
    name: str
    city: str
    queries: List[QuerySearchVacancies]
