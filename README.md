# picture2openscad.py
A python tool to convert a picture to OpenSCAD 3D model - pix2cube.
So the people can use this tool to convert 2D logo or pictures into a 3D model and then create things with any 3D Printer after export SLT file from OpenSCAD.

After v1.3, also added scatter chart function to convert multi-dim dataset into 3D chart 

# Requirement of dependency
 * import cv2
 * import numpy as np

# Demo:


im = pic2scad.ImportPicture(picture_filename, picture_color_space = "GRAY", picture_color_invert= True, picture_flip= "HORI",picture_norm_type="NORM_MINMAX" )

pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,0], pixelcube = [1,1,1], zdepth = 10, exclude_threshold = [-1], color_mode="GRAY", color_alpha=1)
![](readme/output_exclude_threshold_-1.png?raw=true)

pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,0], pixelcube = [1,1,1], zdepth = 10, exclude_threshold = [0], color_mode="GRAY", color_alpha=1)
![](readme/output_zdepth_10.png?raw=true)

pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,5], pixelcube = [1,1,1], zdepth = 0, exclude_threshold = [0], color_mode="GRAY", color_alpha=1
![](readme/output_zdepth_0_translate_115.png?raw=true)

pic2scad.ModelColor(color_c=[.2,1,0.2,0.2])
![](readme/output_zdepth_0_translate_115_color.png?raw=true)

pic2scad.ScatterChart(dim,index=True)
![](readme/output_14D_scatter_chart.png?raw=true)


# Example picture was created by Alice Lin.
Mount Fuji and sakura, very nice painting by my friend Alice Lin.

![](example/Mount_Fuji.png?raw=true)
