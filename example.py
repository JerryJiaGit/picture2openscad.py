
"""
example.py for picture2openscad.py
Maintained by Jerry Jia <mailto:jiazhen.thinpig@gmail.com>

This is a class that will be used for OpenSCAD 3D object code generation from a 2D picture.
It will support different function for some quick 3D modelling from 2D object.


v1.0 (03/11/2020) changes from initial release
- Demo of create cube based on picture
"""

import picture2openscad

debug_mode = False
picture_filename = "example//Mount_Fuji.png"

pic2scad = picture2openscad.picture2openscad()
im = pic2scad.ImportPicture(picture_filename, picture_gray_invert= True, picture_flip= "HORI",picture_norm_type="NORM_MINMAX" )
pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,5], pixelcube = [1,1,1], zdepth = 0, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2])
pic2scad.ModelUnion()