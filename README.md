#### automate-mcce
Scripts to efficiently automate MCCE run on multiple systems.

#### Prerequisites

automated_mcce.py requires the anaconda python installation. A working MCCE installtion is also required.
#### Installation
You can simpy clone the repository and run the script. 
    git clone https://github.com/MobleyLab/alchemical-analysis.git
    cd alchemical-analysis
    sudo python setup.py install

#### Usage

Script: `automated_mcce`

Help for `automated_mcce.py` (obtained with `python automated_mcce.py -h`) is:

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