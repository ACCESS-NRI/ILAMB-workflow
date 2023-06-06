#!/usr/bin/python

import os,argparse

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument('--local_path',dest='local_path',type=str,nargs=1,default=["./"],help='dir to save softlink of model_reault data')
args = parser.parse_args()


Path='/g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/'
# Path_local=os.path.dirname(os.path.abspath(__file__))
# Experiment='r38i1p1f1'

# f=os.walk(Path+Experiment)

dic={
    'Emon':['cSoil'],
    'Lmon':['cVeg','gpp','lai','nbp','ra','rh','tsl'],
    'Amon':['evspsbl','hfls','hfss','hurs','pr','rlds','rlus','rsds','rsus','tasmax','tasmin','tas'],
    'Omon':['hfds'],
}

exlist=os.listdir(Path)

if not os.path.exists(args.local_path[0]+'/ACCESS-ESM1-5'):
    os.makedirs(args.local_path[0]+'/ACCESS-ESM1-5')

local_path=args.local_path[0]+'/ACCESS-ESM1-5'

for ex in exlist:
    if not os.path.exists(local_path+'/'+ex):
        os.makedirs(local_path+'/'+ex)
        Experiment=ex
        for folder in dic.keys():
            for subfolder in dic[folder]:
                for root,dirs,files in os.walk(Path+Experiment+'/'+folder+'/'+subfolder+'/gn/files'):
                    if files!=[]:
                        src=root+'/'+files[0]
                        dist=local_path+'/'+Experiment+'/'+subfolder+'.nc'
                        os.symlink(src,dist)
                        break

                # src=Path+Experiment+'/'+folder+'/'+subfolder+'/gn/files'
                # dist=os.path.dirname(os.path.abspath(__file__))+'/'+Experiment+'/'+subfolder
                # os.symlink(src,dist)
        


# for dirpath,dirnames,filenames in f:

#     for folder in dirnames:
#         # list_d=['Amon','Emon','LImon','Lmon','Omon','SImon']
#         if(folder in dic.keys()):
#             subf=os.walk(dirpath+'/'+folder)
#             for subpath,subnames,subfilenames in subf:
#                 for subfolder in subnames:
#                     src=subpath+'/'+subfolder+'/gn/files'
#                     dist=os.path.dirname(os.path.abspath(__file__))+'/'+subfolder

#                     os.symlink(src,dist)
#                 break

#     break


# for folder in dic.keys():
#     for subfolder in dic[folder]:
#         src=Path+Experiment+'/'+folder+'/'+subfolder+'/gn/files'
#         dist=os.path.dirname(os.path.abspath(__file__))+'/'+subfolder
#         os.symlink(src,dist)