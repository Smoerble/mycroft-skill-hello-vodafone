# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'smo based on eward'

LOGGER = getLogger(__name__)


class HelloVodafoneSkill(MycroftSkill):
    def __init__(self):
        super(HelloVodafoneSkill, self).__init__(name="HelloVodafoneSkill")

    def initialize(self):
        #thank_you_intent = IntentBuilder("ThankYouIntent"). \
        #    require("ThankYouKeyword").build()
        #self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        #how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
        #    require("HowAreYouKeyword").build()
        #self.register_intent(how_are_you_intent,
        #                     self.handle_how_are_you_intent)

        hello_vodfane_intent = IntentBuilder("HelloVodafoneIntent"). \
            require("HelloVodafoneKeyword").build()
        self.register_intent(hello_vodafone_intent,
                             self.handle_hello_vodafone_intent)

    #def handle_thank_you_intent(self, message):
    #    self.speak_dialog("welcome")

    #def handle_how_are_you_intent(self, message):
    #    self.speak_dialog("how.are.you")

    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.vodafone")

    def stop(self):
        pass


def create_skill():
    return HelloVodafoneSkill()
