# SHML Coding Challenge
## The objectives of this challenge
* Plugging missing parts in our segmentation pipeline
* Generating Filter Maps using pre-trained model.
* Generating Feature Maps using pre-trained model.

<br>

### Your Computer
Please first clone or download as .zip file of this repository.

Working on the assignment in a virtual environment is highly encouraged.

In this assignment, we recommend you use Python `3.8.5` 

You will need to make sure that your virtualenv setup is of the correct version of python. 

We will be using *PyTorch* in this assignment.

Please see below for executing a virtual environment. You will need to install Anaconda before following the next steps

```shell
cd SHML_Coding_Challenge
conda env create -f environment.yml
conda activate dl_crack

# Install dependencies
cat requirements.txt | xargs -n 1 pip install

# Work on the assignment

# Deactivate the virtual environment when you are done
conda deactivate
```

## Working on the Problem

You will execute the following shell command to invoke the python code

```shell
python SHML_assignment.py --model Linknet --backbone densenet169 --image-path './data/11215-11.jpg'
```

As you might have already guessed, the above command will not go through. To successfully execute the program, you need to develop and plug your code in the missing parts. In the file `SHML_assignment.py`, we indicate `TODO` or `Your Code` for you to fill in with your implementation.

You only need to edit this python file, and only inside the specified TODO blocks!


## PLEASE DO NOT MODIFY ANY PART OF THE CODE OUTSIDE THE TODO BLOCKS. YOU DO NOT NEED TO IF YOU DO IT RIGHT!


Your part of the code should fit our designed pipeline. You may be penalized if we find you have modified any part of the code which you were not supposed. We have given clear indications for where you need to add your code.


## How to submit

Run the following command to zip all the necessary files for submitting your assignment.

```shell
sh collectSubmission.sh <USC_ID>
```

This will create a file named `<USC_ID>.zip` (eg. 4916525888.zip). Please submit this file through the [Google form]().
If you have to create own .zip file, make sure to ONLY include the files and folders given in the `collectSubmission.sh` script file, and name your file as `<USC_ID>.zip`.

We will deduct points if you don't follow the above submission guideline.
