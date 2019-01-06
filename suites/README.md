### test framework based on pytest
- use develop as main branch


### how to run it
- pytest -s -v
- pytest --html=./result.html
- pytest -v -m webtest
- pytest -v -m "not webtest"
- pytest -v test_server.py::TestClass
- pytest -v test_server.py::TestClass test_server.py::test_send_http
- pytest -v -k http
- pytest -k "not send_http" -v
- pytest -k "http or quick" -v


