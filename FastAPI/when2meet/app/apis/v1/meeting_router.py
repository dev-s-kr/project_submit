from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
