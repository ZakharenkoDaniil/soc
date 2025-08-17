import os

from automapper import mapper
from tortoise import Tortoise
from dotenv import load_dotenv

from dto.input_event_dto import InputEventDto
from dto.output_event_dto import OutputEventDto
from model.event_entity import EventEntity


async def init():
    load_dotenv()
    db_url = os.getenv("DB_URL")
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['model.event_entity']}
    )
    await Tortoise.generate_schemas()
    mapping_config()


def mapping_config():
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
    mapper.add(EventEntity,
               OutputEventDto,
               fields_mapping={
                   "id_issue": "EventEntity.event_id",
                   "created": "EventEntity.created",
                   "updated": "EventEntity.updated",
                   "status": "EventEntity.status",
                   "severity": "EventEntity.severity",
                   "tool": "EventEntity.tool",
                   "type": "EventEntity.event_type",
                   "description": "EventEntity.description",
                   "event_details": "EventEntity.details"
               })
