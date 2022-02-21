# 参数面板 不传可以使用参数面版默认值
import json
import requests

appParams = {
    "test1": "456"
}

# 任务信息
taskInfo = {
    "appName": "差旅报销RPA",  # 流程名称
    "appVersion": "1.0.0",  # 流程版本号
    "robotIds": "064acbb2-a889-413b-92ed-112092fa4b79",  # 机器人Ids
    "taskName": "test_trip1",  # 任务名称可以随便取
    "appParams": json.dumps(appParams),  # 参数
}


def create_task(server, key_secret, taskInfo):
    """
    初始化函数。:p aram server: 服务器 例如 http://localhost http://localhost:8080
    :p aram key_secret: 私钥 见个个中心
    :p aram taskInfo: 任务信息
    :return resp: 请求返回 可以判断status_code是不是等于200

    """
    headers = {"X-Referer": "Console", "X-KeySecret": key_secret}
    resp = requests.post(server + "/v1/api/serviceTask", headers=headers, data=json.dumps(taskInfo))
    return resp


print(create_task("http://172.28.97.37:80", "d80f6672-84d5-41c1-abbd-7f97e847c1ec", taskInfo))
