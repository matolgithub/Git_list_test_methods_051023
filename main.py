class SimpleList:
    def __init__(self, simple_list=[1, 6, 9, 4, 2, 1, 9, 15]):
        self.simple_list = simple_list

    def test_list(self):
        self.simple_list.reverse()
        print(f"The reverse list is: {self.simple_list}")

        self.simple_list.sort(reverse=True)
        print(self.simple_list)

        self.simple_list.sort()
        print(self.simple_list)

        value_index_4 = self.simple_list.pop(4)
        print(self.simple_list)
        print(value_index_4)

        max_value = max(self.simple_list)
        print(max_value)


if __name__ == "__main__":
    test_list_object = SimpleList()
    test_list_object.test_list()
