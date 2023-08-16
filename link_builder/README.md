# LINK BUILDER

Easy to use, you just need to initialise a file, which contain the path, like this:
```
/g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1
/g/data/oi10/replicas/CMIP6/CMIP/BCC/BCC-ESM1/historical/r1i1p1f1
/g/data/oi10/replicas/CMIP6/CMIP/CCCma/CanESM5/historical/r1i1p1f1
```

Hint: one line for one path

and the script will automatically go through the path and build the symlink or generate a new netCDF file.

## How to run

```
python convert.py --init [path of your file] --output [path you want to store the new symlink or new file]
```