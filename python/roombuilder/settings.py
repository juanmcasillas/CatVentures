import logging
import os.path
import shutil


class Config:
    convert = "/usr/local/bin/convert"
    bg_color = (255, 255, 255)  # white
    bg_trans = (0, 0, 0, 0)  # transparent
    control_color = (0, 0, 0)  # black
    basedir = "../assets"
    default_screen_size = (320, 200)
    outdir = "./rooms"
    verbose = False
    # right options to build a PSD file.
    logfile = "-"
    objectFactory = {}
    psd_options = [
        "-depth",
        "8",
        "-type",
        "truecoloralpha",
        "-set",
        "colorspace:auto-grayscale",
        "off",
    ]

    def outputdir(fname):
        return os.sep.join([ Config.outdir, fname])


def LoadConfig():

    global Config
    global LOG


    #Config = type('', (object,), {})()
    
    if Config.logfile.lower() != '-':
        # log to file create a new one each run
        if os.path.exists(LogFile):
            tgt = "%s.old" % LogFile
            shutil.copyfile(LogFile,tgt)
        logging.basicConfig(filename=LogFile, filemode='w+',
                format='%(asctime)s [%(levelname)s] %(message)s', 
                level=logging.DEBUG) # normal: logging.INFO
    else:
        # to standard output
        logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', 
                level=logging.INFO) # normal: logging.INFO

    LOG = logging.getLogger("roombuilder")
    #
    # to log exceptions 
    #logging.error("Exception occurred", exc_info=True)

    