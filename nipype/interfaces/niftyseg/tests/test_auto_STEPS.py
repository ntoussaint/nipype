# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..steps import STEPS


def test_STEPS_inputs():
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
    position=4,
    ),
    kernel_size=dict(argstr='-STEPS %f',
    mandatory=True,
    position=2,
    ),
    mask_file=dict(argstr='-mask %s',
    mandatory=False,
    ),
    mrf_value=dict(argstr='-MRF_beta %s',
    mandatory=False,
    ),
    out_file=dict(argstr='-out %s',
    genfile=True,
    ),
    prob_flag=dict(argstr='-outProb',
    ),
    prob_update_flag=dict(argstr='-prop_update',
    ),
    template_num=dict(argstr='%i',
    mandatory=True,
    position=3,
    ),
    terminal_output=dict(nohash=True,
    ),
    warped_img_file=dict(argstr='%s',
    mandatory=True,
    position=5,
    ),
    warped_seg_file=dict(argstr='-in %s',
    mandatory=True,
    position=1,
    ),
    )
    inputs = STEPS.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_STEPS_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = STEPS.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value