from src.math_operations import add,sub


def test_add():
    assert add(2,3) == 5
    assert add(4,5) == 9
    assert add(-1,1) == 0
    
def test_sub():
    assert sub(5,4) == 1
    assert sub(10,8) == 2
    assert sub(-1,-2) == 1