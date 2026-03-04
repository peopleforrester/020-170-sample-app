# PR Testing Sample App

Python calculator application for Demo 020-170 (PR Testing with Coverage Reports).

## Structure

```
src/
  calculator.py  - Basic math operations (add, subtract, multiply, divide)
  utils.py       - Formatting and validation utilities
tests/
  test_calculator.py - Tests for calculator module
  test_utils.py      - Tests for utils module
```

## Coverage Demo

With all tests present, coverage is ~100%. Deleting `tests/test_utils.py` drops
coverage to ~53% (only calculator.py is covered), well below the 80% threshold.

## Local Testing

```bash
pip install -r requirements.txt
pytest tests/ --cov=src --cov-report=term --cov-fail-under=80
```

## Build Badge

![Build Status](BADGE_URL_PLACEHOLDER)
# test change
