This is a brief readme to explain how to use the script to build softlink:

1. First of all, this is only for data in ACCESS-ESM-1_5 history data.

2. Before you run this script, make sure you have the pass to GROUP fs38.

3. When you start to use it, there are three environment variables you need to define in pbs.job file:
```
  $MODULE_PATH=YOUR_MODULE_PATH
  $MODULE=YOUR_MODULE
  $LOCAL_PATH=YOUR_LOCAL_PATH
```

4. Once you get everything done, execute pbs.job and you will get every softlink to ACCESS-ESM-1_5 in your $LOCAL_PATH
