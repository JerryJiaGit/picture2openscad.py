# picture2openscad.py
A python tool to convert a picture to OpenSCAD 3D model - pix2cube

# Demo:
pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,0], pixelcube = [1,1,1], zdepth = 10, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2])
![](readme/output_zdepth_10.png?raw=true)

pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,5], pixelcube = [1,1,1], zdepth = 0, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2])
![](readme/output_zdepth_0_translate_115.png?raw=true)

pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,5], pixelcube = [1,1,1], zdepth = 0, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2])
![](readme/output_zdepth_0_translate_115_color.png?raw=true)

# Example picture was created by Alice Lin.
