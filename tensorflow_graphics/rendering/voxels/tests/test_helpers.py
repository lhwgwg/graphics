#Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test helpers for the voxels module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def generate_random_test_voxels_render():
  """Generates random test for the voxels rendering functions."""
  batch_shape = np.random.randint(1, 3)
  voxels_shape = np.random.randint(2, 8, size=(3)).tolist()
  signals_dimension = np.random.randint(2, 4)

  random_voxels = np.random.uniform(size=[batch_shape] + voxels_shape +
                                    [signals_dimension])
  return random_voxels


def generate_preset_test_voxels_visual_hull_render():
  """Generates preset test for the visual hull voxels rendering function."""
  voxels = np.array([[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.3, 0.7, 0.1], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.3, 0.2, 0]]],
                      [[[0.15, 0.69, 0.57], [0.07, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.17, 0.01, 1.22], [0.2, 1, 0.4], [0.67, 0.94, 0.14]]],
                      [[[0, 0, 0], [0.17, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.88, 0.09, 0.45]]],
                      [[[1, 0, 0], [0, 0, 0], [1, 0, 0]],
                       [[0.88, 0.09, 0.5], [0.71, 0.61, 0.4], [0.14, 0, 0.22]],
                       [[0.71, 0.61, 0.45], [0.71, 0.7, 0.43], [0.3, 0.2, 0]]]],
                     [[[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
                       [[0.3, 0.7, 0.1], [0.15, 0.69, 0.5], [0.88, 0.09, 0.45]],
                       [[0.07, 0.33, 0.55], [0.2, 1, 0.4], [0.4, 0.34, 0.43]]],
                      [[[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                       [[0.19, 0.06, 0.24], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.67, 0.94, 0.14], [0.2, 1, 0.4], [0.15, 0.69, 0.57]]],
                      [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.74, 0.67, 0.4], [0.64, 0.8, 0.19], [0.9, 0.6, 0.48]],
                       [[0.1, 0.9, 0], [0.02, 0.37, 0.56], [0.62, 0.98, 0.19]]],
                      [[[0.04, 0.87, 0.37], [0, 0, 0], [1, 0, 0]],
                       [[0.3, 0.7, 0.1], [0.24, 0.12, 0.7], [0.76, 0.64, 0.79]],
                       [[0.7, 0.2, 0.2], [0.4, 1, 0.9], [0.19, 0.66, 0.03]]]]])

  images = np.array([[[[0, 0, 0],
                       [0.77686984, 0.59343034, 0.59343034],
                       [0.45118836, 0.87754357, 0.32967995]],
                      [[0.19748120, 0.63940506, 0.67372021],
                       [0.91107838, 0.73286470, 0.57683792],
                       [0.64654532, 0.85772593, 0.82795514]],
                      [[0.15633518, 0.28107627, 0.42305019],
                       [0.91107838, 0.73286470, 0.57683792],
                       [0.69272126, 0.86330457, 0.57258507]],
                      [[0.86466472, 0, 0],
                       [0.82271559, 0.50341470, 0.67372021],
                       [0.82093385, 0.77909002, 0.58521709]]],
                     [[[0, 0, 0.63212055],
                       [0.73552274, 0.77236231, 0.65006225],
                       [0.48829142, 0.81175293, 0.74842145]],
                      [[0, 0.950212931, 0],
                       [0.75092470, 0.22894841, 0.64654532],
                       [0.63940506, 0.92792154, 0.67044104]],
                      [[0, 0, 0],
                       [0.89771579, 0.87381422, 0.65699148],
                       [0.52288608, 0.89460078, 0.52763345]],
                      [[0.64654532, 0.58104845, 0.30926567],
                       [0.72746821, 0.76776373, 0.79607439],
                       [0.724729, 0.844327, 0.676967]]]])  # pyformat: disable

  return voxels, images


