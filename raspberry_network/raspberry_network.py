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

from raspberry_network.network_monitor import NetworkMonitor


class RaspberryNetwork(object):

    def __init__(self, time=1.0, interface="eth0"):
        self.monitor = NetworkMonitor(time, interface)
        self.monitor.when_change = lambda value: self.blink(value)

    def start(self):
        self.monitor.start()

    def blink(self, value):
        print('Update network', value)


if __name__ == '__main__':
    RaspberryNetwork(1/15, 'wlp3s0').start()
