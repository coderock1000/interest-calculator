import tkinter as tk

def calculate_interest():
    p = float(entry_p.get())
    r = float(entry_r.get())
    t = float(entry_t.get())
    si = (p * r * t) / 100
    result.config(text=f"Interest: {si}")

app = tk.Tk()
app.title("Simple Interest Calculator")

tk.Label(app, text="Principal").pack()
entry_p = tk.Entry(app)
entry_p.pack()

tk.Label(app, text="Rate (%)").pack()
entry_r = tk.Entry(app)
entry_r.pack()

tk.Label(app, text="Time (years)").pack()
entry_t = tk.Entry(app)
entry_t.pack()

tk.Button(app, text="Calculate", command=calculate_interest).pack()

result = tk.Label(app, text="")
result.pack()

app.mainloop()
