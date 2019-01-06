# aitp

### 安装
- pip install -r requirements.txt
- (来自 pip freeze > requirements.txt)

### 运行
-  pytest -s -q --alluredir ./reports/xml
- allure generate ./reports/xml -o ./reports/html