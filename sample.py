import sys
import xml.dom.minidom
import os

def main(country):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    files = os.listdir(os.path.join(dir_path, 'xml', country))
    c = 0
	for file in files:
                print 'Reading file: '+file
                base_path = os.path.join(dir_path, 'xml', country)
                #doc = xml.dom.minidom.parse(os.path.join(base_path, file))
                content = open(os.path.join(base_path,file), 'r')
                for line in content:
                        try:
                            	doc = xml.dom.minidom.parseString(line)

                        except:
                               	pass

                print 'Finished '+str(c)

if __name__ == "__main__":
        main(sys.argv[1])
