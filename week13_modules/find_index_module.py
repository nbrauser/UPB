if __name__ == '__main__':
    print("Imported find index module")
    print('Running find index module : ', __name__)
    test_str = "Test String"


def find_index(search_list, target):
    for idx, val in enumerate(search_list):
        #  print(idx, val)
        if val == target:
            return idx
    return -1


#  print(find_index(['Apple', 'Orange', 'Kiwi'], 'Kiwi'))
