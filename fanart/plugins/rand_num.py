from nonebot import on_command, CommandSession

import random
import re
from typing import Optional

HELPER_MESSAGE = """
参数格式不正确。当前支持的参数格式为：
0. 无参数 将返回1-100之间的随机数（包括1和100）
1. 自然数-自然数 其中两个自然数会分别被识别为随机指令的上下限。如：5-20
2. 正整数 这个正整数会被识别味随机指令的上限。如：20
3. 两个以上以空格或tab分隔的字符串。将会从中随机选择一个字符串作为结果。如：吃饭 睡觉 打豆豆
"""


@on_command('random', only_to_me=False, aliases=('随机', 'roll'))
async def rand_num(session: CommandSession) -> None:
    args = session.current_arg_text.strip()
    start = 1
    end = 100
    match_obj: Optional[re.Match] = None
    if (match_obj := re.fullmatch(r"(\d+)-(\d+)", args)) is not None:
        start, end = [int(num) for num in match_obj.group(1, 2)]
    elif (match_obj := re.fullmatch(r"(\d+)", args)) is not None:
        end = int(match_obj.group(1))
    elif args != "":
        choices = args.split()
        if len(choices) < 2:
            await session.send(HELPER_MESSAGE)
            return
        start = 0
        end = len(choices) - 1
        await session.send(f"随机 [{' '.join(choices)}] 结果为：{choices[random.randint(start, end)]}")
        return

    if start > end:
        await session.send(f"随机数上限{end}小于随机数下限{start}。请输入正确的范围后重试")
        return

    result = random.randint(start, end)
    await session.send(f"随机 [{start}-{end}] 的结果为：{result}")
