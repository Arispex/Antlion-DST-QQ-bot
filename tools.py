import json
import config
import requests


def get_server_info(num: int):
    """
    Get server info
    """
    # 读取服务器配置文件
    with open(f"server.json", "r") as f:
        data = json.load(f)
    if num <= len(data):
        return data[str(num)]
    else:
        return "Error"


def get_server_row_id(num: int) -> str:
    """
    Get server row id
    """
    # 获取ip port
    server_info = get_server_info(num)
    if server_info == "Error":
        return "Error"
    else:
        ip = server_info["ip"]
        port = server_info["port"]

        # 获取row id
        url = f"https://lobby-cdn.klei.com/{config.REGION}-Steam-{config.EVENT}.json.gz"
        response = requests.get(url)
        if response.status_code == 200:
            for row in response.json()["GET"]:
                if row["__addr"] == ip and row["port"] == int(port):
                    return row["__rowId"]
        else:
            return "Error"