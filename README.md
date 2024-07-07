# Lines Of Code Badge Workflow

This GitHub Action workflow helps you generate a badge displaying the lines of code in your repository.

## How to Use

Follow these steps to set up the Lines Of Code badge in your repository.

### Step 1: Copy the Workflow YAML

Copy the following YAML code into a new file located at `.github/workflows/lines-of-code.yml` in your repository:


```yml
name: Lines Of Code

on: [push]

jobs:
  print-repo-url:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Install requirements
      run: pip install -r requirements.txt
    - name: Create Workspace Folder
      run: mkdir -p wrdir
    - name: get Lines Of Code repo
      run: git clone https://github.com/yasserbdj96/linesofcode.git wrdir
    - name: Get this repository badges 
      run: python wrdir/main.py --URL="https://github.com/${{ github.repository }}"
    - name: remove
      run: rm -rf wrdir
    #- name: Copy badges back to current repo     
    #  run: cp -R ./badges/. .
    - name: Commit and push changes
      run: |
        git config --global user.email "github-actions@github.com"
        git config --global user.name "GitHub Actions"
        git add .
        git commit -m "Add badges folder."
        git push
```

### Step 2: Configure Repository Settings:
Ensure your repository is configured correctly to use GitHub Actions.

Step 1:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/1.png" alt="Repository Settings Step 1"><br>
Step 2:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/2.png" alt="Repository Settings Step 2"><br>
Step 3:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/3.png" alt="Repository Settings Step 3"><br>

## Credits

This workflow uses the [linesofcode](https://github.com/yasserbdj96/linesofcode) project by [yasserbdj96](https://github.com/yasserbdj96).

For more information, refer to the original [linesofcode repository](https://github.com/yasserbdj96/linesofcode).