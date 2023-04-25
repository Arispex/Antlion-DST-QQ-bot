# ⚠️该项目已废弃

如果你正在寻找类似的项目，不妨看看[这个](https://github.com/Qianyiovo/DontStarveTogetherBot)。

# Antlion-DST-QQ-bot

Don't Starve Together(饥荒联机版)QQ机器人
无需任何服务端模组访问服务器数据

基于*NoneBot2*(https://github.com/nonebot/nonebot2)

## 工作原理

访问Klei lobby listings file(大厅列表文件)获取服务器数据

## 命令

+ 添加服务器 [IP] [Port] - 添加新服务器
+ 清空服务器 - 清空已添加的所有服务器

+ 世界信息 [服务器序号] - 获取服务器基础世界信息（比如：天数，季节，房间名称...)
+ 在线玩家 [服务器序号] - 获取服务器在线玩家
+ 敬请期待...

## 配置

### config.py

+ LOBBY_TOKEN - 大厅列表文件访问令牌(向Klei员工索要)
+ REGION - 服务器地区(Sing, US, EU, China)

+ EVENT -  服务器事件(noevent)

## 环境

*Python*  >=  3.7.3

库：

+ nonebot2

+ requests

## 安装

......

NoneBot2 Document: See [Docs](https://v2.nonebot.dev/)

## 已知问题

+ 回复消息过于缓慢

这是国内的网络导致的，机器人需要请求两次Klei's API

解决办法：

代理
