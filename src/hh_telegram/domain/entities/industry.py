from dataclasses import dataclass
from typing import NewType, List, Optional

IndustryId = NewType('IndustryId', int)

@dataclass(slots=True)
class Industry:
    id: IndustryId
    text: str
    subindustries: Optional[List["Industry"]]
    callback_name: str
