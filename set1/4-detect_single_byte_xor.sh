#!/bin/bash

while IFS= read -r line; do
  python 3-single_byte_xor.py "$line"
done < $1
