import json
import requests


def post_api():
    sid_test = json.loads('{"sid":"1000", "state":"已完成"}')  # json.loads 将字符串转化为字典 json.dumps
    sid_headers = {'content-type': 'application/json'}
    url1 = ' http://172.28.151.235:5000/test/api'

    print(sid_test)
    print(sid_headers)
    print(url1)

    response = requests.post(url1, headers=sid_headers, data=sid_test)
    res = response.text
    print(res)
    # print(json.dumps(res))

    return res


if __name__ == '__main__':
    text = post_api()
    print(text)

