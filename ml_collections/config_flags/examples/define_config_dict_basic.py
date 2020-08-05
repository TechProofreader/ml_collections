# Copyright 2020 The ML Collections Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python 3
r"""Example of basic DEFINE_flag_dict usage.

To run this example:
python define_config_dict_basic.py -- --my_config_dict.field1=8 \
  --my_config_dict.nested.field=2.1 --my_config_dict.tuple='(1, 2, (1, 2))'
"""

from absl import app
from absl import flags

import ml_collections
from ml_collections.config_flags import config_flags

config = ml_collections.ConfigDict()
config.field1 = 1
config.field2 = 'tom'
config.nested = ml_collections.ConfigDict()
config.nested.field = 2.23
config.tuple = (1, 2, 3)

FLAGS = flags.FLAGS
config_flags.DEFINE_config_dict('my_config_dict', config)


def main(_):
  print(FLAGS.my_config_dict)


if __name__ == '__main__':
  app.run(main)
