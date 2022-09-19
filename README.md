# RunCoverage-Mac
 
## What is it?
RunCoverage.py is a simple script I created to simplify running code coverage tests on VS for Mac in CS 3500 at the University of Utah!

## What does it do?
Overall it's pretty simple. The script just runs your tests, generates the report, and then opens that report in your web browser of choice.

## How do I use it?
Simply drop the RunCoverage.py file into the root of your CS github folder (spreadsheet-GavinPlusPlus for example), then execute the command with `python3 RunCoverage.py`. After that the program will ask you for the relative directory to the test project (`Spreadsheet/FormulaTests` for example) and you are all done.

## Dependencies:
- Python 3.7+
- coverlet: Must be added to each project you intend to run tests on (`dotnet add package coverlet.collector`)
- reportgenerator: Turns the coverlet XML into a human readable report (`dotnet tool install -g dotnet-reportgenerator-globaltool`)

## Compatability:
- Tested and working on macOS 13.0 Ventura Beta 7

