# projectpccv2
This is the cgi supported version of projectpcc.

* ABOUT *

Gene expression/Disease Severity Correlation Checker based on Real-Time PCR Experiment.

Source code can be from the repository here:
https://github.com/aydinme/projectpccv2

Screenshots of a step by step demo run can be found in the same repository

Link to tool: 
http://bfx3.aap.jhu.edu/maydin1/finalproject/index.cgi


Summary of the Program:
	This program is an external tool to check for gene expression/severity
correlations based on Real-Time PCR experiments. In a Real-Time Experiment, readings
are acquired from different filters. This program assumes that there are two readings;
1 for target gene which is from the FAM Channel, the other for control gene which is from the HEX Channel..
	There are many Real-Time PCR Softwares out there that exports different outputs. However, all of them has these following titles;

Label	Target Channel	Ct Value 	Control Channel 	Ct Value	Extra Info

	Based on the Real-Time PCR Instrument we are using, the program should be modified since outputs would be different. This version 1 of the program	assumes that the Real-Time PCR export data is within the following format;

Channel1	Channel2	Severity Score
ct value1	ct value1	severity value 1
ct value2	ct value2	severity value 2
ct value3	ct value3	severity value 3
...		...		...
...		...		...
...		...		...

Then the program calculates the expression correlation based on severity scores 
and displays them within a boxplot.. 


Step by step Instructions for the use of program:

1) Open your browser and go to the following site.
http://bfx3.aap.jhu.edu/maydin1/finalproject/index.cgi

2) Enter the number of samples you have and click submit.

3) Enter the ct values for the target gene and control gene on the first two columns.
	Enter the severity score on the final column.

4) Click Submit.

5) If the values are valid, the tool will confirm that a file has been created
based on your inputs. 

6) The program will output a boxplot for this correlation relation and show mean expression values based on the inputs.


