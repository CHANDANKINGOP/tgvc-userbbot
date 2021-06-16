"""
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from os import environ

# import logging
from pyrogram import Client, idle

API_ID = int(environ["3898418"])
API_HASH = environ["5a82313211da04d63297bd4de436228c"]
SESSION_NAME = environ["BQACI4LJFMVIfLNZBRdD0IgUbRE0t7Q5KWESgt70IAZdiWE2v1qecl7cWoVLixdS7HZPWsSPBf7DxdvEtcdSWukClAGRtNbOjTUORI5vWEklIeYZCLneNWCadRzz9AhyCARU1Xwo33eyGftqhAiKPZaow9O0lDxd0JtjvqSXLn0GojabdrJ3-fKMBhXrPL1zXIOQxacxzmlyMJaaPbjk6_SfMCgPclE1zUCGr2-F8bS38GWjSejx_1wTD1S98DfSltwcO7FA_7eB-db7aGmO1KFbTi5XV2N0bpktbCX6zqfDpeI01Siz-6AMm1LFuy6-xnzszsSkThuAkRTi6r0_Q9VqX9XNvAA"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
