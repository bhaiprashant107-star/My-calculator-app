import tkinter as tk
from tkinter import messagebox

# बटन क्लिक हैंडल करने के लिए फंक्शन
def button_click(char):
    current = entry_var.get()
    entry_var.set(current + str(char))

# 'C' (Clear Everything) बटन के लिए फंक्शन
def clear_all():
    entry_var.set("")

# 'Del' (Backspace - एक नंबर काटने) के लिए फंक्शन
def delete_one():
    current = entry_var.get()
    entry_var.set(current[:-1])

# '=' (Calculate Result) बटन के लिए फंक्शन
def calculate():
    try:
        expression = entry_var.get()
        # भाग के लिए '÷' को '/' में बदलें और गुणा के लिए '×' को '*' में बदलें
        expression = expression.replace('÷', '/').replace('×', '*')
        
        # Zero से भाग देने पर एरर हैंडलिंग
        if '/0' in expression:
            messagebox.showerror("Error", "Zero (0) से भाग नहीं दिया जा सकता!")
            entry_var.set("")
            return
            
        result = eval(expression)
        # अगर रिजल्ट पॉइंट में है, तो उसे सुंदर दिखाने के लिए राउंड करें
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "गलत इनपुट!")
        entry_var.set("")

# मुख्य विंडो (GUI Window) सेटअप
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("360x520")
root.configure(bg="#171c2c") # सुंदर डार्क बैकग्राउंड कलर
root.resizable(False, False)

# इनपुट डिस्प्ले के लिए वेरिएबल
entry_var = tk.StringVar()

# डिस्प्ले स्क्रीन (जहाँ नंबर दिखेंगे)
display = tk.Entry(
    root, 
    textvariable=entry_var, 
    font=("Arial", 28, "bold"), 
    bg="#222b45", 
    fg="#ffffff", 
    bd=0, 
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=25, padx=15, pady=20)

# बटन लेआउट ग्रिड
# सुंदर रंगों का कॉम्बिनेशन: 
# Numbers = #2e3b5e (Navy Blue), Operations = #ff9500 (Orange), Clear/Del = #ff3b30 (Red)
buttons = [
    ('C', 1, 0, '#ff3b30'), ('Del', 1, 1, '#ff3b30'), ('%', 1, 2, '#ff9500'), ('÷', 1, 3, '#ff9500'),
    ('7', 2, 0, '#2e3b5e'), ('8', 2, 1, '#2e3b5e'), ('9', 2, 2, '#2e3b5e'), ('×', 2, 3, '#ff9500'),
    ('4', 3, 0, '#2e3b5e'), ('5', 3, 1, '#2e3b5e'), ('6', 3, 2, '#2e3b5e'), ('-', 3, 3, '#ff9500'),
    ('1', 4, 0, '#2e3b5e'), ('2', 4, 1, '#2e3b5e'), ('3', 4, 2, '#2e3b5e'), ('+', 4, 3, '#ff9500'),
    ('0', 5, 0, '#2e3b5e'), ('.', 5, 1, '#2e3b5e'), ('=', 5, 2, '#00e676') # '=' के लिए सुंदर ग्रीन कलर
]

# बटन बनाने के लिए फ्रेम
button_frame = tk.Frame(root, bg="#171c2c")
button_frame.pack(fill="both", expand=True, padx=10, pady=5)

# ग्रिड का कॉन्फ़िगरेशन ताकि बटन सही से फैल सकें
for i in range(6):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# बटनों को फ्रेम में जोड़ना
for (text, row, col, bg_color) in buttons:
    # '=' बटन को 2 कॉलम की जगह दी गई है ताकि यह बड़ा और अच्छा दिखे
    colspan = 2 if text == '=' else 1
    
    # बटन का काम तय करना
    if text == 'C':
        cmd = clear_all
    elif text == 'Del':
        cmd = delete_one
    elif text == '=':
        cmd = calculate
    else:
        cmd = lambda x=text: button_click(x)
        
    btn = tk.Button(
        button_frame, 
        text=text, 
        font=("Arial", 18, "bold"), 
        bg=bg_color, 
        fg="#ffffff", 
        activebackground="#43507a", 
        activeforeground="#ffffff",
        bd=0, 
        cursor="hand2",
        command=cmd
    )
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# एप्लीकेशन को चालू करना
root.mainloop()
