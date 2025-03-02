# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from importlib import import_module

from qiime2.plugin import (Plugin, Bool, Int, Str, Choices, Range, List, Set,
                           Collection, Visualization, Metadata, MetadataColumn,
                           Categorical, Numeric, TypeMatch)

from .format import (
    IntSequenceFormat,
    IntSequenceFormatV2,
    IntSequenceMultiFileDirectoryFormat,
    MappingFormat,
    SingleIntFormat,
    IntSequenceDirectoryFormat,
    IntSequenceV2DirectoryFormat,
    MappingDirectoryFormat,
    FourIntsDirectoryFormat,
    RedundantSingleIntDirectoryFormat,
    UnimportableFormat,
    UnimportableDirectoryFormat,
    EchoFormat,
    EchoDirectoryFormat,
    Cephalapod,
    CephalapodDirectoryFormat,
    ImportableOnlyFormat,
    ExportableOnlyFormat
)

from .type import (IntSequence1, IntSequence2, IntSequence3, Mapping, FourInts,
                   SingleInt, Kennel, Dog, Cat, C1, C2, C3, Foo, Bar, Baz,
                   AscIntSequence, Squid, Octopus, Cuttlefish)
from .method import (concatenate_ints, split_ints, merge_mappings,
                     identity_with_metadata, identity_with_metadata_column,
                     identity_with_categorical_metadata_column,
                     identity_with_numeric_metadata_column,
                     identity_with_optional_metadata,
                     identity_with_optional_metadata_column,
                     params_only_method, no_input_method, deprecated_method,
                     optional_artifacts_method, long_description_method,
                     docstring_order_method, variadic_input_method,
                     unioned_primitives, type_match_list_and_set, union_inputs,
                     list_of_ints, dict_of_ints, returns_int, varied_method,
                     collection_inner_union, collection_outer_union,
                     dict_params, list_params, _underscore_method)
from .visualizer import (most_common_viz, mapping_viz, params_only_viz,
                         no_input_viz)
from .pipeline import (parameter_only_pipeline, typical_pipeline,
                       optional_artifact_pipeline, visualizer_only_pipeline,
                       pipelines_in_pipeline, resumable_pipeline,
                       resumable_varied_pipeline,
                       resumable_nested_varied_pipeline,
                       internal_fail_pipeline, de_facto_list_pipeline,
                       de_facto_dict_pipeline, de_facto_collection_pipeline,
                       list_pipeline, collection_pipeline, pointless_pipeline,
                       failing_pipeline)
from ..cite import Citations

from .examples import (concatenate_ints_simple, concatenate_ints_complex,
                       typical_pipeline_simple, typical_pipeline_complex,
                       comments_only, identity_with_metadata_simple,
                       identity_with_metadata_merging,
                       identity_with_metadata_column_get_mdc,
                       variadic_input_simple, optional_inputs,
                       comments_only_factory, collection_list_of_ints,
                       collection_dict_of_ints,
                       )


citations = Citations.load('citations.bib', package='qiime2.core.testing')
dummy_plugin = Plugin(
    name='dummy-plugin',
    description='Description of dummy plugin.',
    short_description='Dummy plugin for testing.',
    version='0.0.0-dev',
    website='https://github.com/qiime2/qiime2',
    package='qiime2.core.testing',
    user_support_text='For help, see https://qiime2.org',
    citations=[citations['unger1998does'], citations['berry1997flying']]
)

import_module('qiime2.core.testing.transformer')
import_module('qiime2.core.testing.validator')


# Register semantic types
dummy_plugin.register_semantic_types(IntSequence1, IntSequence2, IntSequence3,
                                     Mapping, FourInts, Kennel, Dog, Cat,
                                     SingleInt, C1, C2, C3, Foo, Bar, Baz,
                                     AscIntSequence, Squid, Octopus,
                                     Cuttlefish)

# Register formats
dummy_plugin.register_formats(
    IntSequenceFormatV2, MappingFormat, IntSequenceV2DirectoryFormat,
    IntSequenceMultiFileDirectoryFormat, MappingDirectoryFormat,
    EchoDirectoryFormat, EchoFormat, Cephalapod, CephalapodDirectoryFormat,
    ImportableOnlyFormat, ExportableOnlyFormat)

