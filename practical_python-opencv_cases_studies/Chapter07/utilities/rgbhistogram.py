import cv2


class RGBHistogram:
	def __init__(self, bins):
		# Store the number of bins the histogram will use
		self.bins = bins

	def describe(self, image, mask=None):
		# Compute a 3D histogram in the RGB colorspace, then normalize the histogram so that images
		# with the same content will have roughly the same histogram
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
		cv2.normalize(hist, hist)

		# Return the 3D histogram as a flattened array
		return hist.flatten()
