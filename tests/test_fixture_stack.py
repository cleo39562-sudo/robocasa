import unittest

import numpy as np

from robocasa.models.fixtures.fixture_stack import FixtureStack


class TestFixtureStack(unittest.TestCase):
    def test_base_and_layers_use_stack_generator(self):
        config = {
            "name": "seeded_stack",
            "size": [0.6, 0.6, 0.6],
            "pos": [0.0, 0.0, 0.5],
            "levels": ["box"],
            "percentages": [1.0],
        }
        generator = np.random.default_rng(25)
        scene_fixtures = {}

        stack = FixtureStack(
            config, scene_fixtures, scene_configs={}, scene_style={}, rng=generator
        )

        base, layer = stack.fixtures
        self.assertIs(scene_fixtures["seeded_stack_base"], base)
        self.assertIs(scene_fixtures["seeded_stack_1"], layer)
        self.assertIs(layer.rng, generator)
        self.assertIs(base.rng, generator)
