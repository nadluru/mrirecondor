#!/bin/sh

cmdName=$1
PFileName=$2
outputFolderName=$3

echo Setting up VIPRIR binaries.
TargetPath=VIRPIRBinariesForCondor
mkdir ${TargetPath}
mv ./${cmdName} ${TargetPath}
chmod -R a=wrx ${TargetPath}

echo Setting up the environment.
export HOME=/home/`whoami`
export PATH=$PWD/${TargetPath}:$PATH

rm -f *.dat
${cmdName} -f ${PFileName} -condor_htc -threads 1 -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -causal -export_complex_images -motion_detection_xyz -wdth_low_prep 225 -wdth_high_prep 225 -prep_phase 0 -write_slice 112 -pils -pils_self -export_smaps -dat_files -smap_res 6 -recon_ss 1 -fout -smaps_only

${cmdName} -f ${PFileName} -condor_htc -threads 1 -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -causal -export_complex_images -motion_detection_xyz -wdth_low_prep 225 -wdth_high_prep 225 -prep_phase 0 -write_slice 112 -pils -external_smaps -end_frame 262 -target_res 600 -max_tornado -dat_files -fout -write_cpx_only

mkdir ${outputFolderName}
mv DICOMS_SMAP_FRAME ./${outputFolderName}
mv DICOMS_COMP ./${outputFolderName}
mv SMAPS ./${outputFolderName}

tar -zcvf ${outputFolderName}.tar.gz ${outputFolderName}

echo Removing VIPRIR binaries folder and dat files
rm -rf $PWD/${TargetPath}
rm -f *.dat
