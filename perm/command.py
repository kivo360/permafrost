"""
    The command line goes here
"""

import click
from perm.validator import get_valid_emails


@click.group()
@click.option('-d', '--debug', default=False)
@click.pass_context
def cli(ctx, debug):
    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context
@click.argument('first')
@click.argument('last')
@click.argument('domain')
@click.option('-m', '--middle', default=None)
def names(ctx, first, last, domain, middle):
    valid_emails = get_valid_emails(first, last, domain, middle=middle, debug=ctx.obj["DEBUG"])
    click.echo(valid_emails)
