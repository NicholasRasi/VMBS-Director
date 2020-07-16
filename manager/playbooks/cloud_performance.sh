#!/bin/bash

# execute the benchmark
echo "Starting the benchmark..."
cd ~/cloud-benchmark/
source env/bin/activate
python main.py
deactivate

# execute the tools
echo "Starting the tools"
cd ~/cloud-benchmark-tools/
source env/bin/activate
python main.py --stop
deactivate