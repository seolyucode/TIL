REST

Representational State Transfer

자원을 이름으로 구분하여 해당 자원의 상태를 주고 받는 모든 것. 상태를 전달하는 것.

웹의 기존 기술과 HTTP 프로토콜을 그대로 활용

CRUD Operation

* Create
* Read
* Update
* Delete
* Head



```python
import requests
import json

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url = 'http://...'
data = {'data1': '이설유', 'data2': '1'}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(json.loads(r.text))
```

