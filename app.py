import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

def setup_window():
    root = tk.Tk()
    root.title("Language Translator")
    root.geometry("400x300")
    return root

def create_input_field(root):
    tk.Label(root, text="Text to Translate:").pack(pady=5)
    text_entry = tk.Text(root, height=5, width=50)
    text_entry.pack(pady=5)
    return text_entry

def create_language_dropdowns(root):
    languages = {
        'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Chinese': 'zh-cn',
        'Japanese': 'ja', 'Korean': 'ko', 'Hindi': 'hi', 'Arabic': 'ar'
    }
    
    tk.Label(root, text="Source Language:").pack(pady=5)
    source_language = ttk.Combobox(root, values=list(languages.keys()))
    source_language.pack(pady=5)
    source_language.set('English')

    tk.Label(root, text="Target Language:").pack(pady=5)
    target_language = ttk.Combobox(root, values=list(languages.keys()))
    target_language.pack(pady=5)
    target_language.set('Spanish')

    return source_language, target_language, languages

def create_buttons(root, text_entry, source_language, target_language, languages, result_label):
    translate_button = tk.Button(root, text="Translate", command=lambda: translate_text(text_entry, source_language, target_language, languages, result_label))
    translate_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear", command=lambda: clear_text(text_entry, result_label))
    clear_button.pack(pady=5)

def create_result_label(root):
    tk.Label(root, text="Translated Text:").pack(pady=5)
    result_label = tk.Label(root, text="", wraplength=380, justify="left")
    result_label.pack(pady=5)
    return result_label

def translate_text(text_entry, source_language, target_language, languages, result_label):
    translator = Translator()
    text = text_entry.get("1.0", tk.END).strip()
    src_lang = languages[source_language.get()]
    tgt_lang = languages[target_language.get()]

    if text:
        try:
            translation = translator.translate(text, src=src_lang, dest=tgt_lang)
            result_label.config(text=translation.text)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter text to translate.")

def clear_text(text_entry, result_label):
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")

def main():
    root = setup_window()

    text_entry = create_input_field(root)
    source_language, target_language, languages = create_language_dropdowns(root)
    result_label = create_result_label(root)
    create_buttons(root, text_entry, source_language, target_language, languages, result_label)

    root.mainloop()

if __name__ == "__main__":
    main()
