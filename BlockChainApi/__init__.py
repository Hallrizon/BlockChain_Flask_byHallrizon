import json
import os
import hashlib
import types


class Main:
    objects = {}

    def __init__(self, *args, **kwargs):

        for arg in args:
            if isinstance(arg, types.MethodType) or isinstance(arg, types.FunctionType):
                arg()

            if str(type(arg)) == "<class 'type'>":
                self.objects[arg.__name__] = arg()

            # if str(arg) == "<class 'BlockChainApi.BlockChain'>":
            #  self.BlockChain = arg()


class BlockChain:
    dir_path = os.curdir + '/blockchain/'
    static_path = '/blockchain/'

    def __init__(self):
        print("--__--")

    def get_hash(self, filename):
        try:
            file = open(self.dir_path + filename, 'rb').read()
        except:
            print("Not found " + filename)
            return False

        return hashlib.md5(file).hexdigest()

    def get_last_files(self):
        last_index = os.listdir(self.dir_path).__len__()
        path = self.dir_path + str(last_index)
        return {
            "index": last_index,
            "path": path
        }

    # reading hash the previous one block  from end to start
    def check_integrity(self):
        last_block = self.get_last_files()
        last_block_index = last_block['index']

        result = []
        while last_block_index != 1:
            file = open(self.dir_path + str(last_block_index))
            hash_block = json.load(file)['hash']

            prev_file = str(last_block_index - 1)
            actual_hash = self.get_hash(prev_file)

            if hash_block == actual_hash:
                print('Block ' + str(last_block_index) + ' has right hash -> block:' + str(prev_file) + " = Okay")
                res = "true"
            else:
                print(print('Block ' + str(last_block_index) + ' has right hash -> block:' + str(prev_file) + " = Bad"))
                res = "false"

            result.append({'block': prev_file, 'result': res})
            last_block_index -= 1
        return result

    def write_block(self, name, amount, to_whom):

        name_last_block = self.get_last_files()
        name_last_block = name_last_block['index']

        file_path = str(self.dir_path) + str(name_last_block + 1)

        prev_hash = self.get_hash(str(name_last_block))

        data = {
            'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash,
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
