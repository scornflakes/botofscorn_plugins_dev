###
# Copyright (c) 2014, scornflakes
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###


# -*- coding: utf-8 -*-

import datetime
import random
from random import randint

from supybot.commands import *
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring


_ = PluginInternationalization('MNFHRules')


class MNFHRules(callbacks.Plugin):
    """Add the help for "@plugin help MNFHRules" here
    This should describe *how* to use this plugin."""
    pass

    @internationalizeDocstring
    def isitfriday(self, irc, msg, args):
        """Tells you if it's Friday or not.
        """
        if datetime.datetime.now().weekday() == 4:
            irc.reply("\x0313 YOU'RE DAMN RIGHT IT'S FRIDAY!!!")
        else:
            irc.reply("It's not Friday, You can pretend it is, but it just won't be the same.")

    isitfriday = wrap(isitfriday)

    @internationalizeDocstring
    def isitmonday(self, irc, msg, args):
        """Tells you if it's Monday or not.
        """
        if datetime.datetime.now().weekday() == 0:
            irc.reply("Please no, don't let it be so. Please.")
        else:
            irc.reply("*sigh of relief* it's not monday.")

    isitmonday = wrap(isitmonday)

    @internationalizeDocstring
    def welcome(self, irc, msg, args, newusername):
        """Welcomes the user to the chan!!
        """
        current_channel = msg.args[0]
        if current_channel == '#mnfh':
            irc.reply(
                "Welcome to #mnfh {0}! We look forward to getting to know you! "
                "Please read more about the chat and rules here: http://mnfh.net/rules".format(newusername))
        else:

            irc.reply(
                "Welcome to {0}, {1}! We look forward to getting to know you! ".format(current_channel, newusername))
    welcome = wrap(welcome, ['text'])

    @internationalizeDocstring
    def dance(self, irc, msg, args):
        """ Tells bot to dance!
        """
        irc.reply('\x03%s\\o/' % str(randint(0, 16)).zfill(1))
        irc.reply('\x03%s/o/' % str(randint(0, 16)).zfill(1))
        irc.reply('\x03%s\\o\\' % str(randint(0, 16)).zfill(1))

    dance = wrap(dance)


    @internationalizeDocstring
    def whatislove(self, irc, msg, args):
        """ what is love?
        """
        irc.reply("Baby don't hurt me")
        irc.reply("Don't hurt me")
        irc.reply('No more')

    whatislove = wrap(whatislove)

    @internationalizeDocstring
    def snuggle(self, irc, msg, args, user_name):
        """ snuggle...
        """
        irc.reply("(\xe3\x81\xa3\xe2\x8c\x92\xe2\x80\xbf\xe2\x8c\x92)\xe3\x81\xa3 %s" % user_name)

    snuggle = wrap(snuggle, ['text'])

    @internationalizeDocstring
    def oplist(self, irc, msg, args):
        """ lists channel ops
        """
        current_channel = msg.args[0]
        irc.reply(("%sxx. (Ignore the 'xx's) Use .callops now if there's a problem. " % self.registryValue('ops', current_channel).replace(',', 'xx, ')))
    oplist = wrap(oplist)


    def callops(self, irc, msg, args):
        """ lists channel ops
        """
        current_channel = msg.args[0]
        irc.reply(("%s" % self.registryValue('ops', current_channel)).replace(',', ', '))
    callops = wrap(callops)


    @internationalizeDocstring
    def stab(self, irc, msg, args, user_name):
        """ Stab function to stab your enemies
        """
        if random.random() < 0.0001:
            irc.reply(
                "%s tries to stab %s, but instead they slip and accidentally stab themself!" % (msg.nick, user_name))
            irc.reply("\x0308o()\x0304xxxx\x0308[{\x0315::::::*\x0300%s*\x0315::::::>" % msg.nick)
        elif 'scornbot' in user_name.lower():
            irc.reply("{0:s} tries to stab scornbot, "
                      "instead scornbot dodges the attack and draws his weapon and fires.".format(msg.nick))
            irc.reply(
                '\u003d\u03b5\u002f\u0335\u0347\u033f\u033f\u002f\u0027\u033f\u0027\u033f\u033f  '
                'BANG!            X_X < {0}.'.format( msg.nick))
        else:
            irc.reply("\x0308o()\x0304xxxx\x0308[{\x0315::::::*\x0300%s*\x0315::::::>" % user_name)
    stab = wrap(stab, ['text'])

    @internationalizeDocstring
    def bandaid(self, irc, msg, args, user_name):
        """ bandages person
        """
        irc.reply("patches %s up with a band-aid \x0308(:::::[::::]:::::)\x0300, "
                  "\x0313'Now you be careful next time'" % user_name)

    bandaid = wrap(bandaid, ['text'])

    @internationalizeDocstring
    def eyeroll(self, irc, msg, args, user_name):
        """ roll your eyes at person
        """
        if not user_name:
            user_name = ""
        irc.reply("\xe2\x97\x94\xcc\xaf\xe2\x97\x94 %s" % user_name)
    eyeroll = wrap(eyeroll, [optional('text')])

    @internationalizeDocstring
    def opno(self, irc, msg, args, user_name):
        """ a no that only an op can do
        """
        current_channel = msg.args[0]
        if not user_name:
            user_name = ""
        if msg.nick in self.registryValue('ops', current_channel):
            irc.reply("Please do not do that, %s" % user_name)
        else:
            irc.reply("you aren't an op, %s" % msg.nick)
    opno = wrap(opno, [optional('text')])

    @internationalizeDocstring
    def minvite(self, irc, msg, args, username):
        """ invite to #mnfh
        """
        irc.invite(username, '#mnfh', msg="you've been invited to #mnfh")
        irc.reply("you have been invited to #mnfh. Please type ''/join #mnfh''")

    minvite = wrap(minvite, ['text'])



    def testops(self, irc, msg, args):
        """ test op command
        """
        current_channel = msg.args[0]
        irc.reply(irc.state.channels[current_channel].modes)
    testops = wrap(testops)

    @internationalizeDocstring
    def gizoogle(self, irc, msg, args,  text):
        """
        Example:
        import gizoogle
        print(gizoogle.translate('Hey, How are you?'))
        # Will print 'Yo, how tha fuck is yo slick ass?'
        """
        from BeautifulSoup import BeautifulSoup
        import requests
        url = 'http://www.gizoogle.net/textilizer.php'

        html = requests.post(url, data={'translatetext': text}).text
        irc.reply( BeautifulSoup(html).textarea.contents[0].strip())
    gizoogle = wrap(gizoogle, ['text'])

Class = MNFHRules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
