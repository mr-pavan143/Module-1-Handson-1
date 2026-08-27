"""
app.py

Main GUI application for the Fuzzy Shower Controller.
"""

import tkinter as tk
from tkinter import ttk

from gui.dashboard import Dashboard


class ShowerApp:
    """
    Main application window.
    """

    def __init__(self, simulation):

        self.simulation = simulation

        self.root = tk.Tk()

        self.root.title(
            "Fuzzy Shower Temperature Controller"
        )

        self.root.geometry(
            "1000x650"
        )

        self.root.resizable(
            False,
            False
        )


        self.create_ui()


    # ------------------------------------------------------
    # Create UI
    # ------------------------------------------------------

    def create_ui(self):

        title = ttk.Label(
            self.root,
            text="AI Fuzzy Shower Controller",
            font=(
                "Arial",
                22,
                "bold"
            )
        )

        title.pack(
            pady=20
        )


        self.dashboard = Dashboard(

            self.root,

            self.simulation

        )


        self.dashboard.pack(
            fill="both",
            expand=True
        )


    # ------------------------------------------------------
    # Start GUI
    # ------------------------------------------------------

    def start(self):

        self.root.mainloop()



# ----------------------------------------------------------
# Launch Function
# ----------------------------------------------------------

def launch_gui(simulation):

    app = ShowerApp(
        simulation
    )

    app.start()



if __name__ == "__main__":

    from simulation.simulation import ShowerSimulation


    simulation = ShowerSimulation()


    launch_gui(
        simulation
    )