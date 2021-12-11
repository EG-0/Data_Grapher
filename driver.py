from tkinter import *
from tkscrolledframe import ScrolledFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from fileClass import FrameBox

###################### Functions for various operations #######################
### HOW THE APPLICATION LOOKS ###
# Create buttons and file handling for each frame
def create_buttons_for_frame():

   file_button_one = Button(root, text = "Open File", command = frame_one_obj.open_df_one)
   file_button_one.grid(row = 1, column = 1)

   file_button_two = Button(root, text = "Open File", command = frame_one_obj.open_df_two)
   file_button_two.grid(row = 1, column = 4)

   file_button_three = Button(root, text = "Open File", command = frame_one_obj.open_df_three)
   file_button_three.grid(row = 1, column = 7)

def create_labels_for_frame():
   my_label_one = Label(root, text = "Choose Data to Graph")
   my_label_one.grid(row = 1, column = 0)

   my_label_two = Label(root, text = "   Choose Data to Graph")
   my_label_two.grid(row = 1, column = 3)

   my_label_three = Label(root, text = "   Choose Data to Graph")
   my_label_three.grid(row = 1, column = 6)

###################### Creating Items #########################################
# Creating tkinter window
root = Tk()
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
root.geometry(str(w) + "x" + str(h))
root.title("Data Grapher v0.2")

# Creating a frame to put graphs in
sf = ScrolledFrame(root, width = w - 10, height = h - 165)
sf.grid(row = 4, column = 0, columnspan = 10)

sf.bind_arrow_keys(root)
sf.bind_scroll_wheel(root)

# Creating additional frame within scrollable frame for graphs
frame_one = sf.display_widget(Frame)

# Place frames in object to hold info about
frame_one_obj = FrameBox(frame_one, root)

# Creating a label to designate each of the graphs
graph_label_one = Label(root, text = "          Choose Files to Graph")
graph_label_one.grid(row = 0, column = 2, columnspan = 3)

# Creating Buttons
create_buttons_for_frame()

# Creating a label
create_labels_for_frame()

root.mainloop()
