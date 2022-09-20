# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1
    print('#1')
    import json
    json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
    py_obj = json.loads(json_obj)
    print(py_obj)
    # 2
    print('#3')
    import json

    python_obj = {
        "name": "David",
        "class": "I",
        "age": 6}
    json_obj2 = json.dumps(python_obj, indent=4)
    print(json_obj2)

    # 4
    print('#4')
    import json
    py_dic = {'4': 5, '6': 7, '1': 3, '2': 4}
    json_obj3 = json.dumps(py_dic, indent=4, sort_keys=True)
    print(json_obj3)
    # 5
    print('#5')
    import json

    json_obj_dict = '{"name": "David", "age": 6, "class": "I"}'
    json_obj_list = '["Red", "Green", "Black"]'
    json_obj_string = '"Python Json"'
    json_obj_int = '1234'
    json_obj_float = '21.34'

    dict1 = dict(
                    py_obj_dict=json.loads(json_obj_dict),
                    py_obj_list=json.loads(json_obj_list),
                    py_obj_string=json.loads(json_obj_string),
                    py_obj_int=json.loads(json_obj_int),
                    py_obj_float=json.loads(json_obj_float))
    print(dict1)

    # 4
    print('#4')

