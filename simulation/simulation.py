"""
simulation.py

Runs the complete shower simulation.
"""

import os
import sys
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

sys.modules.pop("config", None)

from fuzzy_system.controller import FuzzyController

from simulation.shower import Shower

from project_config import (
    DEFAULT_TARGET_TEMP,
    SIMULATION_TIME,
    TIME_STEP
)


class ShowerSimulation:

    def __init__(
        self,
        target_temperature=DEFAULT_TARGET_TEMP
    ):

        self.target_temperature = target_temperature

        self.controller = FuzzyController()

        self.shower = Shower()

        self.history = []

    # -------------------------------------------------------
    # Single Simulation Step
    # -------------------------------------------------------

    def step(self):

        current = self.shower.get_temperature()

        result = self.controller.compute_control(

            current,

            self.target_temperature

        )

        self.shower.apply_valves(

            result["hot_valve_percent"],

            result["cold_valve_percent"]

        )

        new_temp = self.shower.update_temperature()

        record = {

            "current_temperature": current,

            "new_temperature": new_temp,

            "hot_valve": result["hot_valve_percent"],

            "cold_valve": result["cold_valve_percent"]

        }

        self.history.append(record)

        return record

    # -------------------------------------------------------
    # Run Simulation
    # -------------------------------------------------------

    def run(self):

        print("\nStarting Shower Simulation\n")

        for second in range(SIMULATION_TIME):

            record = self.step()

            print(

                f"Time {second+1:03d} | "

                f"Temp {record['new_temperature']:.2f}°C | "

                f"Hot {record['hot_valve']:.2f}% | "

                f"Cold {record['cold_valve']:.2f}%"

            )

            time.sleep(TIME_STEP)

        print("\nSimulation Finished")

    # -------------------------------------------------------
    # Get History
    # -------------------------------------------------------

    def get_history(self):

        return self.history

    # -------------------------------------------------------
    # Reset
    # -------------------------------------------------------

    def reset(self):

        self.history.clear()

        self.shower.reset()


if __name__ == "__main__":

    simulation = ShowerSimulation()

    simulation.run()