import argparse

parser = argparse.ArgumentParser(description='Keine Description')

parser.add_argument('--dir',
                    metavar='path',
                    type=str,
                    help='',
                    required=True)

parser.add_argument('--plaform',
                    metavar='path',
                    type=str,
                    help='',
                    required=True)

args = parser.parse_args()

pub_dir = args.dir
platform = args.platform

print(pub_dir, platform)
