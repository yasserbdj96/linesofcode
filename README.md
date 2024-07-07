#

<h4>How to Use?</h4>
copy this yml code to .github/workflows/

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

make sure of the repository settings:

<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/1.gif" alt="by yasserbdj96">
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/2.gif" alt="by yasserbdj96">
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/3.gif" alt="by yasserbdj96">