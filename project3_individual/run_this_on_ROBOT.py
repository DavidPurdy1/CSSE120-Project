"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).
This is the  INDIVIDUAL  part of the project.

This code contains the one and only  MAIN  function for running on the robot.

This code constructs a robot with an associated MQTT object and runs an
infinite loop while listening for messages from the laptop and responding to
them via its "delegate" object.

Authors:  Your professors (for the framework)
    and David Purdy.
Fall term, 2019-2020.
"""

import time
import libs.rosebot as rb
import libs.mqtt_remote_method_calls as mqtt
import project3_individual.robot_number as robot_number


def main():
    """
    This code, which must run on the ROBOT:
      1. Constructs a robot, an MQTT SENDER, and a DELEGATE to respond
           to messages FROM the LAPTOP sent TO the ROBOT via MQTT.
      2. Stays in an infinite loop while a listener (for MQTT messages)
           runs in the background, "delegating" work to the "delegate".
    """
    robot = rb.RoseBot()

    delegate = DelegateForRobotCode(robot)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)

    number = robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_laptop(lego_robot_number=number)

    time.sleep(1)  # To let the connection process complete
    print()
    print("Starting to listen for messages. The delegate responds to them.")
    print()

    # Stay in an infinite loop while the listener (for MQTT messages)
    # runs in the background:
    while True:
        time.sleep(0.01)
        if delegate.is_time_to_quit:
            break


class DelegateForRobotCode(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """

    def __init__(self, robot):
        """
          :type robot: rb.RoseBot
        """
        print("Constructing a delegate for the Robot.")
        self.robot = robot  # type: rb.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot loop

    def set_mqtt_sender(self, mqtt_sender):
        """
          :type mqtt_sender: mqtt.MqttClient
        """
        print("Setting the MqttClient associated with this delegate.")
        self.mqtt_sender = mqtt_sender

    def drive(self, l_speed, r_speed):
        self.robot.drive_system.go(l_speed, r_speed)
        print_message_received('drive', [l_speed, r_speed])

    # above controls the movement of the robot
    def stop(self):
        self.robot.drive_system.stop()
        print_message_received('stop')

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()
        print_message_received('grab')

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def movement(self, distance):
        print_message_received('movement', [distance])
        counter = 0
        while True:
            color_number = self.robot.color_sensor.get_color_as_number()
            self.robot.drive_system.go(60, 60)
            time.sleep(.4)
            self.robot.drive_system.stop()
            if self.robot.color_sensor.get_color_as_number() != color_number:
                counter = counter + 1
                if counter == int(distance):
                    break
        self.robot.drive_system.go(0, 0)

    # above is the basic move one square method, when the color sensor senses a change it adds 1 to
    # counter as long as counter is less than the amount of squares it needs to move it is good

    def increment_movement(self, times):
        counter = 0
        while counter <= int(times):
            self.robot.drive_system.go(60, 60)
            time.sleep(.2)
            counter = counter + 1
        self.robot.drive_system.go(0, 0)


# above not utilized in the final product

def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments=None):
    print()
    print("The robot has SENT a message to the LAPTOP")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,')
    print('your code raised the following exception:')
    print()
    time.sleep(1)
    raise
