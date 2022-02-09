import renpy
from installer import _, download, remove, exists, move, processing, run, mkdir, unpack, error

if renpy.linux:

    # Download vscode.
    download("https://code.visualstudio.com/sha/download?build=stable&os=linux-x64", "temp:vscode-linux-x64.tar.gz")

    # Back up the data directory.
    remove("temp:vscode-data")
    if exists("vscode/VSCode-linux-x64/data"):
        move("vscode/VSCode-linux-x64/data", "temp:vscode-data")

    # Unpack vscode.
    mkdir("vscode")
    remove("vscode/VSCode-linux-x64")
    unpack("temp:vscode-linux-x64.tar.gz", "vscode")

    # Restore the data directory.
    if exists("temp:vscode-data"):
        move("temp:vscode-data", "vscode/VSCode-linux-x64/data")
    else:
        mkdir("vscode/VSCode-linux-x64/data")

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/VSCode-linux-x64/code", "vscode/VSCode-linux-x64/resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--install-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

elif renpy.windows:

    # Download vscode.
    download("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-archive", "temp:vscode-win32-x64.tar.gz")

    # Back up the data directory.
    remove("temp:vscode-data")
    if exists("vscode/VSCode-win32-x64/data"):
        move("vscode/VSCode-win32-x64/data", "temp:vscode-data")

    # Unpack vscode.
    mkdir("vscode/VSCode-win32-x64")
    remove("vscode/VSCode-win32-x64")
    unpack("temp:vscode-win32-x64.tar.gz", "vscode/VSCode-win32-x64")

    # Restore the data directory.

    if exists("temp:vscode-data"):
        move("temp:vscode-data", "vscode/VSCode-win32-x64/data")
    else:
        mkdir("vscode/VSCode-win32-x64/data")

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/VSCode-win32-x64/Code.exe", "vscode/VSCode-win32-x64/resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--install-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

elif renpy.macintosh:

    download("https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal", "temp:vscode-darwin-universal.zip")

    # Unpack vscode.
    mkdir("vscode")
    remove("vscode/Visual Studio Code.app")
    unpack("temp:vscode-darwin-universal.zip", "vscode")

    # Create the data directory, if it doesn't exist.
    mkdir("vscode/code-portable-data")

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/Visual Studio Code.app/Contents/MacOS/Electron", "vscode/Visual Studio Code.app/Contents/Resources/app/out/cli.js", "--ms-enable-electron-run-as-node",
        "--install-extension", "LuqueDaniel.languague-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

else:
    error(_("Visual Studio Code is not supported on your platform."))
