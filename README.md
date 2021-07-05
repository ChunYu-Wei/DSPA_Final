# README
## File Discription
/testcase/* : testcases
/data/* : expiriment results
./genData.py : program used to generate data
./main.py : program that used to test **Map**
./Map.py : an API of **Map**
./example.py : the example of usage of **Map**
./stddic.py : the example of usage of standard dictionary

## Dependency
python3

## Environment
On Linux machine

## Usage
### ./genData.py 
To generate the testcase
Need to define the output filename and the numer of operations in the generated case
>python3 ./genData.py --output <output filename> --num <number of operations>
ex: python3 ./genData.py --output 1000.in --num 1000

### ./main.py 
Run the testcase
>python3 ./main.py --input <input filename>
operation>
ex: python3 ./main.py --input 1000.in 

### ./example.py
>python3 ./example.py

### ./stddic.py
>python3 ./stddic.py

