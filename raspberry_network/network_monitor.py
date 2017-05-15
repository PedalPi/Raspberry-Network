# Copyright 2017 SrMouraSilva
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

import threading


class NetworkMonitor(object):

    def __init__(self, time=1.0, interface="eth0"):
        self.time = time
        self.stopped = True
        self.interface = interface

        self.current = 0
        self.when_change = lambda x: ...

    def start(self):
        self.thread = threading.Timer(self.time, lambda: self.update())
        self.thread.start()
        self.stopped = False

    def update(self):
        with open('/sys/class/net/{}/statistics/tx_packets'.format(self.interface)) as f:
            current = int(f.read().split('\n')[0])
            if current > self.current:
                self.current = current
                self.when_change(current)

        if not self.stopped:
            self.start()

    def stop(self):
        self.stopped = True
