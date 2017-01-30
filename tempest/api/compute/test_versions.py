# Copyright (c) 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tempest.api.compute import base
from tempest import test


class TestVersions(base.BaseV2ComputeTest):

    @test.idempotent_id('6c0a0990-43b6-4529-9b61-5fd8daf7c55c')
    def test_list_api_versions(self):
        """Test that a get of the unversioned url returns the choices doc.

        A key feature in OpenStack services is the idea that you can
        GET / on the service and get a list of the versioned endpoints
        that you can access. This comes back as a status 300
        request. It's important that this is available to API
        consumers to discover the API they can use.

        """
        result = self.versions_client.list_versions()
        versions = result['versions']
        # NOTE(sdague): at a later point we may want to loosen this
        # up, but for now this should be true of all Novas deployed.
        self.assertEqual(versions[0]['id'], 'v2.0',
                         "The first listed version should be v2.0")