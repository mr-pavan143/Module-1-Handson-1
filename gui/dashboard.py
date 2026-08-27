"""
dashboard.py

Creates the dashboard interface.
"""

import tkinter as tk
from tkinter import ttk


class Dashboard(ttk.Frame):


    def __init__(
        self,
        parent,
        simulation
    ):

        super().__init__(
            parent
        )

        self.simulation = simulation


        self.create_widgets()


    # ------------------------------------------------------
    # Widgets
    # ------------------------------------------------------

    def create_widgets(self):


        self.temperature_label = ttk.Label(

            self,

            text="Temperature: -- °C",

            font=(
                "Arial",
                18
            )

        )

        self.temperature_label.grid(

            row=0,

            column=0,

            padx=40,

            pady=30

        )



        self.hot_label = ttk.Label(

            self,

            text="Hot Valve: -- %",

            font=(
                "Arial",
                16
            )

        )


        self.hot_label.grid(

            row=1,

            column=0,

            pady=20

        )



        self.cold_label = ttk.Label(

            self,

            text="Cold Valve: -- %",

            font=(
                "Arial",
                16
            )

        )


        self.cold_label.grid(

            row=2,

            column=0,

            pady=20

        )



        self.start_button = ttk.Button(

            self,

            text="Run Simulation",

            command=self.run_simulation

        )


        self.start_button.grid(

            row=3,

            column=0,

            pady=30

        )


    # ------------------------------------------------------
    # Update Dashboard
    # ------------------------------------------------------

    def update_display(self):


        if len(self.simulation.history) > 0:


            data = self.simulation.history[-1]


            self.temperature_label.config(

                text=

                f"Temperature : "
                f"{data['new_temperature']:.2f} °C"

            )


            self.hot_label.config(

                text=

                f"Hot Valve : "
                f"{data['hot_valve']:.2f}%"

            )


            self.cold_label.config(

                text=

                f"Cold Valve : "
                f"{data['cold_valve']:.2f}%"

            )


        self.after(
            1000,
            self.update_display
        )


    # ------------------------------------------------------
    # Run Simulation
    # ------------------------------------------------------

    def run_simulation(self):

        self.simulation.step()

        self.update_display()