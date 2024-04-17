#Import Statements and Function to Download Model Weights
import os
import requests
import yaml
import glob as glob
from mmdet.apis import init_detector
def download_weights(url, file_save_name):
    """
    Download weights for any model.
    :param url: Download URL for the weihgt file.
    :param file_save_name: String name to save the file on to disk.
    """
    # Make chekcpoint directory if not presnet.
    if not os.path.exists('checkpoint'):
        os.makedirs('checkpoint')
    # Download the file if not present.
    if not os.path.exists(os.path.join('checkpoint', file_save_name)):
        file = requests.get(url)
        open(
            os.path.join('checkpoint', file_save_name), 'wb'
        ).write(file.content)