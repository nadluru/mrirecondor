#!/bin/sh
#Om Shanti. Om Sai Ram.
#July 15, 2014. 9:10 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 10, 2014. 
#Om Shanti. Om Sai Ram.
#July 10, 2014. 5:53 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 1, 2014.
#Nagesh Adluru.

echo Setting up ANTS binaries.
TargetPath=ANTSBinariesForCondor
mkdir ${TargetPath}
mv ./ANTS ${TargetPath}
mv ./ImageMath ${TargetPath}
mv ./N4BiasFieldCorrection ${TargetPath}
mv ./SetOrigin ${TargetPath}
mv ./WarpImageMultiTransform ${TargetPath}
mv ./AverageImages ${TargetPath}
mv ./AverageAffineTransform ${TargetPath}
mv ./MultiplyImages ${TargetPath}
mv ./ThresholdImage ${TargetPath}
chmod -R a=wrx ${TargetPath}

echo Setting up the environment.
export HOME=/home/`whoami`
export PATH=$PWD/${TargetPath}:$PATH

Image=$1
Template=$2
regDir=$3

mkdir $regDir
mv ${Image} ./${regDir}
mv ${Template} ./${regDir}
mv ./antsIntroduction.sh ./${regDir}
cd ${regDir}
chmod a=wrx antsIntroduction.sh

sh antsIntroduction.sh -d 3 -r ${Template} -i ${Image} -o ${regDir} -m 30x90x20 -n 0 -s CC -t "GR"

cd ..
echo Removing ANTS binaries folder.
rm -rf $PWD/${TargetPath}

