import argparse
import json
import os
import sys
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("-k", '--key', help='the key v')
parser.add_argument("-v", '--val', help='the val v')

args = parser.parse_args()
key = args.key
value = args.val

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
text = os.path.join('.', 'text.json')


def write_to_json(k, v):
    with open(storage_path, 'r+') as file:
        if file.read() == '':
            json.dump({k: v}, file)
            return
        file.seek(0)
        jf_file = json.load(file)
    with open(storage_path, 'w') as file:
        jf_target = jf_file
        if k in jf_target:
            v_old = jf_target[k]
            if type(v_old) == list:
                v_old.append(v)
                jf_target[k] = v_old
            else:
                jf_target[k] = [v_old, v]
        else:
            jf_target[k] = v
        json.dump(jf_file, file, indent=4)


if args.key is None:
    print('Enter a key!')
    sys.exit(-1)
elif args.val:
    write_to_json(key, value)
    print(f'Value "{value}" has been added to storage with key "{key}".')
else:
    with open(storage_path, 'r') as f:
        if f.read() == '':
            print('Storage is empty!')
            sys.exit(-1)
        f.seek(0)
        storage = json.load(f)
        if key not in storage:
            print('There is no such a key!')
            sys.exit(0)
        val = storage[key]
        if type(val) == list:
            print(', '.join(val))
        else:
            print(val)
