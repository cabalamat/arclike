# ARC-solution

[ARC-solution](https://github.com/top-quarks/ARC-solution) by Johan Sokrates Wind was the winning solution to the 2020 ARC Challenge.

It was written in C++ with some Python code which runs the C++ code.

## How it works

The git repository includes a PDF which gives a brief explanation of how it works.

It has a series of image transformation functions, which typically take an image as input, do something with it, and return another image as output.

The most important image transformations are:

* `Cut (image) → list of images`. Tries to ﬁgure out a background color and splits the remaining pixels into corner connected groups.
* `filterCol (image, color) → image`. Erases all colors except the given one (sets them to 0).
* `colShape (image, color) → image`. Change all non-zero pixels to ”color”.
* `composeGrowing (list of images) → image`. Stack the list of images on top of each other, treating 0 as transparent. The image with the fewest non-zero pixels is at the top.
* `compress (image) → image`. Extract minimal sub-image containing all non-zero pixels.
* `rigid (image, id) → image`. Perform rotation (0/90/180/270 degrees) and/or ﬂip.
* `pickMax (list of images, id) → image`. Extract the image with maximum property, for example id = 0 extracts the image with the most non-zero pixels.