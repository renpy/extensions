import renpy
from installer import _, remove, exists, move, processing, run, mkdir, unpack, error, info

def download(url, filename, hash=None):
    """
    Downloads `url` to `filename`, a tempfile.
    """

    import installer
    import requests
    import time
    import renpy
    from renpy.store import interface, _

    download_url = url
    download_file = installer._friendly(filename)

    filename = installer._path(filename)

    if hash is not None:
        if installer._check_hash(filename, hash):
            return

    progress_time = time.time()

    try:

        response = requests.get(url, stream=True, proxies=renpy.exports.proxies, timeout=15, headers={"Referer" : "https://code.visualstudio.com/download", "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 renpy/8'})
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 1))

        downloaded = 0

        with open(filename, "wb") as f:

            for i in response.iter_content(65536):

                f.write(i)
                downloaded += len(i)

                if time.time() - progress_time > 0.1:
                    progress_time = time.time()
                    if not installer.quiet:
                        interface.processing(
                            _("Downloading [installer.download_file]..."),
                            complete=downloaded, total=total_size)

    except requests.HTTPError as e:
        if not installer.quiet:
            raise

        interface.error(_("Could not download [installer.download_file] from [installer.download_url]:\n{b}[installer.download_error]"))

    if hash is not None:
        if not installer.quiet:
            raise Exception("Hash check failed.")
        if not installer._check_hash(filename, hash):
            interface.error(_("The downloaded file [installer.download_file] from [installer.download_url] is not correct."))



info(_("Visual Studio Code is licensed under {a=https://code.visualstudio.com/license}Microsoft Software License Terms{/a}, and may collect some information about you and your use.\n\nBy installing Visual Studio Code, you agree to thse terms."))

if renpy.linux:

    renpy_arch = getattr(renpy, "arch", "x86_64")

    if renpy_arch == "armv7l":
        arch = "arm"
    elif renpy_arch == "aarch64":
        arch = "arm64"
    else:
        arch = "x64"

    # Download vscode.
    download("https://code.visualstudio.com/sha/download?build=stable&os=linux-{}".format(arch), "temp:vscode-linux-{}.tar.gz".format(arch))

    # Back up the data directory.
    remove("temp:vscode-data")
    if exists("vscode/VSCode-linux-{}/data".format(arch)):
        move("vscode/VSCode-linux-{}/data".format(arch), "temp:vscode-data")

    # Unpack vscode.
    mkdir("vscode")
    remove("vscode/VSCode-linux-{}".format(arch))
    unpack("temp:vscode-linux-{}.tar.gz".format(arch), "vscode")

    # Restore the data directory.
    if exists("temp:vscode-data"):
        move("temp:vscode-data", "vscode/VSCode-linux-{}/data".format(arch))
    else:
        mkdir("vscode/VSCode-linux-{}/data".format(arch))

    # Install the Ren'Py extension.
    processing(_("Installing the Ren'Py extension."))
    run("vscode/VSCode-linux-{}/code".format(arch), "vscode/VSCode-linux-{}/resources/app/out/cli.js".format(arch), "--ms-enable-electron-run-as-node",
        "--install-extension", "renpy.language-renpy",
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
        "--install-extension", "renpy.language-renpy",
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
        "--install-extension", "renpy.language-renpy",
        environ={ "VSCODE_DEV" : "", "ELECTRON_RUN_AS_NODE" : "1" })

else:
    error(_("Visual Studio Code is not supported on your platform."))
