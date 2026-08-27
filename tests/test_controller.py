"""
test_controller.py

Tests complete shower controller.
"""


import sys
import os


sys.path.append(

    os.path.dirname(
        os.path.dirname(__file__)
    )

)



from fuzzy_system.controller import FuzzyController



# ---------------------------------------------------------
# Test Complete Controller
# ---------------------------------------------------------

def test_controller_output():


    controller = FuzzyController()



    result = controller.compute_control(

        current_temperature=25,

        target_temperature=38

    )



    assert (

        "hot_valve_percent"

        in result

    )


    assert (

        "cold_valve_percent"

        in result

    )



    assert (

        0 <= result["hot_valve_percent"] <= 100

    )


    assert (

        0 <= result["cold_valve_percent"] <= 100

    )