# Copyright 2016 NEC Corporation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.api.compute.keypairs import base
from tempest.common.utils import data_utils
from tempest import test


class KeyPairsV210TestJSON(base.BaseKeypairTest):
    credentials = ['primary', 'admin']
    min_microversion = '2.10'

    @classmethod
    def setup_clients(cls):
        super(KeyPairsV210TestJSON, cls).setup_clients()
        cls.client = cls.os_adm.keypairs_client
        cls.non_admin_client = cls.os.keypairs_client

    def _create_and_check_keypairs(self, user_id):
        key_list = list()
        for i in range(2):
            k_name = data_utils.rand_name('keypair')
            keypair = self._create_keypair(k_name,
                                           keypair_type='ssh',
                                           user_id=user_id)
            self.assertEqual(k_name, keypair['name'],
                             "The created keypair name is not equal "
                             "to the requested name!")
            self.assertEqual(user_id, keypair['user_id'],
                             "The created keypair is not for requested user!")
            keypair.pop('private_key', None)
            keypair.pop('user_id')
            key_list.append(keypair)
        return key_list
