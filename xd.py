from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt

im = io.imread('./allimages/Capture0.PNG', as_gray=True)
val = filters.threshold_otsu(im)
drops = ndimage.binary_fill_holes(im < val)
plt.imshow(drops, cmap='gray')
plt.show()

from skimage import measure
labels = measure.label(drops)
print(labels.max())
