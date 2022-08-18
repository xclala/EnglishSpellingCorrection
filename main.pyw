from textblob import TextBlob
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

path = askopenfilename()
try:
    with open(path, encoding='utf-8') as f:
        text = f.read()
    with open(path, "w+", encoding='utf-8') as f:
        f.write(str(TextBlob(text).correct()))
    messagebox.showinfo("正确的拼法已经覆盖原文件！", "正确的拼法已经覆盖原文件！")
except FileNotFoundError:
    print("File not found.")