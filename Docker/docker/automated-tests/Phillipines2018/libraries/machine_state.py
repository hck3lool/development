import lxml.etree as etree
import logging
import xmldocument.xmldoc as xml


def _set_current_active_event(fileobj, event):
    content = xml.get_element(fileobj)
    active_event = content.xpath("//machine-state/active-event")[0]
    active_event.text = event
    return etree.tostring(content)

def set_current_active_event(filename, event):
    with open(filename) as f:
        value = _set_current_active_event(f, event)

    with open(filename, "w") as f:
        f.write(value)
