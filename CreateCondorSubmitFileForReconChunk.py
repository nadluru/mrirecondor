#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Om Shanti. Om Sai Ram. November 14, 2014. 2:05 p.m. Madison, WI.
#Om Shanti. Om Sai Ram. October 6, 2014. 10:27 a.m. Madison, WI.
#Om Shanti. Om Sai Ram.
#July 18, 2014. 7:33 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 15, 2014. 9:06 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 10, 2014. 8:50 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 8, 2014. 2:45 p.m. Madison.
#Om Shanti. #Om Sai Ram.
#May 20, 2014. 10:40 a.m. Madison.
#Om Shanti.
#February 15, 2014.
#Om Shanti.
#January 7, 2014.
#Om Shanti.
#January 2, 2014.
#November 13, 2013.
#June 18, 2013.
#Nagesh Adluru.

import sys
import os
import subprocess as sp
import glob
from os.path import isfile,isdir,join

PFileName = "P14848.7"
outputFolderName = "DatFileFolder"
cmdName="recon24_102914"
vdsName = "VIPR_IR_256_100_1000.grad"
dcmName = "I001.dcm"
suffix="November142014"

submitFile=open("%s%s.submit" % (cmdName,suffix),"w")
submitFile.write("Universe=vanilla\n")
submitFile.write("getenv=True\n")
submitFile.write("Executable=recon_basic.sh\n")

submitFile.write("PeriodicRemove =  (((CurrentTime - EnteredCurrentStatus) > (2*24*3600)) && JobStatus == 5)\n")
submitFile.write("Requirements = ( OpSys == \"LINUX\" && Arch == \"X86_64\" )\n")
submitFile.write("request_cpus = 1\n")
submitFile.write("request_memory = 8000\n")
submitFile.write("request_disk = 1000000\n")
submitFile.write("periodic_release = (JobStatus == 5) && ((CurrentTime - EnteredCurrentStatus) > 30) && (NumSystemHolds < 10)\n")
submitFile.write("match_list_length = 5\n")
submitFile.write("requirements = (TARGET.Name =!= LastMatchName1)\n")

submitFile.write("should_transfer_files = yes\n")
submitFile.write("when_to_transfer_output = ON_EXIT\n\n")

PFile = "/study/iggrant/MPnRAGE_MOTION_CORRECTION/323637/%s" % (PFileName)
cmdFile = "/home/adluru/GenericLabSupportProject/VIPRIRReconCHTCProject/%s" % (cmdName)
dcmFile = "/home/adluru/GenericLabSupportProject/VIPRIRReconCHTCProject/%s" % (dcmName)
vdsFile = "/home/kecskemeti/%s" % (vdsName)

submitFile.write("transfer_input_files = %s, %s, %s, %s\n" % (PFile, cmdFile, dcmFile, vdsFile))

# Chunking data.
for frameIdx in range(0, 250, 1):
  submitFile.write("initialdir=/scratch/VIPRIRReconTest\n")
  submitFile.write("Log=test%d.log\n" % (frameIdx))
  submitFile.write("Output=test%d.out\n" % (frameIdx))
  submitFile.write("Error=test%d.err\n" % (frameIdx))
  
  submitFile.write("transfer_output_files = %s\n" % (outputFolderName))
  submitFile.write("Arguments=%s %s %s %s %s\n" % (cmdName, PFileName, frameIdx, frameIdx + 1, outputFolderName))
  #submitFile.write("+WantGlidein=true\n")
  submitFile.write("Queue\n\n")

submitFile.close()