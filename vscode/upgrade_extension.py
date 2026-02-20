import renpy
from installer import _, download, remove, exists, move, processing, run, mkdir, unpack, error, info

if renpy.linux:

    renpy_arch = getattr(renpy, "arch", "x86_64")

    if renpy_arch == "armv7l":
        arch = "arm"
    elif renpy_arch == "aarch64":
        arch = "arm64"
    else:
        arch = "x64"

    # Upgrade the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/VSCode-linux-{}/bin/code".format(arch), "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", })

    run("vscode/VSCode-linux-{}/bin/code".format(arch), "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "", })

elif renpy.windows:

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode\\VSCode-win32-x64\\bin\\code.cmd", "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "" })

    run("vscode\\VSCode-win32-x64\\bin\\code.cmd", "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "",  })

elif renpy.macintosh:

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/Visual Studio Code.app/Resources/app/bin/code", "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "",  })

    run("vscode/Visual Studio Code.app/Resources/app/bin/code", "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "",  })

else:
    error(_("Visual Studio Code is not supported on your platform."))
