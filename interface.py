from corruptor import Corruptor
import os

ROM_DIR = 'roms'
EXPORT_DIR = 'corrupted_roms'

class Interface:
    def __init__(self, rom_path, export_path, run_command):
        self.rom_path = rom_path
        self.export_path = export_path
        self.run_command = run_command
        self.initial_setup()
        self.main_menu()

    def initial_setup(self):
        input("""

    Welcome to the Haggleforth™ Rom Corruptor!
        
The Haggleforth™ Rom corruptor is an incremental corruptor, meaning it only corrupts
a small amount at a time, storing the corruption in patches that can be toggled on and off.

Press Enter to continue...
""")

        if self.rom_path == None:
            for root, dirs, files in os.walk(ROM_DIR):
                for i, filename in enumerate(files):
                    print(f"{i+1}. {filename}")

                rom_index = int(input("Give the index of the rom you'd like to use: "))
                self.rom_path = os.path.join(root, files[rom_index-1])

        if self.export_path == None:
            self.export_path = os.path.join(EXPORT_DIR, input("Give a name for the new corruption: "))

        if(self.run_command == None):
            self.run_command = input("Give the command for running the rom: ")

        self.corruptor = Corruptor(self.rom_path, self.export_path, 0.00005)

    def launch_emulator(self):
        self.corruptor.export_rom()
        os.system(f'{self.run_command} "{self.export_path}"')

    def toggle_patches(self):
        print("Patches:")
        for index, patch in enumerate(self.corruptor.patches):
            print(f"\t{index+1} - {'enabled' if patch.enabled else 'disabled'}")

        patches = input("List the patches you wish to toggle (ex: 1 2 3): ")
        print(len(patches))
        if len(patches) == 0:
            return
        
        patches = [int(i) for i in patches.split(' ')]

        for patch in patches:
            self.corruptor.patches[patch - 1].toggle()


    def print_directions(self):
        print("""If the game isn't sufficiently corrupted, try generating a new patch.

If a patch is unsuccessful, try regenerating the current patch.

If the game is broken even after regenerating the current patch, try toggling patches.

If all else fails, start a new session


""")
        input("A corruption patch will now be generated and ran. (Press Enter to continue): ")

    def main_menu(self):
        self.print_directions()
        self.corruptor.create_patch(False)
        self.launch_emulator()
        while True:
            choice = int(input('''
1: Run as-is
2: Regenerate current patch and run
3: Generate new patch and run
4: Toggle patches and run
5: Change corruption ammount
6: New session
7: Run initial setup again

Choice: '''))

            if choice == 1:
                pass
            elif choice == 2:
                self.corruptor.create_patch(True)
            elif choice == 3:
                self.corruptor.create_patch(False)

            elif choice == 4:
                self.toggle_patches()

            elif choice == 5:
                percent = float(input(f"What percent of bytes should be corrupted? (Current is {self.corruptor.corrupt_lvl * 100}): ")) / 100
                self.corruptor.corrupt_lvl = percent
                continue

            elif choice == 6:
                self.corruptor.patches = []

            elif choice == 7:
                self.initial_setup()

            self.launch_emulator()