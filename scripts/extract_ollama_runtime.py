"""Optional Kaggle helper: extract a checksum-verified official zstd runtime.

The notebook verifies the release digest before invoking this command. Requires
zstandard in the isolated notebook environment, not the core application.
"""
import argparse
from pathlib import Path
import tarfile


def main():
    import zstandard
    parser=argparse.ArgumentParser()
    parser.add_argument('archive',type=Path);parser.add_argument('target',type=Path)
    args=parser.parse_args();args.target.mkdir(parents=True,exist_ok=True)
    with args.archive.open('rb') as stream, zstandard.ZstdDecompressor().stream_reader(stream) as reader:
        with tarfile.open(fileobj=reader,mode='r|') as tar:
            tar.extractall(args.target,filter='data')


if __name__=='__main__':main()
