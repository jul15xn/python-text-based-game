def set_color(text, foreground = 37, background = 40):
    return f"[{background};{foreground}m{text}"

def set_console_color(foreground = 37, background = 40):
    print(f"[{background};{foreground}m", end='')

def reset_colors():
    print(f"[0m", end='')