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
${cmdName} -f ${PFileName} -condor_htc -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -export_smaps -fr_start 0 -dat_files -mpnrage_vfa_ss -max_tornado -causal -pils_self -smap_res 8.0 -threads 1 -rend 1
mkdir DICOMS_SMAP_FRAME
mv *.sdcopen DICOMS_SMAP_FRAME/

${cmdName} -f ${PFileName} -condor_htc -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -external_smaps -alpha_1 4.0 -alpha_2 6.0 -mag_ss 2 -threads 1 -rend 1

mkdir DICOMS_COMP
mv *.sdcopen DICOMS_COMP/

mkdir SMAPS
mv SMAP_* SMAPS/


mkdir ${outputFolderName}
mv DICOMS_SMAP_FRAME ./${outputFolderName}
mv DICOMS_COMP ./${outputFolderName}
mv SMAPS ./${outputFolderName}
mv *.dat ./${outputFolderName}

tar -zcvf ${outputFolderName}.tar.gz ${outputFolderName}

echo Removing VIPRIR binaries folder and dat files
rm -rf $PWD/${TargetPath}
rm -f *.dat








