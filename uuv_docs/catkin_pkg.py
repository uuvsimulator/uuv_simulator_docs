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

from .package import PackageConfigLoader
from .launch import LaunchLoader
from .messages import MessagesLoader
from .scripts import ScriptsLoader


class CatkinPkgConfigGenerator:
    def __init__(self, catkin_pkg, repository_name, git_root_url):
        loader_args = [catkin_pkg, repository_name, git_root_url]

        self._loaders = [
            PackageConfigLoader(*loader_args), 
            LaunchLoader(*loader_args),
            MessagesLoader(*loader_args),
            ScriptsLoader(*loader_args)]

    def get_markdown(self):
        content = ''
        for loader in self._loaders:
            content += loader.get_markdown()

        return content