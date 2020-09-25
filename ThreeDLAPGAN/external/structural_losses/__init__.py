import sys
sys.path.append("/home/angps/Documents/")
from ThreeDLAPGAN.external.structural_losses.tf_nndistance import nn_distance
from ThreeDLAPGAN.external.structural_losses.tf_approxmatch import approx_match, match_cost
# try:    
#     from tf_nndistance import nn_distance
#     from tf_approxmatch import approx_match, match_cost
# except:
#     print('External Losses (Chamfer-EMD) were not loaded.')
