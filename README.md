#### automate-mcce
Scripts to efficiently automate MCCE run on multiple systems.
The purpose of these scripts is to automate MCCE calculations on multiple PDB files. 
Future updates will also include, automated post-processing capabilities. 

#### Prerequisites
To run MCCE calculations in automated mode through `automated_mcce.py`, you will needthe anaconda python distribution and a working MCCE installtion.
#### Installation
You can simpy clone the repository and run the script. 
```
    git clone git@github.com:GunnerLab/automate-mcce.git
```
#### Usage
Script: `automated_mcce.py`

Help for `automated_mcce.py` (obtained via `python automated_mcce.py -h`) is:

```
Run MCCE on multiple PDB files

optional arguments:
  -h, --help            show this help message and exit

required arguments:
  -i INPUT_DIRECTORY, --input_directory INPUT_DIRECTORY
                        path to the directory containing input PDB files,
                        already preprocessed for MCCE calculations
  -d DESTINATION_DIRECTORY, --destination_directory DESTINATION_DIRECTORY
                        path to the directory where output of mcce
                        calculations will be stored.
  -e MCCE_DIRECTORY, --mcce_directory MCCE_DIRECTORY
                        path to the directory where MCCE is installed.
```

#### Example
As an example, you can run a sample mcce calculation on a directory containing pdb files inside the tests directory.
`python automated_mcce.py -i tests/test_pdbs/ -d ~/test/ -e ~/mcce`
Please note that this will run the quick MCCE protocol. To specify the type of MCCE protocol, you will have to edit the `automated_run` function in `automated_mcce`. For more information see help for class `MCCE_Params`.  