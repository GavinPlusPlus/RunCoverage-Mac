# Troubleshooting

## Common issues:
"zsh: command not found: python3": 
- This script requires python3 to be installed on your system, you can download a copy of it below.
- https://www.python.org/downloads/

Unable to change directory:
- Please make sure that the script is located is located at the root of your git folder
- Ex: (spreadsheet-GIT_USER_NAME)
- Also keep in mind directory names are CASE-SENSITIVE!

Coverlet:
- Please check to see if coverlet is installed in your solution, this can be done with the following command in the project directory.
- `dotnet install package coverlet.collector`
- After verifying it is installed attempt to run the script again. 

reportgenerator: 
- If the script returns that it could not run the reportgenerator command you may need to verify it is installed and add it to your path.
- To install reportgenerator first run the following command: `dotnet tool install -g dotnet-reportgenerator-globaltool`
- Attempt to run the script again. If it fails again you may need to add the tool to your PATH variable.
- To do this first open up terminal to your home folder, it should take you there by default but if not run: `cd %`
- Once you are at the home folder type and run the following command: `nano .zshrc`
- Once nano is open paste the following text in: `export PATH=$PATH:/$HOME/.dotnet/tools`
- After that all you need to do is press, Control + X, Y, and Return.
- Now all you have to do is type `exit`, close terminal, and then reportgenerator should be completely installed.

Other:
- If you are still having issues getting the script to work after trying these troubleshooting steps feel free to open an issue on the git repository, although I cannot guarantee I can help. Thanks! 