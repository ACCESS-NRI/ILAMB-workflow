import os
import netCDF4 as nc
import xarray as xr
import argparse
import gc

print('start')
def cmip6(path,dic,length,output='./',model_name='',submodel_name=''):
    #################################################################################
    #index
    MODEL_NAME_INDEX=-(length-6)
    SUBMODEL_NAME_INDEX=-(length-8)
    EXPERIMENT_INDEX=-(length-9)
    ENSEMBLE_INDEX=-(length-10)
    VARIABLE_INDEX=-(length-12)
    VARIABLE_GROUP_INDEX=-(length-11)
    

    for root,dirs,files in os.walk(path+model_name+submodel_name,topdown=False):
        root_list=root.split('/')
        
        if len(root_list)==length:
            #output file structure
            output_path=output+'/'+root_list[MODEL_NAME_INDEX]+'/'+root_list[SUBMODEL_NAME_INDEX]+'/'+root_list[EXPERIMENT_INDEX]+'/'+root_list[ENSEMBLE_INDEX]
            #target output file name
            output_filename=root_list[VARIABLE_INDEX]+'.nc'

            if root_list[VARIABLE_GROUP_INDEX] in dic.keys() and root_list[VARIABLE_INDEX] in dic[root_list[VARIABLE_GROUP_INDEX]]:
                if not os.path.isdir(output_path):
                    os.makedirs(output_path)
                if output_filename not in os.listdir(output_path):
                    if len(files)==1:
                        src=root+'/'+files[0]
                        dist=output_path+'/'+output_filename
                        os.symlink(src,dist)
                    else:
                        with xr.open_mfdataset(root+'/*.nc',use_cftime=True,data_vars=[root_list[VARIABLE_INDEX]],combine_attrs='drop_conflicts') as new_dataset:
                            new_dataset.to_netcdf(output_path+'/'+output_filename)


def cmip5(path,dic,output='./',model_name='',submodel_name=''):
    #index
    MODEL_NAME_INDEX=-9
    SUBMODEL_NAME_INDEX=-8
    EXPERIMENT_INDEX=-7
    ENSEMBLE_INDEX=-3
    VARIABLE_INDEX=-1
    VARIABLE_GROUP_INDEX=-4

    for root,dirs,files in os.walk(path+model_name+submodel_name,topdown=False):
        root_list=root.split('/')
       
        if len(root_list)==16:
            #output file structure
            output_path='./'+root_list[MODEL_NAME_INDEX]+'/'+root_list[SUBMODEL_NAME_INDEX]+'/'+root_list[EXPERIMENT_INDEX]+'/'+root_list[ENSEMBLE_INDEX]
            #target output file name
            output_filename=root_list[VARIABLE_INDEX]+'.nc'

            if root_list[VARIABLE_GROUP_INDEX] in dic.keys() and root_list[VARIABLE_INDEX] in dic[root_list[VARIABLE_GROUP_INDEX]]:
                if not os.path.isdir(output_path):
                    os.makedirs(output_path)
                if output_filename not in os.listdir(output_path):
                    if len(files)==1:
                        src=root+'/'+files[0]
                        dist=output_path+'/'+output_filename
                        os.symlink(src,dist)
                    else:
                        try:
                            with xr.open_mfdataset(root+'/*.nc',use_cftime=True,data_vars=[root_list[VARIABLE_INDEX]],combine_attrs='drop_conflicts') as new_dataset:
                                new_dataset.to_netcdf(output_path+'/'+output_filename)
                        except Exception as e:
                            print(root)
                            print(e)
            


#################################################################################

if __name__=='__main__':

    dic={
        'Emon':['cSoil'],
        'Lmon':['cVeg','gpp','lai','nbp','ra','rh','tsl'],
        'Amon':['evspsbl','hfls','hfss','hurs','pr','rlds','rlus','rsds','rsus','tasmax','tasmin','tas'],
        'Omon':['hfds'],
        }

    parser=argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '--init',
        dest='init_file',
        type=str,
        nargs=1,
        default=['./init.txt'],
    )

    parser.add_argument(
        '--output',
        dest='output_root',
        type=str,
        nargs=1,
        default=['./'],
    )
    args = parser.parse_args()

    ####################################
    INIT_FILE=args.init_file[0]
    OUTPUT_ROOT=args.output_root[0]
    ####################################

    if not os.path.isdir(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT)

    with open(INIT_FILE) as f:
        for line in f.readlines():
            if line.strip().startswith("#"):
                continue
            line=line.split(',')
            if len(line)>1:
                print(line,len(line))
                raise Exception('Sorry, your init file format is Wrong, please follow the doc and reorganise it')
            group=line[0].split('/')[3].strip()
            path=line[0].strip()
            print(group)
            if group in ['oi10']:
                cmip6(path,dic,15,output=OUTPUT_ROOT)
            elif group in ['fs38']:
                cmip6(path,dic,16,output=OUTPUT_ROOT)
            elif group in ['rr3','al33']:
                cmip5(path,dic,OUTPUT_ROOT)
            else:
                raise Exception('Sorry, the group you chosen is unavailable')
