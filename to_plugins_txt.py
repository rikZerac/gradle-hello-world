import xml.etree.ElementTree as ET
import sys


def main():
    root = ET.parse(sys.stdin).getroot()
    odd = False
    plugin_line = ''
    for child in root:
        if not odd:
            plugin_line += child.text
        else:
            plugin_line += ':' + child.text
            print(plugin_line)
            plugin_line = ''
        odd = not odd


if "__main__" == __name__:
    main()
