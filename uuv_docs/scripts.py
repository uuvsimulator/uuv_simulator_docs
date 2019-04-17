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
import code


class ScriptsLoader:
    def __init__(self, catkin_pkg, repository_name, git_root_url):
        rp = rospkg.RosPack()
        self._catkin_pkg = catkin_pkg
        self._catkin_pkg_path = rp.get_path(catkin_pkg)
        self._repository = repository_name
        self._git_root_url = git_root_url

    @property
    def has_scripts(self):
        return os.path.isdir(self.scripts_path)

    @property
    def scripts_path(self):
        return os.path.join(self._catkin_pkg_path, 'scripts')

    def update_data(self):
        output = dict()
        output.update(self._get_scripts())

        return output

    def _get_scripts(self):
        output = dict()

        if not self.has_scripts:
            return output

        for script_filename in os.listdir(self.scripts_path):
            output[script_filename] = dict()
            
            # Read script 
            with open(os.path.join(self.scripts_path, script_filename), 'r') as script_file:
                content = script_file.read()
            
            if '#!/usr/bin/env python' in content:
                output[script_filename]['type'] = 'python'
                output[script_filename]['doc'] = self._get_module_docstring(
                    os.path.join(self.scripts_path, script_filename))
            elif '#!/usr/bin/env bash' in content or '#!/bin/bash' in content:
                output[script_filename]['type'] = 'shell'

        return output

    def _get_module_docstring(self, filename):
        co = compile(open(filename).read(), filename, 'exec')
        if co.co_consts and isinstance(co.co_consts[0], str):
            docstring = co.co_consts[0]
        else:
            docstring = None
        return docstring

    def get_markdown(self):
        output = self.update_data()

        output_str = ''

        if self.has_scripts:
            output_str = '# Scripts\n\n'

            for script in output:
                output_str += '## `{}`\n\n'.format(script)

                if 'type' in output[script]:
                    output_str += '> **Script type:** `{}`\n\n'.format(output[script]['type'])

                if 'doc' in output[script]:
                    if output[script]['doc'] is not None and len(output[script]['doc']) > 0: 
                        output_str += output[script]['doc'] + '\n\n'
                    
        return output_str