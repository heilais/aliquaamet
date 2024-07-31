def hex_to_rgb(hex_color):
    # Remove '#' if present
    hex_color = hex_color.lstrip('#')
    # Convert to RGB
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb

# Example usage:
start_color = hex_to_rgb("#87CEFA")
print(start_color)  # Output: (135, 206, 250)
