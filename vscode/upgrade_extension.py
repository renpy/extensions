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
    run("vscode/VSCode-linux-{}/code".format(arch), "vscode/VSCode-linux-{}/resources/app/out/cli.js".format(arch), "--ms-enable-electron-run-as-node",
        "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

    run("vscode/VSCode-linux-{}/code".format(arch), "vscode/VSCode-linux-{}/resources/app/out/cli.js".format(arch), "--ms-enable-electron-run-as-node",
        "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

elif renpy.windows:

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/VSCode-win32-x64/Code.exe", "vscode/VSCode-win32-x64/resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

    run("vscode/VSCode-win32-x64/Code.exe", "vscode/VSCode-win32-x64/resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

elif renpy.macintosh:

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/Visual Studio Code.app/Contents/MacOS/Electron", "vscode/Visual Studio Code.app/Contents/Resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--uninstall-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

    run("vscode/Visual Studio Code.app/Contents/MacOS/Electron", "vscode/Visual Studio Code.app/Contents/Resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

else:
    error(_("Visual Studio Code is not supported on your platform."))
