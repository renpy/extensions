#!/usr/bin/env python3

import pathlib
import ecdsa
import ecdsa.util


ROOT = pathlib.Path(__file__).parent


def main():

    with open(ROOT / '..' / 'keys' / 'renpy_ecdsa_private.pem', 'rb') as f:
        key = ecdsa.SigningKey.from_pem(f.read())


    for p in pathlib.Path('.').glob("*/*.py"):
        data = p.read_bytes()

        sig = key.sign_deterministic(data)

        with open(str(p) + ".sig", "wb") as f:
            f.write(sig)

if __name__ == "__main__":
    main()
