"""
Main Entry Point
Fuzzy Shower Temperature Controller
"""

import sys
import os


# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

sys.modules.pop("config", None)

from project_config import DEFAULT_TARGET_TEMP
from simulation.simulation import ShowerSimulation
from gui.app import launch_gui



def main():

    print("=" * 50)
    print("Fuzzy Shower Temperature Controller")
    print("=" * 50)


    simulation = ShowerSimulation(
        target_temperature=DEFAULT_TARGET_TEMP
    )


    simulation.run()


    launch_gui(
        simulation
    )



if __name__ == "__main__":

    main()