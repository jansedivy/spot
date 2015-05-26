import subprocess


class AppleScript():
    @staticmethod
    def run(script):
        program = "echo $(osascript <<EOF {}\nEOF)".format(script)

        return subprocess.check_output(program, shell=True).decode('utf-8').strip()
