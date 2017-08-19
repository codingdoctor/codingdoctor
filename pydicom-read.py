import dicom
import os
import numpy
from matplotlib import pyplot, cm

PathDicom = "./image/"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
  for filename in fileList:
    if ".dcm" in filename.lower():  # check whether the file's DICOM
    lstFilesDCM.append(os.path.join(dirName,filename))

# Get ref file
RefDs = dicom.read_file(lstFilesDCM[1])

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))
# print('Dimension in Ref file: {}'.format(RefDs.pixel_array.shape))
# print('Dim + slides: {} px x {} px x {} slides'.format(RefDs.Rows, RefDs.Columns, len(lstFilesDCM)))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))
x = numpy.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = numpy.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
z = numpy.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])

# The array is sized based on 'ConstPixelDims'
ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)
# print('Dim in numpy array: {}'.format(ArrayDicom.shape))

# loop through all the DICOM files
for filenameDCM in lstFilesDCM[1:-1]: # Modify to get desired slides
  # read the file
  ds = dicom.read_file(filenameDCM)
  # store the raw image data
  ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array

## display CT
show_num = 11
print('Showing number: {}'.format(show_num))
pyplot.figure(dpi=150)
pyplot.title('Slide Number: {}'.format(show_num))
pyplot.axes().set_aspect('equal', 'datalim')
# pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, numpy.flipud(ArrayDicom[:, :, show_num]))
pyplot.show()
