import os, sys
import argparse
from .gerty import Gerty


def valid_path(path: str):
    if os.path.exists(path):
        return path
    raise argparse.ArgumentTypeError(f"Path does not exist: {path}")


def run():
    parser = argparse.ArgumentParser(
        prog="a llama2 application",
        description="A simple script to run through a particular knowledge base and embed all data into a db",
    )
    parser.add_argument(
        "knowledge_base",
        nargs="+",
        type=str,
        help="A directory containing text files for the knowledge-base",
    )
    parser.add_argument(
        "--url", action="store_true", help="Knowledge_base given is a url"
    )
    parser.add_argument(
        "-c", "--cache", type=valid_path, help="Cache knowledge base to this file"
    )
    parser.add_argument(
        "--context-length",
        type=int,
        default=4096,
        help="Context length to load the LLama embedding model with",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=1000,
        help="Chunk size for the embedded knowledge",
    )

    args = parser.parse_args()

    gerty = Gerty(
        n_ctx=args.context_length,
    )

    if args.url:
        gerty.embed_db(
            args.knowledge_base, args.cache, url=args.url, chunksize=args.chunk_size
        )
    else:
        gerty.embed_db(
            args.knowledge_base,
            args.cache,
            url=args.url,
            chunksize=args.chunk_size,
            glob="*.txt",
        )

    return


if __name__ == "__main__":
    run()
