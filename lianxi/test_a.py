import pytest

def func(x):
    return x + 1
@pytest.mark.parametrize('a,b',[(10,20),(20,30),(30,40),(3,4),(5,6)])
def test_answer(a,b):
    assert func(a) == b
if __name__ == "_main_":
    pytest.main(["test_a.py"])
