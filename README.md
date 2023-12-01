# Sentinel-2 Image Matching Project

This project is dedicated to developing an algorithm for matching Sentinel-2 satellite images. The core of the algorithm involves keypoint detection and image matching, offering valuable insights into corresponding points across different images.

## Directory Structure and Files

- `cv_algorithm.py`: Houses the implementation of the keypoint detection and image matching algorithm.
- `md_inference.py`: A Python script designed for executing image matching between two specified input images.

### Running the Inference Script

To execute the image matching algorithm and generate matches between two images, utilize the `md_inference.py` script.

Specify paths to images and the desired number of matches.

### Issues and Limitations

While the algorithm excels in matching images from different bands of the same scene, limitations may arise when matching images from different seasons, as illustrated in the demo.

### Dependencies

Install the dependencies using:

```bash
pip install -r requirements.txt
```

### Acknowledgments

The project utilizes images from the [Deforestation in Ukraine from Sentinel2 data](https://www.kaggle.com/datasets/isaienkov/deforestation-in-ukraine) dataset.