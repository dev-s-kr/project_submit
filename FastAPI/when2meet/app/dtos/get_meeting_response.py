from app.dtos.frozen_config import FROZEN_CONFIG
from pydantic import BaseModel


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: str