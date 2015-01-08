# Hotkeyify

**Hotkeyify** is a little Python 3 script which provides **global media hotkeys**\* for Spotify's 
Linux client (*"Linux Preview"*). Hotkeyify can optionally act as a wrapper, launching Spotify when
it is started and terminating Spotify when the script quits. Hotkeyify always quits when Spotify
terminates.

\*) Global hotkeys are provided using GTK+ using the X Windowing System.

## Dependencies

Aside from **Python 3**, Hotkeyify requires the [keybinder](https://github.com/engla/keybinder)
library, which in turn depends on GObject (and its Python bindings).

### Requirements as Ubuntu Packages

In Ubuntu (and derivatives), you can provide the required libraries by installing the following
packages and their respective dependencies:

* `python3-gi`
* `libkeybinder-3.0-0`
* `gir1.2-keybinder-3.0`

### Requirements as Arch Packages

In Arch, you can provide the required libraries by installing the following packages
and their respective dependencies:

* `extra/libkeybinder`
* `extra/python-gobject`
* `aur/python3-keybinder`

## Getting Hotkeyify

Once you have installed Hotkeyify's dependencies, you're almost good to go. Simply get the 
`hotkeyify.py` script, either by downloading the file individually from GitHub, by downloading the
source ZIP from GitHub, or by cloning the repository.

No actual installation is required for normal use.

To use Hotkeyify as a wrapper script, see the instructions further below.

## Using Hotkeyify

Run the `hotkeyify.py` script (in a terminal or with your application launcher). It binds four media
hotkey, which default to the following mappings:

* `XF86AudioPlay` -> Play/Pause (Play if paused, pause if playing)
* `XF86AudioStop` -> Pause (Pause if playing, do nothing if paused)
* `XF86AudioNext` -> Next Track
* `XF86AudioPrev` -> Previous Track

When you exit Spotify, Hotkeyify will detect that and quit automatically. If you launched Hotkeyify
while Spotify was already running, terminating Hotkeyify (e.g. by sending it a SIGTERM or pressing
`Ctrl+C` (SIGINT) when running in a terminal) will not quit Spotify.

## Using Hotkeyify as a Wrapper Script

If Spotify is not running when you launch Hotkeyify, the script automatically launches the Spotify
client (without arguments). Additionally, the script will terminate Spotify (gracefully) when it
quits.

This allows you use Hotkeyify as a wrapper for Spotify, automatically registering the global hotkeys
when you launch it, and unregistering them when Spotify exits.

### Setting up Hotkeyify as a `spotify` replacement

To conveniently use Hotkeyify as a Spotify wrapper, you can set up a (removable) replacement for the
`spotify` executable in your `PATH`.

The actual `spotify` executable is usually located in `/usr/bin` -- if it is somewhere else on your
system, you need to tell Hotkeyify about it (see further below).

1. Make sure you have a place in your `PATH` where you can put binaries that will shadow your system
   binaries. For example, you can have a folder in your home folder, i.e. `~/bin`:
    1. If you do not have such a folder, create it (`mkdir ~/bin`).
    2. Make sure it is prepended to your `PATH` variable. To check, open a terminal, enter `echo $PATH`
       and press Enter. If the printed list of folders does not include your custom `bin` folder first
       (it is likedly expanded to the full form `/home/<username>/bin`, continue with step 1.3 below, 
       otherwise continue to step 2.
    3. Open the file `~/.profile` in a text editor (create it if it does not exist). Append the 
       following line:  
       `PATH=$HOME/bin:$PATH`  
       Save the file and exit your editor. You may have to log out and back in (or reboot) to apply
       this change.

2. Create a symbolic link to `hotkeyify.py` named `spotify`. We assume here that you placed Hotkeyify 
   in the folder `~/Hotkeyify`; if you placed it somewhere else, simply use the full path to 
   `hotkeyify.py` in the command below:  
   `ln -s ~/Hotkeyify/hotkeyify.py ~/bin/spotify`

Now you're good to go! Whenever you now run `spotify` (from your terminal, command runner or
application launcher), Hotkeyify is launched automatically along with Spotify.


## License

Hotkeyify is open source released under the ISC License. The license text is included below, and
can also be found in the [LICENSE](LICENSE) file. Some more information on this license and
comparisons to other licenses can be found at [ChooseALicense.com](http://choosealicense.com/licenses/)
and the [Open Source Initiative](http://opensource.org/licenses/ISC).

```
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
```
