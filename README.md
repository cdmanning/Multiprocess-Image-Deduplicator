# Multiprocess-Image-Deduplicator
Multiprocess Image Deduplicator is a high-performance Python utility that uses perceptual hashing to detect duplicate images across different image formats (.png, .jpg, .jpeg). While leveraging multiprocessing to scale the workload across your CPU cores, this utility will detect duplicate images without wasting time or your systems memory. Unlike scripts that rely on pixel-perfect match detection, this deduplicator utility analyzes the structural features of your images. If you've converted a PNG to a JPG, or compressed a photo to save space, this script should still catch it.


## ✨ Features

* Dynamically scales to utilize every available core on your CPU, cutting down processing times
* Successfully matches duplicate images even if they have been converted between .png, .jpg, and .jpeg
* Uses a 16-bit perceptual hash size to virtually eliminate false positives on large libraries
* Groups duplicates on the fly directly inside worker subprocesses to ensure O(N) time efficiency and minimal memory usage
* Moves all copies of detected duplicate pairs into a dedicated folder, allowing you to double-check for false positives.


## 🚀 Getting Started

1. Clone the repository using: `git clone https://github.com/cdmanning/Multiprocess-Image-Deduplicator.git`

2. Ensure you have [Python 3.12][1] installed and correctly added to your system PATH.

3. Run `setup.bat` to automatically install all required Python libraries and generate the necessary project folders.

4. Place the images that you wish to be deduplicated inside the `Inputs` folder. 

    * A sample dataset has already been places inside `Inputs` feel free to delete it before running the utility

4. Run `run.bat` to run the utility.

[1]: https://www.python.org/downloads/
