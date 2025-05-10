import tkinter as tk
import json
import os

# Fixed mapping (must stay consistent)
char_to_here = {
    'a': 'ghc', 'b': 'qzr', 'c': 'vnt', 'd': 'lxm', 'e': 'kto', 'f': 'dru',
    'g': 'wye', 'h': 'bsa', 'i': 'nem', 'j': 'uxp', 'k': 'miv', 'l': 'jrk',
    'm': 'tah', 'n': 'oec', 'o': 'spg', 'p': 'xdb', 'q': 'zyl', 'r': 'fcu',
    's': 'nid', 't': 'akj', 'u': 'rbo', 'v': 'hqn', 'w': 'cme', 'x': 'ibe',
    'y': 'ztu', 'z': 'ylg', ' ': '5'
}

here_to_char = {}
for char, code in char_to_here.items():
    here_to_char[code + '0'] = char.lower()
    if char != ' ':
        here_to_char[code + '1'] = char.upper()

json_file = 'here_dictionary.json'

def save_json():
    with open(json_file, 'w') as f:
        json.dump(char_to_here, f)

def check_json_validity():
    if not os.path.exists(json_file):
        print("JSON file not found, generating...")
        save_json()
    else:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                if len(k) != 1 or not k.isalpha() and k != ' ' or len(v) != 3:
                    print(f"Invalid entry in dictionary: {k}: {v}")
        except Exception as e:
            print("JSON Error:", e)

check_json_validity()

def translate_to_here(text):
    result = ''
    for char in text:
        if char.lower() in char_to_here:
            base = char_to_here[char.lower()]
            result += base + ('1' if char.isupper() else '0')
        elif char == ' ':
            result += '5'
    return result

def translate_to_english(text):
    i = 0
    result = ''
    while i < len(text):
        if text[i] == '5':
            result += ' '
            i += 1
        elif i + 4 <= len(text):
            block = text[i:i+4]
            if block in here_to_char:
                result += here_to_char[block]
                i += 4
            else:
                result += '?'
                i += 4
        else:
            result += '?'
            break
    return result

def run_translation():
    if mode.get() == "eng_to_here":
        output.delete("1.0", tk.END)
        output.insert(tk.END, translate_to_here(input_text.get("1.0", tk.END).strip()))
    else:
        output.delete("1.0", tk.END)
        output.insert(tk.END, translate_to_english(input_text.get("1.0", tk.END).strip()))

# GUI
root = tk.Tk()
root.title("Here: Py Edition")
root.geometry("700x250")

mode = tk.StringVar(value="eng_to_here")

tk.Label(root, text="Here Translator").pack()

frame = tk.Frame(root)
frame.pack()

tk.Radiobutton(frame, text="English to Here", variable=mode, value="eng_to_here").grid(row=0, column=0, padx=10)
tk.Radiobutton(frame, text="Here to English", variable=mode, value="here_to_eng").grid(row=0, column=1, padx=10)

input_text = tk.Text(root, height=5, width=80)
input_text.pack(pady=5)

tk.Button(root, text="Translate", command=run_translation).pack()

output = tk.Text(root, height=5, width=80)
output.pack(pady=5)

root.mainloop()
