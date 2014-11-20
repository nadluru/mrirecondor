#!/bin/sh


cmdName=$1
PFileName=$2
outputFolderName=$3
/home/kecskemeti/AUTO_RECON_SCRIPTS/recon24_mpnrage_081714 -f P03584.7 -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -export_smaps -fr_start 0 -dat_files -mpnrage_vfa_ss -max_tornado -causal -pils_self -alpha_1 4.0 -alpha_2 6.0 -waisman -write_slice 112
mv ph_000_mag.dat SSw.mag
mv Complex_Image_Frame_000_V_000.dat SSw.cpx

/home/kecskemeti/AUTO_RECON_SCRIPTS/recon24_mpnrage_081714 -f P03584.7 -viability -ir_prep_head -update_rate 1 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -external_smaps -fr_start 0 -dat_files -mpnrage_vfa_ss -max_tornado -causal -pils_self -waisman -write_slice 112
mv ph_000_mag.dat SS.mag
mv Complex_Image_Frame_000_V_000.dat SS.cpx

/home/kecskemeti/AUTO_RECON_SCRIPTS/recon24_mpnrage_081714 -f P03584.7 -viability -ir_prep_head -update_rate 5 -b0_eddy_correct 1 -export_complex_images -motion_detection_xyz -wdth_low_prep 525 -wdth_high_prep 525 -prep_phase 0 -mpnrage_vfa -pils -external_smaps -fr_start 0 -dat_files -max_tornado -causal -pils_self -alpha_1 4.0 -alpha_2 6.0 -target_res 600 -end_frame 53 -waisman -pils_fixed_frame -write_slice 112
mkdir FRAMES
mv Co* FRAMES/
