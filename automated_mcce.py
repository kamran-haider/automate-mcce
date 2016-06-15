#!/usr/local/bin/env python
# -*- coding: utf-8 -*-
import sys
from optparse import OptionParser


"""
Automate MCCE Calculations.
Description
-----------
This module implements a program to set up and run automated mcce calculations.
Notes
-----
This is still in development.
References
----------
Examples
--------
Coming soon!

TODO
----
	* Envision batch mcce runs.
	* Do we always start from a folder containing PDB files or are there other ways too?
	* Collect all current utility functions.
	*
"""

def automated_run(input_dir, destination_dir, mcce_dir):
	# check if all inout_dir exists and is not empty
	# check if mcce exists and is executable
	# if outout dir doesnot exist, create it 
	pass





def main():
    parser = OptionParser()
    parser.add_option("-i", "--input_directory", dest="input_directory", type="string", help="Directory containing input PDB files.")
    parser.add_option("-d", "--destination_directory", dest="destination_directory", type="string", help="Directory where output of mcce calculations will be stored.")
    parser.add_option("-e", "--mcce_directory", dest="mcce_directory", type="string", help="Ligand file")
    (options, args) = parser.parse_args()
    if len(args) == 0:
        print "no argument given!"
        parser.print_help()    
    else:
        print "Setting up calculations..."
    	automated_run(options.input_directory, options.destination_directory, options.mcce_directory)

# Using entry point approach for future conda packaging
def entry_point():
    main()
    
if __name__ == '__main__':
    entry_point()


