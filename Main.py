import tkinter as tk
from ADT_module import StackmainGUI
from stack_module import StackGUI
from queue_module import QueueGUI
from priortyqueue_module import PriorityQueueGUI
from tree_module import BinaryTreeGUI
from graph_module import GraphVisualizer
from huffman_module import HuffmanCodingGUI
from singlelinkedlist_module import LinkedListApp
from doublelinkedlist_module import App
from travelingsalesman_module import TSPApp
from hash_table_module import HashTableGUI
from heapqueue_module import HeapPriorityQueueApp 

# Main Application Class
class DataStructureSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Structure Simulator")
        self.root.geometry("500x700")  # Adjusted height for button descriptions

        # Set the background color to light blue
        self.root.configure(bg='lightblue')

        # Highlighted header
        header_frame = tk.Frame(self.root, bg='deepskyblue')
        header_frame.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")
        tk.Label(header_frame, text="Data Structure", font=("Arial", 20), bg='deepskyblue').pack(pady=10)

        # Configure grid columns to be equal width
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)

        # Create buttons with increased size and align them in a grid
        button_font = ("Arial", 14)  # Increased font for buttons
        descriptions = [
            "Abstract Data Types",
            "Last In First Out Structure",
            "First In First Out Structure",
            "Queue with Priority Levels",
            "Hierarchical Data Structure",
            "Compression Algorithm",
            "Single Linked List Structure",
            "Double Linked List Structure",
            "Solve the Traveling Salesman Problem",
            "Graph Representation",
            "Key-Value Pair Structure",
            "Heap-based Priority Queue"
        ]

        # Button and description positions
        buttons = [
            (self.open_ADT_window, "ADT"),
            (self.open_stack_window, "Stack"),
            (self.open_queue_window, "Queue"),
            (self.open_priortyqueue_window, "Priority Queue"),
            (self.open_tree_window, "Tree"),
            (self.open_huffman_window, "Huffman"),
            (self.open_singlelinkedlist_window, "Single Linked List"),
            (self.open_doublelinkedlist_window, "Double Linked List"),
            (self.open_travelingsalesman_window, "Travel Salesman"),
            (self.open_graph_window, "Graph"),
            (self.open_hash_table_window, "Hash Table"),
            (self.open_heapqueue_window, "Heap Queue")  # Added Heap Queue button
        ]

        for idx, (command, text) in enumerate(buttons):
            row = (idx // 3) * 2 + 1  # Determine row for button
            column = idx % 3  # Determine column based on index

            # Create button with increased size
            tk.Button(self.root, text=text, command=command, font=button_font, width=20, height=2).grid(row=row, column=column, padx=10, pady=(10, 0), sticky="ew")

            # Create description label with increased font size
            tk.Label(self.root, text=descriptions[idx], font=("Arial", 12), bg='lightblue').grid(row=row + 1, column=column, padx=10, pady=(0, 20), sticky="ew")

        # Highlighted footer
        footer_frame = tk.Frame(self.root, bg='deepskyblue')
        footer_frame.grid(row=12, column=0, columnspan=3, pady=20, sticky="ew")
        footer_label = tk.Label(footer_frame, text="S094 Jency Nadar", font=("Arial", 12), bg='deepskyblue')
        footer_label.pack(pady=10)

    # Functions to Open New Windows
    def open_ADT_window(self):
        new_window = tk.Toplevel(self.root)
        StackmainGUI(new_window)

    def open_stack_window(self):
        new_window = tk.Toplevel(self.root)
        StackGUI(new_window)

    def open_queue_window(self):
        new_window = tk.Toplevel(self.root)
        QueueGUI(new_window)

    def open_priortyqueue_window(self):
        new_window = tk.Toplevel(self.root)
        PriorityQueueGUI(new_window)

    def open_tree_window(self):
        new_window = tk.Toplevel(self.root)
        BinaryTreeGUI(new_window)

    def open_graph_window(self):
        new_window = tk.Toplevel(self.root)
        GraphVisualizer(new_window)

    def open_huffman_window(self):
        new_window = tk.Toplevel(self.root)
        HuffmanCodingGUI(new_window)

    def open_singlelinkedlist_window(self):
        new_window = tk.Toplevel(self.root)
        LinkedListApp(new_window)

    def open_doublelinkedlist_window(self):
        new_window = tk.Toplevel(self.root)
        App(new_window)

    def open_travelingsalesman_window(self):
        new_window = tk.Toplevel(self.root)
        TSPApp(new_window)

    def open_hash_table_window(self):
        new_window = tk.Toplevel(self.root)
        HashTableGUI(new_window)

    def open_heapqueue_window(self): 
        new_window = tk.Toplevel(self.root)
        HeapPriorityQueueApp(new_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructureSimulatorApp(root)
    root.mainloop()
