import socket


class BaseConfig:
    JOB_MANAGER = 'local'
    NPROC_PER_JOB = 1


class MacConfig(BaseConfig):
    DFF_ROOT = '/Users/zheng/Projects/DFF/Developing'
    PACKMOL_BIN = '/Users/zheng/Projects/DFF/Developing/bin32m/Packmol/packmol.exe'
    GMX_BIN = '/usr/local/bin/gmx'

    MS_TOOLS_DIR = '/Users/zheng/Projects/msd-server'
    WORK_DIR = '/tmp/MSDServer/'


class ClusterConfig(BaseConfig):
    DFF_ROOT = '/share/apps/dff/msdserver'
    PACKMOL_BIN = '/share/apps/tools/packmol'
    GMX_BIN = '/share/apps/gromacs/msdserver/bin/gmx'

    MS_TOOLS_DIR = '/home/msdserver/msd-server'
    WORK_DIR = '/share/workspace/msdserver/MSDServer/'

    JOB_MANAGER = 'torque'
    JOB_QUEUE = 'cpu'
    NPROC_PER_JOB = 8


Config = ClusterConfig
if socket.gethostname() == 'cluster.hpc.org':
    Config = ClusterConfig
elif socket.gethostname() == 'z-Mac.local':
    Config = MacConfig
else:
    raise Exception('MSDServer will not work on this machine')