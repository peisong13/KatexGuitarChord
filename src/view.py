import webview
from main import gen_katex_chord

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

window = webview.create_window(
    title="Katex Guitar Chord",
    url = "../build/index.html",
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