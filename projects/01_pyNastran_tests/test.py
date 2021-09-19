
import os
import sys
#import gnspy
import pyNastran
import csv

from pyNastran.bdf.bdf import BDF, read_bdf
from pyNastran.utils import object_attributes, object_methods


bdf_filename="data/source.bdf"
bulkdata_filename="modify_rbe2_to_rbe2mpc.bdf"

bulkdata_file = open(bulkdata_filename, "w")

bdf = BDF()
bdf = read_bdf(bdf_filename, xref=False, punch=False)
#print(bdf.get_bdf_stats())
bdf_out = BDF()

rbe_dict = bdf.get_card_ids_by_card_types(
    card_types=['RBE2'], combine=False)

rbe_node_start_id=9001
nid=rbe_node_start_id
eid=rbe_node_start_id
mpcid=rbe_node_start_id
for rbeid in rbe_dict['RBE2']:
    rbe=bdf.RigidElement(rbeid)
    print("Independent Node RBE ",rbeid,": ", rbe.independent_nodes)
    print("Dependent Nodes RBE ",rbeid,": ", rbe.dependent_nodes)
    #rbe
    new_rbe_grids=[]
    # create for each dependent node a new node
    for n in rbe.dependent_nodes:
        #print("New grid ",nid," for rbe grid: ",bdf.Node(n))
        xyz_new=bdf.Node(n).xyz
        #print(nid, xyz_new)
        bdf_out.add_grid(nid,xyz_new)
        new_rbe_grids.append(nid)
        #link new nodes with MPC to old nodes
        bdf_out.add_mpc(mpcid,[ nid , n ], [rbe.cm, rbe.cm], [1.0, -1.0])
        nid=nid+1
    # create new rbe element    
    bdf_out.add_rbe2(eid,rbe.gn,rbe.cm,new_rbe_grids)
    eid=eid+1
    mpcid=eid
    
bdf_out.write_bdf(bulkdata_filename)
print(bdf_out.get_bdf_stats())

bulkdata_file.close()