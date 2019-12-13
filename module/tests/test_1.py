import sys
import os

from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from module_a.mod_a import mod_a1, mod_a2
import pytest
import json
import requests

# !pip install pytest-env


print(os.environ['APP_HOST'])

# @pytest.mark.parametrize("num, output",[(1,1),(2,1),(3,2),(4,0)])
# def test_div(num, output):
#     assert mod_a1(num) % 3 == output

# def test_div1():
#     assert mod_a1(20) % 6 == 0

def test_mod2():
    # os.environ["APP_HOST"] = "local"
    assert mod_a2() == "local"

def test_mod21():
    os.environ["APP_HOST"] = "local1"
    assert mod_a2() == "local1"


# def test_request_comp_search():
#     data = {
#         "some": "data"
#         }
#     r = requests.post(url, data=json.dumps(data), headers={'content-type': 'application/json'})
#     # assert is_successful(r)
#     data = r.json()
#     assert r.status_code == 200