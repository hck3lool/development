import ldtp
import logging

class WindowObject(object):
    def __init__(self, name, parent):
        # Mandatory attributes
        self.name = name
        self.parent = parent

        # Runtime properties (Obtained if needed, to save execution time)
        self.label = ''
        self.center = 0, 0
        self.width = 0
        self.height = 0
        self.x_origin = 0
        self.y_origin = 0
        self.visible = True

    def get_property(self, property_name):
        return ldtp.getobjectproperty(self.parent.name, self.name,
                                      property_name)

    def get_object_center(self):
        object_size = ldtp.getobjectsize(self.parent.name, self.name)
        self.x_origin = object_size[0]
        self.y_origin = object_size[1]
        self.width = object_size[2]
        self.height = object_size[3]

        half_width = self.width / 2
        half_height = self.height / 2
        x_object_center = self.x_origin + half_width
        y_object_center = self.y_origin + half_height

        self.center = x_object_center, y_object_center
        return x_object_center, y_object_center

    def verify_if_object_is_visible(self):
        self.get_object_center()
        if 0 <= self.center[0] <= self.parent.width and \
           0 <= self.center[1] <= self.parent.height:
            self.visible = True
            return True
        self.visible = False
        return False

    def click_object(self):
        if not self.verify_if_object_is_visible():
            logging.debug("The center of {} is not "
                          "clickable {}".format(self.name, self.center))
            raise RuntimeError('The object is not clickable')
        ldtp.generatemouseevent(self.center[0], self.center[1])
        logging.debug("Clicked {} coordinates: {}, {}".format(self.name,
            self.center[0],
            self.center[1]))
