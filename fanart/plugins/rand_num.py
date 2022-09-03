from nonebot import on_command, CommandSession

import random
import re
from typing import Optional


@on_command('random', only_to_me=False, aliases=('随机', 'roll'))
async def rand_num(session: CommandSession) -> None:
    # 取得消息的内容，并且去掉首尾的空白符
    args = session.current_arg_text.strip()
    start = 1
    end = 100
    match_obj: Optional[re.Match] = None
    if (match_obj := re.fullmatch(r"(\d+)-(\d+)", args)) is not None:
        start, end = [int(num) for num in match_obj.group(1, 2)]
    elif (match_obj := re.fullmatch(r"(\d+)", args)) is not None:
        end = int(match_obj.group(1))
    elif args != "":
        await session.send(
            """参数格式不正确。目前支持的参数格式为：\n"""
            """一个数字，决定随机数的上限。如输入56会返回一个1~56之间的随机数。\n"""
            """数字-数字的形式，如2-56。两个数分别为随机数的上下限。""")
        return
    result = random.randint(start, end)
    await session.send(f"[{start}-{end}]结果为：{result}")
