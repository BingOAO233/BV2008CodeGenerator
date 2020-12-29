import csv
import json


class csvReader:
    def __init__(self):
        self._csvFile = None
        pass

    def open(self, path: str):
        result = []
        with open(file=path, encoding='utf-8-sig') as f:
            self._csvFile = csv.reader(f)
            for row in self._csvFile:
                result.append(row)
        return result[0], result[1:]


def object_convert(attr_names: list, data_list: list):
    obj_arr = []
    for data in data_list:
        obj = {}
        for i in range(0, len(attr_names)):
            obj[attr_names[i]] = data[i]
        obj_arr.append(obj)
        print(obj)
    return obj_arr


def json_stringify(obj):
    return json.dumps(obj, ensure_ascii=False)


def app(session: int):
    reader = csvReader()
    headers, data = reader.open('rawData/{}/rawListS.csv'.format(session))
    obj_list = object_convert(headers, data)
    with open('./pList-{}.json'.format(session), 'w') as f:
        f.write(json_stringify(obj_list))


if __name__ == '__main__':
    app(15)
