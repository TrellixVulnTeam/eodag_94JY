# -*- coding: utf-8 -*-
# Copyright 2018, CS Systemes d'Information, http://www.c-s.fr
#
# This file is part of EODAG project
#     https://www.github.com/CS-SI/EODAG
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
from __future__ import absolute_import, print_function, unicode_literals

from eodag.plugins.authentication.base import Authentication


class OAuth(Authentication):

    def __init__(self, config):
        super(OAuth, self).__init__(config)
        self.access_key = None
        self.secret_key = None

    def authenticate(self):
        self.access_key = self.config['credentials']['aws_access_key_id']
        self.secret_key = self.config['credentials']['aws_secret_access_key']
        return self.access_key, self.secret_key
