from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import json

# 添加服务器
add_server = on_command("添加服务器", permission=SUPERUSER)


@add_server.handle()
async def add_server_handle(bot: Bot, event: Event):
    msg_spilt = event.get_plaintext().split(" ")
    # 判断语法
    if len(msg_spilt) == 3:
        # 获取用户输入的信息
        ip = msg_spilt[1]
        port = msg_spilt[2]
        # 写入服务器配置文件
        with open("server.json", "r") as fp:
            server_list = json.load(fp)
            server_list[str(len(server_list) + 1)] = {"ip": ip, "port": port}
        with open("server.json", "w") as fp:
            json.dump(server_list, fp)
        await add_server.finish("添加成功, 新服务器序号为: "+str(len(server_list)))
    else:
        # 语法错误
        await add_server.finish("添加服务器失败\n"
                                "原因：语法错误\n"
                                "语法：添加服务器 [IP] [Port]")


# 清空服务器
clear_server = on_command("清空服务器", permission=SUPERUSER)


@clear_server.handle()
async def clear_server_handle(bot: Bot, event: Event):
    with open("server.json", "w") as fp:
        json.dump({}, fp)
    await clear_server.finish("清空成功")