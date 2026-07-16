import math
import multiprocessing
from multiprocessing import Process, Queue
import os
from PIL import Image
import imagehash
from collections import defaultdict
import shutil
from pathlib import Path


def hash_images(subset, image_folder, qout):
    local_structure = defaultdict(list)
    for filename in subset:
        try:
            with Image.open(Path(image_folder, filename)) as img:
                img_hash = imagehash.phash(img, hash_size=16)
                local_structure[img_hash].append(filename)
        except Exception as e:
            print(f"Skipping damaged file {filename}: {e}")
    qout.put(local_structure)


def compute_hashes(image_folder, image_files, number_of_files):

    num_workers = min(multiprocessing.cpu_count(), len(image_files))
    chunk_size = math.ceil(number_of_files / num_workers) if number_of_files > 0 else 1
    merged_structure = defaultdict(list)
    qout = Queue()
    subsets = [
        image_files[i : i + chunk_size] for i in range(0, len(image_files), chunk_size)
    ]
    processes = [
        Process(target=hash_images, args=(subset, image_folder, qout))
        for subset in subsets
    ]
    for process in processes:
        process.start()
    for _ in processes:
        local_structure = qout.get()
        for img_hash, filenames in local_structure.items():
            merged_structure[img_hash].extend(filenames)
    for process in processes:
        process.join()
    return merged_structure


def checkImages(image_folder, merged_structure):
    duplicates = []
    for filenames in merged_structure.values():
        if len(filenames) > 1:
            duplicates.extend(filenames)
    if not duplicates:
        print("No duplicate images found.")
        return
    print(f"Found {len(duplicates)} duplicate files. Moving them now...")
    path = Path(os.getcwd(), "Duplicate Images")
    os.makedirs(path, exist_ok=True)
    for val in duplicates:
        file_to_move = Path(image_folder, str(val))
        if file_to_move.exists():
            shutil.move(file_to_move, path)


def preparation():
    image_folder = Path("Inputs")
    image_files = [
        file.name
        for file in image_folder.iterdir()
        if file.is_file() and file.suffix.lower() in (".jpg", ".jpeg", ".png")
    ]
    number_of_files = len(image_files)
    return image_folder, image_files, number_of_files


if __name__ == "__main__":
    image_folder, image_files, number_of_files = preparation()
    if number_of_files == 0:
        print("No images found in the Input folder.")
    else:
        merged_structure = compute_hashes(image_folder, image_files, number_of_files)
        checkImages(image_folder, merged_structure)
