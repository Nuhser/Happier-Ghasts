import argparse
import shutil

parser = argparse.ArgumentParser(
    prog = "Happier Ghasts Release Builder"
)

parser.add_argument("-v", "--version", action="version", version='%(prog)s 1.0.0')
parser.add_argument("-r", "--release", dest="release", help="Release number used on Github and Modrinth")

args = parser.parse_args()

shutil.make_archive(f"Happier_Ghasts_Data_Pack_v{args.release}", "zip", "data_pack")
shutil.make_archive(f"Happier_Ghasts_Resource_Pack_v{args.release}", "zip", "resource_pack")