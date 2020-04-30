# closest-color

Short script to find the visually closest matching color from a set of colors, given a target color.

A file containing the colors from the 256colors set is provided in `/color-sets/256-colors.txt`.

## Usage
Install the dependencies
```
pip3 install -r requirements.txt
```
Create a file containing colors in hex format, separated by newline, e.g.
```
#00ffd7
#00ffff
#5f0000
#5f005f
...
```
Run the script
```
./main.py <path_to_colors_file> <target_color e.g. #ffffff>
```
