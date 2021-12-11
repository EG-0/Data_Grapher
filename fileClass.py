from tkinter import *
from tkinter import filedialog
from tkfilebrowser import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2Tk
from matplotlib.figure import Figure
from io import StringIO
import os

import pandas as pd
import matplotlib.pyplot as plt

class FrameBox:

   def __init__(self, frame_function, frame):
      self.__frame = frame_function
      self.__outer_frame = frame

      # Variables used to store files
      self.df_one = self.remove_file()
      self.df_two = self.remove_file()
      self.df_three = self.remove_file()

      # Variable to mark if the initial checkbox menu has been created
      self.created = False

      # Variables to control each checkbox
      self.__var1 = None # Controls CPU Utilization
      self.__var2 = None # Controls Memory Utilization
      self.__var3 = None # Controls IO Utilization
      self.__var4 = None # Controls Disk Read Bytes
      self.__var5 = None # Controls Disk Write Bytes
      self.__var6 = None # Controls Network Sent Bytes
      self.__var7 = None # Controls Network Receivced Bytesj
      self.__var8 = None # Controls IO Bandwidth

      # Variables to control whether or not file is displayed
      self.__file1 = IntVar()
      self.__file2 = IntVar()
      self.__file3 = IntVar()

      # Variables to hold name of file in checkbox
      self.__file1_button = None
      self.__file2_button = None
      self.__file3_button = None

      # Variable to remember df file name
      self.__df_one_n = None
      self.__df_two_n = None
      self.__df_three_n = None

      # Variable to determine grouping size of boxplot
      self.__group_size = 6

   def remove_file(self):
      empty = StringIO("""cpu_utilization,memory_utilization,io_utilization,disk_read_bytes,disk_write_bytes,bytes_sent,bytes_received,io_bandwidth,time
         1,,,,,,,
         """)
      df = pd.read_csv(empty, sep = ",")

      return df

   # Function handles opening and choosing a file to run for first file
   def open_df_one(self):
      self.__df_one_n = self.__frame.filename = askopenfilename(parent = self.__frame, initialdir="~/Documents", \
               title = "Select a file", filetypes = (("txt files", "*.txt"), ("csv files", "*.csv")))

      if self.__frame.filename != "":
         self.filebutton_button(1)
         self.df_one = self.build_file(self.__df_one_n)
         if self.created is False:
            self.create_boxes()

   # Function handles opening and choosing a file to run for first file
   def open_df_two(self):
      self.__df_two_n = self.__frame.filename = askopenfilename(parent = self.__frame, initialdir="~/Documents", \
               title = "Select a file", filetypes = (("txt files", "*.txt"), ("csv files", "*.csv")))

      if self.__frame.filename != "":
         self.filebutton_button(2)
         self.df_two = self.build_file(self.__df_two_n)
         if self.created is False:
            self.create_boxes()

   # Function handles opening and choosing a file to run for first file
   def open_df_three(self):
      self.__df_three_n = self.__frame.filename = askopenfilename(parent = self.__frame, initialdir="~/Documents", \
               title = "Select a file", filetypes = (("txt files", "*.txt"), ("csv files", "*.csv")))

      if self.__frame.filename != "":
         self.filebutton_button(3)
         self.df_three = self.build_file(self.__df_three_n)
         if self.created is False:
            self.create_boxes()

   # Function to load dataframe into the file
   def build_file(self, name):
      return pd.read_csv(name)


   # Function creates button to display filename chosen and allows user to remove it
   def filebutton_button(self, flag):

      try:
         if self.__df_one_n == None:
            self.__file1_button.destroy()
         if self.__df_two_n == None:
            self.__file2_button.destroy()
         if self.__df_three_n == None:
            self.__file3_button.destroy()
      except Exception:
         pass

      if flag == 1:
         self.__file1_button = Checkbutton(self.__outer_frame, text = os.path.basename(self.__frame.filename), variable = self.__file1)
         self.__file1_button.grid(row = 1, column = 2)
      if flag == 2:
         self.__file2_button = Checkbutton(self.__outer_frame, text = os.path.basename(self.__frame.filename), variable = self.__file2)
         self.__file2_button.grid(row = 1, column = 5)
      if flag == 3:
         self.__file3_button = Checkbutton(self.__outer_frame, text = os.path.basename(self.__frame.filename), variable = self.__file3)
         self.__file3_button.grid(row = 1, column = 8)

   # Function either hides or builds graphs depending on if they are checked.
   def hide_graphs(self):
      # Check whether or not files should be hidden or not
      if not self.__file1.get():
         self.df_one = self.remove_file()
      else:
         self.df_one = self.build_file(self.__df_one_n)

      if not self.__file2.get():
         self.df_two = self.remove_file()
      else:
         self.df_two = self.build_file(self.__df_two_n)

      if not self.__file3.get():
         self.df_three = self.remove_file()
      else:
         self.df_three = self.build_file(self.__df_three_n)


   # Function handles what graph options to display on screen
   def graph_options(self):

      #Checking to ensure file was found
      if self.__frame.filename == "":
         return

      self.__var1 = IntVar()
      self.__var2 = IntVar()
      self.__var3 = IntVar()
      self.__var4 = IntVar()
      self.__var5 = IntVar()
      self.__var6 = IntVar()
      self.__var7 = IntVar()
      self.__var8 = IntVar()

      # Create checkboxes for each metric
      checkb_cpu_util = Checkbutton(self.__outer_frame, text = "CPU Utilization", variable = self.__var1)
      checkb_mem_util = Checkbutton(self.__outer_frame, text = "Memory Utilization", variable = self.__var2)
      checkb_io_util = Checkbutton(self.__outer_frame, text = "I/O Utilization", variable = self.__var3)
      checkb_disk_readb = Checkbutton(self.__outer_frame, text = "Disk Read Bytes", variable = self.__var4)
      checkb_disk_writeb = Checkbutton(self.__outer_frame, text = "Disk Write Bytes", variable = self.__var5)
      checkb_bytes_sent = Checkbutton(self.__outer_frame, text = "Bytes Sent", variable = self.__var6)
      checkb_bytes_rec = Checkbutton(self.__outer_frame, text = "Bytes Received", variable = self.__var7)
      checkb_io_bandwidth = Checkbutton(self.__outer_frame, text = "IO Bandwidth", variable = self.__var8)

      # Display checkboxes on screen
      checkb_cpu_util.grid(row = 3, column = 0)
      checkb_mem_util.grid(row = 3, column = 1)
      checkb_io_util.grid(row = 3, column = 2)
      checkb_disk_readb.grid(row = 3, column = 3)
      checkb_disk_writeb.grid(row = 3, column = 4)
      checkb_bytes_sent.grid(row = 3, column = 5)
      checkb_bytes_rec.grid(row = 3, column = 6)
      checkb_io_bandwidth.grid(row = 3, column = 7)

   # Function used to create checkboxes
   def create_boxes(self):
      self.created = True
      self.graph_options()
      update_checkbox = Button(self.__outer_frame, text = "Update Checkbox", command = self.update_boxes)
      update_checkbox.grid(row = 2, column = 3)

   # Function wipes graphs
   def update_boxes(self):
      # Destroys all widgets in the frame
      for widget in self.__frame.winfo_children():
          widget.destroy()

      # Hides frame away till needed
      self.__frame.pack_forget()

      # Adds graphs back if they are checked
      self.hide_graphs()
      self.util_graph()
      self.diskrw_graph()
      self.bytes_sr_graph()

