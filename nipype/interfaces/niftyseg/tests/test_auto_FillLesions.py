# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..lesions import FillLesions


def test_FillLesions_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bin_mask=dict(argstr='-mask %s',
    mandatory=False,
    ),
    cwf=dict(argstr='-cwf %f',
    mandatory=False,
    ),
    debug=dict(argstr='-debug',
    mandatory=False,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_dilation=dict(argstr='-dil %d',
    mandatory=False,
    ),
    in_file=dict(argstr='-i %s',
    mandatory=True,
    position=1,
    ),
    lesion_mask=dict(argstr='-l %s',
    mandatory=True,
    position=2,
    ),
    match=dict(argstr='-match %f',
    mandatory=False,
    ),
    omp_core=dict(argstr='-omp %d',
    ),
    other=dict(argstr='-other',
    mandatory=False,
    ),
    out_datatype=dict(argstr='-odt %s',
    mandatory=False,
    ),
    out_file=dict(argstr='-o %s',
    position=3,
    ),
    search=dict(argstr='-search %f',
    mandatory=False,
    ),
    size=dict(argstr='-size %d',
    mandatory=False,
    ),
    smooth=dict(argstr='-smo %f',
    mandatory=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    verbose=dict(argstr='-v',
    mandatory=False,
    ),
    )
    inputs = FillLesions.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FillLesions_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = FillLesions.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
