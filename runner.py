import os

from behave.__main__ import main as behave_main

if __name__ == "__main__":
    features_path = os.path.join(os.getcwd(), "features")
    print(features_path)
    tags = os.getenv("TAGS", "@to-be-provided")
    #tags = os.getenv("TAGS", "@element")
    print(f"{tags} executed")
    behave_args = [
        features_path,
        '-t', tags
         # , '--format', 'behave_html_formatter:HTMLFormatter'
         # , '--out', 'reports/behave_report.html'
         # , '--no-skipped'
         # , '--no-capture'
         # , '-f', 'plain'
     ]

    # Execute Behave
    exit_code = behave_main(behave_args)

    # You can add custom logic here based on the exit_code
    if exit_code != 0:
        print("Behave tests failed!")
    else:
        print("Behave tests passed successfully.")