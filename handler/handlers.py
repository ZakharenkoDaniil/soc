import logging

from dto.input_event_dto import InputEventDto
from mapper.dto_to_entity_mapper import input_event_dto_to_event_entity
from model.event_entity import EventEntity

logger = logging.getLogger(__name__)


async def post_new_event_handler(event_dto: InputEventDto):
    event_entity = input_event_dto_to_event_entity(event_dto)
    logger.info("input event with event_id = " + event_entity.event_id)
    await event_entity.save()


async def get_events_by_issue_id(issue_id: str):
    events = await EventEntity.filter(event_id=issue_id)
    if not events:
        logger.info("event with event_id not found")
    else:
        logger.info("found " + str(len(events)) + " events by event_id = " + issue_id)
    return events

