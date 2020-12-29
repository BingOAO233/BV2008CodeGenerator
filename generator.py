# generator.py
# this is a python script used to auto generate bv2008 code
# to use this please copy UID into input/*.in
import glob
import json


def json_load(path: str):
    with open(path, encoding='gbk') as f:
        return json.load(f)


def main():
    with open(glob.glob(r'./input/*.in')[0], encoding='utf-8') as f:
        names = f.read()
        names = names.split('\n')
        # print(names)
    config = json_load('./config.json')
    member_list = json_load('./storage/pList-{}.json'.format(config['session']))
    # print(config)

    member_dic = {}
    for member in member_list:
        member_dic[member['name']] = member

    with open('./output/out.txt', 'w', encoding='utf-8') as f:
        i = 0
        # print(member_dic.keys())
        for name in names:
            # print(name)
            if name in member_dic.keys():
                if member_dic[name]['UID'] == '':
                    continue
                print(str(i) + ':' + name)
                i += 1
                f.write('{},{},{},{}\n'.format(name, member_dic[name]['UID'], config['time'], config['info']))


if __name__ == '__main__':
    main()
