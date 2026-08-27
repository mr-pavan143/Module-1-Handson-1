"""
graphs.py

Creates visualization graphs for the shower simulation.

Graphs:
1. Temperature vs Time
2. Valve Opening Percentage
"""

import os

import matplotlib.pyplot as plt


class SimulationGraphs:
    """
    Generates simulation graphs.
    """

    def __init__(
        self,
        history
    ):

        self.history = history

        self.output_folder = "results"

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )


    # -----------------------------------------------------
    # Extract Data
    # -----------------------------------------------------

    def extract_data(self):

        time = []

        temperature = []

        hot_valve = []

        cold_valve = []


        for index, item in enumerate(
            self.history
        ):

            time.append(
                index + 1
            )

            temperature.append(
                item["new_temperature"]
            )

            hot_valve.append(
                item["hot_valve"]
            )

            cold_valve.append(
                item["cold_valve"]
            )


        return (
            time,
            temperature,
            hot_valve,
            cold_valve
        )


    # -----------------------------------------------------
    # Temperature Graph
    # -----------------------------------------------------

    def temperature_graph(self):

        (
            time,
            temperature,
            _,
            _

        ) = self.extract_data()


        plt.figure(
            figsize=(8,5)
        )


        plt.plot(

            time,

            temperature,

            label="Water Temperature"

        )


        plt.xlabel(
            "Time"
        )

        plt.ylabel(
            "Temperature °C"
        )


        plt.title(
            "Shower Temperature Response"
        )


        plt.legend()

        plt.grid()


        plt.savefig(

            f"{self.output_folder}/temperature_graph.png"

        )


        plt.close()



    # -----------------------------------------------------
    # Valve Graph
    # -----------------------------------------------------

    def valve_graph(self):

        (
            time,
            _,
            hot,
            cold

        ) = self.extract_data()



        plt.figure(

            figsize=(8,5)

        )


        plt.plot(

            time,

            hot,

            label="Hot Valve"

        )


        plt.plot(

            time,

            cold,

            label="Cold Valve"

        )


        plt.xlabel(
            "Time"
        )


        plt.ylabel(
            "Valve Opening (%)"
        )


        plt.title(
            "Valve Control Behaviour"
        )


        plt.legend()


        plt.grid()


        plt.savefig(

            f"{self.output_folder}/fuzzy_surface.png"

        )


        plt.close()



    # -----------------------------------------------------
    # Generate All Graphs
    # -----------------------------------------------------

    def generate(self):

        self.temperature_graph()

        self.valve_graph()


        print(
            "Graphs generated successfully."
        )



# ---------------------------------------------------------
# Standalone Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    sample_history = [

        {
            "new_temperature": 30,
            "hot_valve":80,
            "cold_valve":20
        },

        {
            "new_temperature":35,
            "hot_valve":70,
            "cold_valve":30
        },

        {
            "new_temperature":38,
            "hot_valve":60,
            "cold_valve":40
        }

    ]


    graph = SimulationGraphs(
        sample_history
    )


    graph.generate()