from typing import Optional, Dict, Any

from nonebot import on_notice, NoticeSession
from nonebot.log import logger
from config import MONITORING_GROUPS
from helpers.types import UploadedFile
from pydantic import ValidationError




@on_notice('group_upload')
async def upload_recognition(session: NoticeSession):
    if session.ctx.group_id not in MONITORING_GROUPS:
        logger.info(f"Group {session.ctx.group_id} is not in the monitoring groups. Skip this upload")
        return
    try:
        file = UploadedFile(**session.event.file)
    except (ValidationError, TypeError) as e:
        logger.warn(f"File format in incorrect! Some thing is going wrong. The file: {file}. The error: {e}")
        return

    await session.send(f"检测到文件上传事件。文件信息： 文件名-{file.name}；文件大小-{file.size}；文件url-{file.url}")
    return
