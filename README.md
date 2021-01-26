# SHML Coding Challenge
## The objectives of this challenge

* Plugging missing parts in our segmentation pipeline
* Generating Filter Maps using pre-trained model.
* Generating Feature Maps using pre-trained model.

## Your Computer

Please first clone or download as .zip file of this repository.
Working on the assignment in a virtual environment is highly encouraged.
In this assignment, we recommend you use Python `3.8.5` 

You will need to make sure that your virtualenv setup is of the correct version of python. 
We will be using *PyTorch* in this assignment.

Please see below for executing a virtual environment. You will need to install Anaconda before following the next steps

<br>

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
<br>

## Context

Given is the part of the code base for our crack segmentation project. We have already provided our trained model and have set up the barebone pipeline for generating filter maps and feature maps. However, you need to plug in your implementations for few core functions in order to complete the feature extraction program.

To have a fair assessment, we have scoped the computational complexity of the project in a way that you would not need GPUs or Cloud Computing Resources in order to demonstrate your coding abilities. We have done the heavy lifiting for you and all you need to have is a really good understanding of Deep Learning, Image Segmentation, Python and Pytorch (and ofcourse, a working modern computer :D)

The model we are using and which you need to initialize is from the pytorch segmentation library. You may need to go through the following link when you reach the model initialization part of the problem.

[Pytorch Segmentation Library](https://github.com/qubvel/segmentation_models.pytorch).

## Working on the Problem

You will execute the following shell command to invoke the python code

<br>

```shell
python SHML_assignment.py --model Linknet --backbone densenet169 --image-path './data/11215-11.jpg'
```
<br>

As you might have already guessed, the above command will not go through. To successfully execute the program, you need to develop and plug your code in the missing parts. In the file `SHML_assignment.py`, we indicate `TODO` or `Your Code` for you to fill in with your implementation.

You only need to edit this python file, and only inside the specified TODO blocks!

### PLEASE DO NOT MODIFY ANY PART OF THE CODE OUTSIDE THE TODO BLOCKS. YOU DO NOT NEED TO IF YOU DO IT RIGHT!

Your part of the code should fit our designed pipeline. Your work may not be considered if we find you have modified any part of the code which you were not supposed. We have given clear indications for where you need to add your code.

## How to verify your implementation

Check the following three steps:

1. The above shell command should execute the program without failing at any point.
2. There should be 6 different filter maps in the `./filter_maps` folder
3. There should be 17 different feature maps in the `./feature_maps` folder

## How to submit

Run the following command to zip all the necessary files for submitting your assignment.

```shell
sh collectSubmission.sh <USC_ID>
```

This will create a file named `<USC_ID>.zip` (eg. 4916525888.zip). Please submit this file through the [Google form](https://forms.gle/d7XqErfT4aAkdCWHA).

If you have to create own .zip file, make sure to ONLY include the files and folders given in the `collectSubmission.sh` script file, and name your file as `<USC_ID>.zip`.
