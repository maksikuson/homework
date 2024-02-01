from tkinter import *

root = Tk()
root.title("Color Picker")
root.geometry("600x400")
root.configure(background='white')

main_frame = Frame(root, background='white')
main_frame.pack()


def update_color(frame, name, code):
    frame.entry_name.delete(0, END)
    frame.entry_name.insert(0, name)
    frame.entry_code.delete(0, END)
    frame.entry_code.insert(0, code)
    root.configure(background=code)
    
    
def create_color_frame(frame, name, code, button_width=20):
    frame.entry_name = Entry(frame, width=20, justify='left')
    frame.entry_name.pack(side=LEFT, padx=10)
    
    Button(frame, text=name, bg=code, fg="black", width=button_width,
           command=lambda: update_color(frame, name, code)).pack(side=LEFT, padx=10, pady=5)
    
    frame.entry_code = Entry(frame, width=20, justify='right')
    frame.entry_code.pack(side=RIGHT, padx=10)
    
    
colors = [
    ("DarkSlateGray3", "#79CDCD", 100),
    ("DarkSlateGray4", "#87CEEB", 100),  
    ("DarkTurquoise", "#00CED1", 100),
    ("DarkViolet", "#9400D3", 100),
    ("DeepPink1", "#FF1493", 100),  
    ("DeepPink2", "#EE1289", 100),
    ("DeepPink3", "#CD1076", 100),  
    ("DeepPink4", "#8B0A50", 100),
    ("DeepSkyBlue1", "#00BFFF", 100),  
    ("DeepSkyBlue2", "#00B2EE", 100),
    ("DeepSkyBlue3", "#009ACD", 100),
    ("DeepSkyBlue4", "#00688B", 100),
    ("DimGray", "#696969", 100),
    ("DodgerBlue1", "#1E90FF", 100),
    ("DodgerBlue2", "#1874cd", 100),
    ("DodgerBlue3", "#1874CD", 100),
    ("DodgerBlue4", "#104E9B", 100)
]
    
for color in colors:
    frame= Frame(main_frame, background='white')
    frame.pack()
    create_color_frame(frame, color[0], color[1], color[2])
    
root.mainloop()