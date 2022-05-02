from PIL import Image
from glob import glob
from os import path
from shutil import copytree, rmtree


def get_all_file_names(dir_name: str) -> list:
    """
    Recursively gets all file names from given directory

    Args:
        dir_name (str): Directory name
    Returns:
        list: Names of all files in directory
    """
    all_names = sorted(glob(path.join(dir_name, "*.png")))
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
    for image_name in file_names:
        Image.open(image_name).resize(new_size).save(image_name)


if __name__ == "__main__":
    process_images((136, 136))
