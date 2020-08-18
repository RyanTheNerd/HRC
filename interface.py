from corruptor import Corruptor
import os

class Interface:
    def __init__(self):
        self.rom_path = "smb3.nes"
        self.export_path = "smb3_corrupt.nes"
        self.corruptor = Corruptor(self.rom_path, self.export_path, 0.00005)
        self.main_menu()

    def launch_emulator(self):
        self.corruptor.export_rom()
        os.system(f"fceux {self.export_path}")

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


    def print_welcome_message(self):
        print("""\tWelcome to the Haggleforth™ Rom Corruptor!
The Haggleforth™ Rom corruptor is an incremental corruptor, meaning it only corrupts 
a small amount at a time, storing the corruption in patches that can be toggled on and off.

If the game isn't sufficiently corrupted, try generating a new patch.

If a patch is unsuccessful, try regenerating the current patch.

If the game is broken even after regenerating the current patch, try toggling patches.


""")
        input("A corruption patch will now be generated and ran. (Press Enter to continue): ")

    def main_menu(self):
        self.print_welcome_message()
        self.corruptor.create_patch(False)
        self.launch_emulator()
        while True:
            choice = int(input('''
1: Run as-is
2: Regenerate current patch and run
3: Generate new patch and run
4: Toggle patches and run
5: New session

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
                self.corruptor.patches = []

            self.launch_emulator()


interface = Interface()


        

