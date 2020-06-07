"""
Capstone Team Project.  Code to run on a LAPTOP (NOT the robot).

This code contains the one and only  MAIN  function for running on the laptop.

This code:
  1. Displays and runs the Graphical User Interface (GUI), and
  2. Talks to the robot (by sending MQTT messages) through the GUI, and
  3. Listens for messages from the robot in the background, and
  4. Acts upon any such messages via its DelegateForLaptopCode object.

In particular, this code constructs the one and only   tkinter.Tk   object
and runs  mainloop   on it.  It obtains most of its GUI (including callbacks)
from calling:
  get_my_frame()
and displaying the frame thereby obtained.

Authors:  Your professors (for the framework)
    and David Purdy
Fall term, 2019-2020.
"""

import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

import libs.mqtt_remote_method_calls as mqtt
import project3_individual.robot_number as robot_number
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Displays and runs the Graphical User Interface (GUI) and
      2. Constructs the MQTT object for SENDING messages to the ROBOT and
           RECEIVING messages from the ROBOT.  ALso constructs a "delegate"
           object to which the MQTT RECEIVER routes messages from the ROBOT.
    """
    root = tkinter.Tk()

    root.title("Team 11, Person David Purdy")

    frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    frame.grid()

    direction_entry_box_label = ttk.Label(frame, text='Left or right')
    direction_entry_box_label.grid(row=0, column=0)
    direction_entry_box = ttk.Entry(frame)
    direction_entry_box.grid(row=0, column=1)

    distance_entry_box_label = ttk.Label(frame, text='How many spaces')
    distance_entry_box_label.grid(row=1, column=0)
    distance_entry_box = ttk.Entry(frame)
    distance_entry_box.grid(row=1, column=1)

    horse_img = ImageTk.PhotoImage(Image.open("project3_individual/horse.png"))
    horse_button = ttk.Button(frame, image=horse_img)
    horse_button["command"] = lambda: horse_button_callback(mqtt_sender, direction_entry_box, )
    horse_button.grid(row=2, column=0)

    pawn_img = ImageTk.PhotoImage(Image.open("project3_individual/Pawn.png"))
    pawn_button = ttk.Button(frame, image=pawn_img)
    pawn_button["command"] = lambda: pawn_button_callback(mqtt_sender, distance_entry_box)
    pawn_button.grid(row=2, column=1)

    rook_img = ImageTk.PhotoImage(Image.open("project3_individual/rook.png"))
    rook_button = ttk.Button(frame, image=rook_img)
    rook_button["command"] = lambda: rook_button_callback(mqtt_sender, distance_entry_box)
    rook_button.grid(row=3, column=0)

    bishop_img = ImageTk.PhotoImage(Image.open("project3_individual/Bishop.png"))
    bishop_button = ttk.Button(frame, image=bishop_img)
    bishop_button["command"] = lambda: bishop_button_callback(mqtt_sender, direction_entry_box)
    bishop_button.grid(row=3, column=1)

    root.bind_all('w', lambda event: keyboard_drive(mqtt_sender, 60, 60))
    root.bind_all('s', lambda event: keyboard_drive(mqtt_sender, -60, -60))
    root.bind_all('a', lambda event: keyboard_drive(mqtt_sender, 0, 100))
    root.bind_all('d', lambda event: keyboard_drive(mqtt_sender, 100, 0))
    root.bind_all('space', lambda event: claw_grab(mqtt_sender))
    root.bind_all('l', lambda event: claw_lower(mqtt_sender))
    root.bind_all('<KeyRelease>', lambda event: keyboard_drive(mqtt_sender, 0, 0))
    # sends info to keyboard drive on the key press and keyboard drive sends it to the robot
    # -------------------------------------------------------------------------
    # Construct a DELEGATE (for responding to MQTT messages from the robot)
    # and a MQTT SENDER (to send messages to the robot).  The latter gets sent
    # to the   mX_laptop_code   modules via their  get_my_frame   methods.
    # Then  "connect"  the MQTT SENDER to the MQTT server, arranging for
    # messages to go to and from YOUR robot, while also making the
    # MQTT LISTENER start running in a loop in the background.
    # -------------------------------------------------------------------------
    delegate = DelegateForLaptopCode(root, frame)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)

    number = robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_robot(lego_robot_number=number)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
    mqtt_sender.close()


class DelegateForLaptopCode(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a ROBOT via MQTT.
    """

    def __init__(self, root, frame):
        """
          :type root:  tkinter.Tk
          :type frame  ttk.Frame
        """
        self.root = root
        self.frame = frame
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        """
          :type mqtt_sender:  mqtt.MqttClient
        """
        self.mqtt_sender = mqtt_sender

    # -------------------------------------------------------------------------
    # : Add methods here as needed.
    # -------------------------------------------------------------------------


