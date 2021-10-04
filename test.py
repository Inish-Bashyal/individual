import pytest
@pytest.fixture()
def tester():
    Username ="ADMIN" or "INISH"
    password="ADMIN"
    return [Username,password]
def testing_1(tester):
    Username=""
    assert (tester[0] or tester[1])==Username
def testing_2(tester):
    Username="ADMIN"
    assert tester[0] or tester[1]==Username
def testing_3(tester):
    Username="INISH"
    assert tester[1] or tester[1]==Username
def testing_4(tester):
    password='ADMIN'
    assert tester[1]==password
def testing_5(tester):
    password='asdfgh'
    assert tester[1]==password
def testing_6(tester):
    password=''
    assert tester[1]==password