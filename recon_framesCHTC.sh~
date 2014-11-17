#!/bin/sh

cmdName = $1
PFileName = $2
startFrameIdx = $3
endFrameIdx =  $4
outputFolderName = $5

echo Setting up VIPRIR binaries.
TargetPath=VIRPIRBinariesForCondor
mkdir ${TargetPath}
mv ./${cmdName} ${TargetPath}
chmod -R a=wrx ${TargetPath}

echo Setting up the environment.
export HOME=/home/`whoami`
export PATH=$PWD/${TargetPath}:$PATH

rm -f *.dat
${cmdName} -f ${PFileName} -condor_htc -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -export_smaps -fr_start 0 -dat_files -mpnrage_vfa_ss -max_tornado -causal -pils_self -rawon 2 -smap_res 8.0 -threads 1 -rend 1

${cmdName} -f ${PFileName} -condor_htc -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -external_smaps -fr_start ${startFrameIdx} -dat_files -max_tornado -causal -pils_self -alpha_1 4.0 -alpha_2 6.0 -target_res 600 -end_frame ${endFrameIdx} -waisman -pils_fixed_frame -write_slice 112 -threads 1 -rend 1


mkdir FRAMES
mv Co* FRAMES/



mkdir ${outputFolderName}
mv FRAMES ./${outputFolderName}

tar -zcvf ${outputFolderName}.tar.gz ${outputFolderName}

echo Removing VIPRIR binaries folder and dat files
rm -rf $PWD/${TargetPath}
rm -f *.dat