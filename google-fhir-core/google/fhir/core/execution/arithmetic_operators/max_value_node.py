# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Support for the MaxValueNode."""
from google.fhir.core.execution.expressions import expression_node


class MaxValueNode(expression_node.ExpressionNode):
  """The MaxValueNode operator returns the maximum representable value for the given type."""

  def __init__(self=None, value_type=None):
    super().__init__()
    self.value_type = value_type