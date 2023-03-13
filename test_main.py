from main import cube

def TestCube():
    assert cube(1) == 1
    assert cube(2) == 8
    print("the cube function is Tested Successfully")

if __name__ == "__main__":
    TestCube()