def generate_preset_test_voxels_absorption_render():
  """Generates preset test for the absorption voxels rendering function."""
  voxels = np.array([[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.3, 0.7, 0.1], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.3, 0.2, 0]]],
                      [[[0.15, 0.69, 0.57], [0.07, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.17, 0.01, 1.22], [0.2, 1, 0.4], [0.67, 0.94, 0.14]]],
                      [[[0, 0, 0], [0.17, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.88, 0.09, 0.45]]],
                      [[[1, 0, 0], [0, 0, 0], [1, 0, 0]],
                       [[0.88, 0.09, 0.5], [0.71, 0.61, 0.4], [0.14, 0, 0.22]],
                       [[0.71, 0.61, 0.45], [0.71, 0.7, 0.43], [0.3, 0.2, 0]]]],
                     [[[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
                       [[0.3, 0.7, 0.1], [0.15, 0.69, 0.5], [0.88, 0.09, 0.45]],
                       [[0.07, 0.33, 0.55], [0.2, 1, 0.4], [0.4, 0.34, 0.43]]],
                      [[[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                       [[0.19, 0.06, 0.24], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.67, 0.94, 0.14], [0.2, 1, 0.4], [0.15, 0.69, 0.57]]],
                      [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.74, 0.67, 0.4], [0.64, 0.8, 0.19], [0.9, 0.6, 0.48]],
                       [[0.1, 0.9, 0], [0.02, 0.37, 0.56], [0.62, 0.98, 0.19]]],
                      [[[0.04, 0.87, 0.37], [0, 0, 0], [1, 0, 0]],
                       [[0.3, 0.7, 0.1], [0.24, 0.12, 0.7], [0.76, 0.64, 0.79]],
                       [[0.7, 0.2, 0.2], [0.4, 1, 0.9], [0.19, 0.66, 0.03]]]]])

  images = np.array([[[[0, 0, 0],
                       [0.6175, 0.413375, 0.43],
                       [0.27325, 0.7525, 0.2]],
                      [[0.107375, 0.453075, 0.481625],
                       [0.7919875, 0.54112625, 0.383775],
                       [0.4523725, 0.736325, 0.70984]],
                      [[0.085, 0.165, 0.275],
                       [0.7919875, 0.54112625, 0.383775],
                       [0.5212, 0.737375, 0.38]],
                      [[0.75, 0, 0],
                       [0.664084, 0.336275, 0.466],
                       [0.64637875, 0.593425, 0.391625]]],
                     [[[0, 0, 0.5],
                       [0.5597, 0.59340875, 0.4478125],
                       [0.3052, 0.653475, 0.5447]],
                      [[0, 0.875, 0],
                       [0.59275, 0.124575, 0.472],
                       [0.4463875, 0.826425, 0.46804]],
                      [[0, 0, 0],
                       [0.76438, 0.7207, 0.44976],
                       [0.351055, 0.7713925, 0.3484]],
                      [[0.51, 0.435, 0.185],
                       [0.53624, 0.58452, 0.6264125],
                       [0.5294, 0.6985, 0.512425]]]])  # pyformat: disable

  return voxels, images


def generate_preset_test_voxels_emission_absorption_render():
  """Generates preset test for the emission absorption voxels rendering function."""
  voxels = np.array([[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.3, 0.7, 0.1], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.3, 0.2, 0]]],
                      [[[0.15, 0.69, 0.57], [0.07, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.17, 0.01, 1.22], [0.2, 1, 0.4], [0.67, 0.94, 0.14]]],
                      [[[0, 0, 0], [0.17, 0.33, 0.55], [0, 0, 0]],
                       [[0.71, 0.61, 0.43], [1, 0.1, 0], [0.71, 0.61, 0.43]],
                       [[0.1, 0.9, 0], [0.2, 1, 0.4], [0.88, 0.09, 0.45]]],
                      [[[1, 0, 0], [0, 0, 0], [1, 0, 0]],
                       [[0.88, 0.09, 0.5], [0.71, 0.61, 0.4], [0.14, 0, 0.22]],
                       [[0.71, 0.61, 0.45], [0.71, 0.7, 0.43], [0.3, 0.2, 0]]]],
                     [[[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
                       [[0.3, 0.7, 0.1], [0.15, 0.69, 0.5], [0.88, 0.09, 0.45]],
                       [[0.07, 0.33, 0.55], [0.2, 1, 0.4], [0.4, 0.34, 0.43]]],
                      [[[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                       [[0.19, 0.06, 0.24], [1, 0.1, 0], [0.2, 0.1, 0.8]],
                       [[0.67, 0.94, 0.14], [0.2, 1, 0.4], [0.15, 0.69, 0.57]]],
                      [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0.74, 0.67, 0.4], [0.64, 0.8, 0.19], [0.9, 0.6, 0.48]],
                       [[0.1, 0.9, 0], [0.02, 0.37, 0.56], [0.62, 0.98, 0.19]]],
                      [[[0.04, 0.87, 0.37], [0, 0, 0], [1, 0, 0]],
                       [[0.3, 0.7, 0.1], [0.24, 0.12, 0.7], [0.76, 0.64, 0.79]],
                       [[0.7, 0.2, 0.2], [0.4, 1, 0.9], [0.19, 0.66, 0.03]]]]])

  images = np.array([[[[0, 0, 0],
                       [0.19553845, 0.27123076, 0.82],
                       [0.08, 0.39999998, 0.4]],
                      [[0.10144142, 0.46858389, 0.8065],
                       [0.47932099, 0.41181099, 0.6751],
                       [0.22078022, 0.23262935, 1.11352]],
                      [[0.0935, 0.18149999, 0.55],
                       [0.47932099, 0.41181099, 0.6751],
                       [0.30814825, 0.43694864, 0.67]],
                      [[0, 0, 0],
                       [0.5677705, 0.17392569, 0.766],
                       [0.48741499, 0.44055107, 0.6865]]],
                     [[[0, 0, 1],
                       [0.28019208, 0.40287539, 0.7525],
                       [0.13121746, 0.42573205, 0.8461]],
                      [[0, 0, 0],
                       [0.16451199, 0.064448, 0.848],
                       [0.24191167, 0.69841443, 0.77812]],
                      [[0, 0, 0],
                       [0.56974806, 0.50646416, 0.74728],
                       [0.09611898, 0.32276643, 0.6436]],
                      [[0.0148, 0.32189999, 0.37],
                       [0.3099809, 0.33312645, 0.9433],
                       [0.55598098, 0.41542985, 0.9224]]]])  # pyformat: disable

  return voxels, images