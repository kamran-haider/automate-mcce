#!/usr/bin/python
import sys
import os
import time
import os.path
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call # This is needed to submit jobs

pdb_files = '/home/salah/mcce-charges/pdbs/'
destination_runs = '/home/salah/johnChodera_project_on_github/mcce-charges/mcce_runs/quick/'
# comment for testing
dirs_in_pdb_files = [d for d in os.listdir(pdb_files) if os.path.isdir(os.path.join(pdb_files, d))]
good_res_list = [
'26O',
'7MQ',
'ALA',
'ARG',
'ASN',
'ASP',
'BCB',
'BCL',
'BCR',
'BCT',
'BDL',
'BKB',
'BPB',
'BPH',
'_BR',
'_CA',
'CL1',
'CLA',
'CLD',
'_CL',
'_CL',
'CTR',
'CUA',
'CUB',
'_CU',
'CYD',
'CYL',
'CYS',
'DUA',
'FAL',
'FAR',
'FE2',
'FME',
'FS2',
'FS4',
'GLN',
'GLU',
'GLY',
'H3M',
'HA0',
'HA3',
'HAM',
'HAN',
'HCQ',
'HEAD2',
'HEA',
'HEB',
'HEC',
'HEF',
'HEM',
'HIB',
'HIB',
'HIL',
'HIS',
'HIS',
'HLI',
'HMA',
'HMB',
'HMC',
'HOH',
'ILE',
'_LA',
'LDA',
'LEU',
'LHG',
'LYS',
'MEL',
'MEM',
'MET',
'_MG',
'MYG',
'_NA',
'_NA',
'NH4',
'NS5',
'NTG',
'NTR',
'OCS',
'OEC',
'OPC',
'PAA',
'PDD',
'PEH',
'PHE',
'PHO',
'PL1',
'PL9',
'PL9',
'PQN',
'PRO',
'PTR',
'RSB',
'SER',
'SO4',
'THR',
'TML',
'TPO',
'TRP',
'TYF',
'TYL',
'TYR',
'UB1',
'UB6',
'UBQ',
'UNK',
'UQ2',
'VAL',
'_ZN',
'0WN',
'1N1',
'40L',
'AQ4',
'B49',
'BOS',
'EMH',
'FMM',
'KIM',
'LQQ',
'NIL',
'RXT',
'TRA',
'XIN',
'ZD6',
'276',
'4MK',
'AXI',
'BAX',
'CAB',
'EUI',
'IRE',
'LEV',
'MI1',
'P06',
'STI',
'VGH',
'YY3',
'0WN',
'1N1',
'40L',
'AQ4',
'B49',
'BOS',
'EMH',
'FMM',
'KIM',
'LQQ',
'NIL',
'RXT',
'TRA',
'XIN',
'ZD6',
'276',
'4MK',
'AXI',
'BAX',
'CAB',
'EUI',
'IRE',
'LEV',
'MI1',
'P06',
'STI',
'VGH',
'YY3',
]


def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)	


def deleteHH(dirName,fname_base):
        #print fname_base
        lines_ = open(fname_base).readlines()
        for line in lines_:
                a = line
                #print a
                line = line.split()
		filename = fname_base.split('/')
		create_new = dirName+'/' + 'new'+filename[-1]
                with open(create_new,'a') as tpl:
                        if len(line) > 6:
				if line[3] != 'HOH' and line[3] in good_res_list:
					if line[2][:1] != 'H' and line[2] != 'OXT':
                                		tpl.write(a)
                tpl.close()



def change_runprm(runprm,prot,str1,str2,str3,str4):
	lines_ = open(runprm).readlines()
	for line in lines_:
                a = line
                line = line.split()
		#print line[-1]
		create_new = runprm+'2'
		with open(create_new,'a') as prm:
			if len(line) != 0:
				if line[-1] == '(INPDB)':
					newLine = 'new'+prot+'   '+line[-1]+'\n'
					prm.write(newLine)
				elif line[-1] == '(DO_PREMCCE)':
					newLine = str1+'    '+line[-1]+'\n'
                                        prm.write(newLine)
				elif line[-1] == '(DO_ROTAMERS)':
                                        newLine = str2+'    '+line[-1]+'\n'
                                        prm.write(newLine)
				elif line[-1] == '(DO_ENERGY)':
                                        newLine = str3+'    '+line[-1]+'\n'
                                        prm.write(newLine)
				elif line[-1] == '(DO_MONTE)':
                                        newLine = str4+'    '+line[-1]+'\n'
                                        prm.write(newLine)
				else:
					prm.write(a)
				
i = 0

print dirs_in_pdb_files

for topDir in dirs_in_pdb_files:
	#print type(topDir)
	onlyfiles = [f for f in os.listdir(pdb_files+topDir) if os.path.isfile(os.path.join(pdb_files+topDir, f))]
	pdbfile = topDir.split('-')
	mydirectory = destination_runs + pdbfile[0]
	if not os.path.exists(mydirectory):
		sys_call = 'mkdir ' + destination_runs + pdbfile[0]
		os.system(sys_call)
	#sys_call = 'cd ' + destination_runs + pdbfile[0] + '/'
	#os.chdir(sys_call)
	for pdb_file in onlyfiles:
		if "_fixed_ph7.4.pdb" in pdb_file:
			#print pdb_file[:4]
			#print pdbfile[0]
			mydirectory = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
			if not os.path.exists(mydirectory):
				sys_call = 'mkdir ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together' 
				os.system(sys_call)
			sys_call = 'cp ' + pdb_files + topDir + '/' + pdb_file + ' ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
			os.system(sys_call)
			fname_base = destination_runs + pdbfile[0] + '/' + pdb_file[:4]+'_together' + '/' + pdb_file
			dirName =  destination_runs + pdbfile[0] + '/' + pdb_file[:4]+'_together'
			deleteHH(dirName,fname_base)
			sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce/run.prm ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
			os.system(sys_call)
			sys_call = 'cp /home/salah/johnChodera_project_on_github/mcce-charges/mcce/submit.sh ' + destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
                        os.system(sys_call)
			infile = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together' + '/submit.sh'
			i += 1
			new_word = '-N mcce'+str(i)
			replace(infile,'-N mcce',new_word)
			runprm = destination_runs+pdbfile[0]+'/'+pdb_file[:4]+'_together'+'/run.prm'
			change_runprm(runprm,pdb_file,'t','t','t','f')
			sys_call = 'mv '+destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'+'/run.prm2 '+ destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'+'/run.prm'
                        os.system(sys_call)
			mysubmit = destination_runs + pdbfile[0] + '/'+ pdb_file[:4]+'_together'
			#print mysubmit
			os.chdir(mysubmit)
			qsub_call = "qsub %s"
			call(qsub_call % "submit.sh", shell=True)
			time.sleep(2.0)
print 'Done'
