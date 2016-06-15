#!/usr/local/bin/env python
# -*- coding: utf-8 -*-
import sys, os
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
def generate_prm(source_prm, ):
	pass

def automated_run(input_dir, destination_dir, mcce_dir):
	"""Performs an automated mcce calculation on a set of pdb file, located in an input folder.

	Parameters
	----------
	input_dir : str
		String consisting of a valid path of a directory containing pdb files.
	destination_dir : str
		String consisting of a path representing a target directory where results of each mcce calculation will be stored.
	mcce_dir :  str
		Location of the mcce installation, should contain mcce executable.

	Notes
	-----
	This function will not work if each pdb file that should be processed is present in its own sub-directory. It is suggested that
	all pdb files are collected in the input directory before running this."""

	# check if input_dir exists and is not empty
	if not os.path.isdir(input_dir):
		sys.exit("Input directory not found.")
	if destination_dir == None:
		sys.exit("Output directory not specified.")
	# check if mcce exists
	input_pdb_files = [pdb_file for pdb_file in os.listdir(input_dir) if pdb_file.endswith(".pdb")]
	for pdb_file in input_pdb_files:
		print "Working on: ", pdb_file
		output_dir = destination_dir + "/mcee_results_" + pdb_file[0:-4]
		if not os.path.exists(output_dir):
		    os.makedirs(output_dir)





def main():
    parser = OptionParser()
    parser.add_option("-i", "--input_directory", dest="input_directory", type="string", help="Directory containing input PDB files.")
    parser.add_option("-d", "--destination_directory", dest="destination_directory", type="string", help="Directory where output of mcce calculations will be stored.")
    parser.add_option("-e", "--mcce_directory", dest="mcce_directory", type="string", help="Ligand file")
    (options, args) = parser.parse_args()
    if len(args) == 1:
        print "\nNo argument given!"
        parser.print_help()
    else:
        print "Setting up calculations..."
    	automated_run(options.input_directory, options.destination_directory, options.mcce_directory)

# Using entry point approach for future conda packaging
def entry_point():
    main()
    
if __name__ == '__main__':
    entry_point()


