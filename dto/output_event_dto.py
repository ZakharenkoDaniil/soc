from typing import Dict, AnyStr, Any

from pydantic import BaseModel


class OutputEventDto(BaseModel):
    id_issue: str
    created: str
    updated: str
    status: str
    severity: str
    tool: str
    type: str
    description: str
    event_details: Dict[AnyStr, Any]