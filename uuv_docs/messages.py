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


class MessagesLoader:
    def __init__(self, catkin_pkg, repository_name, git_root_url):
        rp = rospkg.RosPack()
        self._catkin_pkg = catkin_pkg
        self._catkin_pkg_path = rp.get_path(catkin_pkg)
        self._repository = repository_name
        self._git_root_url = git_root_url

    @property
    def has_msgs(self):
        return os.path.isdir(self.msg_path)

    @property
    def has_srvs(self):
        return os.path.isdir(self.srv_path)

    @property
    def msg_path(self):
        return os.path.join(self._catkin_pkg_path, 'msg')

    @property
    def srv_path(self):
        return os.path.join(self._catkin_pkg_path, 'srv')

    def update_data(self):
        output = dict()
        output.update(self._get_msgs())
        output.update(self._get_srvs())

        return output
    
    def _get_msgs(self):
        output = dict()

        if not self.has_msgs:
            return output

        output['msg'] = dict()
        for msg_filename in os.listdir(self.msg_path):
            with open(os.path.join(self.msg_path, msg_filename), 'r') as msg_file:
                output['msg'][msg_filename] = msg_file.read()
        return output

    def _get_srvs(self):
        output = dict()

        if not self.has_srvs:
            return output

        output['srv'] = dict()
        for srv_filename in os.listdir(self.srv_path):
            with open(os.path.join(self.srv_path, srv_filename), 'r') as srv_file:
                output['srv'][srv_filename] = srv_file.read()
        return output

    def get_markdown(self):
        output = self.update_data()

        output_str = ''

        if self.has_msgs:
            output_str = '# ROS Messages\n\n'

            for msg in output['msg']:
                output_str += '## `{}`\n\n'.format(msg.replace('.msg', ''))
                output_str += '```\n'
                output_str += output['msg'][msg] + '\n'
                output_str += '```\n\n'

        if self.has_srvs:
            output_str = '# ROS Services\n\n'

            for srv in output['srv']:
                output_str += '## `{}`\n\n'.format(srv.replace('.srv', ''))
                output_str += '```\n'
                output_str += output['srv'][srv] + '\n'
                output_str += '```\n\n'
                
        return output_str

