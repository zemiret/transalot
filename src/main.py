import json
import os
from translator import translate


def test():
    map_file = None
    out_file = None
    in_file = None
    try:
        map_file = open(os.path.realpath('src/mappings/lotrPython.json'))
        in_file = open(os.path.realpath('playground/lotrpy.py'))
        out_file = open(os.path.realpath('out/out.py'), 'w+')

        mapping = json.load(map_file)
        reverse_mapping = {(v, k) for k, v in mapping.items()}

        content = in_file.read()
        for k, v in reverse_mapping:
            content = content.replace(k, v)

        out_file.write(content)

    finally:
        map_file.close()
        out_file.close()
        in_file.close()


def main():
    mapping_filepath = os.path.realpath('src/mappings/lotrPython.json')
    in_dir_path = os.path.realpath('playground')
    out_dir_path = os.path.realpath('out')
    translate(mapping_filepath, in_dir_path, out_dir_path)


if __name__ == "__main__":
    main()
