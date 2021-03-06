import argparse
import os
import cv2
import sys
import shutil

import numpy as np
import torch
import torch.nn as nn
import torchvision

import matplotlib
import matplotlib.pyplot as plt
import albumentations as A

import segmentation_models_pytorch as smp
from segmentation_models_pytorch.encoders import get_preprocessing_fn

IMG_DIMS = 512
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def get_children(model: torch.nn.Module):
    """Generate Feature Maps
    Args:
        model: Segmentation Model intitalized from smp library
    Return:
        flatt_children: List of deeply neseted flattened children
    """

    flatt_children = []    
    #####################################################################################
    # TODO:Flatten model architecutre and returns a list of all nested child layers #
    #####################################################################################

    # HINT: Think recursively to parse and append deeply nested children 

    # TIP: if model has no children; model is last child! :O, 
    #      else look for children from children...to the last child
    
    ####################################################################################
    #                                   END OF YOUR CODE                               #
    ####################################################################################    

    return flatt_children

def save_plot(plt, fig, save_dir):
    """Plot Saver
    Args:
        plt: matplotlib pyplot
        fig: figure of the plot
        save_dir: path to save the generated filter map plot
    Return:
        None
    """ 
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)    
    plt.savefig(save_dir + '.png', bbox_inches='tight', pad_inches = 0)

