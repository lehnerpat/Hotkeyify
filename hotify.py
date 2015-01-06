#!/usr/bin/env python3
"""
Copyright (c) 2014, Patrick Lehner <lehner (dot) patrick (at) gmx (dot) de>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""

import dbus
import os
import signal
import subprocess
import sys
import time

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')

from gi.repository import GLib
from gi.repository import Gtk 
from gi.repository import Keybinder

### handling signals (SIGINT etc)

# Handling signals (such as SIGINT, SIGTERM, ...) with Gtk seems to be a bit complicated.
#   Thankfully, the following setup function is provided at http://stackoverflow.com/a/26457317/1761499
def initSignal():
    def signal_action(signal):
        if signal in [1,2,15]:
            global killSpotifyOnQuit
            if killSpotifyOnQuit and isSpotifyRunning():
                dbusSpotifyQuit() # ask spotify nicely to quit
                time.sleep(0.5) # give it some time
                if isSpotifyRunning(): # if it hasnt managed to quit yet
                    global spotifyPID
                    os.kill(spotifyPID, signal.SIGKILL) #kill it
            Gtk.main_quit()
            sys.exit(0)

    def idle_handler(*args):
        #print("Python signal handler activated.")
        GLib.idle_add(signal_action, priority=GLib.PRIORITY_HIGH)

    def handler(*args):
        #print("GLib signal handler activated.")
        signal_action(args[0])

    def install_glib_handler(sig):
        unix_signal_add = None

        if hasattr(GLib, "unix_signal_add"):
            unix_signal_add = GLib.unix_signal_add
        elif hasattr(GLib, "unix_signal_add_full"):
            unix_signal_add = GLib.unix_signal_add_full

        if unix_signal_add:
            #print("Register GLib signal handler: %r" % sig)
            unix_signal_add(GLib.PRIORITY_HIGH, sig, handler, sig)
        else:
            print("Can't install GLib signal handler, too old gi.")

    SIGS = [getattr(signal, s, None) for s in "SIGINT SIGTERM SIGHUP".split()]
    for sig in filter(None, SIGS):
        #print("Register Python signal handler: %r" % sig)
        signal.signal(sig, idle_handler)
        GLib.idle_add(install_glib_handler, sig, priority=GLib.PRIORITY_HIGH)


### Spotify interaction methods

spotifyPID = None

def isSpotifyRunning():
    global spotifyPID
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                exepath = os.readlink(os.path.join('/proc', pid, 'exe'))
                if exepath.endswith('/spotify'):
                    spotifyPID = int(pid)
                    return True
            except IOError:
                continue
    spotifyPID = False
    return False

def checkIfPIDStillRunning(pid):
    try:
        exepath = os.readlink(os.path.join('/proc', str(pid), 'exe'))
        return True
    except IOError:
        return False

def pidCheckingWrapper(*args, **kwargs):
    global spotifyPID
    #print("checking...")
    if not checkIfPIDStillRunning(spotifyPID):
        Gtk.main_quit()
        sys.exit(0)
    #print("Still running")
    return True

mplayer_iface = None # will be filled by a dbus call below

def dbusSpotifyPlayPause():
    global mplayer_iface
    mplayer_iface.PlayPause()

def dbusSpotifyPause():
    global mplayer_iface
    mplayer_iface.Pause()

def dbusSpotifyNext():
    global mplayer_iface
    mplayer_iface.Next()

def dbusSpotifyPrev():
    global mplayer_iface
    mplayer_iface.Previous()

def dbusSpotifyQuit():
    global mplayer_iface
    mplayer_iface.Quit()


### Util methods

def methodCallWrapper(keystr, user_data):
    user_data()


### Main Code

##############################################################################
# define here the key mappings you want for which actions
#  the dict key is the glib keystring, which can be something like '<Ctrl><Alt>M';
#  see https://developer.gnome.org/gtk3/stable/gtk3-Keyboard-Accelerators.html#gtk-accelerator-parse
#  and https://git.gnome.org/browse/gtk+/tree/gdk/gdkkeysyms.h (symbolic names,
#  leave out the leading 'GDK_KEY_')
#  the value is the method (reference) from the spotify object above; currently
#  only works with parameterless methods
mappings = {
    'XF86AudioPlay': dbusSpotifyPlayPause,
    'XF86AudioNext': dbusSpotifyNext,
    'XF86AudioPrev': dbusSpotifyPrev,
    'XF86AudioStop': dbusSpotifyPause
}
##############################################################################


initSignal() # set up signal handling (SIGINT, SIGTERM, etc)

sp = None
killSpotifyOnQuit = False

if not isSpotifyRunning():
    sp = subprocess.Popen(['spotify'])
    killSpotifyOnQuit = True
    #spotifyPID = sp.pid
    time.sleep(1)
    isSpotifyRunning()
    #print(spotifyPID)

# set up the periodic checker task to quit when spotify exits
GLib.timeout_add_seconds(5, pidCheckingWrapper)

# get DBus interface
session_bus = dbus.SessionBus()
mplayer_iface = dbus.Interface(session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/"), 'org.freedesktop.MediaPlayer2')


# bind the hotkeys defined above
Keybinder.init()
for k,v in mappings.items():
    Keybinder.bind(k, methodCallWrapper, v)

# start the gtk main loop
Gtk.main()

