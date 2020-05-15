"""Main module."""

import argparse
import os
import sys

from monitor.consumer_example import consumer_example
from monitor.producer_example import producer_example


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--service-uri',
                        help="Service URI in the form host:port",
                        required=True)
    parser.add_argument('--ca-path',
                        help="Path to project CA certificate",
                        required=True)
    parser.add_argument('--key-path',
                        help="Path to the Kafka Access Key",
                        required=True)
    parser.add_argument('--cert-path',
                        help="Path to the Kafka Certificate Key",
                        required=True)
    parser.add_argument('--consumer', action='store_true',
                        default=False, help="Run Kafka consumer example")
    parser.add_argument('--producer', action='store_true',
                        default=False, help="Run Kafka producer example")
    args = parser.parse_args()
    validate_args(args)

    kwargs = {
        k: v for k, v in vars(args).items() if k not in ("producer", "consumer")
    }

    if args.producer:
        producer_example(**kwargs)
    elif args.consumer:
        consumer_example(**kwargs)


def validate_args(args):
    for path_option in ("ca_path", "key_path", "cert_path"):
        path = getattr(args, path_option)
        if not os.path.isfile(path):
            path1 = path_option.replace('_', '-')
            fail(f"Failed to open --{path1} at path: {path}.\n"
                 f"You can retrieve these details from Aiven Console")

    if args.producer and args.consumer:
        fail("--producer and --consumer are mutually exclusive")
    elif not args.producer and not args.consumer:
        fail("--producer or --consumer are required")


def fail(message):
    print(message, file=sys.stderr)
    exit(1)


if __name__ == '__main__':
    main()
