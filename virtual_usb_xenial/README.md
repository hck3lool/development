Preconditions:
	- HOST:
		- Distributor ID: Ubuntu
		- Description: Ubuntu 16.04.1 LTS
		- Release: 16.04
		- Codename: xenial

# How to run?

#@ Setup environment in the HOST ---------------------------------------------------------------------
# Please grant permissions for all scripts
	- chmod 777 {script_name}

1. Executes the script sudo ./01_build_modules
	1.1 Check the virtual images exist into the folder created
2. Executes the script sudo ./02_enable_modules
	2.1 Check each module was loaded with the command --> lsmod | grep {module_name} 
3. Executes the script sudo ./03_create_partitions
	3.1 Wait 15 seconds and verify the partitions (sdb1 and sdc1) exists whit the command --> ls -l /dev/sd*
4. Executes the script sudo ./04 docker installation (omit if you have installed Docker previously)
5. Navigates into the docker folder and executes sudo ./install.sh
	5.1 Check the images was created with the command --> sudo docker image ls
		- philippines
		- ubuntu 14.04


#@ Setup container environment ----------------------------------------------------------------------

1. Executes the command sudo docker run -it --privileged philippines
	1.1 Check in /root path appears the following folders:
		- automated-tests
		- data
		- machine-scripts
		- main-files
		- packages
		- vnc

2. Navigates into the machine-scripts folder and executes sudo ./main-script.sh


#@ Run automation tests -----------------------------------------------------------------------------

1. Navigates into the machine-scripts folder and executes sudo ./run-tests.sh


# Note: Only if is neccessary
#@ Disable modules ----------------------------------------------------------------------------------

1. If you want disable the modules created executes the script disable_modules.sh

