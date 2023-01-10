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
This is the main module. Here we're using a manager class to manage the full
periodic table and all of its functions.
'''

# Project modules
from obj.manager import Manager

def main():
    my_Manager = Manager()
    my_Manager.work()

if __name__ == "__main__":
    main()