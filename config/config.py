from automapper import mapper
from tortoise import Tortoise

from dto.input_event_dto import InputEventDto
from model.event_entity import EventEntity


async def init():
    await Tortoise.init(
        db_url='postgres://soc:pgsocpwd@localhost:5430/soc',
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
