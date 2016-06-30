#!/usr/bin/python
import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call  # This is needed to submit jobs
from good_res import good_res_list

#pdb_files = '/home/salah/mcce-charges/pdbs/'
#destination_runs = '/home/salah/johnChodera_project_on_github/mcce-charges/mcce_runs/quick/'

pdb_files = 'tests/'
destination_runs = 'output/'

# comment for testing
dirs_in_pdb_files = [d for d in os.listdir(
    pdb_files) if os.path.isdir(os.path.join(pdb_files, d))]


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def deleteHH(dirName, fname_base):
        # print fname_base
    lines_ = open(fname_base).readlines()
    for line in lines_:
        a = line
        # print a
        line = line.split()
        filename = fname_base.split('/')
        create_new = dirName + '/' + 'new' + filename[-1]
        with open(create_new, 'a') as tpl:
            if len(line) > 6:
                if line[3] != 'HOH' and line[3] in good_res_list:
                    if line[2][:1] != 'H' and line[2] != 'OXT':
                        tpl.write(a)
        tpl.close()


def deleteHH_edited(dirName, fname_base):
    # print fname_base

    lines_ = open(fname_base).readlines()
    for line in lines_:
        a = line
        line = line.split()
    filename = fname_base.split('/')
    print filename
    create_new = dirName + '/' + 'new' + filename[-1]
    print create_new
    """

            with open(create_new,'a') as tpl:
                    if len(line) > 6:
			if line[3] != 'HOH' and line[3] in good_res_list:
				if line[2][:1] != 'H' and line[2] != 'OXT':
                            		tpl.write(a)
            tpl.close()
    """


def change_runprm(runprm, prot, str1, str2, str3, str4):
    lines_ = open(runprm).readlines()
    for line in lines_:
        a = line
        line = line.split()
        # print line[-1]
        create_new = runprm + '2'
        with open(create_new, 'a') as prm:
            if len(line) != 0:
                if line[-1] == '(INPDB)':
                    newLine = 'new' + prot + '   ' + line[-1] + '\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_PREMCCE)':
                    newLine = str1 + '    ' + line[-1] + '\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_ROTAMERS)':
                    newLine = str2 + '    ' + line[-1] + '\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_ENERGY)':
                    newLine = str3 + '    ' + line[-1] + '\n'
                    prm.write(newLine)
                elif line[-1] == '(DO_MONTE)':
                    newLine = str4 + '    ' + line[-1] + '\n'
                    prm.write(newLine)
                else:
                    prm.write(a)

i = 0
# print dirs_in_pdb_files

# Here we loop over directories, each one of which contains a 'system',
# meaning a bunch of pdb files
for topDir in dirs_in_pdb_files:
    # print type(topDir)
    # within each directory, we pick up files
    onlyfiles = [f for f in os.listdir(
        pdb_files + topDir) if os.path.isfile(os.path.join(pdb_files + topDir, f))]

    pdbfile = topDir.split('-')
    # mydirectory is path to new directory where results will be stored, we
    # create it if it doesn't already exist
    mydirectory = destination_runs + pdbfile[0]
    if not os.path.exists(mydirectory):
        sys_call = 'mkdir ' + destination_runs + pdbfile[0]
        os.system(sys_call)
    #sys_call = 'cd ' + destination_runs + pdbfile[0] + '/'
    # os.chdir(sys_call)
    # loop over files in each directory
    for pdb_file in onlyfiles:
        # work only on pdbs with specific name, let's replace it with a 'pdb extension test'
        # if "_fixed_ph7.4.pdb" in pdb_file:
        if pdb_file.endswith(".pdb"):
            # print pdb_file[:4]
            # print pdbfile[0]
            # add a suffic to the pdb file name, (specific case) and make a
            # subdirectory in destination directory
            mydirectory = destination_runs + \
                pdbfile[0] + '/' + pdb_file[:4] + '_together'
            if not os.path.exists(mydirectory):
                sys_call = 'mkdir ' + destination_runs + \
                    pdbfile[0] + '/' + pdb_file[:4] + '_together'
                os.system(sys_call)
            # copy the pdb file into output subdirectory
            sys_call = 'cp ' + pdb_files + topDir + '/' + pdb_file + ' ' + \
                destination_runs + pdbfile[0] + \
                '/' + pdb_file[:4] + '_together'
            os.system(sys_call)
            # full path to pdb file
            fname_base = destination_runs + \
                pdbfile[0] + '/' + pdb_file[:4] + '_together' + '/' + pdb_file
            # full path of output directory
            dirName = destination_runs + \
                pdbfile[0] + '/' + pdb_file[:4] + '_together'
            # edit PDB file(noy sure what this function really does?)
            deleteHH(dirName, fname_base)
            # copy run.prm
            #sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce/run.prm ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
            sys_call = 'cp /home/kamran/mcce/run.prm.quick ' + \
                destination_runs + pdbfile[0] + \
                '/' + pdb_file[:4] + '_together'
            os.system(sys_call)
            # copy a sample submit.sh script
            sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce/submit.sh ' + \
                destination_runs + pdbfile[0] + \
                '/' + pdb_file[:4] + '_together'
            # os.system(sys_call)
            # print sys_call
            # full path of submit.sh
            infile = destination_runs + \
                pdbfile[0] + '/' + pdb_file[:4] + '_together' + '/submit.sh'
            # counter for mcce runs
            i += 1
            new_word = '-N mcce' + str(i)

            replace(infile, '-N mcce', new_word)
            runprm = destination_runs + \
                pdbfile[0] + '/' + pdb_file[:4] + '_together' + '/run.prm'
            print runprm
            """

			change_runprm(runprm,pdb_file,'t','t','t','f')
			sys_call = 'mv '+destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'+'/run.prm2 '+ destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'+'/run.prm'
                        os.system(sys_call)
			mysubmit = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
			#print mysubmit
			os.chdir(mysubmit)
			qsub_call = "qsub %s"
			call(qsub_call % "submit.sh", shell=True)
			time.sleep(2.0)
	"""
# print 'Done'
