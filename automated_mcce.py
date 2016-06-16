#!/usr/local/bin/env python
# -*- coding: utf-8 -*-
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
__author__ = 'Kamran Haider'

#=============================================================================================
# IMPORTS
#=============================================================================================

import sys, os, re
from optparse import OptionParser




class MCEE_Param(object):
	"""A class representing an MCCE parameter file

	Notes
	-----
		This class uses run.prm.quick as a template file to build an object.
		Should there be an option to initialize with quick or full (?)
	"""
	def __init__(self, mcce_directory, calculation_type = "quick"):
		"""Initialize parameters for an MCCE calculation.

		Parameters
		----------
		mcce_directory : str
			A string containing full path of the MCCE installation directory.
		run_type : str, default=quick
			A string specifying the type of MCCE calculation, if not specified "quick" is used by default. 
		"""

		self.mcce_directory = mcce_directory
		self.calculation_type = calculation_type
		self.mcce_params = self.load_params()

	def load_params(self):
		"""Loads parameters for MCCE calculation from run.prm file in MCCE installation directory.

		Returns
		-------
		params : dict
			A dictionary of MCCE calculation parameters with key 
		"""
		prm_source_file = open(self.mcce_directory + "run.prm.quick", "r")
		prm_lines = prm_source_file.readlines()
		prm_source_file.close()
		params = {}
		for line in prm_lines:
			words = line.split(" ")
			if re.search(r'\((.\w*)\)', words[-1]):
				parameter = words[-1].strip("()\n")
				value = words[0]
				params[parameter] = value
		return params

	def edit_parameters(self, **kwargs):
		"""Edits MCCE parameters by updating values in MCCE parameter dictionary keys.

		Parameters
		----------
		**kwargs : Arbitrary keyword arguments
			Any number of parameters can be specified as MCCE_PARAM="VALUE", where MCCE_PARAM is a valid
			parameter name and "VALUE" is a string with corresponding value.

		Examples
		--------
		>>> prm = MCEE_Param("~/mcce/")
		>>> prm.edit_parameters(DO_PREMCCE="t", DO_ROTAMERS="t", DO_ENERGY="t", DO_MONTE="f")
		>>> prm.edit_parameters(DO_PREMCCE="t", DO_ROTAMERS="t")

		Notes
		-----
		During parameter editing, there is no way to check if legal values are passed on, this is probably handled by
		MCCE initialization step. It is therefore assumed that this function is used responsibly.
		"""
		for parameter in kwargs:
			update_value = kwargs[parameter]
			if parameter not in self.mcce_params.keys():
				raise KeyError("Could not find %s parameter in parameter dictionary, please supply valid parameters" % parameter)
			else:
				self.mcce_params[parameter] = update_value

	def write_runprm(self, destination_dir):
		"""Writes run.prm file in a sub-directory

		Parameters
		----------
		destination_dir : string
			String containing path of the directory, where run.prm will be saved.
		"""
		runprm_filepath = destination_dir + "run.prm"



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
    	#automated_run(options.input_directory, options.destination_directory, options.mcce_directory)
    	prm = MCEE_Param("/home/kamran/mcce")
    	prm.edit_parameters(DO_PREMCCE="t", DO_ROTAMERS="t", DO_ENERGY="t", DO_MONTE="f")
    	print prm.mcce_params
    	prm.write_runprm(".")



# Using entry point approach for future conda packaging
def entry_point():
    main()
    
if __name__ == '__main__':
    entry_point()


