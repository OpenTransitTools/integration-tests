import os
import argparse


def make_parser(prog_name='scripts/browserstack/gen.py', do_parse=True):
    """
    create a commandline arg PARSER for creating browserstack .cap files
    """
    parser = argparse.ArgumentParser(
        prog=prog_name,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-landscape", "--landscape", "--l", "-l",
        help="produce landscape cap files",
        action="store_true"
    )

    parser.add_argument("-number_caps", "--num", "--n", "-n",
        help="limit the number of cap files to this number",
        action="store_true"
    )

    def_caps_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'caps')
    parser.add_argument("-caps_dir", "--dir", "--d", "-d",
        default=def_caps_dir,
        help="directory to store the generated .caps files"
    )

    parser.add_argument("-devices", "--csv", "--c", "-c",
        default="devices.csv",
        help=".csv file listing the browserstack devices, from which we'll create .cap files"
    )

    parser.add_argument("-browserstack_key", "--key", "--k", "-k",
        required=True,
        help="provide the uname:password 'ACCESS KEY' from BrowserStack's automate (see README.md)"
    )

    ret_val = parser.parse_args() if do_parse else parser
    return ret_val
