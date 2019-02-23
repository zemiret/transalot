import json
import os
import sys

from translator import translate
import argparse


def _create_parser_with_options():
    convert_str_to_path = (lambda str_path: os.path.realpath(str_path))

    parser = argparse.ArgumentParser()

    parser.add_argument('--input', '-i',
                        required=True,
                        type=convert_str_to_path,
                        help='Input directory or file to be translated.')
    parser.add_argument('--output', '-o',
                        type=convert_str_to_path,
                        required=True,
                        help='Output directory or file name.')
    parser.add_argument('--map', '-m',
                        required=True,
                        type=convert_str_to_path,
                        help='Mapping that you want to use for your language.')

    return parser


def _get_paths_from_arguments(parser):
    parsed_arguments = parser.parse_args()

    input_filepath = parsed_arguments.input
    output_filepath = parsed_arguments.output
    mapping_filepath = parsed_arguments.map

    return input_filepath, output_filepath, mapping_filepath


def main():
    parser = _create_parser_with_options()

    if len(sys.argv) == 1:
        parser.print_usage()
    else:
        in_filepath, out_filepath, mapping_filepath = _get_paths_from_arguments(parser)
        translate(mapping_filepath, in_filepath, out_filepath)


if __name__ == "__main__":
    main()