dummy_plugin.register_formats(
    FourIntsDirectoryFormat, UnimportableDirectoryFormat, UnimportableFormat,
    citations=[citations['baerheim1994effect']])

dummy_plugin.register_views(
    int, IntSequenceFormat, IntSequenceDirectoryFormat,
    SingleIntFormat, RedundantSingleIntDirectoryFormat,
    citations=[citations['mayer2012walking']])


# Create IntSequence1 import example usage example
def is1_use(use):
    def factory():
        from qiime2.core.testing.format import IntSequenceFormat
        from qiime2.plugin.util import transform
        ff = transform([1, 2, 3], to_type=IntSequenceFormat)

        ff.validate()
        return ff

    to_import = use.init_format('to_import', factory, ext='.hello')

    use.import_from_format('ints',
                           semantic_type='IntSequence1',
                           variable=to_import,
                           view_type='IntSequenceFormat')


dummy_plugin.register_artifact_class(
    IntSequence1,
    directory_format=IntSequenceDirectoryFormat,
    description="The first IntSequence",
    examples={'IntSequence1 import example': is1_use}
)


# Create IntSequence2 import example usage example
def is2_use(use):
    def factory():
        from qiime2.core.testing.format import IntSequenceFormatV2
        from qiime2.plugin.util import transform
        ff = transform([1, 2, 3], to_type=IntSequenceFormatV2)

        ff.validate()
        return ff

    to_import = use.init_format('to_import', factory, ext='.hello')

    use.import_from_format('ints',
                           semantic_type='IntSequence2',
                           variable=to_import,
                           view_type='IntSequenceFormatV2')


dummy_plugin.register_artifact_class(
    IntSequence2,
    directory_format=IntSequenceV2DirectoryFormat,
    description="The second IntSequence",
    examples={'IntSequence2 import example': is2_use}
)
dummy_plugin.register_semantic_type_to_format(
    IntSequence3,
    directory_format=IntSequenceMultiFileDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    Mapping,
    directory_format=MappingDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    FourInts,
    directory_format=FourIntsDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    SingleInt,
    directory_format=RedundantSingleIntDirectoryFormat
)
dummy_plugin.register_semantic_type_to_format(
    Kennel[Dog | Cat],
    directory_format=MappingDirectoryFormat
)

dummy_plugin.register_semantic_type_to_format(
    C3[C1[Foo | Bar | Baz] | Foo | Bar | Baz,
       C1[Foo | Bar | Baz] | Foo | Bar | Baz,
       C1[Foo | Bar | Baz] | Foo | Bar | Baz]
    | C2[Foo | Bar | Baz, Foo | Bar | Baz]
    | C1[Foo | Bar | Baz | C2[Foo | Bar | Baz, Foo | Bar | Baz]]
    | Foo
    | Bar
    | Baz,
    directory_format=EchoDirectoryFormat)

dummy_plugin.register_semantic_type_to_format(
    AscIntSequence,
    directory_format=IntSequenceDirectoryFormat)

dummy_plugin.register_semantic_type_to_format(
    Squid | Octopus | Cuttlefish,
    directory_format=CephalapodDirectoryFormat)

# TODO add an optional parameter to this method when they are supported
dummy_plugin.methods.register_function(
    function=concatenate_ints,
    inputs={
        'ints1': IntSequence1 | IntSequence2,
        'ints2': IntSequence1,
        'ints3': IntSequence2
    },
    parameters={
        'int1': Int,
        'int2': Int
    },
    outputs={
        'concatenated_ints': IntSequence1
    },
    name='Concatenate integers',
    description='This method concatenates integers into'
                ' a single sequence in the order they are provided.',
    citations=[citations['baerheim1994effect']],
    examples={'concatenate_ints_simple': concatenate_ints_simple,
              'concatenate_ints_complex': concatenate_ints_complex,
              'comments_only': comments_only,
              # execute factory to make a closure to test pickling
              'comments_only_factory': comments_only_factory(),
              },
)

T = TypeMatch([IntSequence1, IntSequence2])
dummy_plugin.methods.register_function(
    function=split_ints,
    inputs={
        'ints': T
    },
    parameters={},
    outputs={
        'left': T,
        'right': T
    },
    name='Split sequence of integers in half',
    description='This method splits a sequence of integers in half, returning '
                'the two halves (left and right). If the input sequence\'s '
                'length is not evenly divisible by 2, the right half will '
                'have one more element than the left.',
    citations=[
        citations['witcombe2006sword'], citations['reimers2012response']]
)

