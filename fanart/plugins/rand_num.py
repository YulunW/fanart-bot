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
        choices = args.split(" ")
        start = 0
        end = len(choices) - 1
        await session.send(f"随机 [{args}] 结果为：{choices[random.randint(start, end)]}")
        return

    if start > end:
        await session.send(f"随机数上限{end}小于随机数下限{start}。请输入正确的范围后重试")
        return

    result = random.randint(start, end)
    await session.send(f"随机 [{start}-{end}] 的结果为：{result}")
