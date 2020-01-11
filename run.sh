#!/usr/bin/env bash
#chmod +x run.sh && ./run.sh

# Process Data
python3 nfl_fantasy.py

# Push to repository
git add .
git commit -s -m "nfl fantasy stats"
git push
echo "I am done processing data. Bye!"