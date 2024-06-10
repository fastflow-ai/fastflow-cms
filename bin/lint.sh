#!/usr/bin/env bash

if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./fastflow_cms && toml-sort pyproject.toml --all --in-place
else
  ruff check . && black ./fastflow_cms --check && toml-sort pyproject.toml --all --in-place --check
fi
