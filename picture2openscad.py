"""
picture2openscad.py
Maintained by Jerry Jia <mailto:jiazhen.thinpig@gmail.com>

This is a class that will be used for OpenSCAD 3D object code generation from a 2D picture.
It will support different function for some quick 3D modelling from 2D object.


v1.0 (03/11/2020) changes from initial release
- basic picture2openscad


Use:

import picture2openscad

debug_mode = False
picture_filename = "example//Mount_Fuji.png"

pic2scad = picture2openscad.picture2openscad()
im = pic2scad.ImportPicture(picture_filename, picture_gray_invert= True, picture_flip= "HORI",picture_norm_type="NORM_MINMAX" )
pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,5], pixelcube = [1,1,1], zdepth = 0, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2])
pic2scad.ModelUnion()


"""

import cv2 
import numpy as np


class picture2openscad(object):
    """
    

    
    """

    def __init__(self, debug_mode=None):
        """
        Class constructor.
        picture_x_limit, x limitation, default 500
        picture_y_limit, y limitation, default 500
        picture_limit_scale , auto scale if size larger than limitation, default False

        Inputs:
            optional:
                debug mode - 1 if we want huge debug spew
        Return:
            Remote Agent handle
        """
        if debug_mode:
            self.debug_mode = 1
        else:
            self.debug_mode = 0

        self.scad_filename = "output.scad"
        open(self.scad_filename, "w").close()

        self.picture_x_limit = 500
        self.picture_y_limit = 500
        self.picture_limit_scale = False

        #self.binary_threshold = 0



    def EnableDebug(self):
        """
        Externally callable function to enable debug mode.
        """
        self.debug_mode = 1

    def DisableDebug(self):
        """
        Externally callable function to disable debug mode.
        """
        self.debug_mode = 0


    def ImportPicture(self,picture_filename, picture_gray_invert=True, picture_flip= "NONE",picture_norm_type="NORM_MINMAX" ):
        """
        This function will import image from picture_filename, support common picture format.
        Input: picture filename
        
        
        picture_gray_invert , invert gray, default True
        picture_flip = NONE , do picture flip default NONE disable, set to VERT -> vertical, HORI -> horizontal, VERT_HORI -> vertical and horizontal
        picture_norm_type="NORM_MINMAX" , do picture normalization default NORM_MINMAX, NORM_INF, NORM_L1, NORM_L2

        Output: image object in gray range[0:1]
        """
        try:
            im = cv2.imread(picture_filename)
        except:
            if self.debug_mode: print("Error: ImportPicture error with opening file " + inputfilename)
            return
        
        InputPicture_shape = im.shape 

        if InputPicture_shape[0] > self.picture_y_limit or InputPicture_shape[1] > self.picture_x_limit:
            if self.debug_mode: print("Warning: ImportPicture size is larger than limit " + str(self.picture_x_limit) +"," + str(self.picture_y_limit) + ",auto scale is " + str(self.picture_limit_scable))
            if self.picture_limit_scale:
                if InputPicture_shape[0] < InputPicture_shape[1]:
                    cv2.resize(src=im, dst=im, dsize=[self.picture_x_limit, self.picture_x_limit/InputPicture_shape[1]*InputPicture_shape[0]], interpolation=cv2.INTER_AREA)
                if InputPicture_shape[0] > InputPicture_shape[1]:
                    cv2.resize(src=im, dst=im, dsize=[self.picture_y_limit/InputPicture_shape[0]*InputPicture_shape[1], self.picture_u_limit], interpolation=cv2.INTER_AREA)
        
        ScaleInputPicture_shape = im.shape
        
        # color space convert
        if len(ScaleInputPicture_shape)==3: im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # flip
        if picture_flip == "VERT": im = cv2.flip(im,0) # flip
        if picture_flip == "HORI": im = cv2.flip(im,1) # flip
        if picture_flip == "VERT_HORI": im = cv2.flip(im,-1) # flip

        # invert
        if picture_gray_invert: im = abs(im-255) # gray invert

        im = np.float32(im)

        # scale and shift by NORM_MINMAX
        if picture_norm_type == "NORM_MINMAX":
            cv2.normalize(im, dst=im, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
            if self.debug_mode:cv2.imshow("NORM_MINMAX", np.uint8(im*255))

        # scale and shift by NORM_INF
        if picture_norm_type == "NORM_INF":
            cv2.normalize(im, dst=im, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
            if self.debug_mode:cv2.imshow("NORM_INF", np.uint8(im*255))

        # scale and shift by NORM_L1
        if picture_norm_type == "NORM_L1":
            cv2.normalize(im, dst=im, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
            if self.debug_mode:cv2.imshow("NORM_L1", np.uint8(im*10000000))

        # scale and shift by NORM_L2
        if picture_norm_type == "NORM_L2":
            cv2.normalize(im, dst=im, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
            if self.debug_mode:cv2.imshow("NORM_L2", np.uint8(im*10000))

        if self.debug_mode:
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return im


    def PixelCubeZDepth(self, im_src, offset=[0,0,0], translate = [1,1,0], pixelcube = [.2,.2,.2], zdepth = 5, exclude_threshold = 0, color_mode="GRAY", color_code=[.2,1,0.2,0.2]):
        """
        This function will create cube based image from ImportPicture()
        Input:
            im_src
            offset=[0,0,0]           ,final pixel location offset
            translate = [1,1,0]      ,final pixel cube scale, z=0 means cube z will depends on ZDepth, otherwise z location will be controlled by picture color
            pixelcube = [.2,.2,.2]   ,pixel cube size
            zdepth = 5               ,zdepth will control cube z length, zdepth=0 meas cube z depth will not controlled by picture color
            exclude_threshold = 0    ,color excluded to build cube, default is 0
            color_mode="GRAY"        ,color mode, GRAY means will color cube based on picture color
            color_code=[.2,1,0.2,0.2]    ,if color mode is not GRAY, you can customize cube color [r,g,b,a]

        Output: none
        """
        pixel_index = 0
        scad_output = open(self.scad_filename, "a")

        for y in range(0,im_src.shape[0]):
            for x in range(0,im_src.shape[1]):
                if im_src[y][x] != exclude_threshold:  # exclude_threshold
                    if color_mode == "GRAY": 
                        r=im_src[y][x]
                        g=im_src[y][x]
                        b=im_src[y][x]
                        a=1.0
                    else:
                        r=color_code[0]
                        g=color_code[1]
                        b=color_code[2]
                        a=color_code[3]
                    print("color( c = ["+str(r)+","+str(g)+","+str(b)+","+str(a)+"])", file=scad_output)
                    translate_x = x * translate[0] + offset[0]
                    translate_y = y * translate[1] + offset[1]
                    translate_z = (1-im_src[y][x])*translate[2] + offset[2]
                    cube_x = pixelcube[0]
                    cube_y = pixelcube[1]
                    if zdepth == 0: cube_z = pixelcube[2]
                    else: cube_z = pixelcube[2]*(1-im_src[y][x]) * zdepth
                    print("translate([" + str(translate_x) + "," + str(translate_y) + ","+str(translate_z)+"])", file=scad_output)
                    print("cube(["+str(cube_x)+","+str(cube_y)+","+str(cube_z)+"],center = false);", file=scad_output)
                pixel_index = pixel_index + 1
        scad_output.close()

    def ModelUnion(self):
        """
        This function will add union for OpenScad models at first line.

        """
        #transformation_code = "union()"
        UnionCode = "union(){"
        with open(self.scad_filename, 'r+') as scad_file:
            scad_content = scad_file.read()  
            scad_file.seek(0, 0)
            scad_file.write(UnionCode+"\n"+scad_content)
        
        scad_output = open(self.scad_filename, "a")
        print("}", file=scad_output)
        scad_output.close()