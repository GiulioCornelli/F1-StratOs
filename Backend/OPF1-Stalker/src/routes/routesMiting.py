#librerie esterne
from fastapi import APIRouter

#librerie custom

routerMeeting = APIRouter(prefix="/api/meetings", tags=["Meetings"])


@routerMeeting.get("/getAllMeetings")
async def getAllMeetings() :
    pass