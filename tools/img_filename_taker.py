from img_tools import get_all_file_names
import json
import os

if __name__ == "__main__":
    filenames = get_all_file_names("../raw_data/cards")
    dump_dict = {}
    for i, fname in enumerate(filenames):
        splitted_path = fname.split("/")
        dump_dict[os.path.join(splitted_path[-2], splitted_path[-1])] = i
    json.dump(dump_dict, open("names.json", "w"), indent=1)
