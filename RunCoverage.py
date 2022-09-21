# RunCoverage.py
# This script is designed to speed up the code coverage process of VS for Mac
# by running all needed commands and automatically opening your coverage results
# in the default browser of your system.
#
# Version 1.2
# Written by: Gavin Kerr (GavinPlusPlus)

import subprocess
import os
import glob
import sys

print("================================")
print("=        RunCoverage.py        =")
print("=    Written by: Gavin Kerr    =")
print("=         Version 1.2          =")
print("================================")


# Get File Path
complete_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = ""

# Test if path is passed via args first
if (len(sys.argv) > 1): 
    project_dir = sys.argv[1]
else:
    print(f"Current Director: {complete_dir}/")
    project_dir = input("Relative File Path To The Test Project (Ex: Spreadsheet/FormulaTests): ")

# Complete file path
complete_dir = complete_dir + "/" + project_dir
try:
    os.chdir(complete_dir)    
except FileNotFoundError:
    print(f"ERROR! Unable to change directory to {complete_dir}")
    print("Please check for typos and that it exists")
    sys.exit(-1)

# Run Test
print(f"\nRunning tests on {complete_dir}")

# Capture Results
test_results = subprocess.run(['dotnet', 'test', '--collect:"XPlat Code Coverage"'], stdout=subprocess.PIPE).stdout.decode('utf-8').split("\n")

# Iterate through until finding Attachments
found_attachments = False
result_xml = ""

for s in test_results:
    if (s.find("Attachments:") != -1):
        found_attachments = True
        continue
    if (found_attachments):
        result_xml = s.strip()
        break

# Run Report
print("Generating report...")
try: 
    run_report = subprocess.run(['reportgenerator', f'-reports:{result_xml}', '-targetdir:TestResults'], stdout=subprocess.PIPE).stdout.decode('utf-8')
# Check to make sure reportgenerator could be found
except FileNotFoundError:
    print("ERROR! reportgenerator global tool not found!")
    print("Is the tool in your .zshrc path?")
    print("If you are having trouble please check the README at github.com/GavinPlusPlus/RunCoverage-Mac")
    sys.exit(-1)


# Open Results
subprocess.run(['open', f'{complete_dir}/TestResults/index.htm'], stdout=subprocess.DEVNULL)
print("\nDone! Thanks!")
