from automapper import mapper

from dto.input_event_dto import InputEventDto
from model.event_entity import EventEntity


def input_event_dto_to_event_entity(source: InputEventDto):
    return mapper.map(source)


def event_entity_to_output_event_dto(source: EventEntity):
    return mapper.map(source)
