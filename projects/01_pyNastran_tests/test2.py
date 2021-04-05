import pyNastran as pyn
# from pyNastran.bdf.bdf import BDF, read_bdf, CrossReferenceError

from pyNastran.bdf.cards import nodes
#from pyNastran.bdf.cards.elements import *

from pyNastran.bdf.bdf_interface import add_card

node = nodes.GRID(1, [0.,0.,0.],0,0,'','','test node')
node = nodes.GRID(2, [1.,0.,0.],0,0,'','','test node')
node = nodes.GRID(3, [1.,1.,0.],0,0,'','','test node')
node = nodes.GRID(4, [1.,1.,1.],0,0,'','','test node')
node = nodes.GRID(5, [1.,1.,1.],0,0,'','','test node')

print(node.xyz)

#elem = shell.CTRIA3(22332, 100, [1,2,3], 0., '', comment='test element')
#print(elem)

#quad = add_card.CQUAD(98,333,[1,2,3,4],'')
quad = add_card.CQUAD4(23,232,[1,2,3,4],None,None,comment='quad')
quad.nodes_ref([1,2,3,4])
rbe = add_card.RBE2(983,1,123456,2,'','test')
print(rbe)
print(quad.Area())