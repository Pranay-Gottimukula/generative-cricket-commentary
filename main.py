from interface.cli import run_cli
from scripts.pipeline_runner import run_pipeline

'''
    Entry point of Interface
    Collects Input path and sends it through pipeline
'''

if __name__ == "__main__":
    args = run_cli()
    run_pipeline(input_path=args.input, output_path=args.output)
