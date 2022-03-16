import os
import argparse


def make_parser(prog_name='scripts/browserstack/gen.py', do_parse=True):
    """
    create a commandline arg PARSER for creating browserstack .cap files
    """

    # default output (caps) directory -and- default devices.csv path
    this_dir = os.path.dirname(os.path.abspath(__file__))
    def_caps_dir = os.path.join(this_dir, 'caps')
    def_devices_csv = os.path.join(this_dir, 'devices.csv')

    parser = argparse.ArgumentParser(
        prog=prog_name,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("--landscape", "--landscape", "--l", "-l",
        help="produce landscape cap files",
        action="store_true"
    )

    parser.add_argument("--number", "--num", "--n", "-n",
        default=111111111,
        help="limit the number of cap files (or urls) to this number"
    )

    parser.add_argument("--urls", "--u", "-u",
        help="print browserstack URL to these devices",
        action="store_true"        
    )

    parser.add_argument("--baseline", "--b", "-b",
        help="print browserstack URL to these devices",
        action="store_true"        
    )

    parser.add_argument("--caps_dir", "--dir", "--d", "-d",
        default=def_caps_dir,
        help="directory to store the generated .caps files"
    )

    parser.add_argument("--devices_csv", "--csv", "--c", "-c",
        default=def_devices_csv,
        help=".csv file path listing the browserstack devices, from which we'll create .cap files"
    )

    parser.add_argument("--os_filter", "--of", "-of", "-o",
        nargs="*",
        help="OS filter [iOS, OS-X, andriod, windows]"
    )

    parser.add_argument("--browser_filter", "--bf", "-bf",
        nargs="*",
        help="BROWSER filter [firefox, chrome, safari, opera]"
    )

    parser.add_argument("--browserstack_key", "--key", "--k", "-k",
        required=True,
        help="provide the uname:password 'ACCESS KEY' from BrowserStack's automate (see README.md)"
    )

    ret_val = parser.parse_args() if do_parse else parser
    return ret_val
