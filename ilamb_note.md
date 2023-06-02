# ilamb-tutorial

SB> Check with Rhaegar and possibly add text here to say this tutorial is also useful for ILAMB and IOMB to start with.<SB
                                                                                                   
## 1) Background: International Land Model Benchmarking (ILAMB) and International Ocean Model Benchmarking (IOMB)

As earth system models (ESMs) become increasingly complex, there is a growing need for comprehensive and multi-faceted evaluation of model projections. The International Land Model Benchmarking (ILAMB) project is a model-data intercomparison and integration project designed to improve the performance of land models and, in parallel, improve the design of new measurement campaigns to reduce uncertainties associated with key land surface processes.

If you have used (and installed) `ilamb` on NCI and know the basic principle of `ilamb`, you can start from [Section 5) Guide for using ilamb on NCI](#5-guide-for-use-on-nci).

## 2) Installing `ilamb`

For NCI users, ACCESS-NRI is providing a `conda` environment called `ilamb_dev` through the `xp65` project, with ilamb installed. You can load and activate it via:

```
>>> module use /g/data/xp65/public/modules
>>> module load conda/ilamb_dev
>>> conda activate ilamb_dev
```

We will soon add `ilamb` also to the ACCESS-NRI MED `conda` environment, `access-med` under project`xp65`.

If you want to install `ilamb` yourself, please follow the official installation instructions at [https://www.ilamb.org/doc/install.html](https://www.ilamb.org/doc/install.html).

## 3) Configuring `ilamb`

Before you can run `ilamb`, you need to configure a few things:

3.1. [Organise the ILAMB_ROOT path](#31-organise-the-ilamb_root-path)  
3.2. [Set up a `config` file](#32-set-up-a-config-file)  
3.3. [Download a `shapefiles` files locally](#33-download-a-shapefiles-files-locally) (Optional online, necessary offline e.g. on NCI compute nodes)

### 3.1. Organise the ILAMB_ROOT path

`ilamb` demands files to be organised in a specific directory structure of `DATA` and `MODELS`.

If you do not have your own files yet, you can download and use [example files](https://www.ilamb.org/Downloads/minimal_ILAMB_data.tgz) provided as part of the  of `ilamb`'s [*First Steps* Tutorial](https://www.ilamb.org/doc/first_steps.html)

The following tree represents the organization of the contents of this extracted sample data (Note: We renamed the main directory name):
```
ILAMB_ROOT (renamed from "ILAMB_sample")
├── DATA
│   ├── albedo
│   │   └── CERES
│   │       └── albedo_0.5x0.5.nc
│   └── rsus
│       └── CERES
│           └── rsus_0.5x0.5.nc
└── MODELS
    └── CLM40cn
        ├── rsds
        │   └── rsds_Amon_CLM40cn_historical_r1i1p1_185001-201012.nc
        └── rsus
            └── rsus_Amon_CLM40cn_historical_r1i1p1_185001-201012.nc
```

There are two main branches in this directory. The first is the `DATA` directory–this is where we keep the observational datasets each in a subdirectory bearing the name of the variable. While not strictly necesary to follow this form, it is a convenient convention. The second branch is the `MODEL` directory in which we see a single model result from CLM.

#### 3.1.1. Add files to DATA

There is a lot of DATA available to add. Take a look at https://www.ilamb.org/ILAMB-Data/ and https://www.ilamb.org/IOMB-Data/ for extensive lists for ILAMB-Data (land modelling) and IOMB-Data (ocean modelling).

`ilamb` has a commandline prompt to add new DATA in a substructure. To fetch all available DATA from the website, you can simply go to your $ILAMB_ROOT and type
```
>>> ilamb-fetch
```

The command will compare the above website with your current DATA and make suggestions for downloads:
```
Comparing remote location:

      https://www.ilamb.org/ILAMB-Data/

To local location:

      ./

I found the following files which are missing, out of date, or corrupt:

      .//DATA/twsa/GRACE/twsa_0.5x0.5.nc
      .//DATA/rlus/CERES/rlus_0.5x0.5.nc
      ... (we have abbreviated the extensive list here)

Download replacements? [y/n]
```

You can use `ilamb-fetch -h` to see how you can adjust the remote and local locations. If you want to download IOMB-Data, you can for example use
```
ilamb-fetch --remote_root https://www.ilamb.org/IOMB-Data/
```


#### 3.1.2. Add files to MODEL
  
If you want to add your own `MODEL` to `ilamb`, you can do so by following [this description](https://www.ilamb.org/doc/add_model.html).
  
For `NCI` users, our `ilamb_dev` `conda` enrivonment already provides all observational datasets from the `ilamb` official web and the [ACCESS-ESM1_5](https://access-hive.org.au/configurations/access-esm/) model result for user at `ILAMB_ROOT`. Stay tune for more observational and model data or tell us which ones we should definitely add.

### 3.2. Set up a `config` file

Now that we have the data, we need to setup a `config` file which the `ilamb` package will use to initiate a benchmark study.  

`ilamb` provides default config files [here](https://github.com/rubisco-sfa/ILAMB/tree/master/src/ILAMB/data).

Below we explain both which variables you can define, but start by showing you the minimum setup from the [tutorial's](https://www.ilamb.org/doc/first_steps.html). `sample.cfg` [file](https://github.com/rubisco-sfa/ILAMB/blob/master/src/ILAMB/data/sample.cfg):

#### Minimum configure file with a direct and a derived variable

```
# This configure file specifies the variables

[h1: Radiation and Energy Cycle]

[h2: Surface Upward SW Radiation]
variable = "rsus"

[CERES]
source   = "DATA/rsus/CERES/rsus_0.5x0.5.nc"

[h2: Albedo]
variable = "albedo"
derived  = "rsus/rsds"

[CERES]
source   = "DATA/albedo/CERES/albedo_0.5x0.5.nc"
```

In brief: This file allows you to create different header descriptions of the experiments (`h1`: top level for grouping of variables, `h2`: sub-level for each variable), but most importantly the `variable`s that we will look into and their `source`. In the eaxmple, `rsus` (*Surface Upward Shortwave Radiation*) and `albedo` are the used variables. The latter is actually derived from two variables by dividing the *Surface Upward Shortwave Radiation* by the *Surface Downward Shortwave Radiation*, `derived = rsus/rsds`. Finally, sources are defined as `source` with a text-font header without `h1` or `h2`.

#### Changing configure file variables

This is the list of all the variables you can modify in config file:
```
source              = None
#Full path to the observational dataset

cmap                = "jet"
#The colormap to use in rendering plots (default is 'jet')

variable            = None
#Name of the variable to extract from the source dataset

alternate_vars      = None
#Other accepted variable names when extracting from models

derived             = None
#An algebraic expression which captures how the confrontation variable may be generated

land                = False
#Enable to force the masking of areas with no land (default is False)

bgcolor             = "#EDEDED"
#Background color

table_unit          = None
#The unit to use when displaying output in tables on the HTML page

plot_unit           = None
#The unit to use when displaying output on plots on the HTML page

space_mean          = True
#Disable to compute sums of the variable over space instead of mean values

relationships       = None
#A list of confrontations with whose data we use to study relationships, the syntax is "h2 tag/observational dataset". You will see the relationship part in the output if you specify some relationship.

ctype               = None
#Choose a specific Confrontion class. 

regions             = None
#Specify the regions of confrontation

skip_rmse           = False
#akip rmse in program

skip_iav            = True
#Ship iav in program

mass_weighting      = False
#if switch to true, using an average data in a period to normalize

weight              = 1    
# if a dataset has no weight specified, it is implicitly 1

```

### 3.3. Download a `shapefiles` files locally

You can download the `shapefiles` that are needed to run `ilamb` and `cartopy` offline here:

- For Land: https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/physical/ne_110m_land.zip
- For Ocean: https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/physical/ne_110m_ocean.zip

You can put them on whatever path you like, but we recommend to use the parent directory of $ILAMB_ROOT, that is
```
├── ILAMB_ROOT
├── shapefiles
│   ├── ne_110m_land.shp
│   └── ne_110m_ocean.shp
```

Finally, you need to define that path as `CARTOPY_DATA_DIR` via 
```
export CARTOPY_DATA_DIR=/path/where/you/downloaded/the/shapefiles/at
```

## 4. Run `ilamb`

#### ilamb-run
Now that we have the configuration file set up, you can run the study using the `ilamb-run` script. Executing the command:
```
ilamb-run --config sample.cfg --model_root $ILAMB_ROOT/MODELS/ --regions global
```
If you are on some institutional resource, you may need to launch the above command using a submission script, or request an interactive node. As the script runs, it will yield output which resembles the following:
```
Searching for model results in /Users/ncf/sandbox/ILAMB_sample/MODELS/

                                          CLM40cn

Parsing config file sample.cfg...

                   SurfaceUpwardSWRadiation/CERES Initialized
                                     Albedo/CERES Initialized

Running model-confrontation pairs...

                   SurfaceUpwardSWRadiation/CERES CLM40cn              Completed  37.3 s
                                     Albedo/CERES CLM40cn              Completed  44.7 s

Finishing post-processing which requires collectives...

                   SurfaceUpwardSWRadiation/CERES CLM40cn              Completed   3.3 s
                                     Albedo/CERES CLM40cn              Completed   3.3 s

Completed in  91.8 s
```
What happened here? First, the script looks for model results in the directory you specified in the `--model_root` option. It will treat each subdirectory of the specified directory as a separate model result. Here since we only have one such directory, `CLM40cn`, it found that and set it up as a model in the system. Next it parsed the configure file we examined earlier. We see that it found the CERES data source for both variables as we specified it. If the source data was not found or some other problem was encountered, the green `Initialized` will appear as red text which explains what the problem was (most likely `MisplacedData`). If you encounter this error, make sure that `ILAMB_ROOT` is set correctly and that the data really is in the paths you specified in the configure file.

Next we ran all model-confrontation pairs. In our parlance, a confrontation is a benchmark observational dataset and its accompanying analsys. We have two confrontations specified in our configure file and one model, so we have two entries here. If the analysis completed without error, you will see a green `Completed` text appear along with the runtime. Here we see that `albedo` took a few seconds longer than `rsus`, presumably because we had the additional burden of reading in two datasets and combining them.

The next stage is the post-processing. This is done as a separate loop to exploit some parallelism. All the work in a model-confrontation pair is purely local to the pair. Yet plotting results on the same scale implies that we know the maxmimum and minimum values from all models and thus requires the communcation of this information. Here, as we are plotting only over the globe and not extra regions, the plotting occurs quickly.

#### Viewing the Output

The whole process generates a directory of results which by default is called `_build`. To view the results locally on your computer, navigate into this directory and start a local `http` server:
```
python -m http.server
```
You should see a message similar to this:
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
Open this link in your browser and you will see a webpage with a summary table in the center. As we have so few variables and a single model at this point, the table will not be very helpful. As we add more variables and models, this summary table helps you understand relative differences in scores among models. For now, clicking on a row of the table will expand it to reveal the underlying datasets used. Clicking on CERES will take you to another page which presents detailed scores and plots.

#### ilamb_doctor
`ilamb_doctor ` is a script you can use to diagnosing some missing model values or what is incorrect or missing from a given analysis. It takes options similar to `ilamb-run` and is used in the following way:
```[ILAMB/test]$ ilamb-doctor --config test.cfg --model_root ${ILAMB_ROOT}/MODELS/CLM

Searching for model results in /Users/ncf/ILAMB//MODELS/CLM

                                   CLM40n16r228
                                   CLM45n16r228
                                   CLM50n18r229

We will now look in each model for the variables in the ILAMB
configure file you specified (test.cfg). The color green is used to reflect
which variables were found in the model. The color red is used to
reflect that a model is missing a required variable.

                           Biomass/GlobalCarbon CLM40n16r228 biomass or cVeg
               GrossPrimaryProductivity/Fluxnet CLM40n16r228 gpp
                  GrossPrimaryProductivity/GBAF CLM40n16r228 gpp
        GlobalNetEcosystemCarbonBalance/Hoffman CLM40n16r228 nbp
                      NetEcosystemExchange/GBAF CLM40n16r228 gpp, rh, and ra
           TerrestrialWaterStorageAnomaly/GRACE CLM40n16r228 tws
                                   Albedo/MODIS CLM40n16r228 rsus and rsds
                      SurfaceAirTemperature/CRU CLM40n16r228 tas
                            Precipitation/GPCP2 CLM40n16r228 pr
                           Biomass/GlobalCarbon CLM45n16r228 biomass or cVeg
               GrossPrimaryProductivity/Fluxnet CLM45n16r228 gpp
                  GrossPrimaryProductivity/GBAF CLM45n16r228 gpp
        GlobalNetEcosystemCarbonBalance/Hoffman CLM45n16r228 nbp
                      NetEcosystemExchange/GBAF CLM45n16r228 gpp, rh, and ra
           TerrestrialWaterStorageAnomaly/GRACE CLM45n16r228 tws
                                   Albedo/MODIS CLM45n16r228 rsus and rsds
                      SurfaceAirTemperature/CRU CLM45n16r228 tas
                            Precipitation/GPCP2 CLM45n16r228 pr
                           Biomass/GlobalCarbon CLM50n18r229 biomass or cVeg
               GrossPrimaryProductivity/Fluxnet CLM50n18r229 gpp
                  GrossPrimaryProductivity/GBAF CLM50n18r229 gpp
        GlobalNetEcosystemCarbonBalance/Hoffman CLM50n18r229 nbp
                      NetEcosystemExchange/GBAF CLM50n18r229 gpp, rh, and ra
           TerrestrialWaterStorageAnomaly/GRACE CLM50n18r229 tws
                                   Albedo/MODIS CLM50n18r229 rsus and rsds
                      SurfaceAirTemperature/CRU CLM50n18r229 tas
                            Precipitation/GPCP2 CLM50n18r229 pr
```
Here we have run the command on some inputs in our test directory. You will see a list of the confrontations we run and the variables which are required or their synonyms. What is missing in this tutorial is the text coloring which will indicate if a given model has the required variables.

We have finish the introduction of basic `ilamb` usage. We believe you have some understanding of `ilamb` and cont wait to use it. if you still have any question or you want some developer level support, you can find more detail in their [official tutorial](https://www.ilamb.org/doc/tutorial.html). Nest we will start to teach you how to use `ilamb` on NCI in a convenient way.  

## 5) Guide for using `ilamb` on NCI
For people who reach this part, you must have some basic understanding of ilamb and what to start your trip on NCI. so we make a quick guide for you.

### ILAMB_ROOT
for obervational data and model result of `ACCESS_ESM1-5`, we have prebuild it for people to use, the structure is showing below:
```
.
├── DATA -> /g/data/kj13/datasets/ilamb/DATA
└── MODELS
    ├── r10i1p1f1
    ├── r11i1p1f1
    ├── r12i1p1f1
    ├── r13i1p1f1
    ├── r14i1p1f1
    ├── r15i1p1f1
    ├── r16i1p1f1
    ├── r17i1p1f1
    ├── r18i1p1f1
    ├── r19i1p1f1
    ├── r1i1p1f1
    ├── r20i1p1f1
    ├── r21i1p1f1
    ├── r22i1p1f1
    ├── r23i1p1f1
    ├── r24i1p1f1
    ├── r25i1p1f1
    ├── r26i1p1f1
    ├── r27i1p1f1
    ├── r28i1p1f1
    ├── r29i1p1f1
    ├── r2i1p1f1
    ├── r30i1p1f1
    ├── r31i1p1f1
    ├── r32i1p1f1
    ├── r33i1p1f1
    ├── r34i1p1f1
    ├── r35i1p1f1
    ├── r36i1p1f1
    ├── r37i1p1f1
    ├── r38i1p1f1
    ├── r39i1p1f1
    ├── r3i1p1f1
    ├── r40i1p1f1
    ├── r4i1p1f1
    ├── r5i1p1f1
    ├── r6i1p1f1
    ├── r7i1p1f1
    ├── r8i1p1f1
    └── r9i1p1f1
```

`DATA` directory point to the observational dataset, and `MODELS` directory contains all the experiment in `ACCESS_ESM1-5` historical data. for each experiment directory, the structure is:
```
.
└── ACCESS-ESM1-5-R1
    ├── cSoil.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Emon/cSoil/gn/files/d20191115/cSoil_Emon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── cVeg.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/cVeg/gn/files/d20191115/cVeg_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── evspsbl.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/evspsbl/gn/files/d20191115/evspsbl_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── gpp.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/gpp/gn/files/d20191115/gpp_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── hfds.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Omon/hfds/gn/files/d20191115/hfds_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── hfls.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/hfls/gn/files/d20191115/hfls_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── hfss.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/hfss/gn/files/d20191115/hfss_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── hurs.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/hurs/gn/files/d20191115/hurs_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── lai.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/lai/gn/files/d20191115/lai_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── nbp.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/nbp/gn/files/d20191115/nbp_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── pr.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/pr/gn/files/d20191115/pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── ra.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/ra/gn/files/d20191115/ra_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── rh.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/rh/gn/files/d20191115/rh_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── rlds.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/rlds/gn/files/d20191115/rlds_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── rlus.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/rlus/gn/files/d20191115/rlus_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── rsds.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/rsds/gn/files/d20191115/rsds_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── rsus.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/rsus/gn/files/d20191115/rsus_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── tasmax.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/tasmax/gn/files/d20191115/tasmax_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── tasmin.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/tasmin/gn/files/d20191115/tasmin_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    ├── tas.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Amon/tas/gn/files/d20191115/tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
    └── tsl.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Lmon/tsl/gn/files/d20191115/tsl_Lmon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-194912.nc
```

You can see, the directory contains many kinds of different geoscience data which you can use in ilamb, each `.nc` file is a softlink to the data source.

### Shapfiles

it is some map data which `cartopy` used to display the output. Typically, when you run ilamb, it will automatically download this file through the process, But we predownload it to local so that the whole process will work locally without internet.

To use this folder, you can specific a environment variable named `CARTOPY_DATA_DIR` to the Absolute path to Shapfiles. for NCI user we will show how to define this in the `PBS.job` script

### Mdoelroute.txt

this is a convenient way for people to define modelresult dataset they need. a example is like:
```
bcc-csm1-1          , MODELS/CMIP5/bcc-csm1-1     , CMIP5
CanESM2             , MODELS/CMIP5/CanESM2        , CMIP5
CESM1-BGC           , MODELS/CMIP5/CESM1-BGC      , CMIP5
...
BCC-CSM2-MR         , MODELS/CMIP6/BCC-CSM2-MR    , CMIP6
CanESM5             , MODELS/CMIP6/CanESM5        , CMIP6
CESM2               , MODELS/CMIP6/CESM2          , CMIP6
```

where the first entry can be any name you like, the next is the path of the
top level model directory (path can be absolute or relative to ILAMB_ROOT),
and the last is a group identifier. For each model in this list, ILAMB will
walk through all netcdf files and directories under that path, following
symbolic links. It builds a small database (dictionary) of which files have
which variables. There is no special organization needed.

For more specific example, if you want to confront some different experiments of `ACCESS_ESM1-5`, you can organise your Modelroute.txt file like this:
```
ACCESS_ESM1-5-r1i1p1f1          , MODELS/r1i1p1f1/ACCESS_ESM1-5-R1     , CMIP6
ACCESS_ESM1-5-r2i1p1f1          , MODELS/r2i1p1f1/ACCESS_ESM1-5-R1     , CMIP6
ACCESS_ESM1-5-r3i1p1f1          , MODELS/r3i1p1f1/ACCESS_ESM1-5-R1     , CMIP6
...
```

### PBS jobs submit
If you not familiar with the PBS jobs on NCI, you could find the guide [here](https://opus.nci.org.au/display/Help/4.+PBS+Jobs)

We provide some example of PBS jobs script:
```
#!/bin/bash

#PBS -N test
#PBS -l wd
#PBS -P iq82
#PBS -q express
#PBS -l walltime=10:00:00  
#PBS -l ncpus=1
#PBS -l mem=32GB           
#PBS -l jobfs=10GB        
#PBS -l storage=gdata/kj13+gdata/fs38
#PBS -v MODULEPATH=$MODULEPATH:/g/data/kj13/environments
   
module load conda/ilamb_dev
export ILAMB_ROOT=$PWD/ILAMB_ROOT
export CARTOPY_DATA_DIR=$PWD

ilamb-run --config CMIP.cfg --model_setup $PWD/modelroute.txt --regions global
```
We will not explain all the PBS Directives here, just pick up something we think is necessary.

`#PBS -q express` for people who want to run the process in a queue which can connect to internet, you can change this into `#PBS -q copyq`. But we recommand you to run in a local env cause we have download everything you need in local.

`#PBS -l storage=gdata/kj13+gdata/fs38`
Because `ACCESS_ESM1-5` model result was store in group fs38 and all the `ilamb` data and file are store in group kj13. you may need the authority to access both of this two groups first.

`module load conda/ilamb_dev`
Load the conda env we build for ilamb.

`export ILAMB_ROOT=$PWD/ILAMB_ROOT`Define the env variable to `ILAMB_ROOT`.

`CARTOPY_DATA_DIR=$PWD`Define the env variable to `CARTOPY_DATA_DIR`
 
 `ilamb-run --config CMIP.cfg --model_setup $PWD/modelroute.txt --regions global`
 this is the main directive to run ilamb.`--config` to specify the config file you use.`model_setup`specify the path to modelroute.txt.`--region`define the region of this ilamb process,youhave some alternative choice [here](https://www.ilamb.org/doc/ilamb_run.html).
