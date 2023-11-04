import requests as rq


def test():
    result = rq.post("http://127.0.0.1:8000/api/v1/analysis",
                     json={"url": "https://www.alibaba.com", "rules": ["linking", "img-alt-text"]})
    print('result', result)


if __name__ == "__main__":
    test()
