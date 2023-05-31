import numpy as np
import cv2

# Function to get user input for color choices
def get_color_choices(color_type, num_colors):
    color_choices = []
    print(f"Enter {color_type} color choices:")
    for i in range(num_colors):
        color_choice = input(f"Color {i + 1}: ")
        color_choices.append(color_choice)
    return color_choices

# Define the standard dimensions of the cloth pattern
standard_width = 500
standard_height = 500

# Get input from the user for the number of colors in the warp and weft
num_warp_colors = int(input("Enter the number of colors for the warp: "))
num_weft_colors = int(input("Enter the number of colors for the weft: "))

# Get user input for color choices
warp_color_choices = get_color_choices("warp", num_warp_colors)
weft_color_choices = get_color_choices("weft", num_weft_colors)

# Get input from the user for the count of each color in the warp
print("Enter the count of each color for the warp:")
warp_color_counts = []
for color in warp_color_choices:
    color_count = int(input(f"Count of {color}: "))
    warp_color_counts.append(color_count)

# Get input from the user for the count of each color in the weft
print("Enter the count of each color for the weft:")
weft_color_counts = []
for color in weft_color_choices:
    color_count = int(input(f"Count of {color}: "))
    weft_color_counts.append(color_count)

# Calculate the total count of colors for the warp and weft
total_warp_count = sum(warp_color_counts)
total_weft_count = sum(weft_color_counts)

# Calculate the number of repetitions needed to fill the standard dimensions
num_warp_reps = int(np.ceil(standard_width / total_warp_count))
num_weft_reps = int(np.ceil(standard_height / total_weft_count))

# Calculate the actual dimensions of the cloth pattern
width = num_warp_reps * total_warp_count
height = num_weft_reps * total_weft_count

# Create a grid of coordinates for the cloth pattern
X, Y = np.meshgrid(np.arange(width), np.arange(height))

# Generate the cloth pattern
pattern = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        # Calculate the color index for each cell in the pattern
        color_index = (j // total_weft_count) % num_warp_colors
        if (i // total_warp_count) % 2 == 1:
            color_index = (color_index + 1) % num_warp_colors

        # Set the value in the pattern based on the color count
        pattern[i, j] = weft_color_counts[i % num_weft_colors] * warp_color_counts[color_index]

# Scale the pattern to 0-255 range for display
pattern_scaled = ((pattern - np.min(pattern)) / (np.max(pattern) - np.min(pattern))) * 255
pattern_scaled = pattern_scaled.astype(np.uint8)

# Create a grayscale image from the pattern
image = cv2.cvtColor(pattern_scaled, cv2.COLOR_GRAY2BGR)

# Display the image
cv2.imshow("Cloth Pattern", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
