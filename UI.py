import tkinter as tk
from calculator import calculate_for_ui

def main():
    root = tk.Tk()
    root.title("Networks calculator")
    root.geometry("800x600")

    textIPv4 = tk.Label(root, text="IPv4 address:")
    textIPv4.grid(row=0, column=0)

    varIPv4 = tk.StringVar(root, value="192.168.209.1")
    entryIPv4 = tk.Entry(root, textvariable=varIPv4)
    entryIPv4.grid(row=0, column=1)


    textMask = tk.Label(root, text="Mask:")
    textMask.grid(row=1, column=0)

    varMask = tk.StringVar(root, value="255.255.128.0")
    entryMask = tk.Entry(root, textvariable=varMask)
    entryMask.grid(row=1, column=1)

    def callback_calculate(output: tk.Text):
        ipv4 = entryIPv4.get()
        mask = entryMask.get()
        list_all_info = calculate_for_ui(ipv4, mask)
        for i, item in enumerate(list_all_info):
            output.insert(tk.END, f"{i+1}. {item}\n")
        output.insert(tk.END, "\n")

    output = tk.Text(root)
    output.grid(row=3, column=1)

    btnCalc = tk.Button(root, text="Calculate!", command=lambda: callback_calculate(output))
    btnCalc.grid(row=2, column=1)

    def clear_output():
        output.delete(1.0, tk.END)

    btnClear = tk.Button(root, text="Clear", command=clear_output)
    btnClear.grid(row=4, column=1)


    root.mainloop()


if __name__ == "__main__":
    main()
