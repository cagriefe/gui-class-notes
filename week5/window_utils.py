def center_window(screen_width, screen_height, window_width, window_height):
    # Calculate the x coordinate for the window to be centered
    x = int((screen_width / 2) - (window_width / 2))
    
    # Calculate the y coordinate for the window to be centered
    y = int((screen_height / 2) - (window_height / 2))

    # Return the geometry string for the window
    # This string specifies the width, height, and position of the window
    return f"{window_width}x{window_height}+{x}+{y}"