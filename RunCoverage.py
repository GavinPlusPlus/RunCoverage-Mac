# RunCoverage.py
# This script is designed to speed up the code coverage process of VS for Mac
# by running all needed commands and automatically opening your coverage results
# in the default browser of your system.
#
# Version 1.0
# Written by: Gavin Kerr (GavinPlusPlus)

import subprocess
import os

print("================================")
print("=        RunCoverage.py        =")
print("=    Written by: Gavin Kerr    =")
print("=         Version 1.0          =")
print("================================")

# Get File Path
project_dir = input("Relative File Path To The Test Project (Ex: Spreadsheet/FormulaTests): ")
complete_dir = os.path.dirname(os.path.realpath(__file__))
complete_dir = complete_dir + "/" + project_dir
os.chdir(complete_dir)

# Run Test
print(f"\nRunning tests on {complete_dir}")

# Capture Results
test_results = subprocess.run(['dotnet', 'test', '--collect:"XPlat Code Coverage"'], stdout=subprocess.PIPE).stdout.decode('utf-8')
split_results = test_results.split('\n')

# Iterate through until finding Attachments
found_attachments = False
result_xml = ""

for s in split_results:
    if (s.find("Attachments:") != -1):
        found_attachments = True
        continue
    if (found_attachments):
        result_xml = s.strip()
        break

# Run Report
print("Generating report...")
run_report = subprocess.run(['reportgenerator', f'-reports:{result_xml}', '-targetdir:TestResults'], stdout=subprocess.DEVNULL)

# Open Results
subprocess.run(['open', f'{complete_dir}/TestResults/index.htm'], stdout=subprocess.DEVNULL)
print("\nDone! Thanks!")
