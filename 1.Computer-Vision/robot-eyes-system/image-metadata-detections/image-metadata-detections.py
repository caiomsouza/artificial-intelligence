
# PyExifTool
# http://smarnach.github.io/pyexiftool/
# git clone git://github.com/smarnach/pyexiftool.git
# python setup.py install

# Test exiftool in the command line 
# exiftool -s IMG_6983.JPG 
# 

# exiftool -c "%.6f" -d "%d/%m/%Y-%H:%M" -CreateDate -Aperture -ShutterSpeed -GPSLongitude -GPSLatitude IMG_6983.JPG

# cat exif_format.txt $Filename,$Directory,$CreateDate,$ShutterSpeed,$Aperture,$GPSLongitude ,$GPSLatitude ,$GPSSatellites

# http://www.surfaces.co.il/smile-youre-on-candid-gps/

# http://www.sno.phy.queensu.ca/~phil/exiftool/faq.html



# https://pypi.python.org/pypi/ExifRead/2.1.1


import exiftool


#files = ['Tesla_aged_36.jpg', 'abba.png', 'cibele_paris.jpg', 'IMG_6983.JPG']
files = ['IMG_6983.JPG']
#file_http = ['http://hub.qgis.org/attachments/5368/AM00100M_F1_20110930_1556.jpg']


print 'Some data 1 ...'

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)

for d in metadata:
    print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d['SourceFile'],
                                     d['EXIF:GPSLatitude'],
                                     d['EXIF:GPSLongitude'],
                                     d['EXIF:DateTimeOriginal']))


print 'All data ...'

for d in metadata:
    print d



print 'Some data 2 ...'

for d in metadata:
    print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d['EXIF:Model'],
                                     d['EXIF:LensModel'],
                                     d['Composite:ImageSize'],
                                     d['File:FileTypeExtension']))

print 'Some data 3 ...'

for d in metadata:
    print("{:20.20} {:20.20}".format(d['EXIF:GPSLatitude'],
                                     d['EXIF:GPSLongitude']))


# http://www.latlong.net/Show-Latitude-Longitude.html

# latitude hay que poner un numero como negativo example: -3.65

# http://www.w3.org/2003/12/exif/


# http://www.exiv2.org/tags.html

# Code to treat the error KeyError: 'Exif.Image.DateTime'

#https://gist.github.com/cgoldberg/8474158