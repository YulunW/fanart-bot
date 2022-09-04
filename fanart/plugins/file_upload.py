from nonebot import on_notice, NoticeSession
from nonebot.log import logger
from config import MONITORING_GROUPs


@on_notice('group_upload')
async def upload_recognition(session: NoticeSession):
    if int(session.ctx.group_id) in MONITORING_GROUPs:
        logger.info(f"Group {session.ctx.group_id} is not in the monitoring groups. Skip this upload")
        return
    await session.send(session.event.__repr__())
    return
