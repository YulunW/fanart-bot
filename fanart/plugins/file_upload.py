from nonebot import on_notice, NoticeSession
from nonebot.log import logger
from config import MONITORING_GROUPS


@on_notice('group_upload')
async def upload_recognition(session: NoticeSession):
    if session.ctx.group_id not in MONITORING_GROUPS:
        logger.info(f"Group {session.ctx.group_id} is not in the monitoring groups. Skip this upload")
        return
    await session.send(session.event.__repr__())
    return
