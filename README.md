# Truly Random Dice-Thrower for Table-Top RolePlaying Games (TRDTTTRPG)
[![PyPI](https://img.shields.io/pypi/pyversions/truerandomdice.svg)]()
[![PyPI version](https://badge.fury.io/py/truerandomdice.svg)](https://badge.fury.io/py/truerandomdice)
[![Build Status](https://travis-ci.org/EarthModule/TrulyRandomDiceThrower.svg?branch=master)](https://travis-ci.org/EarthModule/TrulyRandomDiceThrower)
[![Coverage Status](https://coveralls.io/repos/github/EarthModule/TrulyRandomDiceThrower/badge.svg?branch=master)](https://coveralls.io/github/EarthModule/TrulyRandomDiceThrower?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/adfaa244b06842d7868b3fe58213c7f7)](https://www.codacy.com/app/EarthModule/TrulyRandomDiceThrower?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=EarthModule/TrulyRandomDiceThrower&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/EarthModule/TrulyRandomDiceThrower/master/landscape.svg?style=flat)](https://landscape.io/github/EarthModule/TrulyRandomDiceThrower/master)

## Overview
Are you tired of that one dice as a player or GM that always seems to give you bad luck?
Do you always use that one "lucky" dice just in case?
Then this Python library is just for you! It takes its randomness from the "atmospheric noise", courtesy of random.org

## Installation
You need api-key from random.org for this library to work.
You can get yours from here: https://api.random.org/api-keys/beta

### Dependencies from other python-packages
peewee,
requests,
rdoclient

### Using Pip

`pip install truerandomdice`

When you download the project for the first time, run set_api_key.py from "truerandomdice" folder.
After it you can test the application by running diceroller.py from the same folder.