dummy_plugin.methods.register_function(
    function=merge_mappings,
    inputs={
        'mapping1': Mapping,
        'mapping2': Mapping
    },
    input_descriptions={
        'mapping1': 'Mapping object to be merged'
    },
    parameters={},
    outputs=[
        ('merged_mapping', Mapping)
    ],
    output_descriptions={
        'merged_mapping': 'Resulting merged Mapping object'},
    name='Merge mappings',
    description='This method merges two mappings into a single new mapping. '
                'If a key is shared between mappings and the values differ, '
                'an error will be raised.'
)

dummy_plugin.methods.register_function(
    function=identity_with_metadata,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': Metadata
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes metadata',
    examples={
        'identity_with_metadata_simple': identity_with_metadata_simple,
        'identity_with_metadata_merging': identity_with_metadata_merging},
)

dummy_plugin.methods.register_function(
    function=long_description_method,
    inputs={
        'mapping1': Mapping
    },
    input_descriptions={
        'mapping1': ("This is a very long description. If asked about its "
                     "length, I would have to say it is greater than 79 "
                     "characters.")
    },
    parameters={
        'name': Str,
        'age': Int
    },
    parameter_descriptions={
        'name': ("This is a very long description. If asked about its length,"
                 " I would have to say it is greater than 79 characters.")
    },
    outputs=[
        ('out', Mapping)
    ],
    output_descriptions={
        'out': ("This is a very long description. If asked about its length,"
                " I would have to say it is greater than 79 characters.")
    },
    name="Long Description",
    description=("This is a very long description. If asked about its length,"
                 " I would have to say it is greater than 79 characters.")
)

dummy_plugin.methods.register_function(
    function=docstring_order_method,
    inputs={
        'req_input': Mapping,
        'opt_input': Mapping
    },
    input_descriptions={
        'req_input': "This should show up first.",
        'opt_input': "This should show up third."
    },
    parameters={
        'req_param': Str,
        'opt_param': Int
    },
    parameter_descriptions={
        'req_param': "This should show up second.",
        'opt_param': "This should show up fourth."
    },
    outputs=[
        ('out', Mapping)
    ],
    output_descriptions={
        'out': "This should show up last, in it's own section."
    },
    name="Docstring Order",
    description=("Tests whether inputs and parameters are rendered in "
                 "signature order")
)


dummy_plugin.methods.register_function(
    function=identity_with_metadata_column,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': MetadataColumn[Categorical | Numeric]
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, '
                'but takes a generic metadata column',
    examples={
        'identity_with_metadata_column_get_mdc':
            identity_with_metadata_column_get_mdc,
    },
)


dummy_plugin.methods.register_function(
    function=identity_with_categorical_metadata_column,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': MetadataColumn[Categorical]
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes a categorical metadata '
                'column'
)


dummy_plugin.methods.register_function(
    function=identity_with_numeric_metadata_column,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': MetadataColumn[Numeric]
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes a numeric metadata column'
)


dummy_plugin.methods.register_function(
    function=identity_with_optional_metadata,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': Metadata
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes optional metadata'
)

dummy_plugin.methods.register_function(
    function=identity_with_optional_metadata_column,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={
        'metadata': MetadataColumn[Numeric | Categorical]
    },
    outputs=[
        ('out', IntSequence1)
    ],
    name='Identity',
    description='This method does nothing, but takes an optional generic '
                'metadata column'
)


dummy_plugin.methods.register_function(
    function=params_only_method,
    inputs={},
    parameters={
        'name': Str,
        'age': Int
    },
    outputs=[
        ('out', Mapping)
    ],
    name='Parameters only method',
    description='This method only accepts parameters.',
)

dummy_plugin.methods.register_function(
    function=unioned_primitives,
    inputs={},
    parameters={
        'foo': Int % Range(1, None) | Str % Choices(['auto_foo']),
        'bar': Int % Range(1, None) | Str % Choices(['auto_bar']),
    },
    outputs=[
        ('out', Mapping)
    ],
    name='Unioned primitive parameter',
    description='This method has a unioned primitive parameter'
)

