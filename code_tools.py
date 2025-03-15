from agno.tools import Toolkit
import os
import subprocess
from agno.tools.python import PythonTools
from agno.tools.shell import ShellTools
from agno.utils.log import logger
from typing import List
from linkedin_tools import linkedin_search_tool

class TerminalTools(Toolkit):
    def __init__(self):
        super().__init__(name="terminal_tools")
        self.register(self.run_terminal_command)

    def run_terminal_command(self, args: List[str], background: bool = False, tail: int = 100) -> str:
        """
        Runs a terminal command using subprocess without opening a new terminal window.

        Args:
            args (List[str]): The command to run as a list of strings.
            background (bool): If True, runs the command in the background.
            tail (int): The number of lines to return from the output.

        Returns:
            str: The output of the command or an error message.
        """
        logger.info(f"Running terminal command: {' '.join(args)}")

        try:
            if background:
                # Run in the background without blocking Python
                process = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return f"Command '{' '.join(args)}' is running in the background (PID: {process.pid})"
            
            # Run command normally and capture output
            result = subprocess.run(args, capture_output=True, text=True, shell=False)

            logger.debug(f"Result: {result}")
            logger.debug(f"Return code: {result.returncode}")

            if result.returncode != 0:
                print(f"Error: {result.stderr.strip()}")
                return f"Error: {result.stderr.strip()}"

            # Return only the last `tail` lines of output
            return "\n".join(result.stdout.strip().split("\n")[-tail:])

        except Exception as e:
            print(f"Failed to run terminal command: {e}")
            logger.warning(f"Failed to run terminal command: {e}")
            return f"Error: {e} ,  let the main agent take care of it"
    