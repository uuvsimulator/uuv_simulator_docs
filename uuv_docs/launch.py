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
import rospkg
import xmltodict


class LaunchLoader:
    def __init__(self, catkin_pkg, repository_name, git_root_url):        
        rp = rospkg.RosPack()
        self._catkin_pkg = catkin_pkg
        self._catkin_pkg_path = rp.get_path(catkin_pkg)
        self._repository_name = repository_name
        self._git_root_url = git_root_url

        self._data = dict()

    @property
    def has_launch(self):
        return os.path.isdir(self.launch_path)

    @property
    def launch_path(self):
        return os.path.join(self._catkin_pkg_path, 'launch')

    def update_data(self):
        self._data = dict()
        self._data.update(self._get_launch_args())

        return self._data

    def _get_launch_args(self):
        output = dict()

        if not self.has_launch:
            return output
 
        for item in os.listdir(self.launch_path):
            if '.launch' not in item:
                continue
            with open(os.path.join(self.launch_path, item), 'r') as launch_file:
                content = launch_file.read()
                
                # Parse the XML contents of the launch file
                launch_content = xmltodict.parse(content)
                launch_name = item.replace('.launch', '')
                            
                # Retrieve the header, if any
                header = content.split('<launch>')[0] 
                
                if len(header) > 0 and '<!--' in header and '-->' in header:
                    header = header.replace('<!--', '').replace('-->', '')
                    while header[0] == ' ':
                        header = header[1::] 
                else:
                    header = ''

                # Add the launch file description
                output[launch_name] = dict()
                if len(header) > 0:
                    output[launch_name]['description'] = header

                input_str = ''
                output[launch_name]['path'] = self._git_root_url + '/' + \
                    self._repository_name + '/tree/master/' + \
                    self._catkin_pkg + '/launch/' + item

                if 'arg' in launch_content['launch']:
                    if isinstance(launch_content['launch']['arg'], list):                
                        for arg in launch_content['launch']['arg']:                        
                            input_str += '* **{}**'.format(arg['@name'])
                            if '@default' in arg:
                                input_str += ' (*default:* `{}`)'.format(arg['@default'])
                            
                            if '@doc' in arg:
                                input_str += ': {}'.format(arg['@doc'])
                            input_str += '\n'
                    else:
                        input_str += '* **{}**'.format(launch_content['launch']['arg']['@name'])
                        if '@default' in launch_content['launch']['arg']:
                            input_str += ' (*default:* `{}`)'.format(launch_content['launch']['arg']['@default'])
                        
                        if '@doc' in launch_content['launch']['arg']:
                            input_str += ': {}'.format(launch_content['launch']['arg']['@doc'])
                        input_str += '\n'
                    output[launch_name]['args'] = input_str
        return output

    def get_markdown(self):
        output = self.update_data()
        output_str = ''

        if not self.has_launch:
            return output_str

        output_str = '# Launch files\n\n'

        for launch_file in output:
            output_str += '## [`{}.launch`]({})\n\n'.format(launch_file, output[launch_file]['path'])

            if 'description' in output[launch_file]:
                output_str += '> **Description**\n\n'
                output_str += output[launch_file]['description'] + '\n\n'
            if 'args' in output[launch_file]:
                output_str += '> **Arguments**\n\n'
                output_str += output[launch_file]['args']
                output_str += '\n'

        return output_str