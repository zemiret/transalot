import os
import json
import shutil


def translate(mapping_filepath, in_dir=os.path.realpath('.'), out_dir=os.path.realpath('out')):
    mapping, reverse_mapping = _create_mapping(os.path.realpath(mapping_filepath))
    _clear_output_dir(out_dir)
    _translate_top_dir(reverse_mapping, in_dir, out_dir)


def _create_mapping(mapping_filepath):
    map_file = None
    try:
        map_file = open(os.path.realpath(mapping_filepath))
        mapping = json.load(map_file)
        reverse_mapping = {(v, k) for k, v in mapping.items()}

        return mapping, reverse_mapping
    finally:
        if map_file is not None:
            map_file.close()


def _clear_output_dir(out_dir_path):
    if os.path.exists(out_dir_path):
        shutil.rmtree(out_dir_path)
    os.mkdir(out_dir_path)


def _translate_top_dir(mapping, in_filepath, out_filepath):
    _assert_correct_input_dir(in_filepath)
    for file in os.listdir(in_filepath):
        translation_in_filepath = os.path.join(in_filepath, file)
        translation_out_filepath = os.path.join(out_filepath, file)
        _scan_and_translate_files(mapping, translation_in_filepath, translation_out_filepath)


def _assert_correct_input_dir(in_filepath):
    if not os.path.exists(in_filepath):
        raise RuntimeError("Input directory does not exist.")
    if not os.path.isdir(in_filepath):
        raise RuntimeError("Input is not a directory.")


def _scan_and_translate_files(mapping, in_filepath, out_filepath):
    if not os.path.exists(in_filepath):
        return

    if os.path.isdir(in_filepath):
        _translate_directory(mapping, in_filepath, out_filepath)
    else:
        _translate_file(mapping, in_filepath, out_filepath)


def _translate_directory(mapping, in_filepath, out_filepath):
    os.mkdir(out_filepath)
    for file in os.listdir(in_filepath):
        translation_in_filepath = os.path.join(in_filepath, file)
        translation_out_filepath = os.path.join(out_filepath, file)
        _scan_and_translate_files(mapping, translation_in_filepath, translation_out_filepath)


def _translate_file(mapping, in_filepath, out_filepath):
    in_file = None
    out_file = None
    try:
        in_file = open(in_filepath)
        out_file = open(out_filepath, 'w+')
        content = in_file.read()
        for to_replace, replacement in mapping:
            content = content.replace(to_replace, replacement)

        out_file.write(content)
    finally:
        if in_file is not None:
            in_file.close()
        if out_file is not None:
            out_file.close()
