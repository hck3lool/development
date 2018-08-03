import ldtp
from window_object import WindowObject
from timer import measure_time
import re
import time
import logging
from robot.api import logger
import pprint

# Object exclusion pattern

OBJECT_FILLER = 'flr*'
OBJECT_UNKNOWN = 'ukn*'
OBJECT_SCROLLBAR = 'scbr*'
OBJECT_PANEL = 'pnl*'
LABEL_MATCH_DATE = 'lbl.*EST'
OBJECT_SEPARATOR = 'spr*'

WINDOW_NAME = 'frm0'
MAX_WIDTH = 2000
MAX_HEIGHT = 2000
OBJECT_WAIT_TIMEOUT = 60


class Window(object):
    """ The Window class represents the main window of the current displayed
    screen. It has a set of subclasses that represents the specific kind of
    screens of the election application.
    """
    def __init__(self, expected_object='', timeout=OBJECT_WAIT_TIMEOUT):
        """
        This methods sets the properties that every window must have (a name
        and a size). All the other properties are optional  (to save execution
        time).
        :param expected_object: The name of an object expected on the screen. If
        not indicated, matches only the name of the window.
        :param timeout: the time LDTP must wait for the element or launch a
        runtime error
        :return:
        """

        # Static properties
        self.name = WINDOW_NAME
        self.width = MAX_WIDTH
        self.height = MAX_HEIGHT

        # Dynamic properties

        self.objects = {}
        self.visible_objects = {}

    @measure_time
    def get_objects_in_window(self):
        """
        This methods gets a list of the objects on the screen, only by name.
        It does not retrieve information of the size, the label, or other
        properties (to save execution time). When an specific property is needed
        we can use the methods to retrieve the information of an specific object
        or of all the objects on the screen.
        :return:
        """
        window_object_list = ldtp.getobjectlist(self.name)
        for window_object in window_object_list:

            self.objects[window_object] = WindowObject(window_object, self)

        return self.objects

    def get_object_by_label(self, label):
        for obj in self.objects.itervalues():
            if label == obj.label:
                return obj.name

    @measure_time
    def wait_until_window_object_exists(self, window_object='',
                                        timeout=OBJECT_WAIT_TIMEOUT):
        # return ldtp.guiexist(self.name, window_object)
        return ldtp.waittillguiexist(self.name, window_object, timeout)

    @measure_time
    def wait_until_any_object_exists(self, window_objects,
        timeout=OBJECT_WAIT_TIMEOUT, window_denied_objects=[]):
        # self.get_objects_in_window()
        logger.trace("Elements found at start: {}".format(self.objects.keys()))

        start_time = time.time()
        end_time = start_time
        # print("Type of timeout: " + str(type(timeout)))
        timeout = int(timeout)
        logger.trace("Looking for the following elements: {}".format(window_objects))
        logger.trace("Looking for denied elements: {}".format(window_denied_objects))
        while end_time - start_time < timeout:
            for element in window_objects:
                if ldtp.guiexist(self.name, element):
                    logging.debug("Found screen element: {}".format(element))
                    self.get_objects_in_window()
                    return True
            for element in window_denied_objects:
                if ldtp.guiexist(self.name, element):
                    logging.debug("Found undesired screen element: {}, exiting"\
                                  .format(element))
                    self.get_objects_in_window()
                    return False
            end_time = time.time()
        self.get_objects_in_window()
        logging.debug("Stoping search")
        logging.debug("Found objects at the end: {}".format(self.objects.keys()))
        return False
