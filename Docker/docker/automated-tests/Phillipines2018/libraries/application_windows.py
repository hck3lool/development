#!/usr/bin/python

import json
import logging
import pprint
import os

import ldtp
from robot.api import logger
os.chdir("/root/automated-tests/Phillipines2018/libraries/")

from window import Window

with open(os.getcwd() + "/window_names.json") as f:
    election_application_screens = json.load(f)

with open(os.getcwd() + "/button_names.json") as f:
    election_app_window_elements = json.load(f)


class ApplicationWindow(Window):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.dictionary = {}


    def wait_for_screen(self, screen, timeout=60, invalid_screen="Null"):
        if screen not in election_application_screens:
            raise ValueError(screen + " Screen is not valid ")
        logger.debug("Looking for screen: {}".format(screen))
        return self.wait_until_any_object_exists(election_application_screens[screen],
                                                 timeout, election_application_screens[invalid_screen])


    def insert_pin_number(self, pin):
        logging.debug("Inserting pin: {}".format(pin))
        for element in pin:
            self.press_button(element)


    def get_object_by_label(self, label):
        if label not in election_app_window_elements.keys():
            logger.debug("Given element: {} not found in the dictionary of known elements. "
                        "The labels lbl{} and ukn{} will be used as fallback, "
                        "but you should try to register known elements.".format(label, label, label))
            label = label.replace(" ", "")
            return [a + label for a in ("lbl", "ukn")]
        return election_app_window_elements[label]["name"]


    def press_button(self, button):
        self.get_objects_in_window()
        logger.trace("Looking for button: {}".format(button))
        logger.trace("Elements found in the screen: {}".format(self.objects.keys()))
        obj = self.get_object_by_label(button)
        logging.debug("Trying to press object: {}".format(pprint.pformat(obj)))
        for element in obj:
            try:
                self.objects[element].click_object()
                logging.debug("Pressed: {}".format(element))
            except(ldtp.LdtpExecutionError, RuntimeError, KeyError):
                continue