def print_message_received(method_name, arguments=None):
    print()
    print("The laptop's delegate has received a message")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def print_message_sent(method_name, arguments=None):
    print()
    print("The laptop has SENT a message to the ROBOT")
    print("  for the  ", method_name, "  method")
    print("  with arguments", arguments)


def keyboard_drive(mqqt_sender, l_speed, r_speed):
    mqqt_sender.send_message('drive', [l_speed, r_speed])
    print_message_sent('drive', [l_speed, r_speed])


def claw_grab(mqqt_sender):
    mqqt_sender.send_message('arm_raise')
    print_message_sent('grab')


def claw_lower(mqqt_sender):
    mqqt_sender.send_message('lower_arm')


def pressed_a_key(event):
    print('You pressed the', event.keysym, 'key')


def released_a_key(event):
    print('You released the', event.keysym, 'key ++')


# above tests to make sure the key is working

def horse_button_callback(mqtt_sender, direction_entry_box):
    mqtt_sender.send_message('raise_arm')
    print_message_sent('raise_arm')

    mqtt_sender.send_message('movement', [2])
    root2 = tkinter.Tk()
    frame2 = ttk.Frame(root2, padding=10, borderwidth=5, relief="groove")
    frame2.grid()
    button = ttk.Button(frame2, text='Are you sure you want to go that way')
    button['command'] = lambda: h_left_or_right(mqtt_sender, direction_entry_box)
    button.grid()

    mqtt_sender.send_message('lower_arm')

# above is the function for the horse movement, has a pop-up for the new window in it

def left_or_right(mqtt_sender, direction_entry_box):
    if direction_entry_box.get() == 'left':
        mqtt_sender.send_message("drive", [-100, 100])
        time.sleep(1)
        mqtt_sender.send_message('stop')
    else:
        mqtt_sender.send_message('drive', [100, -100])
        time.sleep(1)
        mqtt_sender.send_message('stop')


# the above function is meant for the turning of the bishop

def h_left_or_right(mqtt_sender, direction_entry_box):
    if direction_entry_box.get() == 'left':
        mqtt_sender.send_message("drive", [-100, 100])
        time.sleep(.5)
        mqtt_sender.send_message('stop')
    else:
        mqtt_sender.send_message('drive', [100, -100])
        time.sleep(.5)
        mqtt_sender.send_message('stop')


# the above function is meant for the turning of the horse over one square


def pawn_button_callback(mqtt_sender, distance_entry_box):
    distance = distance_entry_box.get()
    if int(distance) < 2:
        mqtt_sender.send_message('raise_arm')
        mqtt_sender.send_message("movement", [distance])
        print_message_sent('movement', [distance])
        mqtt_sender.send_message('lower_arm')
    else:
        print("pawns can't move that far silly!")


# is the function for the pawn's movement, a cap on the amount of spaces it can move,
# distance is the amount of the squares

def rook_button_callback(mqtt_sender, distance_entry_box, ):
    distance = int(distance_entry_box.get())
    mqtt_sender.send_message('raise_arm')
    mqtt_sender.send_message('movement', [distance])
    print_message_sent('movement', [distance])
    mqtt_sender.send_message('lower_arm')
    print_message_sent('lower_arm')


#  above is the function for how the rook moves and distance is the amount of squares moved

def bishop_button_callback(mqtt_sender, direction_entry_box):
    mqtt_sender.send_message('raise_arm')
    mqtt_sender.send_message('movement', [2])
    root2 = tkinter.Tk()
    frame2 = ttk.Frame(root2, padding=10, borderwidth=5, relief="groove")
    frame2.grid()
    button = ttk.Button(frame2, text='Are you sure you want to go that way')
    button['command'] = lambda: left_or_right(mqtt_sender, direction_entry_box)
    button.grid()
    mqtt_sender.send_message('lower_arm')
# how the bishop works, direction tells it which way to turn after it has done the movement message
