from shapeworld.dataset import CaptionAgreementDataset
from shapeworld.generators import RandomAttributesGenerator
from shapeworld.captioners import RegularTypeCaptioner, RelationCaptioner, ExistentialCaptioner


class Spatial(CaptionAgreementDataset):

    def __init__(
        self,
        world_size=64,
        world_color='black',
        shapes=('square', 'rectangle', 'triangle', 'pentagon', 'cross', 'circle', 'semicircle', 'ellipse'),
        colors=('red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'gray'),
        textures=('solid',),
        rotation=True,
        size_range=(0.1, 0.25),
        distortion_range=(2.0, 3.0),
        shade_range=0.4,
        boundary_tolerance=0.25,
        validation_combinations=(('square', 'red', 'solid'), ('triangle', 'green', 'solid'), ('circle', 'blue', 'solid')),
        validation_space_rate_range=(0.0, 1.0),
        validation_combination_rate=0.5,
        test_combinations=(('rectangle', 'yellow', 'solid'), ('cross', 'magenta', 'solid'), ('ellipse', 'cyan', 'solid')),
        test_space_rate_range=(0.0, 1.0),
        test_combination_rate=0.5,
        caption_size=14,
        vocabulary=('.', 'a', 'above', 'an', 'below', 'blue', 'circle', 'cross', 'cyan', 'ellipse', 'gray', 'green', 'is', 'left', 'magenta', 'of', 'pentagon', 'rectangle', 'red', 'right', 'semicircle', 'shape', 'square', 'the', 'to', 'triangle', 'yellow'),
        correct_ratio=0.5,
        train_correct_ratio=None,
        validation_correct_ratio=None,
        test_correct_ratio=None,
        worlds_per_instance=1,
        captions_per_instance=1,
        pixel_noise_stddev=0.0,
        caption_realizer='dmrs',
        language=None
    ):

        world_generator = RandomAttributesGenerator(
            world_size=world_size,
            world_color=world_color,
            shapes=shapes,
            colors=colors,
            textures=textures,
            rotation=rotation,
            size_range=size_range,
            distortion_range=distortion_range,
            shade_range=shade_range,
            collision_tolerance=0.0,
            boundary_tolerance=boundary_tolerance,
            entity_counts=(2,),
            validation_combinations=validation_combinations,
            test_combinations=test_combinations
        )

        world_captioner = ExistentialCaptioner(
            restrictor_captioner=RegularTypeCaptioner(),
            body_captioner=RelationCaptioner(
                reference_captioner=RegularTypeCaptioner(),
                comparison_captioner=RegularTypeCaptioner(),
                relations=('x-rel', 'y-rel')  # , 'z-rel', 'proximity-rel'
            ),
            pragmatical_tautology_rate=1.0
        )

        super(Spatial, self).__init__(
            world_generator=world_generator,
            world_captioner=world_captioner,
            caption_size=caption_size,
            vocabulary=vocabulary,
            correct_ratio=correct_ratio,
            train_correct_ratio=train_correct_ratio,
            validation_correct_ratio=validation_correct_ratio,
            test_correct_ratio=test_correct_ratio,
            worlds_per_instance=worlds_per_instance,
            captions_per_instance=captions_per_instance,
            pixel_noise_stddev=pixel_noise_stddev,
            caption_realizer=caption_realizer,
            language=language
        )


dataset = Spatial
