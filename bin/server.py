# Copyright (C) 2020 Vladislav Yarovoy. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Server-side of cusdub-tz. """

import os

from aiohttp import web

from cdtz import config

LIST_TZ = []


def create_list_tz():
    """Create list timezones. """

    dir_zoneinfo = '/usr/share/zoneinfo'
    for dirpath, dirnames, filenames in os.walk(dir_zoneinfo):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            if open(filepath, 'rb').read(4) == b'TZif':
                filename = filepath.replace(f'{dir_zoneinfo}/', '')
                if filename not in ['Factory', 'localtime', 'posixrules', 'Riyadh8']:
                    LIST_TZ.append(filename)

    LIST_TZ.sort()


async def get_list_tz(request):
    """Returns list timezone. """

    return web.json_response(LIST_TZ)


async def main():
    """The main entry point. """

    app = web.Application()
    app.router.add_get('/tz/list_time_zones', get_list_tz)
    return app


if __name__ == '__main__':
    create_list_tz()
    web.run_app(main(), host=config.HOST, port=config.PORT)
