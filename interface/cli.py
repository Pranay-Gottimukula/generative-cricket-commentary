from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

'''
    CLI Interface using argparse

    Example command: python3 main --input [input_path] --output [output_path]
    Default output is /data/output

'''

def run_cli():
    parser.add_argument("--input",
                        type=str,
                        required=True,
                        help="Path to the input file containing cricket match data."
                    )
    
    parser.add_argument("--output",
                        type=str,
                        default="generative-cricket-commentary/data/output",
                        help="Path to the output file where the commentary will be saved."
                    )

    args: Namespace = parser.parse_args()
    
    return args


