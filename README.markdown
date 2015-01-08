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

## Using Hotify

Run the `hotkeyify.py` script (in a terminal or with your application launcher). It binds four media
hotkey, which default to the following mappings:

* `XF86AudioPlay` -> Play/Pause (Play if paused, pause if playing)
* `XF86AudioStop` -> Pause (Pause if playing, do nothing if paused)
* `XF86AudioNext` -> Next Track
* `XF86AudioPrev` -> Previous Track

When you exit Spotify, Hotkeyify will detect that and quit automatically.


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
