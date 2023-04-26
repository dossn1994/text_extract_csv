## Readme

### Introduction
This code is designed to parse a text file and extract specific information from it. The text file should contain cube calculation data, and the output will be a CSV file containing information about the measures in the cube.

### How to use
1. Place the `inputfile.txt` file in the same directory as the Python script.
2. Run the Python script.
3. The output will be a CSV file called `output_data.csv` in the same directory as the Python script.

### Requirements
This code requires Python 3.x to be installed on your system. It also requires the following libraries to be installed:

- `re`
- `io`
- `csv`

### Explanation
The code uses regular expressions to split the text file into individual lines and remove any leading or trailing white space. It then searches for lines that contain the string `CREATE MEMBER CURRENTCUBE.[Measures]` and extracts the relevant information from those lines.

The code then splits the extracted information by periods and extracts the name of the measure and its calculation. It also removes any unnecessary characters and formatting from the calculation.

Finally, the code writes the extracted information to a CSV file. The CSV file contains three columns: `MEASURES_NAME`, `ACTUAL_CALCULATION`, and `CALCULATION_WITH_FORMAT`.

### Limitations
This code has only been tested on text files containing calculation data that follow a specific format. It may not work on text files that do not follow this format. Additionally, the code assumes that the input text file is named `inputfile.txt` and that the output CSV file will be named `output_data.csv`. If you use a different file name or file format, you will need to modify the code accordingly.
