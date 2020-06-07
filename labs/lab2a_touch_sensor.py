"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   TouchSensor   class.

Authors:  Your professors (for the framework)
    and david, arvind, charles.
Winter term, 2019-2020.
"""
# : 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# : 2. Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_touch_sensor as touch
import time


def main():
    """ Tests the   TouchSensor   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  TOUCH SENSOR  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # Done: 3. The following constructs a   TouchSensor   object,
    #  then sends it as an argument to the TEST functions. In those TEST
    #  functions, you will access the methods of the TouchSensor object.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    touch_sensor = touch.TouchSensor(1)

    run_test_get_reading(touch_sensor)
    run_test_is_pressed(touch_sensor)
    run_test_wait_until_pressed(touch_sensor)
    run_test_wait_until_released(touch_sensor)


def run_test_get_reading(touch_sensor):
    """
    Tests the   get_reading   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   get_reading   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("In the output that will appear, you should see:")
    print("  1  when the physical Touch Sensor is pressed")
    print("  0  when the physical Touch Sensor is NOT pressed")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # Done: 4. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   get_reading   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            reading = touch_sensor.get_reading()
            print(reading)
            time.sleep(0.1)


    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_is_pressed(touch_sensor):
    """
    Tests the   is_pressed   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   is_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("In the output that will appear, you should see:")
    print("  True   when the physical Touch Sensor is pressed")
    print("  False  when the physical Touch Sensor is NOT pressed")
    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # Done: 5. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   is_pressed   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            pressed = touch_sensor.is_pressed()
            print(pressed)
            time.sleep(0.5)


    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_wait_until_pressed(touch_sensor):
    """
    Tests the   wait_until_pressed   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   wait_until_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("Press the ENTER key when ready to WAIT until the")
    print("Touch Sensor is pressed.  Then, when you are ready,")
    input("press the Touch Sensor, which should stop this test.")
    try:
        # ---------------------------------------------------------------------
        # Done: 6. Call the   wait_until_pressed   method on the given
        #  TouchSensor object. Then print a simple message like "Pressed!"
        # ---------------------------------------------------------------------
        touch_sensor.wait_until_pressed()
        print("Pressed")

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_wait_until_released(touch_sensor):
    """
    Tests the   wait_until_released   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   wait_until_released   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready to WAIT until the")
    print("Touch Sensor is RELEASED.  That is, press and hold down")
    print("the Touch Sensor now, then press the ENTER key.")
    print("Then, when you are ready, RELEASE the Touch Sensor")
    input("which should stop this test.")

    # -------------------------------------------------------------------------
    # Done: 7. Call the   wait_until_released   method on the given
    #  TouchSensor object. Then print a simple message like "Released!"
    # -------------------------------------------------------------------------
    touch_sensor.wait_until_released()
    print("Released")

