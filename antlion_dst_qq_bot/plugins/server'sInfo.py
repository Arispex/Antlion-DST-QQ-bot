import tools
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import config
import json
import requests
import re
import time

# 世界信息
world_info = on_command('世界信息')


@world_info.handle()
async def world_info_handle(event: Event, bot:Bot):
    msg_spilt = event.get_plaintext().split(" ")
    # 判断语法是否正确
    if len(msg_spilt) == 2:
        # 获取服务器信息
        server_num = msg_spilt[1]
        row_id = tools.get_server_row_id(int(server_num))
        if row_id == "Error":
            await world_info.finish("服务器不存在")
        else:
            url = f"https://lobby-{config.REGION}.klei.com/lobby/read"
            data = {
                '__gameId': 'DontStarveTogether',
                '__token': config.LOBBY_TOKEN,
                'query': {
                    '__rowId': row_id
                }
            }
            data = json.dumps(data)
            response = requests.post(url, data=data)
            # 判断请求结果
            if response.status_code == 200:
                server_info = response.json()['GET']
                # 判断服务器是否存在
                if len(response.json()["GET"]) == 0:
                    await world_info.finish("服务器不存在")
                else:
                    # 索引服务器信息

                    # 服务器名称
                    server_name = server_info[0]['name']
                    # 服务器模式
                    server_mode = server_info[0]['mode']
                    # 服务器季节
                    server_season = server_info[0]['season']
                    # 服务器数据
                    server_data = server_info[0]['data']
                    # 服务器天数
                    server_day = re.findall(r"day=(.*?),", server_data)[0]
                    # 服务器季节过去的天数
                    server_days_elapsed = re.findall(r"dayselapsedinseason=(.*?),", server_data)[0]
                    # 服务器季节剩余的天数
                    server_days_leftin = re.findall(r"daysleftinseason=(.*?) ", server_data)[0]


                    # 当前时间
                    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # 发送消息
                    await world_info.finish(f"{server_name}\n"
                                            f"模式：{server_mode}\n"
                                            f"天数：{server_day}\n"
                                            f"季节：{server_season}\n"
                                            f"{server_season}已过去：{server_days_elapsed} 天\n"
                                            f"{server_season}还剩下：{server_days_leftin} 天\n"
                                            f"\n数据更新于：{now_time}")
            else:
                await world_info.finish(event, "服务器信息获取失败")
    # 语法错误
    else:
        await world_info.finish("请输入正确的格式：\n"
                           "世界信息 [世界序号]")


# 在线玩家
online_player = on_command('在线玩家')


@online_player.handle()
async def online_player_handle(event: Event, bot:Bot):
    msg_spilt = event.get_plaintext().split(" ")
    # 判断语法是否正确
    if len(msg_spilt) == 2:
        # 获取服务器信息
        server_num = msg_spilt[1]
        row_id = tools.get_server_row_id(int(server_num))
        if row_id == "Error":
            await online_player.finish("服务器不存在")
        else:
            url = f"https://lobby-{config.REGION}.klei.com/lobby/read"
            data = {
                '__gameId': 'DontStarveTogether',
                '__token': config.LOBBY_TOKEN,
                'query': {
                    '__rowId': row_id
                }
            }
            data = json.dumps(data)
            response = requests.post(url, data=data)
            # 判断请求结果
            if response.status_code == 200:
                server_info = response.json()['GET']
                # 判断服务器是否存在
                if len(response.json()["GET"]) == 0:
                    await online_player.finish("服务器不存在")
                else:
                    # 索引服务器信息

                    # 在线玩家
                    server_players_list = server_info[0]['players']
                    # 最大连接数
                    max_connections = server_info[0]['maxconnections']
                    # 连接数
                    connected = server_info[0]['connected']
                    # 房间昵称
                    name = server_info[0]['name']

                    # 处理返回的lua数组 转换成列表
                    server_players_list = server_players_list.replace("\n", "").replace("return ", "").replace("{",'[').replace(
                        "}", "]").replace(" ", "").replace("[[", '[{"').replace("]]", '"}]').replace("=", '"=').replace(
                        ",", ',"').replace('],"[', '},["').replace('""', '"').replace('},[', '},{').replace('=', ':')
                    server_players_list = json.loads(server_players_list)
                    send_data = []
                    for i in server_players_list:
                        send_data.append(f" {i['name']} ({i['prefab']})")

                    await online_player.finish(f'{name}\n在线玩家({str(connected)}/{str(max_connections)})：\n' + "\n".join(send_data))

            else:
                await world_info.finish(event, "服务器信息获取失败")
    # 语法错误
    else:
        await world_info.finish("请输入正确的格式：\n"
                                "世界信息 [世界序号]")
