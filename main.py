from corruptor import Corruptor
from interface import Interface
import argparse

parser = argparse.ArgumentParser(description="Iterative rom corruptor")
parser.add_argument('--rom-path', '-rp', help="Path of the rom to be used")
parser.add_argument('--export-path', '-ep', help="Path of the corrupted rom")
parser.add_argument('--corruption-level', '-cl', help="The level of corruption each patch causes", type=int, default=5)
parser.add_argument('--run-command', '-em', help="The command to run with the corrupted rom", default=None)
parser.add_argument('--script', '-s', help="Run in a non-interactive mode, with only one patch", action="store_true")


args = parser.parse_args()
print(args)

if args.script:
    corruptor = Corruptor(args.rom_path, args.export_path, args.corruption_level)
    corruptor.create_patch()
    corruptor.export_rom()

else:
    Interface(args.rom_path, args.export_path, args.run_command)
