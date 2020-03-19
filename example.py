
"""
example.py for picture2openscad.py
Maintained by Jerry Jia <mailto:jiazhen.thinpig@gmail.com>

This is a class that will be used for OpenSCAD 3D object code generation from a 2D picture.
It will support different function for some quick 3D modelling from 2D object.

v1.2 (03/19/2020)
- Add scatter chart demo for a electricity.csv dataset

v1.1 (03/12/2020)
- Change to use output function for saving result, also add some examples for color image/cube and model functions.

v1.0 (03/11/2020) changes from initial release
- Demo of create cube based on picture
"""

import picture2openscad
import random



def convert_picture(pic,output):
    pic2scad = picture2openscad.picture2openscad()
    '''Import picture'''
    im = pic2scad.ImportPicture(pic, picture_color_space = "GRAY", picture_color_invert= True, picture_flip= "HORI",picture_norm_type="NORM_MINMAX" )
    # im = pic2scad.ImportPicture(pic, picture_color_space = "BGR", picture_color_invert= True, picture_flip= "HORI",picture_norm_type="NORM_MINMAX" )
    '''Build cube'''
    pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,0], pixelcube = [1,1,1], zdepth = 10, exclude_threshold = [-1,-1,-1], color_mode="GRAY", color_alpha=1)
    # pic2scad.PixelCubeZDepth(im, offset=[0,0,0], translate = [1,1,0], pixelcube = [1,1,1], zdepth = 10, exclude_threshold = [1,1,1], color_mode="BGR", color_alpha=1)
    '''Module Func'''
    pic2scad.ModelUnion()
    # pic2scad.ModelRotate(rotate_a=[0,0,1])
    # pic2scad.ModelScale(scale_v=[1,1,1])
    # pic2scad.ModelTranslate(translate_v=[1,1,1])
    # pic2scad.ModelMirror(mirror_v=[1,1,1])
    # pic2scad.ModelColor(color_c=[.2,1,0.2,0.2])

    '''Output result to file'''
    pic2scad.ExportScad(output)

def create_random_scatter(output):
    dim = []
    rand2scad = picture2openscad.picture2openscad()

    for i in range(1000):
        shapetype = random.randint(1,2)
        l_d = random.random()
        w_fa = random.random()
        h_fs = random.random()
        x = random.randint(1,5)
        y = random.randint(1,5)
        z = random.randint(1,5)
        # x = random.uniform(0,5)
        # y = random.uniform(0,5)
        # z = random.uniform(0,5)
        cr = random.random()
        cg = random.random()
        cb = random.random()
        ca = random.random()
        rx = random.randint(0,0)
        ry = random.randint(0,0)
        rz = random.randint(0,0)
        #w_fa = 10
        shapetype = 1
        #h_fs = 1
        cg =cr=cb= h_fs
        dim.append([shapetype,l_d,w_fa,h_fs,x,y,z,rx,ry,rz,cr,cg,cb,ca])
    rand2scad.ScatterChart(dim)
    '''Output result to file'''
    rand2scad.ExportScad(output)

def read_from_csv(inputcsv):
    import pandas as pd
    dim = []
    df=pd.read_csv(inputcsv,header=0,index_col=0)
    df["cost"] = df["cost"] / df["cost"].max()
    df["q"] = df["q"] / df["q"].max()
    df["pl"] = df["pl"] / df["pl"].max()
    df["sl"] = df["sl"] / df["sl"].max()
    df["pk"] = df["pk"] / df["pk"].max()
    df["sk"] = df["sk"] / df["sk"].max()
    df["pf"] = df["pf"] / df["pf"].max()
    df["sf"] = df["sf"] / df["sf"].max()
    for row in df.values:
        shapetype = 1        # 1 for cube, 2 for sphere
        l_d = row[2]
        w_fa = row[4]
        h_fs = row[6]
        x = row[3] * 10
        y = row[5] * 10
        z = row[7] * 10
        cr = row[0]
        cg = .5
        cb = row[0]
        ca = (1-row[1] ) / 4
        rx = 0
        ry = 0
        rz = 0
        #dim.append([2, row[0]*4, 1, 0.05, row[2] * 10,row[4] * 10,row[6] * 10, 0,0,0,row[3],row[5],row[7],row[1]])
        dim.append([shapetype,l_d,w_fa,h_fs,x,y,z,rx,ry,rz,cr,cg,cb,ca])
    return dim

def create_csv_scatter(inputcsv,output):
    dim = []
    dim = read_from_csv(inputcsv)
    csv2scad = picture2openscad.picture2openscad()
    csv2scad.ScatterChart(dim,index=True)
    csv2scad.ExportScad(output)

if __name__ == "__main__":
    debug_mode = False
    scad_filename = "output.scad"

    picture_filename = "example//HydrogenOrbitalsN6L0M0.png"
    #convert_picture(picture_filename,scad_filename)

    csv_filename = "example//electricity.csv"
    create_csv_scatter(csv_filename,scad_filename)
    #create_random_scatter(scad_filename)


