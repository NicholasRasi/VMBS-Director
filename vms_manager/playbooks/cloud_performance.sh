#!/bin/bash

# execute the benchmark
cd ~/cloud-benchmark/
source env/bin/activate
python main.py
deactivate

# execute the tools
cd ~/cloud-benchmark-tools/
source env/bin/activate
python main.py --stop
deactivate