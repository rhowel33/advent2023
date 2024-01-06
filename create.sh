#!/bin/bash

for ((i=1; i<=25; i++))
do
    filename="Day${i}.py"
    touch "$filename"
    echo "#!/usr/bin/env python3" > "$filename"
    echo "" >> "$filename"
    echo "# Advent of Code 2023 Day ${i}" >> "$filename"
done
