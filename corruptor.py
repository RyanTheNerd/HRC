from methods import METHODS
from patch import Patch
import math
import shutil

class Corruptor:
    methods = METHODS
    def __init__(self, rom_path, export_path, corrupt_lvl):
        self.rom_path = rom_path
        self.export_path = export_path
        self.load_rom()

        # Size of patch
        self.corrupt_lvl = corrupt_lvl
        self.patch_size = math.floor(len(self.rom) * corrupt_lvl)
        self.patch_range = [math.floor(len(self.rom) / 4), len(self.rom)]
        self.patches = []

    def load_rom(self):
        with open(self.rom_path, 'rb') as rom:
            self.rom = bytearray(rom.read())

    def export_rom(self):
        # Apply patch to rom
        for patch in self.patches:
            for byte in patch.bytes:
                self.rom[byte.addr] = self.methods[byte.method_name](self.rom[byte.addr]) % 256

        # Export rom
        shutil.copyfile(self.rom_path, self.export_path)
        with open(self.export_path, 'bw') as rom:
            rom.write(bytes(self.rom))

        self.load_rom()

    def create_patch(self, replace_current = False):

        patch = Patch(self.rom, self.patch_range, self.patch_size, 'increment')
        if replace_current == True:
            self.patches[len(self.patches) - 1] = patch
        else:
            self.patches.append(patch)

    def toggle_patches(self, patch_list):
        for patch in enumerate(self.patches):
            if patch.id in patch_list:
                patch.toggle()
            