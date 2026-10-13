# validfilepath

Path validators to be used with argparse.

## Usage
```python
import argparse
from validfilepath import valid_filepath_input, valid_filepath_output
ap = argparse.ArgumentParser()
ap.add_argument('--infile', type=valid_filepath_input)
ap.add_argument('--outfile', type=valid_filepath_output)
```
