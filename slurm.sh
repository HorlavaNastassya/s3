#!/bin/bash
#SBATCH --gres=gpu:v100:2
#SBATCH --constraint="gpu"
#SBATCH --cpus-per-task=20
#SBATCH --nice=0
#SBATCH --time=23:00:00
#SBATCH --nodes=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=g.nasta.work@gmail.com
#SBATCH --ntasks-per-node=1
#SBATCH -o HLR_%j.out
#SBATCH -e HLR_%j.err
module load anaconda/3/2020.02
export PATH=${PATH}:/u/horlavanasta/SKULL_STRIPING/NiftyReg/niftyreg_install/bin
export PATH=${PATH}:/SKULL_STRIPING/NiftyReg/niftyreg_install/bin
export PATH=${PATH}:/u/horlavanasta/SKULL_STRIPING/ANTS/install/bin
 export PATH=${PATH}:/SKULL_STRIPING/ANTS/install/bin
echo $PATH
srun python3 s3_all.py -i /u/horlavanasta/Data/ADNI/ -o /u/horlavanasta/Data/ADNI_reg_output/