dummy_plugin.methods.register_function(
    function=no_input_method,
    inputs={},
    parameters={},
    outputs=[
        ('out', Mapping)
    ],
    name='No input method',
    description='This method does not accept any type of input.'
)

dummy_plugin.methods.register_function(
    function=deprecated_method,
    inputs={},
    parameters={},
    outputs=[
        ('out', Mapping)
    ],
    name='A deprecated method',
    description='This deprecated method does not accept any type of input.',
    deprecated=True,
)


dummy_plugin.methods.register_function(
    function=optional_artifacts_method,
    inputs={
        'ints': IntSequence1,
        'optional1': IntSequence1,
        'optional2': IntSequence1 | IntSequence2
    },
    parameters={
        'num1': Int,
        'num2': Int
    },
    outputs=[
        ('output', IntSequence1)
    ],
    name='Optional artifacts method',
    description='This method declares optional artifacts and concatenates '
                'whatever integers are supplied as input.',
    examples={'optional_inputs': optional_inputs},
)

dummy_plugin.methods.register_function(
    function=variadic_input_method,
    inputs={
        'ints': List[IntSequence1 | IntSequence2],
        'int_set': Set[SingleInt]
    },
    parameters={
        'nums': Set[Int],
        'opt_nums': List[Int % Range(10, 20)]
    },
    outputs=[
        ('output', IntSequence1)
    ],
    name='Test variadic inputs',
    description='This method concatenates all of its variadic inputs',
    input_descriptions={
        'ints': 'A list of int artifacts',
        'int_set': 'A set of int artifacts'
    },
    parameter_descriptions={
        'nums': 'A set of ints',
        'opt_nums': 'An optional list of ints'
    },
    output_descriptions={
        'output': 'All of the above mashed together'
    },
    examples={'variadic_input_simple': variadic_input_simple},
)

T = TypeMatch([IntSequence1, IntSequence2])
dummy_plugin.methods.register_function(
    function=type_match_list_and_set,
    inputs={
        'ints': T
    },
    parameters={
        'strs1': List[Str],
        'strs2': Set[Str]
    },
    outputs=[
        ('output', T)
    ],
    name='TypeMatch with list and set params',
    description='Just a method with a TypeMatch and list/set params',
    input_descriptions={
        'ints': 'An int artifact'
    },
    parameter_descriptions={
        'strs1': 'A list of strings',
        'strs2': 'A set of strings'
    },
    output_descriptions={
        'output': '[0]'
    }
)

dummy_plugin.visualizers.register_function(
    function=params_only_viz,
    inputs={},
    parameters={
        'name': Str,
        'age': Int % Range(0, None)
    },
    name='Parameters only viz',
    description='This visualizer only accepts parameters.'
)


dummy_plugin.visualizers.register_function(
    function=no_input_viz,
    inputs={},
    parameters={},
    name='No input viz',
    description='This visualizer does not accept any type of input.'
)


dummy_plugin.visualizers.register_function(
    function=most_common_viz,
    inputs={
        'ints': IntSequence1 | IntSequence2
    },
    parameters={},
    name='Visualize most common integers',
    description='This visualizer produces HTML and TSV outputs containing the '
                'input sequence of integers ordered from most- to '
                'least-frequently occurring, along with their respective '
                'frequencies.',
    citations=[citations['barbeito1967microbiological']]
)

# TODO add optional parameters to this method when they are supported
dummy_plugin.visualizers.register_function(
    function=mapping_viz,
    inputs={
        'mapping1': Mapping,
        'mapping2': Mapping
    },
    parameters={
        'key_label': Str,
        'value_label': Str
    },
    name='Visualize two mappings',
    description='This visualizer produces an HTML visualization of two '
                'key-value mappings, each sorted in alphabetical order by key.'
)

dummy_plugin.pipelines.register_function(
    function=parameter_only_pipeline,
    inputs={},
    parameters={
        'int1': Int,
        'int2': Int,
        'metadata': Metadata
    },
    outputs=[
        ('foo', IntSequence2),
        ('bar', IntSequence1)
    ],
    name='Do multiple things',
    description='This pipeline only accepts parameters',
    parameter_descriptions={
        'int1': 'An integer, the first one in fact',
        'int2': 'An integer, the second one',
        'metadata': 'Very little is done with this'
    },
    output_descriptions={
        'foo': 'Foo - "The Integers of 2"',
        'bar': 'Bar - "What a sequences"'
    },
)

