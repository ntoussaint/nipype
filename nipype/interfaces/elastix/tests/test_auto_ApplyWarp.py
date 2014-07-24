# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.elastix.registration import ApplyWarp

def test_ApplyWarp_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    moving_image=dict(argstr='-in %s',
    mandatory=True,
    ),
    num_threads=dict(argstr='-threads %01d',
    ),
    output_path=dict(argstr='-out %s',
    mandatory=True,
    usedefault=True,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    transform_file=dict(argstr='-tp %s',
    mandatory=True,
    ),
    )
    inputs = ApplyWarp.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ApplyWarp_outputs():
    output_map = dict(warped_file=dict(),
    )
    outputs = ApplyWarp.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
