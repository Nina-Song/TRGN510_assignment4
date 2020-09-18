# TRGN 510 Assignment 4
  * In this program, it takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has become a HUGO name.
  
## Installation
* Clone
  * In order to get this repository on your local machine, using `git clone` to install this program
  ```
  git clone https://github.com/Nina-Song/TRGN510_Assignment4.git
  ```
* Download the GTF file
  * You need to read the `Homo_sapiens.GRCh37.75.gtf` to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.
  * `Homo_sapiens.GRCh37.75.gtf` can be download using the following code in your terminal
  ```
  wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz
  ```
  and unzip the `.gz` file to the path of where the program is located by `gunzip Homo_sapiens.GRCh37.75.gtf.gz`
  * This program also provides the Unit Test file `expression_analysis.csv` which can be reached by following:
  ```
  git clone https://github.com/davcraig75/unit
  ```

## Usage
  * Run the script on the Unit Test file and create a file with the `ENSG` name converted to `HUGO` name by 
  ```
  ./ensg2hugo.py -f2 expression_analysis.csv > expression_analysis.hugo.csv
  ```
   where `-f2` would pick the 2nd column in the `expres.anal.csv`.
  * This program allow an option `-f [0-9]` to select the column which contains the `ENSG` name originally. If there is no `-f` then the first column is used.
  
## Dependencies
  * wget
  * os
  * re
  * sys
  * pandas
  * dictionary
  * git

## Known issue
  * The dictionary in this program is build based on the `Homo_sapiens.GRCh37.75.gtf`, which is not comprehensive. Some of the Ensembl gene names may not be find a match. In this case, it will result `NaN` in the column.
  
## Contact
  * Nina Song songjiar@usc.edu