dummy_plugin.pipelines.register_function(
    function=typical_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'mapping': Mapping
    },
    parameters={
        'do_extra_thing': Bool,
        'add': Int
    },
    outputs=[
        ('out_map', Mapping),
        ('left', IntSequence1),
        ('right', IntSequence1),
        ('left_viz', Visualization),
        ('right_viz', Visualization)
    ],
    input_descriptions={
        'int_sequence': 'A sequence of ints',
        'mapping': 'A map to a number other than 42 will fail'
    },
    parameter_descriptions={
        'do_extra_thing': 'Increment `left` by `add` if true',
        'add': 'Unused if `do_extra_thing` is false'
    },
    output_descriptions={
        'out_map': 'Same as input',
        'left': 'Left side of `int_sequence` unless `do_extra_thing`',
        'right': 'Right side of `int_sequence`',
        'left_viz': '`left` visualized',
        'right_viz': '`right` visualized'
    },
    name='A typical pipeline with the potential to raise an error',
    description='Waste some time shuffling data around for no reason',
    citations=citations,  # ALL of them.
    examples={'typical_pipeline_simple': typical_pipeline_simple,
              'typical_pipeline_complex': typical_pipeline_complex},
)

dummy_plugin.pipelines.register_function(
    function=optional_artifact_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'single_int': SingleInt
    },
    parameters={},
    outputs=[
        ('ints', IntSequence1)
    ],
    input_descriptions={
        'int_sequence': 'Some integers',
        'single_int': 'An integer'
    },
    output_descriptions={
        'ints': 'More integers'
    },
    name='Do stuff normally, but override this one step sometimes',
    description='Creates its own single_int, unless provided'
)

dummy_plugin.pipelines.register_function(
    function=visualizer_only_pipeline,
    inputs={
        'mapping': Mapping
    },
    parameters={},
    outputs=[
        ('viz1', Visualization),
        ('viz2', Visualization)
    ],
    input_descriptions={
        'mapping': 'A mapping to look at twice'
    },
    output_descriptions={
        'viz1': 'The no input viz',
        'viz2': 'Our `mapping` seen through the lense of "foo" *and* "bar"'
    },
    name='Visualize many things',
    description='Looks at both nothing and a mapping'
)

dummy_plugin.pipelines.register_function(
    function=pipelines_in_pipeline,
    inputs={
        'int_sequence': IntSequence1,
        'mapping': Mapping
    },
    parameters={},
    outputs=[
        ('int1', SingleInt),
        ('out_map', Mapping),
        ('left', IntSequence1),
        ('right', IntSequence1),
        ('left_viz', Visualization),
        ('right_viz', Visualization),
        ('viz1', Visualization),
        ('viz2', Visualization)
    ],
    name='Do a great many things',
    description=('Mapping is chained from typical_pipeline into '
                 'visualizer_only_pipeline')
)

dummy_plugin.pipelines.register_function(
    function=resumable_pipeline,
    inputs={
        'int_list': List[SingleInt],
        'int_dict': Collection[SingleInt],
    },
    parameters={
        'fail': Bool
    },
    outputs=[
        ('list_return', Collection[SingleInt]),
        ('dict_return', Collection[SingleInt]),
    ],
    name='To be resumed',
    description=('Called first with fail=True then again with fail=False '
                 'meant to reuse results from first run durng second run')
)

T = TypeMatch([IntSequence1, IntSequence2])
dummy_plugin.pipelines.register_function(
    function=resumable_varied_pipeline,
    inputs={
        'ints1': Collection[SingleInt],
        'ints2': List[T],
        'int1': SingleInt,
    },
    parameters={
        'string': Str,
        'metadata': Metadata,
        'fail': Bool,
    },
    outputs=[
        ('ints1_ret', Collection[SingleInt]),
        ('ints2_ret', Collection[T]),
        ('int1_ret', SingleInt),
        ('list_ret', Collection[SingleInt]),
        ('dict_ret', Collection[SingleInt]),
        ('identity_ret', T),
        ('viz', Visualization),
    ],
    name='To be resumed',
    description=('Called first with fail=True then again with fail=False '
                 'meant to reuse results from first run durng second run')
)

