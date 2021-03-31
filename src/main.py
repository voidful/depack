import argparse
import sys
import nlp2
import patoolib
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", type=str, help="create archive file")
    parser.add_argument("--file", type=str, nargs='+', help="decompress archive files")

    input_arg, others_arg = parser.parse_known_args(args)
    input_arg = {k: v for k, v in vars(input_arg).items() if v is not None}
    return input_arg, others_arg


def main(arg=None):
    arg, others_arg = parse_args(sys.argv[1:]) if arg is None else parse_args(arg)
    if arg.get('create', None):
        archive_file = arg.get('create')
        filenames = others_arg
        patoolib.create_archive(archive=archive_file, filenames=filenames, verbosity=-1)
    elif arg.get('file', None) or len(others_arg) > 0:
        extract_list = arg.get('file', []) + others_arg
        for path in extract_list:
            if nlp2.is_file_exist(path):
                parent_dir = Path(path).parent.absolute()
                patoolib.extract_archive(path, outdir=parent_dir, verbosity=-1)
    print("Finish")

if __name__ == "__main__":
    main()
