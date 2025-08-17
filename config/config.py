import os

from automapper import mapper
from tortoise import Tortoise
from dotenv import load_dotenv

from dto.input_event_dto import InputEventDto
from model.event_entity import EventEntity


async def init():
    load_dotenv()
    db_url = os.getenv("DB_URL")
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['model.event_entity']}
    )
    await Tortoise.generate_schemas()
    mapper.add(InputEventDto,
               EventEntity,
               fields_mapping={
                   "event_id": "InputEventDto.id_issue",
                   "status": "InputEventDto.status",
                   "severity": "InputEventDto.severity",
                   "tool": "InputEventDto.tool",
                   "event_type": "InputEventDto.type",
                   "description": "InputEventDto.description",
                   "details": "InputEventDto.event_details"
               })
