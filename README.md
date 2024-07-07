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
    - name: Create Workspace Folder
      run: mkdir -p wrdir
    - name: get Lines Of Code repo
      run: git clone https://github.com/yasserbdj96/linesofcode.git wrdir
    - name: Install requirements
      run: pip install -r wrdir/requirements.txt
    - name: Get this repository badges 
      run: cd wrdir && python main.py --URL="https://github.com/${{ github.repository }}"
    - name: Copy badges back to current repo     
      run: mkdir -p badges && cp -R ./wrdir/badges/* ./badges/ && cp -R ./wrdir/badges.md ./badges.md
    - name: remove
      run: rm -rf wrdir
    - name: Commit and push changes
      run: |
        git config --global user.email "github-actions@github.com"
        git config --global user.name "GitHub Actions"
        git add .
        git commit -m "Add badges folder."
        git pull --rebase origin main
        git push origin main
```

### Step 2: Configure Repository Settings:
Ensure your repository is configured correctly to use GitHub Actions.

Step 1:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/1.png" alt="Repository Settings Step 1"><br>
Step 2:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/2.png" alt="Repository Settings Step 2"><br>
Step 3:<br>
<img src="https://raw.githubusercontent.com/yasserbdj96/linesofcode/main/screenshot/3.png" alt="Repository Settings Step 3"><br>

## Example:

| Language   | Files                                          | Total Lines                                          | Code Lines                                          | Comment Lines                                          | Empty Lines                                          |
|:-----------|:-----------------------------------------------|:-----------------------------------------------------|:----------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------|
| SVG        | <img src="badges/SVG/SVG_files.svg">           | <img src="badges/SVG/SVG_total_lines.svg">           | <img src="badges/SVG/SVG_code_lines.svg">           | <img src="badges/SVG/SVG_comment_lines.svg">           | <img src="badges/SVG/SVG_empty_lines.svg">           |
| PYTHON     | <img src="badges/PYTHON/PYTHON_files.svg">     | <img src="badges/PYTHON/PYTHON_total_lines.svg">     | <img src="badges/PYTHON/PYTHON_code_lines.svg">     | <img src="badges/PYTHON/PYTHON_comment_lines.svg">     | <img src="badges/PYTHON/PYTHON_empty_lines.svg">     |
| JSON       | <img src="badges/JSON/JSON_files.svg">         | <img src="badges/JSON/JSON_total_lines.svg">         | <img src="badges/JSON/JSON_code_lines.svg">         | <img src="badges/JSON/JSON_comment_lines.svg">         | <img src="badges/JSON/JSON_empty_lines.svg">         |
| MARKDOWN   | <img src="badges/MARKDOWN/MARKDOWN_files.svg"> | <img src="badges/MARKDOWN/MARKDOWN_total_lines.svg"> | <img src="badges/MARKDOWN/MARKDOWN_code_lines.svg"> | <img src="badges/MARKDOWN/MARKDOWN_comment_lines.svg"> | <img src="badges/MARKDOWN/MARKDOWN_empty_lines.svg"> |
| YAML       | <img src="badges/YAML/YAML_files.svg">         | <img src="badges/YAML/YAML_total_lines.svg">         | <img src="badges/YAML/YAML_code_lines.svg">         | <img src="badges/YAML/YAML_comment_lines.svg">         | <img src="badges/YAML/YAML_empty_lines.svg">         |
| TEXT       | <img src="badges/TEXT/TEXT_files.svg">         | <img src="badges/TEXT/TEXT_total_lines.svg">         | <img src="badges/TEXT/TEXT_code_lines.svg">         | <img src="badges/TEXT/TEXT_comment_lines.svg">         | <img src="badges/TEXT/TEXT_empty_lines.svg">         |
| TOTAL      | <img src="badges/total_files.svg">             | <img src="badges/total_lines.svg">                   | <img src="badges/total_code_lines.svg">             | <img src="badges/total_comment_lines.svg">             | <img src="badges/total_empty_lines.svg">             |

## Credits

This workflow uses the [linesofcode](https://github.com/yasserbdj96/linesofcode) project by [yasserbdj96](https://github.com/yasserbdj96).

For more information, refer to the original [linesofcode repository](https://github.com/yasserbdj96/linesofcode).


<br>
<h2>Support:</h2>
<p>If you enjoy this project and would like to see it continue to improve, or if you would like me to create more interesting projects, please consider <a href="https://github.com/sponsors/yasserbdj96">sponsoring me</a>.</p>
<br>
<br>

<p align="center">
  <samp>
    <a href="https://yasserbdj96.github.io/">website</a> .
    <a href="https://github.com/yasserbdj96">github</a> .
    <a href="https://gitlab.com/yasserbdj96">gitlab</a> .
    <a href="https://www.linkedin.com/in/yasserbdj96">linkedin</a> .
    <a href="https://twitter.com/yasserbdj96">twitter</a> .
    <a href="https://instagram.com/yasserbdj96">instagram</a> .
    <a href="https://www.facebook.com/yasserbdj96">facebook</a> .
    <a href="https://www.youtube.com/@yasserbdj96">youtube</a> .
    <a href="https://pypi.org/user/yasserbdj96">pypi</a> .
    <a href="https://hub.docker.com/u/yasserbdj96">docker</a> .
    <a href="https://t.me/yasserbdj96">telegram</a> .
    <a href="https://gitter.im/yasserbdj96/yasserbdj96">gitter</a> .
    <a href="mailto:yasser.bdj96@gmail.com">e-mail</a> .
    <a href="https://github.com/sponsors/yasserbdj96">sponsor</a>
  </samp>
</p>
