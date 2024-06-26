import webview
from main import gen_katex_chord
import os

class Api:
    def __init__(self):
        pass

    def gen_katex_chord_api(self, chord_name, fret_shift, chord_input):
        print(chord_name, fret_shift, chord_input)
        return gen_katex_chord(chord_name, fret_shift, chord_input)
    
    def error(self):
        raise Exception("An error occurred in Python")
    
    def close_window(self):
        webview.windows[0].destroy()
    
    # minimize window
    def minimize_window(self):
        webview.windows[0].minimize()

if __name__ == "__main__":
    # Create a webview window
    print(os.path.dirname(os.path.abspath(__file__)))
    url_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build/index.html")
    print(url_path)
    window = webview.create_window(
        title="Katex Guitar Chord",
        url = url_path,
        js_api=Api(),
        width=800,
        height=500,
        resizable=False,
        text_select=True,
        confirm_close=True,
        frameless=True,
        easy_drag=False,
    )

    webview.start()