import urllib2
import xml.etree.ElementTree as XMLTree
import serial
import time
import struct
import binascii
likeCount = 0

LIKE_URL = "http://api.facebook.com/restserver.php?" \
        "method=links.getStats&urls=" \
        "https://www.facebook.com/HTC"

SERIAL_DEVICE = "/dev/tty.usbmodemfa131"


def get_like_count():
    response = urllib2.urlopen(LIKE_URL)
    page = response.read()
    xml_root = XMLTree.fromstring(page)
    for element in xml_root.iter():
        if "like_count" in element.tag:
            return element.text

    print("cannot get like count")
    return 0

if __name__ == "__main__":
    serial = serial.Serial(SERIAL_DEVICE, 9600, timeout=1)
    binary_format = ">Ic" #big-endian, unsigned int
    for i in range(50):
      likeCountlast = likeCount
      likeCount = get_like_count()
      print "likeCountlast: ", likeCountlast
      print "likeCount: ", likeCount
      
      if (int(likeCount) - int(likeCountlast))>0:
		  		serial.write("B")	## to notice the likecount is changed 	    	 
      
      if serial.isOpen():
          for i in range(1):
              print "like: ", likeCount
              serial.write(likeCount)
              print serial.readline()
              #print binascii.hexlify(struct.pack(binary_format, int(likeCount), '\n'))
              #serial.write(struct.pack(binary_format, int(likeCount), '\n'))
              # response = serial.readlines()
              # print response
              time.sleep(1)