# Video Subtitle Removal Tool

This Jupyter Notebook demonstrates how to remove subtitles or text overlays from images using Python and OpenCV (cv2) for image processing techniques like thresholding, morphological operations, and inpainting.

![pipeline_img](../maydays/static/img/project_img/jedi_in_temple.jpg)

## Prerequisites
Ensure the following tools are installed and configured:

* Conda

```bash
conda install --file requirements.txt
```

## How It Works

The notebook follows these steps to remove subtitles from an image:
1. Load and Display Image: Loads the input image using OpenCV and displays it within the notebook.
2. Convert to Grayscale: Converts the image to grayscale for simpler processing.
3. Thresholding: Applies binary thresholding to create a binary mask of the areas with text.
4. Morphological Operations:
    * Closing: Uses morphological closing to fill small holes in the foreground text.
    * Dilation: Expands the text regions to connect disjointed parts.
5. Find Contours: Identifies contours in the processed image to locate the text regions.
6. Mask Creation: Creates a mask based on the detected text regions.
7. Inpainting: Uses the mask to inpaint (fill in) the text regions with surrounding image content to remove the subtitles.
8. Display Results: Displays the original image, processed stages (thresholded image, mask, cleaned image), and saves the cleaned image as cleaned_image.jpg.

## Notes
This notebook is designed for simple subtitle removal tasks and may require adjustments for complex images or video frames.
Ensure proper usage and adhere to copyright laws when processing images containing third-party content.

## Contributing
Contributions to the project are welcome! To contribute:

Fork the repository

Create a new branch (git checkout -b feature/my-feature)
Commit your changes (git commit -am 'Add a new feature')
Push the branch (git push origin feature/my-feature)
Open a Pull Request

## Author
Jean LECIGNE

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to adapt this template based on the specifics of your project, such as the repository name, technologies used, implemented features, etc. Ensure to provide clear instructions on installation, usage, and contribution to make your README informative and accessible to anyone interested in exploring or contributing to the project.
