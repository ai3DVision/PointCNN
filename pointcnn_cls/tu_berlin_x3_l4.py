#!/usr/bin/python3

import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import data_utils

load_fn = data_utils.load_cls_train_val
map_fn = None
save_ply_fn = None

num_class = 250

sample_num = 512

batch_size = 200

num_epochs = 2048

step_val = 500

learning_rate_base = 0.01
decay_steps = 8000
decay_rate = 0.5
learning_rate_min = 1e-6

weight_decay = 1e-6

jitter = 0.002
jitter_val = 0.002

rotation_range = [0, math.pi / 12, [0, math.pi], 'g']
rotation_range_val = [0, 0, 0, 'u']
order = 'rzyx'

scaling_range = [0.15, [0.01], 0.15, 'g']
scaling_range_val = [0, [0.01], 0, 'u']

x = 3

xconv_param_name = ('K', 'D', 'P', 'C', 'links')
xconv_params = [dict(zip(xconv_param_name, xconv_param)) for xconv_param in
                [(8, 1, -1, 16 * x, []),
                (12, 2, 256, 32 * x, []),
                (16, 2, 128, 64 * x, []),
                (16, 3, 128, num_class * 2, [])]]

fc_param_name = ('C', 'dropout_rate')
fc_params = [dict(zip(fc_param_name, fc_param)) for fc_param in
             [(num_class * 2, 0.0),
              (num_class * 2, 0.5)]]

sampling = 'random'

optimizer = 'adam'
epsilon = 1e-2

data_dim = 6
use_extra_features = False
with_X_transformation = True
sorting_method = None

keep_remainder = True
