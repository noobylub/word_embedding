# Python Virtual Environment Setup Guide

## 1. Install virtualenv
```bash
pip install virtualenv
```

## 2. Create a virtual environment
```bash
python -m virtualenv myenv
```

## 3. Activate the environment

### Windows (Command Prompt):
```cmd
myenv\Scripts\activate.bat
```

### Windows (PowerShell):
```powershell
myenv\Scripts\Activate.ps1
```

### macOS/Linux:
```bash
source myenv/bin/activate
```

## 4. Verify activation
Your terminal prompt should show:
```
(myenv) ...
```

## 5. Install packages
```bash
pip install <package-name>
```

## 6. Deactivate when done
```bash
deactivate
```

## Tips:
- Add `myenv/` to your .gitignore
- Use `python -m pip install` for better reliability
