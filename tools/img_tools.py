from PIL import Image
import numpy as np
from glob import glob
from os import path
from shutil import copytree, rmtree


class Fix_Image:

    def __init__(self) -> None:
        pass

    def resize(self, img: Image, new_size: tuple) -> Image:
        return img.resize(new_size)

    def remove_blank(self, img: np.array) -> Image:
        """
        Removes blank white space around unit icon
        Args:
            img (np.array): Input image
        Returns:
            Image: PIL Image
        """
        h, w = img.shape[:2]
        img = img.reshape(-1, 4)
        img *= (img != [255, 255, 255, 0]).astype(np.uint8)
        return Image.fromarray(img.reshape(h, w, 4))


def get_all_file_names(dir_name: str) -> list:
    """
    Recursively gets all file names from given directory
    Args:
        dir_name (str): Directory name
    Returns:
        list: Names of all files in directory
    """
    all_names = sorted(glob(path.join(dir_name, "*")))
    collected_names = []
    for name in all_names:
        if path.isfile(name):
            collected_names.append(name)
        elif path.isdir(name):
            collected_names += get_all_file_names(name)
    return collected_names


def process_images(new_size: tuple) -> None:
    """
    Transforms raw image data to processed unit icons. REMOVES ./data directory
    Args:
        new_size (tuple): Size of cleaned images
    """
    if path.exists("./data"):
        rmtree("./data")
    copytree("./raw_data", "./data")
    file_names = get_all_file_names("./data/cards")
    fixer = Fix_Image()
    for image_name in file_names:
        img = np.asarray(Image.open(image_name))
        img = fixer.remove_blank(img)
        img = fixer.resize(img, new_size)
        img.save(image_name)
