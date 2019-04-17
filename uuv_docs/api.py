# Copyright (c) 2016-2019 The UUV Simulator Authors.
# All rights reserved.
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

import os
import xmltodict
import rospkg


class APILoader:
    def __init__(self, catkin_pkg, repository_name, git_root_url):
        rp = rospkg.RosPack()
        self._catkin_pkg = catkin_pkg
        self._catkin_pkg_path = rp.get_path(catkin_pkg)
        self._repository = repository_name
        self._git_root_url = git_root_url