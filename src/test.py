import requests
import pytest



@pytest.fixture
def result():
	url='http://127.0.0.1:5000/video/100'
	r = requests.get(url)
	return r


def test_ini(result):
	assert result.status_code == requests.codes.ok

def test_defaut(result):
	r=result.json()
	assert r["name"]=="How to be productive"
	assert r['views']==10000
	assert r['likes']==1000

