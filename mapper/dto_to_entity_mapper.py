from automapper import mapper

from dto.input_event_dto import InputEventDto


def input_event_dto_to_event_entity(source: InputEventDto):
    return mapper.map(source)
