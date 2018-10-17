import json
import os
import hashlib
import types


# Class for running init scripts
class Main:
    # Save objects for calling function or value
    objects = {}

    def __init__(self, *args, **kwargs):
        # Brute force arguments for calling func or save objects in dictionary self.objects
        for arg in args:
            # Function
            if isinstance(arg, types.MethodType) or isinstance(arg, types.FunctionType):
                arg()
            # Object
            if str(type(arg)) == "<class 'type'>":
                self.objects[arg.__name__] = arg()


class BlockChain:
    # Absolute path
    dir_path = os.curdir + '/blockchain/'
    # Relative path
    static_path = '/blockchain/'

    def __init__(self):
        pass

    # Getting hash from data in file
    def get_hash(self, filename):
        try:
            file = open(self.dir_path + filename, 'rb').read()
            return hashlib.md5(file).hexdigest()
        except:
            print("Not found " + filename)
            return False

    # Getting index and path last file from folder /blockchain/
    def get_last_files(self):
        last_index = os.listdir(self.dir_path).__len__()
        path = self.dir_path + str(last_index)
        return {
            "index": last_index,
            "path": path
        }

    # Reading hash the previous one block
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

    # Create new binary file in folder /blockchain/
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

    def audit_name_blocks_asc(self):
        blockes = os.listdir(self.dir_path)
        blockes = sorted(blockes, key=lambda elem: int(elem))

        count_blockes = len(blockes)

        for item in blockes:
            if int(item) + 1 == int(count_blockes):
                break

            # self-block hash
            actual_hash = self.get_hash(item)

            # next-block hash
            file = open(self.dir_path + str(int(item) + 1))
            next_hash = json.load(file)['hash']

            results = {}
            if next_hash == actual_hash:
                results["success"] = True
                results["self-block"] = item
                results["next-block"] = int(item) + 1
            else:
                results["success"] = False
                results["self-block"] = item
                results["next-block"] = int(item) + 1
            print(results)

    def audit_name_blocks_desc(self):
        blockes = os.listdir(self.dir_path)
        blockes = sorted(blockes, reverse=True, key=lambda elem: int(elem))

        count_blockes = len(blockes)
        i = 0
        for item in blockes:
            i+=1
            if i == int(count_blockes):
                break

            # self-block hash
            actual_hash = self.get_hash(item)

            # next-block hash
            file = open(self.dir_path + str(int(item) - 1))
            next_hash = json.load(file)['hash']

            results = {}
            if next_hash == actual_hash:
                results["success"] = True
                results["self-block"] = item
                results["next-block"] = int(item) + 1
            else:
                results["success"] = False
                results["self-block"] = item
                results["next-block"] = int(item) + 1
            print(results)
