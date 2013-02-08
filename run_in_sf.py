import sublime, sublime_plugin
from subprocess import call
import os
from os.path import basename, dirname
import re

class RunInSfCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        file_name = os.path.basename(file_path)
        suite_name = os.path.basename(os.path.dirname(file_path))
        system_name = basename(file_path[:file_path.rfind("\SystemAreas")])
        path_to_sf = file_path[:file_path.rfind("\Scripts")]
        config_path = os.path.join(path_to_sf, 'Scripts', system_name, 'RunConfigs', suite_name + ".conf")
        launcher_path = os.path.join(path_to_sf, 'ScriptKit', 'TestLauncher.exe')

        # print(file_name, suite_name, config_path, launcher_path)
        os.chdir(path_to_sf)
        call([r'c:\windows\system32\cmd.exe', '/K', launcher_path, '-c', config_path,
             '-o', file_name])



