#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import time, datetime, timedelta

def time_until_end_of_day(dt=None):
    """
    Get timedelta until end of day on the datetime passed, or current time.
    """
    if dt is None:
        dt = datetime.now()
    tomorrow = dt + timedelta(days=1)
    return datetime.combine(tomorrow, time.min) - dt + timedelta(seconds=.01)
    