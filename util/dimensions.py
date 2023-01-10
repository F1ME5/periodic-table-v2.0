# Copyright 2023 Néstor Nahuatlato
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
These collections are used in several modules so I separated them in this module.
'''

from util.algorithms import get_positions, get_labels_positions

#X and Y values for placing buttons.
X_BEGIN = 50
X_INCREASING = 70
X_MAX = 17
Y_BEGIN = 50
Y_INCREASING = 96
Y_MAX = 8

# Generating a tuple that contains all integer values for place buttons horizontally
# One position for each Periodic Table's Group, there are 18 groups
# The meaning of the parameter 'flag' is explained in util.dimensions
x_positions = get_positions(increasing=X_INCREASING, begin=X_BEGIN, max=X_MAX, flag=False)

# Generating a tuple that contains all integer values for place buttons vertically
# One position for each Periodic Table's Period, there are 7 groups
# This function generates two more positions for collocate lanthanoids and actinoids
y_positions = get_positions(increasing=Y_INCREASING, begin=Y_BEGIN, max=Y_MAX, flag=True)

# Generating periods and groups labels values for place labels horizontally and vertically.
groups_positions, periods_positions = get_labels_positions(x_positions, y_positions)