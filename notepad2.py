import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, filedialog, simpledialog

class AdvancedNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Notepad")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        self.create_menu()
        self.setup_font_options()

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.font_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.font_menu.add_command(label="Select Font", command=self.choose_font)
        self.font_menu.add_separator()
        self.font_family_menu = tk.Menu(self.font_menu, tearoff=0)
        self.font_menu.add_cascade(label="Font Family", menu=self.font_family_menu)
        self.font_size_menu = tk.Menu(self.font_menu, tearoff=0)
        self.font_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        self.menu_bar.add_cascade(label="Font", menu=self.font_menu)

    def setup_font_options(self):
        self.chosen_font = tkfont.Font(family="Arial", size=12)

        fonts = ['Arial', 'Times New Roman', 'Courier New', 'Verdana', 'Georgia', 'Comic Sans MS']
        for font in fonts:
            self.font_family_menu.add_command(label=font, command=lambda f=font: self.set_font_family(f))

        sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24]
        for size in sizes:
            self.font_size_menu.add_command(label=str(size), command=lambda s=size: self.set_font_size(s))

    def set_font_family(self, font):
        self.chosen_font.configure(family=font)
        self.text_area.config(font=self.chosen_font)

    def set_font_size(self, size):
        self.chosen_font.configure(size=size)
        self.text_area.config(font=self.chosen_font)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)

    def save_file(self):
        try:
            content = self.text_area.get(1.0, tk.END)
            if not content:
                messagebox.showwarning("Warning", "No content to save.")
                return
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_as_file(self):
        self.save_file()

    def exit_app(self):
        self.root.destroy()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def choose_font(self):
        chosen_font = tkfont.askfont(parent=self.root, title="Select Font")
        if chosen_font:
            self.chosen_font.configure(family=chosen_font['family'])
            self.text_area.config(font=self.chosen_font)

def run_notepad():
    root = tk.Tk()
    app = AdvancedNotepad(root)
    root.mainloop()

if __name__ == "__main__":
    run_notepad()
