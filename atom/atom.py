import renpy
from installer import _, download, remove, exists, move, processing, run, mkdir, unpack, error, info

package = ""

if renpy.windows:
    package = "windows.zip"
elif renpy.macintosh:
    package = "mac.zip"
elif renpy.linux:
    package = "linux.tar.bz2"
else:
    error(_("Atom is not supported on your platform."))

filename = "atom-" + package
temp_filename = "temp:" + filename

download("https://www.renpy.org/dl/atom/" + filename, temp_filename)
unpack(temp_filename, "")
