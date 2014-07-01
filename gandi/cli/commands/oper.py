import click

from gandi.cli.core.cli import cli
from gandi.cli.core.utils import output_generic
from gandi.cli.core.params import pass_gandi


@cli.command()
@pass_gandi
def list(gandi):
    """List operations."""

    output_keys = ['id', 'type', 'step']

    options = {
        'step': ['BILL', 'WAIT', 'RUN'],
    }

    result = gandi.oper.list(options)
    for oper in result:
        gandi.separator_line()
        output_generic(gandi, oper, output_keys)

    return result


@cli.command()
@click.argument('id', type=click.INT)
@pass_gandi
def info(gandi, id):
    """Display information about an operation."""

    output_keys = ['id', 'type', 'step', 'last_error']

    oper = gandi.oper.info(id)
    output_generic(gandi, oper, output_keys)

    return oper
