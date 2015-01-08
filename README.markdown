# Hotify

**Hotify** is a little Python 3 script which provides **global media hotkeys**\* for Spotify's Linux client
(*"Linux Preview"*). Hotify can optionally act as a wrapper, launching Spotify when it is started and
terminating Spotify when the script quits. Hotify always quits when Spotify terminates.

\*) Global hotkeys are provided using GTK+ using the X Windowing System.

## Dependencies

Aside from **Python 3**, Hotify requires the [keybinder](https://github.com/engla/keybinder) library,
which in turn depends on GObject (and its Python bindings).

### Requirements as Ubuntu Packages

In Ubuntu (and derivatives), you can provide the required libraries by installing the following packages
and their respective dependencies:

* `python3-gi`
* `libkeybinder-3.0-0`
* `gir1.2-keybinder-3.0`

### Requirements as Arch Packages

In Arch, you can provide the required libraries by installing the following packages
and their respective dependencies:

* `extra/libkeybinder`
* `extra/python-gobject`
* `aur/python3-keybinder`

## Getting Hotify

Once you have installed Hotify's dependencies, you're almost good to go. Simply get the `hotify.py` 
script, either by downloading the file individually from GitHub, by downloading the source ZIP from
GitHub, or by cloning the repository.

No actual installation is required for normal use. To use Hotify as a wrapper script, see the
instructions further below.

## Using Hotify

Run the `hotify.py` script (in a terminal or with your application launcher). It binds four media
hotkey, which default to the following mappings:

* `XF86AudioPlay` -> Play/Pause (Play if paused, pause if playing)
* `XF86AudioStop` -> Pause (Pause if playing, do nothing if paused)
* `XF86AudioNext` -> Next Track
* `XF86AudioPrev` -> Previous Track

When you exit Spotify, Hotify will detect that and quit automatically.
