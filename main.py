class SimpleList:
    def __init__(self, simple_list=[1, 6, 9, 4, 2, 1, 9, 15]):
        self.simple_list = simple_list

    def test_list(self):
        print("It's really all right!")


if __name__ == "__main__":
    test_list_object = SimpleList()
    test_list_object.test_list()
