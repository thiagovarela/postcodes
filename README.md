# Postcodes

[![Build Status](https://travis-ci.org/thiagovarela/postcodes.svg?branch=master)](https://travis-ci.org/thiagovarela/postcodes)
[![Code Climate](https://codeclimate.com/github/thiagovarela/postcodes/badges/gpa.svg)](https://codeclimate.com/github/thiagovarela/postcodes)
[![Test Coverage](https://codeclimate.com/github/thiagovarela/postcodes/badges/coverage.svg)](https://codeclimate.com/github/thiagovarela/postcodes/coverage)

## Installation


```bash

pip install https://github.com/thiagovarela/postcodes

```

## UK

This library is intended to be an exercise on validating UK postcodes 
 
 
 
### Usage

```python

from postcodes import uk
 
if uk.validate('EC1A 1BB', raise_exception=False):
    print 'Valid'
else:
    print 'False'

```