# Getting started with ILAMB at NCI

As earth system models (ESMs) become increasingly complex, there is a growing need for comprehensive and multi-faceted evaluation of model projections. The International Land Model Benchmarking (ILAMB) project is a model-data intercomparison and integration project designed to improve the performance of land models and, in parallel, improve the design of new measurement campaigns to reduce uncertainties associated with key land surface processes.

This document explains how to run the [International Land Model Benchmarking (ILAMB)](https://www.ilamb.org) and International Ocean Model Benchmarking (IOMB) model evaluation tools on NCI infrastracture.

The documentation provided here is designed to supplement, rather than replace, the official [ILAMB documentation](https://www.ilamb.org/doc/). This documentation is tailored to using the tool within the NCI infrastructure. We encourage users to read the ILAMB documentation and to
try on the [ILAMB Tutorial](https://www.ilamb.org/doc/tutorial.html).

ILAMB development is primarily performed by the [RUBISCO](https://www.bgc-feedbacks.org/) Science Focus Area and supported by the [RGMA](https://climatemodeling.science.energy.gov/program-area/regional-global-model-analysis) Activity of the [EESSD](https://science.osti.gov/ber/Research/eessd) division of the [BER](https://science.osti.gov/ber) program in the United States Department of Energy's Office of Science.

### How to cite ILAMB?

*Collier, N., Hoffman, F. M., Lawrence, D. M., Keppel-Aleks, G., Koven, C. D., Riley, W. J., et al. (2018). The International Land Model Benchmarking (ILAMB) system: Design, theory, and implementation. Journal of Advances in Modeling Earth Systems, 10, 2731–2754. https://doi.org/10.1029/2018MS001354*

### ILAMB CMIP confrontations maintained by ACCESS-NRI


While the datasets and software found on this site can be used to confront models, we also maintain a collection of results for the community use. Below is a short description of each along with a preview and links to the full results page.


[Land Comparison of CMIP5 and CMIP6 Models](http://130.56.247.78/build_oi10_2/index.html)
We examine the performance of historical simulations from a selection of coupled Earth system models with a contribution in the CMIP5 and CMIP6 eras.
![](./image/ilamb_cmip5v6.png)

[Land Comparison of CMIP6 Models](http://130.56.247.78/build_al33/index.html)
This land-focused study includes coupled model results for the historical experiment from the CMIP6 era. We also use this as a testing ground to include new datasets and additional models. If you have a suggestion of a reference dataset or would like to request we include a model, please raise an issue.
![](./image/ilamb_cmip6.png)

[Land Comparison of Offline CMIP6 Models](http://130.56.247.78/build_rr3/index.html)
We examine performance differences among a selection of land models (CLM, ISBA-CTRIP, and JSBACH) run using different forcings (GSWP3, CRUJRA, and Princeton).
![](./image/ilamb_landhist.png)

[Ocean Comparison of CMIP5 and CMIP6 Models](http://130.56.247.78/build_iomb/index.html)
While the focus of ILAMB has been on land, we also have used the software to compare ocean model output which we refer to as International Ocean Model Benchmarking (IOMB). This study is analagous to the land comparison of CMIP5 and CMIP6 era models over the historical period.
![](./image/iomb_cmip5v6.png)


## Observations and Model outputs available at NCI.

We currently only support CF-compliant observational datasets and their confrontation with CMORised model outputs.

The [ILAMB-DATA](https://github.com/rubisco-sfa/ILAMB-Data) collection aggregates data from various sources and formats in a CF-compliant, netCDF4 files which can be used for model benchmarking via ILAMB. The collection has been replicated in the [ACCESS-NRI Replicated Datasets for Climate Model Evaluation
](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f7199_2480_5432_9703) and is maintained by the ACCESS-NRI Model Evaluation and Diagnostics team. Please contact the [ACCESS-NRI team](https://www.access-nri.org.au/model-evaluation-and-diagnostics-med-team/) if you requires help with datasets. The [ILAMB-DATA](https://github.com/rubisco-sfa/ILAMB-Data) is an Open Source project which welcomes contributions from the community.

![](./image/access-nri_dataNCI.png)


You can [request access to the ACCESS-NRI collection](https://my.nci.org.au/mancini/project/ct11/join).

Depending on their needs, users may require access to a range of NCI data collections and projects.
Here we list the NCI collections required to run the CMIP confrontations examples available with ILAMB (see [here](https://github.com/rubisco-sfa/ILAMB/tree/master/src/ILAMB/data)):


| Project Name   | Project Code  | DOI  |
| :-:            | :-:           |:-:   |
|   Earth System Grid Federation (ESGF) Australian CMIP6-era Datasets | fs38 [join](https://my.nci.org.au/mancini/project/fs38/join) |   [10.25914/5e6acd0492b39](https://dx.doi.org/10.25914/5e6acd0492b39)   |
|  Earth System Grid Federation (ESGF) Replicated CMIP6-era Datasets  | oi10 [join](https://my.nci.org.au/mancini/project/oi10/join) |   [10.25914/Q1CT-RM13](https://dx.doi.org/10.25914/Q1CT-RM13)   |
|   CSIRO-Mk3-6-0 model output prepared for CMIP5  | rr3 [join](https://my.nci.org.au/mancini/project/rr3/join) |   N/A |
|    Earth System Grid Federation (ESGF) Replicated CMIP5-era Datasets  | al33 [join](https://my.nci.org.au/mancini/project/al33/join) |   [10.25914/5b98b0f5ef29d](https://dx.doi.org/10.25914/5b98b0f5ef29d)|

Projects for data analysis (choose one):

| Project Name   | Project Code  |
| :-:            | :-:           |
| ACCESS MED Analysis Environments | xp65 [join](https://my.nci.org.au/mancini/project/xp65/join) |
| CLEX Analysis Environments | h55 [join](https://my.nci.org.au/mancini/project/hh5/join) |

## ILAMB on NCI-Gadi

For NCI users, ACCESS-NRI is providing a conda environment with the latest version of ILAMB through project `xp65`. It is also provided through the CLEX analysis environment project `hh5`.

To load the module via project `xp65`, you need to prompt:
```
>>> module use /g/data/xp65/public/modules
>>> module load conda/access-med
```
For `hh5`, you need to use:
```
>>> module use /g/data/hh5/public/modules
>>> module load conda/analysis3
```

To run `ilamb`, you need to execute the command `ilamb-run` with a number of arguments/files:
```py
ilamb-run --config config.cfg --model_setup model_setup.txt --regions global
```

- `config.cfg` defines which observables and observational datasets will be compared
- `model_setup.txt` defines the paths of the models that will be compared

Below we explain how to setup the necessary directory structures and the example files mentioned above. For detailed information on the arguments of `ilamb-run`, please consult the official <a href="https://www.ilamb.org/doc/ilamb_run.html" target="_blank">ILAMB documentation</a>.

## ILAMB directory structure

### ILAMB_ROOT

ILAMB requires files to be organised in a specific directory structure of `DATA` and `MODELS`.
The root of this directory structure is the `ILAMB_ROOT` path (you should export it as `$ILAMB_ROOT`):

```
export ILAMB_ROOT=PATH/OF/ILAMB_ROOT/DIRECTORY
```
  
The following tree represents a typical ILAMB_ROOT setup for CMIP comparison on NCI/Gadi:

```
$ILAMB_ROOT/
|-- DATA -> /g/data/ct11/access-nri/replicas/ILAMB
`-- MODELS
    |-- ACCESS-ESM1-5
    |   `-- historical
    |       `-- r1i1p1f1
    |           |-- cSoil.nc -> /g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r1i1p1f1/Emon/cSoil/gn/latest/cSoil_Emon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_185001-201412.nc
```

There are two main branches in this directory:

1. the `DATA` directory: this is where we keep the observational datasets each in a subdirectory bearing the name of the variable. This directory can be setup as a symlink to the [ACCESS-NRI Replicated Datasets for Climate Model Evaluation
](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f7199_2480_5432_9703).

2. the `MODEL` directory: this directory can be populated with symbolic links to the model outputs.

To facilitate the setup of an ILAMB-ROOT tree. ACCESS-NRI provides a tool to automatically generate the required folder structure.
The `ilamb-tree-generator` is available in the `access-med` environment of the `xp65` project.

The tool will automatically create the folder structure above. Models output can be added by listing them in a yaml file as follow:

```yaml
datasets:
  - {mip: CMIP, institute: CSIRO, dataset: ACCESS-ESM1-5, project: CMIP6, exp: historical, ensemble: r1i1p1f1}
  - {mip: CMIP,institute: BCC, dataset: BCC-ESM1, project: CMIP6, exp: historical, ensemble: r1i1p1f1}
  - {mip: CMIP,institute: CCCma, dataset: CanESM5, project: CMIP6, exp: historical, ensemble: r1i1p1f1}
  - {mip: LUMIP,institute: CSIRO, dataset: ACCESS-ESM1-5, project: CMIP6, exp: hist-noLu, ensemble: r1i1p1f1}
```

The tool can then be run from the command line:

```bash
ilamb-tree-generator --datasets models.yml --ilamb_root $ILAMB_ROOT
```

Note that in order to access these models on Gadi, you will need to join the NCI projects that are associated with the models originally paths and you will need to add these projects to the storage access keywords for [computing jobs](#submitting-a-pbs-job) lateron.

### ILAMB configuration file: `config.cfg`

Now that we have the data, we need to setup a configure file which the ILAMB package will use to initiate a benchmark study. With this file, you configure comparison sections and define which variables from which dataset will be compared. You can find more information on adjusting this file on the official <a href="https://www.ilamb.org/doc/first_steps.html#configure-files" target="_blank">ILAMB documentation</a>.

An example configure file for ILAMB on <i>Gadi</i> could be called `config.cfg` and look like this for comparing your models with two variables of the radiation and energy cycle as measured by <a href="https://ceres.larc.nasa.gov" target="_blank">Clouds and the Earth’s Radiant Energy System (CERES) project</a>:
```
# This configure file specifies comparison sections, variables and observational data for running ILAMB on Gadi.

# See https://www.ilamb.org/doc/first_steps.html#configure-files for the ILAMB Tutorial that addesses Configure Files

# Structure:
# [h1:] Sections
# [h2:] Variables
# [...] Observational Datasets and their paths

############################################################################

[h1: Radiation and Energy Cycle]

[h2: Surface Upward SW Radiation]
variable = "rsus"

[CERES]
source   = "DATA/rsus/CERESed4.1/rsus.nc"

[h2: Albedo]
variable = "albedo"
derived  = "rsus/rsds"

[CERES]
source   = "DATA/albedo/CERESed4.1/albedo.nc"
```

### ILAMB model selection: `model_setup.txt`

In the `model_setup.txt`, you can select all the model output that you want to compare.

Remember that ILAMB is expecting the model output and its variables to be saved in a specific format. See the above [ILAMB_ROOT/MODELS](#ilamb_rootmodels) description on how to find and create the correct links.

Assuming you want to compare the three models that we used in [ILAMB_ROOT/MODELS](#ilamb_rootmodels) (ACCESS-ESM1.5, BCC-ESM1, and CanESM5), you would need to create a `model_setup.txt` file wehere you define both the model labels and their paths:

```
# Model Name (used as label), ABSOLUTE/PATH/TO/MODELS or relative to $ILAMB_ROOT/ , Optional comments
ACCESS_ESM1-5_r1i1p1f1      , MODELS/ACCESS-ESM1-5/historical/r1i1p1f1              , CMIP6
BCC-ESM1_r1i1p1f1           , MODELS/BCC-ESM1/historical/r1i1p1f1                   , CMIP6
CanESM5_r1i1p1f1            , MODELS/CanESM5/historical/r1i1p1f1                    , CMIP6
```

## Run ILAMB

Now that we have the configuration file set up, you can run the study using the `ilamb-run` script via the aforementioned
```
ilamb-run --config config.cfg --model_setup model_setup.txt --regions global
```

Because of the computational costs, you need to run ILAMB through a Portable Batch System (PBS) job on Gadi.

### Submitting a PBS job

The following default PBS file, let's call it `ilamb_test.job`, can help you to setup your own, while making sure to use the correct project (#PBS -P) to charge your computing cost to:

```
#!/bin/bash

#PBS -N ilamb_test
#PBS -l wd
#PBS -P your_compute_project_here
#PBS -q normalbw
#PBS -l walltime=0:20:00  
#PBS -l ncpus=14
#PBS -l mem=63GB           
#PBS -l jobfs=10GB        
#PBS -l storage=gdata/ct11+gdata/hh5+gdata/xp65+gdata/fs38+gdata/oi10

# ILAMB is provided through projects xp65 and hh5. We will use the latter here
#module use /g/data/xp65/public/modules
#module load conda/access-med
module use /g/data/hh5/public/modules
module load conda/analysis3

# Define the ILAMB Path, expecting it to be where you start this job from
export ILAMB_ROOT=./
export CARTOPY_DATA_DIR=/g/data/xp65/public/apps/cartopy-data

# Run ILAMB in parallel with the config.cfg configure file for the models defined in model_setup.txt
mpiexec -n 10 ilamb-run --config config.cfg --model_setup model_setup.txt --regions global
```

You should adjust this file to your own specifications (including the storage access to your models). Save the file in the `$ILAMB_ROOT` and submit its job to the queue from there via 
```
qsub ilamb_test.job
```

Running this job will create a `_build` directory with the comparison results within `$ILAMB_ROOT`. You can adjust the place of this directory via a agrument `--build_dir` argument for `ilamb-run`.

## Visualisation of ILAMB outputs

Result visualisation is an important part of ilamb, it provide a lot of visualized graphs to allow users to evaluate the performance of each models for various aspects. The result is shown in an `html` page.

NCI provides a web-based graphical interface of the Australian Research Environment (ARE) for such purposes.

### Australian Research Environment (ARE)

ARE is a web-based graphical interface for performing your computational research. It combines the familiarity of your regular desktop/laptop with the power of NCI's world-class research HPC capabilities. ARE gives you access to NCI's Gadi supercomputer and data collections, all from a simple, graphical interface. ARE consists of a number of applications that support your research such as Virtual Desktop, JupyterLab, Terminal, etc.

In this tutorial, we mainly provide guidance for use ARE for ilamb result. For user who want more imformation about ARE, you can find it [here](https://opus.nci.org.au/display/Help/ARE+User+Guide). 

#### Access to ARE

ARE can be accessed at [are.nci.org.au](https://are.nci.org.au/). NCI users can use NCI username and password to login. If you are a new user of NCI, please apply an account at [here](https://my.nci.org.au/mancini/signup/0).


#### Virtual Desktop

When you log into ARE, click Virsual Desktop Instance(VDI), and you will see the setup page, it will setup the VDI just like you setup your PBS job on NCI CLI, so just follow the instruction on the page. Make sure that the project on which your `ilamb` data is stored is added to the 'Storage' field. Otherwise you cannot access the directory in your VDI. NCI provides more both user guides for [VDI](https://opus.nci.org.au/display/Help/2.1.+Connecting+to+the+VDI) and [PBS directives](https://opus.nci.org.au/display/Help/PBS+Directives+Explained).


![](./image/storage.png)

**Launch VDI**
 When you get everything setup and click Launch button you'll be redirected to this page:

 ![](./image/running.png)

Maybe you will be in queue for a while, it depends on what kind of queue and how much source you apply, when the status at the top right turn to running, you can click `Launch VDI Desktop` to access your VDI.

**Host ilamb result**

This is the Desktop of your VDI:
![](./image/vdi.png)

Then open a terminal (top left of the VDI screen) and navigate to the ilamb result directory (default is `_build` directory), and use commmand below to host a localserver.
```
python3 -m http.server
```

You can then start Firefox in the VDI screen and access the following address:
localhost address:
```
http://0.0.0.0:8000/
```

For our `config.cfg` example we expect to see the following website (which shows the available observational data in blue after clicking on <i>Albedo</i> and <i>Surface Upward SW Radiation</i>):

![](./image/vdi_window1.png)

Clicking on `CERESed4.1` under the `Albedo` measurements then opens a new tab which allows you to browse through more extended and quantitative comparisons of your selected Models when confronted with measurements from the <a href="https://ceres.larc.nasa.gov" target="_blank">Clouds and the Earth’s Radiant Energy System (CERES) project</a>:

![](./image/ilamb_loop.gif)

#### Jupyter-hub interface

The Jupyter interface available via ARE can also be used to visualise the outputs of ILAMB.

## ILAMB-DATA list

<table>
  <tbody><tr>
    <td>Albedo</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/albedo/CERESed4.1/albedo.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/albedo/GEWEX.SRB/albedo_0.5x0.5.nc">GEWEX.SRB</a></td>
  </tr>
  <tr>
    <td>Biomass</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/ESACCI/biomass.nc">ESACCI</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/GEOCARBON/biomass.nc">GEOCARBON</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/NBCD2000/biomass_0.5x0.5.nc">NBCD2000</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/Saatchi2011/biomass_0.5x0.5.nc">Saatchi2011</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/Thurner/biomass_0.5x0.5.nc">Thurner</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/USForest/biomass_0.5x0.5.nc">USForest</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/biomass/XuSaatchi2021/XuSaatchi.nc">XuSaatchi2021</a></td>
  </tr>
  <tr>
    <td>Burned Area</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/burntArea/GFED4.1S/burntArea.nc">GFED4.1S</a></td>
  </tr>
  <tr>
    <td>Carbon Dioxide</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/co2/NOAA.GMD/co2.nc">NOAA.Emulated</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/co2/HIPPO_AToM/HIPPO_AToM.nc">HIPPOAToM</a></td>
  </tr>
  <tr>
    <td>Diurnal Max Temperature</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/tasmax/CRU4.02/tasmax.nc">CRU4.02</a></td>
  </tr>
  <tr>
    <td>Diurnal Min Temperature</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/tasmin/CRU4.02/tasmin.nc">CRU4.02</a></td>
  </tr>
  <tr>
    <td>Diurnal Temperature Range</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/dtr/CRU4.02/dtr.nc">CRU4.02</a></td>
  </tr>
  <tr>
    <td>Ecosystem Respiration</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/reco/FLUXNET2015/reco.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/reco/FLUXCOM/reco.nc">FLUXCOM</a></td>
  </tr>
  <tr>
    <td>Evapotranspiration</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/evspsbl/GLEAMv3.3a/et.nc">GLEAMv3.3a</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/evspsbl/MODIS/et_0.5x0.5.nc">MODIS</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/evspsbl/MOD16A2/et.nc">MOD16A2</a></td>
  </tr>
  <tr>
    <td>Global Net Ecosystem Carbon Balance</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/nbp/GCP/nbp_1959-2016.nc">GCP</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/nbp/HOFFMAN/nbp_1850-2010.nc">Hoffman</a></td>
  </tr>
  <tr>
    <td>Gross Primary Productivity</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/gpp/FLUXNET2015/gpp.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/gpp/FLUXCOM/gpp.nc">FLUXCOM</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/gpp/WECANN/gpp.nc">WECANN</a></td>
  </tr>
  <tr>
    <td>Ground Heat Flux</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/hfdsl/CLASS/hfdsl.nc">CLASS</a></td>
  </tr>
  <tr>
    <td>Latent Heat</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/hfls/FLUXNET2015/hfls.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfls/FLUXCOM/le.nc">FLUXCOM</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/evspsbl/DOLCE/DOLCE.nc">DOLCE</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfls/CLASS/hfls.nc">CLASS</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfls/WECANN/hfls.nc">WECANN</a></td>
  </tr>
  <tr>
    <td>Leaf Area Index</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/lai/AVHRR/lai_0.5x0.5.nc">AVHRR</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/lai/AVH15C1/lai.nc">AVH15C1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/lai/MODIS/lai_0.5x0.5.nc">MODIS</a></td>
  </tr>
  <tr>
    <td>Methane</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/ch4/FluxnetANN/FCH4_F_ANN_monthly_wetland_tier1.nc">FluxnetANN</a>
    </td>
  </tr>
  <tr>
    <td>Net Ecosystem Exchange</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/nee/FLUXNET2015/nee.nc">FLUXNET2015</a></td>
  </tr>
  <tr>
    <td>Nitrogen Fixation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/fBNF/DaviesBarnard/fBNF_0.5x0.5.nc">Davies-Barnard</a></td>
  </tr>
  <tr>
    <td>Permafrost</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/permafrost/Brown2002/Brown2002.nc">Brown2002</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/permafrost/Obu2018/Obu2018.nc">Obu2018</a></td>
  </tr>
  <tr>
    <td>Precipitation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/pr/CMAPv1904/pr.nc">CMAPv1904</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/pr/FLUXNET2015/pr.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/pr/GPCCv2018/pr.nc">GPCCv2018</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/pr/GPCPv2.3/pr.nc">GPCPv2.3</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/pr/CLASS/pr.nc">CLASS</a></td>
  </tr>
  <tr>
    <td>Runoff</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/mrro/Dai/runoff.nc">Dai</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/mrro/LORA/LORA.nc">LORA</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/mrro/CLASS/mrro.nc">CLASS</a></td>
  </tr>
  <tr>
    <td>Sensible Heat</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/hfss/FLUXNET2015/hfss.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfss/FLUXCOM/sh.nc">FLUXCOM</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfss/CLASS/hfss.nc">CLASS</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/hfss/WECANN/hfss.nc">WECANN</a></td>
  </tr>
  <tr>
    <td>Snow Water Equivalent</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/swe/CanSISE/swe.nc">CanSISE</a></td>
  </tr>
  <tr>
    <td>Soil Carbon</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/cSoil/HWSD/soilc_0.5x0.5.nc">HWSD</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/cSoil/NCSCDV22/soilc_0.5x0.5.nc">NCSCDV22</a></td>
  </tr>
  <tr>
    <td>Surface Air Temperature</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/tas/CRU4.02/tas.nc">CRU4.02</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/tas/FLUXNET2015/tas.nc">FLUXNET2015</a></td>
  </tr>
  <tr>
    <td>Surface Downward LW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rlds/CERESed4.1/rlds.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlds/FLUXNET2015/rlds.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlds/GEWEX.SRB/rlds_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlds/WRMC.BSRN/rlds.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Surface Downward SW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rsds/CERESed4.1/rsds.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsds/FLUXNET2015/rsds.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsds/GEWEX.SRB/rsds_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsds/WRMC.BSRN/rsds.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Surface Net LW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rlns/CERESed4.1/rlns.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlns/FLUXNET2015/rlns.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlns/GEWEX.SRB/rlns_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlns/WRMC.BSRN/rlns.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Surface Net Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rns/CERESed4.1/rns.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rns/FLUXNET2015/rns.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rns/GEWEX.SRB/rns_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rns/WRMC.BSRN/rns.nc">WRMC.BSRN</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rns/CLASS/rns.nc">CLASS</a></td>
  </tr>
  <tr>
    <td>Surface Net SW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rsns/CERESed4.1/rsns.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsns/FLUXNET2015/rsns.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsns/GEWEX.SRB/rsns_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsns/WRMC.BSRN/rsns.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Surface Relative Humidity</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rhums/ERA5/rhums.nc">ERA5</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rhums/CRU4.02/rhums.nc">CRU4.02</a></td>
  </tr>
  <tr>
    <td>Surface Soil Moisture</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/mrsos/WangMao/mrsos_olc.nc">WangMao</a></td>
  </tr>
  <tr>
    <td>Surface Upward LW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rlus/CERESed4.1/rlus.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlus/FLUXNET2015/rlus.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlus/GEWEX.SRB/rlus_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rlus/WRMC.BSRN/rlus.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Surface Upward SW Radiation</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/rsus/CERESed4.1/rsus.nc">CERESed4.1</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsus/FLUXNET2015/rsus.nc">FLUXNET2015</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsus/GEWEX.SRB/rsus_0.5x0.5.nc">GEWEX.SRB</a>, <a href="https://www.ilamb.org/ILAMB-Data/DATA/rsus/WRMC.BSRN/rsus.nc">WRMC.BSRN</a></td>
  </tr>
  <tr>
    <td>Terrestrial Water Storage Anomaly</td>
    <td><a href="https://www.ilamb.org/ILAMB-Data/DATA/twsa/GRACE/twsa_0.5x0.5.nc">GRACE</a></td>
  </tr>
</tbody></table>

## IOMB-DATA list

<table>
  <tbody><tr>
    <td>Alkalinity</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/talk.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Anthropogenic DIC 1994-2007</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/Gruber/Gruber.nc">Gruber</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/OCIM/OCIM.nc">OCIM</a></td>
  </tr>
  <tr>
    <td>Chlorophyll</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/chla.nc">GLODAP2.2022</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/SeaWIFS/SeaWIFS.nc">SeaWIFS</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/MODISAqua/MODISAqua.nc">MODISAqua</a></td>
  </tr>
  <tr>
    <td>Dissolved Inorganic Carbon</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/dissic.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Nitrate</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/no3.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/no3.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Oxygen</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/o2.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/o2.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Phosphate</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/po4.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/po4.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Salinity</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/so.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/so.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Silicate</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/sio3.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/sio3.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Temperature</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/thetao.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/thetao.nc">GLODAP2.2022</a></td>
  </tr>
  <tr>
    <td>Vertical Temperature Gradient</td>
    <td><a href="https://www.ilamb.org/IOMB-Data/DATA/WOA2018/thetao.nc">WOA2018</a>, <a href="https://www.ilamb.org/IOMB-Data/DATA/GLODAP2.2022/thetao.nc">GLODAP2.2022</a></td>
  </tr>
</tbody></table>

## Advanced usages

The analysis with ILAMB can be adjusted in many ways. We suggest to read the ILAMB documentation and <a href="https://www.ilamb.org/doc/ilamb_run.html" target="_blank">tutorials</a> for a complete overview, as we only showcase a few examples below. 

### Changing configure file definitions

You can find more information on adjusting this file on the official <a href="https://www.ilamb.org/doc/first_steps.html#configure-files" target="_blank">ILAMB documentation</a>.

Below we provide a list of definitions you can modify in config file:
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
Above are the general attributes you can use in config file. However, `ILAMB` has develop many sub-classes of Confrontation for some specific case, there are some specific attribute in those sub-classes:
```
--ConfCO2:

emulated_flux       = nbp    
# prety much the same as 'derived', default is nbp in this case

sites               = None
# in this confrontation, it will use site data instead of space data, this attribute is to specify which sites will be used.

force_emulation     = False
# if switch to true, using emulated_flux variable even you have co2 in model-result.

never_emulation     = False
# is switch to true, only use co2 in confront even if you specify emulated_flux and dont have co2 in model_result

lat_bands           = "-90,-60,-23,0,+23,+60,+90"
# it will give a latitude boundary for sites to separate those sites into interval.

--ConfGSNF:

model_flux          = "nee"
# use one variable or derive of some variables to replace the target variable in model_result. It's quite useful if you don't have the variable required by this confrontation in your model_result.

--ConfNBP:

skip_taylor         = "False"
# skip Temporal distribution in program

--ConfSoilCarbon:

soilc_source        = None
# path to observational dataset of 'solic'.

npp_source          = None
# path to observational dataset of 'npp'.

tas_source          = None
# path to observational dataset of 'tas'.

pr_source           = None
# path to observational dataset of 'pr'.

pet_source          = None
# path to observational dataset of 'pet'

fracpeat_source     = None
# path to observational dataset of 'fracpeat'

y0                  = 1980.0
# start year

yf                  = 2006.0
# end year

--ConfEvapFraction:

hfss_source         = None (*)
# path to observational dataset of 'hfss'

hfls_source         = None (*)
# path to observational dataset of 'hlss'

#caution: those two variable is conpulsory if you specify ctype = 'ConfEvapFraction'

--ConfTWSA:

nbasins             = 30
# Adding a member variable called basins, add them as regions

--ConfPermafrost

y0                  = 1985.0
# start year

yf                  = 2005.0
# end year

dmax                = 3.5
# The maximum depth to consider in [m]

Teps                = 273.15
# The temperature threshold to use to indicate permafrost [K]

--ConfAlbedo:

energy_threshold    = 10
# engery threshold to build a mask

skip_weighting      = False
# options while run the mean state analysis

skip_cycle          = False
# options while run the mean state analysis
```
### Model selection via `--model_setup` or `--model_root`

In the above examples, we already showed you how select only a few examples of the available models, which are selected with a file (e.g. `model_setup.txt`) that is used via the `--model_setup` argument.

You can, however, also select all models, by simply using the keyword `--model_root $ILAMB_ROOT/MODELS/`.

### Run specific regions via the `--regions` argument

In the above examples, we have always chosen to perform comparisons on a `global` level.

You can, however, also choose other predefined regions like `aust` (for Australia) based on the <a href="http://www.globalfiredata.org" target="_blank">Global Fire Emissions Database</a> or define your own regions. To run ILAMB for several regions, use the `--regions` option and include the region labels delimited by spaces, e.g. `--regions global aust`

To use your own region, you need to create a new file, for example `regions.txt` with latidude and longitude limits for your regions and use it with the argument `--regions regions.txt`. This could be advisable if you want to include Tasmania (latitudes down to -43.75 degrees) into your comparisons for Australia, which is currently excluded from the default ILAMB `aust` definition (cutoff at -41.25 degress following the definition of the Global Fire Emissions Database):
```
#label, name                         , lat_min, lat_max, lon_min, lon_max
au_tas, Australia including Tasmania , -43.75 , -10.50 , 112.00 , 154.00
```

An Australia-focussed ILAMB run with the same setup as above and default `aust` region, would for example produce the following comparisons for ACCESS-ESM1.5 when confronted with albedo measurements of CERES:

![](./image/ilamb_australia.png)

For even more detailed region definitions, you can follow the <a href="https://www.ilamb.org/doc/custom_regions.html" target="_blank">ILAMB tutorial for custom regions</a>.

### Fix your setup with `ilamb_doctor`

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
                                        ... (abbreviated)
                            Precipitation/GPCP2 CLM50n18r229 pr
```
Here we have run the command on some inputs in our test directory. You will see a list of the confrontations we run and the variables which are required or their synonyms. What is missing in this tutorial is the text coloring which will indicate if a given model has the required variables.

### Advanced Visualisation with the Land Model Testbed (LMT) unified dashboard

The Land Model Testbed (LMT) unified dashboard, powered by Tabulator and the jQuery JS library, illustrates the high-level results from analysis and benchmarking software in the form of data tables (similar to a 2-D heat map). It treats the result as a function of multiple independent (hyperdimensional) inputs and displays the result as a combination of the two inputs.

LMT is the tool which ilamb officially used to deploy their result, it has some useful function which help people to go through ilamb result, so we suggest NCI user to use LMT aswell.

#### Install LMT
There are two ways to get LMT installed, first is you can get it on their official repo [here](https://github.com/climatemodeling/unified-dashboard)

```
git clone https://github.com/climatemodeling/unified-dashboard.git
```

#### Use LMT
When you access to the directory you cloned, you will see the structure like this:
```
.
├── README.md
├── assets
├── dist
├── gulpfile.js
├── package-lock.json
└── package.json
```

Then you need to copy or build softlink of all the subdirectory and `scalar_database.json` in your ilamb result directory to `dist`.

then cd to `dist` and build your localhost there with command:
```
cd ./dist
python3 -m http.server
```

and you will see your ilamb result been deployed by LMT.

### Specific explaination for use `IOMB` to evaluate `ACCESS-OM2` raw data

International Ocean Model Benchmarking (IOMB) is a model evaluation tool for Ocean model, it based on `ILAMB` and has the same way to use. Basecally `IOMB` and `ILAMB` are share the core procedure difference is different variables and observational dataset to compare with and different config file.

Since `IOMB` can not read the raw data of `ACCESS-OM2`, we will introduce a new tool to help people to CMORise non-cmip data.

#### ACCESS Post-Processor v4
ACCESS Post-Processor v4(APP4) is a is a CMORisation tool designed to convert ACCESS model output to ESGF-compliant formats, primarily for publication to CMIP6. It uses CMOR3 and the CMIP6 data request to generate CF-compliant files according to the CMIP6 data standards.

#### install APP4
[Github repo of APP4](https://github.com/ACCESS-Hive/APP4), clone this repo to your local disk
```
git clone https://github.com/ACCESS-Hive/APP4.git
```

#### setup APP4
After you clone the repo, you will find the repo structure like this:
```
.
├── CITATION.cff
├── LICENCE.txt
├── README.md
├── check_app4.sh
├── custom_app4.sh
├── input_files
│   ├── ccmi-2022
│   ├── cmip6-cmor-tables
│   ├── cmip6_pub_env.yml
│   ├── custom_mode_cmor-tables
│   ├── dreq
│   ├── experiments.csv
│   ├── grids.csv
│   ├── grids_om2-025.csv
│   ├── grids_om2.csv
│   ├── json
│   ├── master_map.csv
│   ├── master_map_ccmi2022.csv
│   ├── master_map_om2.csv
│   └── var_subset_lists
├── multiwrap_app4.sh
├── multiwrap_qc4.sh
├── production_app4.sh
├── production_qc4.sh
└── subroutines
    ├── app.py
    ├── app.pyc
    ├── app_functions.py
    ├── app_functions.pyc
    ├── app_wrapper.py
    ├── cleanup.sh
    ├── completion_check.py
    ├── custom_json_editor.py
    ├── database_manager.py
    ├── deprecated
    ├── dreq_mapping.py
    ├── qcfigs_index.py
    ├── quality_check.py
    └── setup_env.sh
```
for `IOMB` we only need some Ocean variables, so first step we need to specify which variable we want.
so we go to `./input_files/var_subset_lists` and create a new `.txt` file
```
cd ./input_files/var_subset_lists
touch IOMB_variable.txt
```
in this new `.txt` file, we could specify `frequency,variable`
```
Omon,chl
Omon,o2
Omon,no3
Omon,po4
Omon,talk
Omon,dissic
Omon,mlotst
Omon,thetao
Omon,so
```
Next step is to change some user options in `custom_app4.sh`

You can define those options based on what you need follow the instruction, here we just provide an example for `IOMB`

To get variables, you can specify attributes like below
```
DATA_LOC=/g/data/p73/archive/non-CMIP/ACCESS-ESM1_5/
EXP_TO_PROCESS=                               # local name of experiment
VERSION=ESM                                   # select one of: [CM2, ESM, OM2[-025]]
START_YEAR=1850                               # internal year to begin CMORisation
END_YEAR=2014                                 # internal year to end CMORisation (inclusive)

VAR_SUBSET=true
VAR_SUBSET_LIST=input_files/var_subset_lists/IOMB_variable.txt

OUTPUT_LOC=/scratch/$PROJECT/$USER/APP4_output 
PROJECT=$PROJECT                              # NCI project to charge compute; $PROJECT = your default project
ADDPROJS=( p73 p66 )                          # additional NCI projects to be included in the storage flags
QUEUE=hugemem                                 # NCI queue to use; hugemem is recommended
MEM_PER_CPU=24                                # memory (GB) per CPU (recommended: 24 for daily/monthly; 48 for subdaily)                    
```

After you get everything done, run `custom_app4.sh`
```
bash custom_app4.sh
```
then you will get CF-compliant netCDF files in `OUTPUT_LOC`

### Cmoriser for ilamb

We have developed a CMORiser for ACCESS raw data specifically for ILAMB. This allows users to run ILAMB directly with ACCESS raw data, eliminating the need for any additional CMORise pre-processing steps.

##### Usage of cmoriser

We've integrated this CMORiser into the ilamb-tree-generator package, making its usage very similar to that of ilamb-tree-generator. This streamlines the configuration of ILAMB for evaluating ACCESS model data.```

First, we need a `.yml` file to contain metadatas which `ilamb-tree-generator`, there is an example:

```
    datasets:
    - {mip: CMIP, institute: CSIRO, dataset: ACCESS-ESM1-5, project: CMIP6, exp: historical, ensemble: r1i1p1f1}
    
    - {mip: non-CMIP, institute: CSIRO, dataset: ACCESS-ESM1-5, project: CMIP6, exp: HI-CN-05,}
```

This example include two datasets, first one is a cmip dataset, which is the origin way to use `ilamb-tree-generator`. The second dataset is an ACCESS raw output which is a non-cmip dataset, most parts are the same but with some special parameters for non-cmip dataset only, following are the detail of each parameters:

```
mip: 
    need to be non-cmip to trigger the cmoriser for non-cmip data.

path:
    For people who want to use there own ACCESS raw data, you can speciy your data root there, otherwise it will automatically use data in `p73` 
```

After you finish set up the `config.yml` file, trigger the `ilamb-tree-generator`, then you will get your cmorised data in `ILAMB-ROOT` which ilamb can read.





