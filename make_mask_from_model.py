#!/usr/bin/env python
from EMAN2 import *
from sparx import *
from sys import argv

"""Usage:  make_mask_from_model.py my_dot_model.mod  128  8  """

mod=argv[1]
box=int(argv[2])
rad=int(argv[3])

ptfil=base_name(mod).rstrip(".mod")+".pt"

cmd="model2point -object "+mod+" "+ptfil
os.system(cmd)  

pts=read_text_row(ptfil)

sph=model_circle(rad,box,box,box)

m=model_blank(box,box,box)

for ea in range(len(pts)):
  m+=rot_shift3D(sph,0,0,0,pts[ea][2]-box/2,pts[ea][3]-box/2,pts[ea][4]-box/2)

b=binarize(m,0.01)
g=gauss_edge(b)
gm=g['maximum']
g/=gm
g.write_image("mask_"+base_name(mod).rstrip(".mod")+"_r"+str(rad)+".mrc")
