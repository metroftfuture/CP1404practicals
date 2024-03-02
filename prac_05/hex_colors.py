COLOR_CODES = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

# Function to look up color codes
def lookup_color(color_name):
    try:
        return COLOR_CODES[color_name]
    except KeyError:
        return "Color not found."

# Main program loop
while True:
    color_name = input("Enter a color name (or blank to stop): ").strip().title()  # Convert to title case
    if color_name == "":
        break
    color_code = lookup_color(color_name)
    print(f"{color_name}: {color_code}")
