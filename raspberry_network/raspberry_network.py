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

from gpiozero import LED
from gpiozero.pins.mock import MockPin

from application.component.component import Component

from raspberry_network.network_monitor import NetworkMonitor


class RaspberryNetwork(Component):

    def __init__(self, application, time=1.0, interface="eth0", pin_led=7, test=False):
        super(RaspberryNetwork, self).__init__(application)
        
        self.monitor = NetworkMonitor(time, interface)
        self.monitor.when_change = lambda value: self.blink()
        
        if test:
            pin_led = MockPin(pin_led)

        self.led = LED(pin_led)

    def init(self):
        self.monitor.start()

    def close(self):
        self.monitor.stop()

    def blink(self):
        self.led.blink(on_time=1/30, off_time=1/30, n=1)


if __name__ == '__main__':
    RaspberryNetwork(None, time=1/15, interface='wlp3s0').init()