##################### FUNCTIONS USED TO GRAPH DATA ############################
   # Function graphs CPU Utilization, Memory Utilization, and IO Utilization
   def util_graph(self):

      # None of the variables are checked
      if not self.__var1.get() and not self.__var2.get() and not self.__var3.get():
         return

      # Normalize data
      self.normalize(self.df_one)
      self.normalize(self.df_two)
      self.normalize(self.df_three)

      # Hold graph title
      title = ""
      # Create Graph
      fig = plt.Figure(figsize = (11, 6), dpi = 100)
      specific = fig.add_subplot(111)
      # Subplot Location(s)
      if self.__var1.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "cpu_utilization")
            c = "blue"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Device Utilization #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "cpu_utilization")
            c = "red"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Device Utilization #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "cpu_utilization")
            c = "green"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Device Utilization #3", color = c)
         title += "CPU Utilization, "
      if self.__var2.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "memory_utilization")
            c = "c"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Memory Utilization #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "memory_utilization")
            c = "m"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Memory Utilization #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "memory_utilization")
            c = "y"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Memory Utilization #3", color = c)
         title += "Memory Utilization, "
      '''
      if self.__var3.get():
         if self.__file1.get():
            specific.plot(self.df_one['time'], self.df_one['io_utilization'], label = "I/O Utilization #1")
         if self.__file2.get():
            specific.plot(self.df_two['time'], self.df_two['io_utilization'], label = "I/O Utilization #2")
         if self.__file3.get():
            specific.plot(self.df_three['time'], self.df_three['io_utilization'], label = "I/O Utilization #3")
         title += "I/O Utilization, "
      '''

      # Add title and legend
      #specific.set_title(title + "vs Time")
      specific.legend(bbox_to_anchor=(1,0), loc="lower right", bbox_transform=fig.transFigure, ncol=3,  prop={'size': 6})
      specific.set_xlabel('Time')
      specific.set_ylabel('Percent Utilization')
      #specific.legend(bbox_to_anchor=(1,1), loc="upper left")
      # Load graph into tkinter
      chart = FigureCanvasTkAgg(fig, self.__frame)
      chart.get_tk_widget().pack()

      # Create frame to place toolbar in
      tool_bar_frame = Frame(self.__frame)
      tool_bar_frame.pack()

      # Place toolbar
      toolbar = NavigationToolbar2Tk(chart, tool_bar_frame)
      toolbar.update()
      chart._tkcanvas.pack()
      self.space_buffer()

   # Function graphs disk reads
   def diskrw_graph(self):

      # Does not generate graph if not checked
      if not self.__var4.get() and not self.__var5.get() and not self.__var8.get():
         return

      # Normalize data
      self.normalize(self.df_one)
      self.normalize(self.df_two)
      self.normalize(self.df_three)

      # Hold graph title
      title = "Disk "
      # Create Graph
      fig = plt.Figure(figsize = (11, 6), dpi = 100)
      specific = fig.add_subplot(111)
      # Subplot Location(s)
      if self.__var4.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "disk_read_bytes")
            c = "r"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Read #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "disk_read_bytes")
            c = "b"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Read #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "disk_read_bytes")
            c = "g"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Read #3", color = c)
         title += "Read "
      if self.__var5.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "disk_write_bytes")
            c = "c"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Write #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "disk_write_bytes")
            c = "m"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Write #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "disk_write_bytes")
            c = "y"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Disk Write #3", color = c)
         title += "Write "
      if self.__var8.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "io_bandwidth")
            c = "k"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="w"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "IO Bandwidth #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "io_bandwidth")
            c = "w"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "IO Bandwidth #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "io_bandwidth")
            c = "lime"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "IO Bandwidth #3", color = c)
         title += "Bandwidth "

      # Add title and legend
      specific.set_title(title + "in Bytes vs Time")
      specific.legend(bbox_to_anchor=(1,0), loc="lower right", bbox_transform=fig.transFigure, ncol=3,  prop={'size': 6})
      specific.set_xlabel('Time')
      specific.set_ylabel('Bytes')
      #specific.legend(bbox_to_anchor=(1,1), loc="upper left")
      # Load graph into tkinter
      chart = FigureCanvasTkAgg(fig, self.__frame)
      chart.get_tk_widget().pack()

      # Create frame to place toolbar in
      tool_bar_frame = Frame(self.__frame)
      tool_bar_frame.pack()

      # Place toolbar
      toolbar = NavigationToolbar2Tk(chart, tool_bar_frame)
      toolbar.update()
      chart._tkcanvas.pack()
      self.space_buffer()

   # Function graphs bytes sents
   def bytes_sr_graph(self):

      # Does not generate graph if not checked
      if not self.__var6.get() and not self.__var7.get():
         return

      # Normalize data
      self.normalize(self.df_one)
      self.normalize(self.df_two)
      self.normalize(self.df_three)

      # Hold graph title
      title = "Bytes "
      # Create Graph
      fig = plt.Figure(figsize = (11, 6), dpi = 100)
      specific = fig.add_subplot(111)
      # Subplot Location(s)
      if self.__var6.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "bytes_sent")
            c = "r"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Sent #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "bytes_sent")
            c = "b"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Sent #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "bytes_sent")
            c = "g"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Sent #3", color = c)
         title += "Sent "
      if self.__var7.get():
         if self.__file1.get():
            data = self.split_data(self.df_one, "bytes_received")
            c = "c"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Received #1", color = c)
         if self.__file2.get():
            data = self.split_data(self.df_two, "bytes_received")
            c = "m"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Received #2", color = c)
         if self.__file3.get():
            data = self.split_data(self.df_three, "bytes_received")
            c = "y"
            bp = specific.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=c, color=c),
               capprops=dict(color=c),
               whiskerprops=dict(color=c),
               flierprops=dict(color=c, markeredgecolor=c),
               medianprops=dict(color="black"))
            specific.set_xticks(self.x_ticks(data))
            specific.set_xticklabels(self.x_ticks(data), fontsize = 8)
            specific.plot([], [], label = "Bytes Received #3", color = c)
         title += "Received "

      # Add title and legend
      specific.set_title(title + "vs Time")
      specific.legend(bbox_to_anchor=(1,0), loc="lower right", bbox_transform=fig.transFigure, ncol=3,  prop={'size': 6})
      #specific.legend(bbox_to_anchor=(1,1), loc="upper left")
      specific.set_xlabel('Time')
      specific.set_ylabel('Bytes')
      # Load graph into tkinter
      chart = FigureCanvasTkAgg(fig, self.__frame)
      chart.get_tk_widget().pack()

      # Create frame to place toolbar in
      tool_bar_frame = Frame(self.__frame)
      tool_bar_frame.pack()

      # Place toolbar
      toolbar = NavigationToolbar2Tk(chart, tool_bar_frame)
      toolbar.update()
      chart._tkcanvas.pack()
      self.space_buffer()

   # Adds space
   def space_buffer(self):
      space_label = Label(self.__frame, text = "\n\n\n")
      space_label.pack()

   # Normalize data
   def normalize(self, df_norm):
      # apply normalization techniques
      for column in df_norm.columns:
         if column == 'time':
            continue
         df_norm[column] = (df_norm[column] - df_norm[column].min()) \
          / (df_norm[column].max() - df_norm[column].min())

   # Function splits data up to be graphed as a candlestick
   def split_data(self, df_n, name):
      return [df_n[name].iloc[i:i+self.__group_size] \
         for i in range(0,len(df_n[name])-self.__group_size+1,\
          self.__group_size)]

   # Function calculates number of seconds to be placed on x-axis
   def x_ticks(self, data):

      lst = []
      counter = 3

      for i in range(0, len(data)):
         lst.append(int(counter))
         counter += self.__group_size / 2

      return lst