dummy_plugin.pipelines.register_function(
    function=resumable_nested_varied_pipeline,
    inputs={
        'ints1': Collection[SingleInt],
        'ints2': List[T],
        'int1': SingleInt,
    },
    parameters={
        'string': Str,
        'metadata': Metadata,
        'fail': Bool,
    },
    outputs=[
        ('ints1_ret', Collection[SingleInt]),
        ('ints2_ret', Collection[T]),
        ('int1_ret', SingleInt),
        ('list_ret', Collection[SingleInt]),
        ('dict_ret', Collection[SingleInt]),
        ('identity_ret', T),
        ('viz', Visualization),
    ],
    name='To be resumed',
    description=('Called first with fail=True then again with fail=False '
                 'meant to reuse results from first run durng second run')
)

dummy_plugin.pipelines.register_function(
    function=internal_fail_pipeline,
    inputs={
        'ints1': Collection[SingleInt],
        'ints2': List[T],
        'int1': SingleInt,
    },
    parameters={
        'string': Str,
        'fail': Bool,
    },
    outputs=[
        ('ints1_ret', Collection[SingleInt]),
        ('ints2_ret', Collection[T]),
        ('int1_ret', SingleInt),
    ],
    name='Internal fail pipeline',
    description=('This pipeline is called inside of '
                 'resumable_nested_variable_pipeline to mimic a nested '
                 'pipeline failing')
)

dummy_plugin.pipelines.register_function(
    function=de_facto_list_pipeline,
    inputs={},
    parameters={
        'kwarg': Bool,
        'non_proxies': Bool
    },
    outputs=[
        ('output', Collection[SingleInt]),
    ],
    name='Pipeline that creates a de facto list of artifacts.',
    description=('This pipeline is supposed to be run in parallel to assert '
                 'that we can handle a de facto list of proxies.')
)

dummy_plugin.pipelines.register_function(
    function=de_facto_dict_pipeline,
    inputs={},
    parameters={
        'kwarg': Bool,
        'non_proxies': Bool
    },
    outputs=[
        ('output', Collection[SingleInt]),
    ],
    name='Pipeline that creates a de facto dict of artifacts.',
    description=('This pipeline is supposed to be run in parallel to assert '
                 'that we can handle a de facto dict of proxies.')
)

dummy_plugin.pipelines.register_function(
    function=list_pipeline,
    inputs={'ints': List[IntSequence1]},
    parameters={},
    outputs=[('output', Collection[SingleInt])],
    name='Takes a list and returns a collection',
    description='Takes a list and returns a collection'
)

dummy_plugin.pipelines.register_function(
    function=collection_pipeline,
    inputs={'ints': Collection[IntSequence1]},
    parameters={},
    outputs=[('output', Collection[SingleInt])],
    name='Takes a collection and returns a collection',
    description='Takes a collection and returns a collection'
)

dummy_plugin.pipelines.register_function(
    function=de_facto_collection_pipeline,
    inputs={},
    parameters={},
    outputs=[('output', Collection[Mapping])],
    name='Returns de facto ResultCollection',
    description='Takes nothing and returns de facto ResultCollection'
)

dummy_plugin.pipelines.register_function(
    function=pointless_pipeline,
    inputs={},
    parameters={},
    outputs=[('random_int', SingleInt)],
    name='Get an integer',
    description='Integer was chosen to be 4 by a random dice roll'
)

dummy_plugin.pipelines.register_function(
    function=failing_pipeline,
    inputs={
        'int_sequence': IntSequence1
    },
    parameters={
        'break_from': Str % Choices(
            {'arity', 'return-view', 'type', 'method', 'internal', 'no-plugin',
             'no-action'})
    },
    outputs=[('mapping', Mapping)],
    name='Test different ways of failing',
    description=('This is useful to make sure all of the intermediate stuff is'
                 ' cleaned up the way it should be.')
)

dummy_plugin.methods.register_function(
    function=union_inputs,
    inputs={
        'ints1': IntSequence1,
        'ints2': IntSequence2,
    },
    parameters={},
    outputs=[
        ('ints', IntSequence1)
    ],
    name='Inputs with typing.Union',
    input_descriptions={
        'ints1': 'An int artifact',
        'ints2': 'An int artifact'
    },
    output_descriptions={
        'ints': '[0]',
    },
    description='This method accepts a list or dict as first input.'
)

