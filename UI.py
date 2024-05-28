import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Networks calculator")
    root.geometry("300x200")

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


    root.mainloop()


if __name__ == "__main__":
    main()
