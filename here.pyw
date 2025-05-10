import tkinter as tk

MAP = {
    "A": "ghc", "B": "qzr", "C": "vnt", "D": "lxm", "E": "kto", "F": "dru",
    "G": "wye", "H": "bsa", "I": "nem", "J": "uxp", "K": "miv", "L": "jrk",
    "M": "tah", "N": "oec", "O": "spg", "P": "xdb", "Q": "zyl", "R": "fcu",
    "S": "nid", "T": "akj", "U": "rbo", "V": "hqn", "W": "cme", "X": "ibe",
    "Y": "ztu", "Z": "ylg"
}
REVERSE = {v: k for k, v in MAP.items()}

class HereGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Here: Py Edition - BAYNEISCODER")
        self.geometry("800x240")
        self.configure(bg="#0d1117")
        self.setup()

    def setup(self):
        tk.Label(self, text="Input:", fg="#58a6ff", bg="#0d1117").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.input = tk.Entry(self, width=80, bg="#161b22", fg="#c9d1d9", insertbackground="#c9d1d9")
        self.input.grid(row=0, column=1, padx=10, pady=5)

        self.mode = tk.StringVar(value="eng_to_here")
        tk.Radiobutton(self, text="English to Here", variable=self.mode, value="eng_to_here", bg="#0d1117", fg="#c9d1d9").grid(row=1, column=0, padx=10, sticky="w")
        tk.Radiobutton(self, text="Here to English", variable=self.mode, value="here_to_eng", bg="#0d1117", fg="#c9d1d9").grid(row=1, column=1, padx=10, sticky="w")

        tk.Button(self, text="Translate", command=self.translate, bg="#238636", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10)

        self.output = tk.Text(self, height=4, bg="#161b22", fg="#c9d1d9", wrap="word")
        self.output.grid(row=3, column=0, columnspan=2, padx=10, sticky="we")

        tk.Button(self, text="Copy", command=self.copy_to_clipboard, bg="#238636", fg="#ffffff").grid(row=4, column=0, columnspan=2, pady=5)

    def translate(self):
        text = self.input.get().strip()
        result = ""
        if self.mode.get() == "eng_to_here":
            for ch in text:
                if ch.isalpha():
                    upper = ch.upper()
                    code = MAP[upper]
                    result += code + ("1" if ch.isupper() else "0")
        else:
            if len(text) % 4 != 0:
                result = "Invalid input length (must be multiple of 4)."
            else:
                try:
                    for i in range(0, len(text), 4):
                        code = text[i:i+3]
                        flag = text[i+3]
                        letter = REVERSE.get(code, "?")
                        result += letter if flag == "1" else letter.lower()
                except Exception:
                    result = "Error during translation."
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, result)

    def copy_to_clipboard(self):
        result = self.output.get("1.0", tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(result)

if __name__ == "__main__":
    app = HereGUI()
    app.mainloop()
