#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests for envinterface.py implemented by Mynti207 team

import pytest
from stupidlang.env_dictimpl import Env
import operator as op

__author__ = "Rahul Dave"
__copyright__ = "Rahul Dave"
__license__ = "mit"


def test_main():
    """
    use global_env function as basis for testing
    """

    # environment initialize
    test_env = Env.empty()
    assert isinstance(test_env, Env)
    assert isinstance(test_env.env, dict)
    assert test_env.env == dict()
    assert len(test_env.env) == 0
    assert test_env.outerenv is None

    # environment extend
    test_env.extend('+', op.add)
    test_compare = dict()
    test_compare['+'] = op.add
    assert test_env.env == test_compare
    assert test_env.env['+'] == test_compare['+']
    assert test_env.env['+'] == op.add
    assert len(test_env.env) == 1

    # environment extend many
    test_env.extend_many({
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        'abs': abs,
        'max': max,
        'min': min,
        'round': round,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '==': op.eq,
        'not': op.not_
    })
    assert len(test_env.env) == 14
    assert test_env.env['max'] == max

    # environment lookup
    assert test_env.lookup('+') == (op.add, test_env)
    with pytest.raises(NameError):
        test_env.lookup('not_there')
