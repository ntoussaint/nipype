# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import RemoveNeck


def test_RemoveNeck_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-4,
    ),
    out_file=dict(argstr='%s',
    hash_files=False,
    keep_extension=True,
    name_source=['in_file'],
    name_template='%s_noneck',
    position=-1,
    ),
    radius=dict(argstr='-radius %d',
    ),
    subjects_dir=dict(),
    template=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    terminal_output=dict(nohash=True,
    ),
    transform=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    )
    inputs = RemoveNeck.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RemoveNeck_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = RemoveNeck.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
