from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(5,5) == 10
        assert Add(10,20) == 30
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()
