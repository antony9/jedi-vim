''' ------------------------------------------------------------------------
Python initialization
---------------------------------------------------------------------------
here we initialize the jedi stuff '''

import vim

# update the system path, to include the jedi path
import sys
import os

# vim.command('echom expand("<sfile>:p:h:h")') # broken, <sfile> inside function
# sys.path.insert(0, os.path.join(vim.eval('expand("<sfile>:p:h:h")'), 'jedi'))
sys.path.insert(0, os.path.join(vim.eval('expand(s:script_path)'), 'jedi'))

# to display errors correctly
import traceback

# update the sys path to include the jedi_vim script
sys.path.insert(0, vim.eval('expand(s:script_path)'))

def append_vir_env():
    venv = vim.eval('g:jedi#virtual_env_path').split()[-1]
    venv = os.path.abspath(venv)
    import glob
    eggs = glob.glob(os.path.join(venv, "*.egg"))
    sys.path.insert(0, venv)
    sys.path.extend(eggs)

try:
    import jedi_vim
    append_vir_env()
except ImportError:
    vim.command('echoerr "Please install Jedi if you want to use jedi_vim."')
sys.path.pop(1)