dummy_plugin.methods.register_function(
    function=list_of_ints,
    inputs={
        'ints': List[SingleInt]
    },
    parameters={},
    outputs=[
        ('output', Collection[SingleInt])
    ],
    name='Reverses list of inputs',
    description='Some description',
    input_descriptions={
        'ints': 'Collection of ints'
    },
    output_descriptions={
        'output': 'Reversed Collection of ints'
    },
    examples={'collection_list_of_ints': collection_list_of_ints}
)

dummy_plugin.methods.register_function(
    function=returns_int,
    inputs={},
    parameters={
        'int': Int
    },
    outputs=[
        ('output', SingleInt)
    ],
    name='Returns int',
    description='Just returns an int',
)

dummy_plugin.methods.register_function(
    function=dict_of_ints,
    inputs={
        'ints': Collection[SingleInt]
    },
    parameters={},
    outputs=[
        ('output', Collection[SingleInt])
    ],
    name='Takes ints',
    description='Some description',
    input_descriptions={
        'ints': 'Collection of ints'
    },
    output_descriptions={
        'output': 'Collection of ints'
    },
    examples={'collection_dict_of_ints': collection_dict_of_ints}
)

dummy_plugin.methods.register_function(
    function=collection_inner_union,
    inputs={
        'ints': Collection[IntSequence1 | IntSequence2]
    },
    parameters={},
    outputs=[
        ('output', Collection[IntSequence1])
    ],
    name='Takes ints',
    description='Some description',
    input_descriptions={
        'ints': 'Collection of ints'
    },
    output_descriptions={
        'output': 'Collection of ints'
    }
)

dummy_plugin.methods.register_function(
    function=collection_outer_union,
    inputs={
        'ints': Collection[IntSequence1] | Collection[IntSequence2]
    },
    parameters={},
    outputs=[
        ('output', Collection[IntSequence1])
    ],
    name='Takes ints',
    description='Some description',
    input_descriptions={
        'ints': 'Collection of ints'
    },
    output_descriptions={
        'output': 'Collection of ints'
    }
)

dummy_plugin.methods.register_function(
    function=dict_params,
    inputs={},
    parameters={
        'ints': Collection[Int],
    },
    outputs=[
        ('output', Collection[SingleInt])
    ],
    name='Parameters only method',
    description='This method only accepts parameters.',
)

dummy_plugin.methods.register_function(
    function=list_params,
    inputs={},
    parameters={
        'ints': List[Int],
    },
    outputs=[
        ('output', Collection[SingleInt])
    ],
    name='Parameters only method',
    description='This method only accepts parameters.',
)

dummy_plugin.methods.register_function(
    function=varied_method,
    inputs={
        'ints1': List[SingleInt],
        'ints2': Collection[IntSequence1],
        'int1': SingleInt
    },
    parameters={
        'string': Str,
    },
    outputs=[
        ('ints', Collection[SingleInt]),
        ('sequences', Collection[IntSequence1]),
        ('int', SingleInt)
    ],
    name='Takes and returns a combination of colletions and non collections',
    description='Takes and returns a combination of colletions and non'
                ' collections'
)

dummy_plugin.methods.register_function(
    function=_underscore_method,
    inputs={},
    parameters={},
    outputs=[
        ('int', SingleInt)
    ],
    name='Starts with an underscore',
    description='Exists to test that the cli does not render actions that'
                ' start with an underscore by default'
)

import_module('qiime2.core.testing.mapped')


other_plugin = Plugin(
    name='other-plugin',
    description='',
    short_description='',
    version='0.0.0-dev',
    website='',
    package='qiime2.core.archive.provenance_lib.tests',
    user_support_text='',
    citations=[]
)
other_plugin.methods.register_function(
    function=concatenate_ints,
    inputs={
        'ints1': IntSequence1,
        'ints2': IntSequence1,
        'ints3': IntSequence1,
    },
    parameters={
        'int1': Int,
        'int2': Int
    },
    outputs={
        'concatenated_ints': IntSequence1
    },
    name='Concatenate integers',
    description='Some description'
)
