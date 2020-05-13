"""
Enables the command line execution of multiple modules within src/
This module combines the argparsing of each module within src/ and enables the execution of the corresponding scripts
so that all module imports can be absolute with respect to the main project directory.
To understand different arguments, run `python run.py --help`
"""
import os
import argparse
import logging
import logging.config
import yaml

with open(os.path.join("config", "config.yml"), "r") as f:
    config = yaml.safe_load(f)

# The logging configurations are called from local.conf
logging.config.fileConfig(os.path.join("config", "local.conf"))
logger = logging.getLogger(config['logging']['LOGGER_NAME'])

from src.load_data import load_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run components of the run source code")
    subparsers = parser.add_subparsers()

    # Sub-parser for downloading the raw data
    sb_fetch = subparsers.add_parser("load_data", description="Fetch the raw data from the source")
    sb_fetch.add_argument("--where", default="Upload",
                          help="'Upload' or 'AWS'; The destination bucket name needs to be provided in case of AWS")
    sb_fetch.add_argument("--bucket", default="None", help="Destination S3 bucket name")
    sb_fetch.set_defaults(func=load_data)



    args = parser.parse_args()
    args.func(args)