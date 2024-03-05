# Copyright (c) 2014 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""FAFT configuration overrides for Quawks."""

from autotest_lib.server.cros.faft.config import rambi


class Values(rambi.Values):
    """Inherit overrides from rambi."""
    """Configure servo-controlled WP pin as open drain"""
    wp_voltage = 'off'