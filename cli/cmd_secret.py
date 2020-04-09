import binascii
import os

import click


@click.command()
@click.argument('bytes', default=128)
def secret(bytes):
    """
    Generate a random secret token.

    Converts the binary output to hexadecimal.

    :return: str
    """
    return click.echo(binascii.b2a_hex(os.urandom(bytes)))
