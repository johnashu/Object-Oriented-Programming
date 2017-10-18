
import xml.etree.ElementTree as etree

times = []
keys = []

def main():
    tree = etree.parse('sample.xml')
    root = tree.getroot()

    for child in root:
        times.append(child.find('text11').text)
        keys.append(child.find('word').text)

if __name__ == "__main__": 
    main()
