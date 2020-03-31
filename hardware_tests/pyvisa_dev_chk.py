#!/usr/bin/python

import sys
import time
import pyvisa
import string

def main(dev_id):
  rm = pyvisa.ResourceManager()
  devices = rm.list_resources()
  
  instid=""
  for x in devices:
      if dev_id in x:
        instid=x
   #inst = rm.open_resource('GPIB0::28::INSTR')
   #print(inst.query("*IDN?"))

  if instid:
      print(instid)
      inst = rm.open_resource(instid)
       
      print("\nSet AMP and FREQ")
      inst.write("AP2.2VL")
      inst.write("FR5KZ")


  else:
      print("device id is invalid")

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        print("Usage: python myscript.py <device_id>")

