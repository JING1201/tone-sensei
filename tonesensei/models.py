# Copyright 2015 Google Inc. All rights reserved.
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

from django.db import models
from django.urls import reverse


class Characters(models.Model):
    languageCharacter = models.CharField(max_length=45)
    answer = models.IntegerField()

    def __unicode__(self):
        return '/$s/' %self.languageCharacter

    def get_post_url(self):
        return reverse('char_edit', kwargs={'pk': self.pk})