def vistensor(tensor, save_dir, ch=0, allkernels=False, nrow=8, padding=1): 
    """Visuzlization Tensor
    Args:
        tensor: image/kernel tensor
        save_dir: path to save the generated filter map plot
        ch: visualization channel 
        allkernels: visualization all tensores
        nrow: number of rows
        padding: pads to add
    Return:
        None
    """ 
    
    n,c,w,h = tensor.shape
    if allkernels: tensor = tensor.view(n*c,-1,w,h )
    elif c != 3: tensor = tensor[:,ch,:,:].unsqueeze(dim=1)
        
    rows = np.min( (tensor.shape[0]//nrow + 1, 64 )  )    
    grid = torchvision.utils.make_grid(tensor, nrow=nrow, normalize=True, padding=padding)
    plt.figure( figsize=(nrow,rows))
    fig = plt.imshow(grid.numpy().transpose((1, 2, 0)), cmap=matplotlib.cm.jet, aspect='auto')
    save_plot(plt, fig, save_dir)

def generate_filter_maps(conv_layers, weights, layer_num):
    """Filter Maps Generator
    Args:
        conv_layers: List of all convolutional layers of the model
        weights: List of weights corresponding to the conv layers
        layer_num: layer_num to generate the specific filter map
    Return:
        None
    """ 

    if not layer_num < len(weights):
        print('Given Layer num exceeds the maximum CNN layer present in the architecture. Extracting the map of the last layer:')
        layer_num = len(weights)-1
    save_dir = os.path.join('./filter_maps', str(conv_layers[layer_num]))
    kernel = weights[layer_num].data.clone()
    vistensor(kernel, save_dir, ch=0, allkernels=False)

def generate_feature_maps(model_blocks, tensor, save_path, layer_num):
    """Generate Feature Maps
    Args:
        model_blocks: List of first layer encoder + decoder blocks
        tensor: processed and permuted image tensor
        save_path: location to save feature map
        layer_num: layer number to extract feature map from
    Return:
        None
    """

    ######################################################################################
    # TODO: Generate and save feature map of the given layer number from image tensor #
    ######################################################################################

    # HINT: Iterating through the model blocks can help you get output of specific layer
    # TIP: You can use the given save plot function after populating the feature map plot 


    
    ######################################################################################
    #                                   END OF YOUR CODE                                #
    ######################################################################################    

def augmentation():
    """Add paddings to make image shape divisible by 32"""

    test_transform = [
        A.PadIfNeeded(IMG_DIMS, IMG_DIMS)
    ]
    return A.Compose(test_transform)

def preprocessing(preprocessing_fn):
    """Construct preprocessing transform

    Args:
        preprocessing_fn (callbale): data normalization function
            (can be specific for each pretrained neural network)
    Return:
        transform: albumentations.Compose

    """
    _transform = [
        A.Lambda(image=preprocessing_fn),
    ]
    return A.Compose(_transform)

def process_image(image):
    """Image Processing

    Args:
        Input Image
    Return:
        Processed Image
    """

    ### Rescale the images
    scale_h = img_rows / image.shape[0]
    scale_w = img_cols / image.shape[1]
    image = cv2.resize(image, dsize=(img_rows, img_cols), fx=scale_h, fy=scale_w)

    ### Image Augmentation
    sample = augmentation()(image = image)
    image = sample['image']

    ### Image Preprocessing
    sample = preprocessing(preprocess_input)(image=image)
    image = sample['image']
    image = torch.from_numpy(image).permute(2,0,1).float()

    return image


def add_args(parser):
    """Argumet Parser
    Args:
        parser : argparse.ArgumentParser
    Return:
        args: parsed arguments
    """

    ##########################################################################
    # TODO: Populate parser with input arguments we will use to execute code #
    ##########################################################################

    # Add parser argument for "--model"

    # Add parser argument for "--backbone"
    
    # Add parser argument for "--data_dir"

    ############################################################################
    #                               END OF YOUR CODE                           #
    ############################################################################
    
    args = parser.parse_args()
    return args    

def create_model(args, classes, activation):
    """Model Initializer
    Args:
        args: Input arguments parsed through parser
        classes: Number of output classes
        activation: Activation Method
    Return:
        Initalized Segmentaion Model
    """
    
    ####################################################################################################
    # TODO: Initialize and return segmentation model through segmentation library (smp)                #
    # TIP: Here is the link to the library repo: https://github.com/qubvel/segmentation_models.pytorch
    ####################################################################################################
    
    # HINT: Get the model name and args from parser
    

    ####################################################################################################
    #                                               END OF YOUR CODE                                   #
    ####################################################################################################

    return model

if __name__ == "__main__":

    #########################################################################################
    # You need to complete TODO block in the add_args function to proceed at this point #
    #########################################################################################
    parser = argparse.ArgumentParser()
    args = add_args(parser)

    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    ### Creating directories to save filter maps and feature maps
    dirs = ['./filter_maps/', './feature_maps/']

    for path in dirs:
        if os.path.exists(path):
            shutil.rmtree(path)
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

    ### Get Preprocessing Function
    preprocess_input = get_preprocessing_fn(args.backbone, pretrained='imagenet')

    ### Set Image Dimensions
    img_rows, img_cols = IMG_DIMS, IMG_DIMS

    # Load and process Image
    image = cv2.imread(args.image_path)
    image = process_image(image)

    # Parameters for model
    n_classes = 1
    activation = 'sigmoid'

    #################################################################################################
    # You need to complete TODO block in the create_model function to proceed at this point         #
    # In addition to that, you need to download the model weights from the following drive          #
    # Weights: https://drive.google.com/drive/folders/1yQGjA0sZbQFKC3Nk4lQ-0IsA067VUBdp?usp=sharing #
    # Please save the weights in the same directory where this file resides                         #
    #################################################################################################

    best_model = create_model(args, n_classes, activation)
    checkpoint = torch.load('best_model_iou.pth', map_location=DEVICE)
    best_model.load_state_dict(checkpoint['model_state_dict'])


    #########################################################################################
    # You need to complete TODO block in the get_children function to proceed at this point #
    #########################################################################################

    # Populate get_children function to flatten the model architecture
    model_children = get_children(best_model)

    assert len(model_children) == 557, "Total Number of Layers should be 557!"
    print('Total Number of Layers:', len(model_children))

    conv_layers = []
    model_weights = []

    ###########################################################################################
    # TODO: Fetch all the convolutional layers and their corresponding model weights          #
    ###########################################################################################

    ### HINT:
    # Iterate through model children you just flattened.
    # Append the layers of interest and their weights to the respective lists initalized above.
    
    ###########################################################################################
    #                                       END OF YOUR CODE                                  #
    ###########################################################################################

    assert len(conv_layers) == 179, "Total conv Layers should be 179!"
    assert len(model_weights) == 179, "Should have weghts for all (179) Convolutional Layers!"
    print('Total Conv Layers: ', len(conv_layers))

    # Generating and saving filter maps
    for i in range(len(conv_layers)):
        if i%25 == 0:
            generate_filter_maps(conv_layers, model_weights, i)


    model_blocks = []
    #####################################################################################
    # TODO: Populate model_blocks list with all the first-level features of encoder and 
    # first-level blocks of decoder #
    #####################################################################################

    # Append all the features of encoder to model_blocks
    ### HINT: Printing model architecture / summary may help to find features to append


    # Append all the blocks of decoder to model_blocks
    ### HINT: Printing model architecture / summary may help to find blocks to append
    
    ####################################################################################
    #                                   END OF YOUR CODE                               #
    ####################################################################################
    
    assert len(model_blocks) == 17, "Number of model (encoder+decoder) blocks should be 17!"
    print('Total blocks: ',  len(model_blocks))

    # Set model to eval
    best_model.to(DEVICE)
    best_model.eval()

    # Align the image dimensions
    x_tensor = image.to(DEVICE).unsqueeze(0)

    ########################################################################################################
    # You need to complete TODO block in the generate_feature_maps function to successfully run this loop
    ########################################################################################################
    for i in range(len(model_blocks)):
        save_path = os.path.join('./feature_maps', 'layer_' + str(i) +'.png')
        generate_feature_maps(model_blocks, x_tensor, save_path, i)

    print('Assignment Successfully Completed: Please check filter_maps and feature_maps directories and verify your outputs')
    