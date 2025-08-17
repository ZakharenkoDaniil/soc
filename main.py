import logging

import uvicorn
from automapper import MappingError
from fastapi import FastAPI
from tortoise import run_async

from config.config import init
from dto.input_event_dto import InputEventDto
from handler.handlers import post_new_event_handler, get_events_by_issue_id

logger = logging.getLogger(__name__)
app = FastAPI()


@app.post("/event")
async def add_new_event(event: InputEventDto):
    try:
        await post_new_event_handler(event)
    except MappingError as mapping_error:
        logger.error("Ошибка мапинга события: " + str(mapping_error))
        return {"Internal Error": 500}
    return {"Success": 200}


@app.get("/event/{uuid}")
async def get_event_by_uuid(uuid: str):
    return await get_events_by_issue_id(uuid)


if __name__ == '__main__':
    run_async(init())
    uvicorn.run(app=app, port=12345)
