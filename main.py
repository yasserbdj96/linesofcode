#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
import os
import json
import re
from tabulate import tabulate
#from PIL import ImageFont, ImageDraw
import argparse
import subprocess
import time

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments with names
parser.add_argument('--URL', '--url', dest='URL', type=str, default=os.getenv('URL', ''), help='')

# Parse the command-line arguments
args = parser.parse_args()
URL = args.URL

#
def clone_repo(repo_url, folder_name='temp'):
    try:
        # Ensure the folder name is a directory
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
        # Run the git clone command
        subprocess.run(['git', 'clone', repo_url, folder_name], check=True)
        print(f"Repository cloned into {folder_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while cloning the repository: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Recursively print all files, excluding specified folders
def print_files(root_dir, exclude_dirs):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove excluded directories from dirnames list
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(file_path)

def is_binary_file(filepath):
    with open(filepath, 'rb') as f:
        chunk = f.read(1024)
        if b'\0' in chunk:
            return True
        return False

def count_lines(filepath, language):
    total_lines = 0
    code_lines = 0
    comment_lines = 0
    empty_lines = 0
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            total_lines += 1
            line = line.strip()
            if not line:
                empty_lines += 1
            elif re.match(language['comment_regex'], line):
                comment_lines += 1
            else:
                code_lines += 1
    return (total_lines, code_lines, comment_lines, empty_lines)

def get_language(filepath, languages):
    for language in languages.values():
        for extension in language['extensions']:
            if filepath.endswith(extension):
                return language
    return None

def get_filetypes(dirpath):
    filetypes = {}
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            filepath = os.path.join(root, file)
            if not is_binary_file(filepath):
                ext = os.path.splitext(file)[1]
                if ext not in filetypes:
                    filetypes[ext] = 0
                filetypes[ext] += 1
    return filetypes

def main():
    dirpath = "temp"
    clone_repo(URL,folder_name=dirpath)
    if not os.path.isdir(dirpath):
        print("Invalid directory path")
        return

    with open("languages.json") as f:
        languages = json.load(f)

    total_lines = 0
    total_code_lines = 0
    total_comment_lines = 0
    total_empty_lines = 0
    lang_lines = {}
    filetypes = get_filetypes(dirpath)
    
    new_dict = {}
    for key in languages:
        name = languages[key]["name"].upper()
        new_dict[name] = 0

    for root, dirs, files in os.walk(dirpath):
        for file in files:
            filepath = os.path.join(root, file)
            if not is_binary_file(filepath):
                language = get_language(filepath, languages)
                if language:
                    (total, code, comment, empty) = count_lines(filepath, language)
                    total_lines += total
                    total_code_lines += code
                    total_comment_lines += comment
                    total_empty_lines += empty
                    lang_name = language["name"].upper()
                    new_dict[f"{lang_name}"] += 1
                    if lang_name not in lang_lines:
                        lang_lines[lang_name] = {'total': 0, 'code': 0, 'comment': 0, 'empty': 0}
                    lang_lines[lang_name]['total'] += total
                    lang_lines[lang_name]['code'] += code
                    lang_lines[lang_name]['comment'] += comment
                    lang_lines[lang_name]['empty'] += empty

    total_files = sum(new_dict.values())

    #all_var=""
    #all_var+="Language    Files    Total Lines      Code Lines       Comment Lines     Empty Lines"+"\n"
    #all_var+="-"*84+"\n"
    data = []
    for lang, lines in lang_lines.items():
        total = lines['total']
        code = lines['code']
        comment = lines['comment']
        empty = lines['empty']
        data.append({'Language': f'{lang}', 'Files': new_dict[f"{lang}"], 'Total Lines': total, 'Code Lines': code, 'Comment Lines': comment, 'Empty Lines': empty})
    #all_var+="{:<12}{:<9}{:<17}{:<17}{:<19}{}".format(lang, new_dict[f"{lang}"], total, code, comment, empty)+"\n"
    #all_var+="-"*84+"\n"
    #all_var+="{:<12}{:<9}{:<17}{:<17}{:<19}{}".format("TOTAL", total_files, total_lines, total_code_lines, total_comment_lines, total_empty_lines)
    #data.append({'Language': 'TOTAL', 'Files': total_files, 'Total Lines': total_lines, 'Code Lines': total_code_lines, 'Comment Lines': total_comment_lines, 'Empty Lines': total_empty_lines})
    force_delete_folder(dirpath)
    return data

def format_table(data):
    headers = ['Language', 'Files', 'Total Lines', 'Code Lines', 'Comment Lines', 'Empty Lines']
    # Sort the data by Total Lines in descending order
    sorted_data = sorted(data, key=lambda x: x['Total Lines'], reverse=True)
    table = []

    for d in sorted_data:
        files = generate_svg_code(f"{d['Language']} Files", format_number(d['Files']), "#08C")
        total_lines = generate_svg_code(f"{d['Language']} Total Lines", format_number(d['Total Lines']), "#08C")
        code_lines = generate_svg_code(f"{d['Language']} Code Lines", format_number(d['Code Lines']), "#08C")
        comment_lines = generate_svg_code(f"{d['Language']} Comment Lines", format_number(d['Comment Lines']), "#08C")
        empty_lines = generate_svg_code(f"{d['Language']} Empty Lines", format_number(d['Empty Lines']), "#08C")

        save_file(f"badges/{d['Language']}",f"{d['Language']}_files.svg", files)
        save_file(f"badges/{d['Language']}",f"{d['Language']}_total_lines.svg", total_lines)
        save_file(f"badges/{d['Language']}",f"{d['Language']}_code_lines.svg", code_lines)
        save_file(f"badges/{d['Language']}",f"{d['Language']}_comment_lines.svg", comment_lines)
        save_file(f"badges/{d['Language']}",f"{d['Language']}_empty_lines.svg", empty_lines)

        s1=f"badges/{d['Language']}"+f"{d['Language']}_files.svg"
        s2=f"badges/{d['Language']}"+f"{d['Language']}_total_lines.svg"
        s3=f"badges/{d['Language']}"+f"{d['Language']}_code_lines.svg"
        s4=f"badges/{d['Language']}"+f"{d['Language']}_comment_lines.svg"
        s5=f"badges/{d['Language']}"+f"{d['Language']}_empty_lines.svg"

        s1=f'<img src="{s1}">'
        s2=f'<img src="{s2}">'
        s3=f'<img src="{s3}">'
        s4=f'<img src="{s4}">'
        s5=f'<img src="{s5}">'


        #row = [d['Language'], d['Files'], d['Total Lines'], d['Code Lines'], d['Comment Lines'], d['Empty Lines']]
        row = [d['Language'], s1, s2, s3, s4, s5]
        table.append(row)
    

    total_files = generate_svg_code(f"Files in All GitHub Repos", format_number(sum(d['Files'] for d in data)), "#08C")
    total_total_lines = generate_svg_code(f"Total Lines of Code (GitHub Repos)", format_number(sum(d['Total Lines'] for d in data)), "#08C")
    total_code_lines = generate_svg_code(f"Code Lines (GitHub Repos)", format_number(sum(d['Code Lines'] for d in data)), "#08C")
    total_comment_lines = generate_svg_code(f"Comment Lines (GitHub Repos)", format_number(sum(d['Comment Lines'] for d in data)), "#08C")
    total_empty_lines = generate_svg_code(f"Empty Lines (GitHub Repos)", format_number(sum(d['Empty Lines'] for d in data)), "#08C")

    save_file(f"badges",f"total_files.svg", total_files)
    save_file(f"badges",f"total_lines.svg", total_total_lines)
    save_file(f"badges",f"total_code_lines.svg", total_code_lines)
    save_file(f"badges",f"total_comment_lines.svg", total_comment_lines)
    save_file(f"badges",f"total_empty_lines.svg", total_empty_lines)

    x1=f"badges"+f"total_files.svg"
    x2=f"badges"+f"total_lines.svg"
    x3=f"badges"+f"total_code_lines.svg"
    x4=f"badges"+f"total_comment_lines.svg"
    x5=f"badges"+f"total_empty_lines.svg"


    #table.append(['TOTAL', sum(d['Files'] for d in data), sum(d['Total Lines'] for d in data),sum(d['Code Lines'] for d in data), sum(d['Comment Lines'] for d in data), sum(d['Empty Lines'] for d in data)])
    table.append(['TOTAL', x1, x2,x3, x4, x5])
    return tabulate(table, headers, tablefmt='pipe')

def save_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        file.write(content)

def format_number(number):
    suffixes = ['', 'k', 'm', 'b', 't']  # Define suffixes for each level of magnitude
    magnitude = 0

    # Determine the appropriate magnitude level
    while abs(number) >= 1000:
        magnitude += 1
        number /= 1000

    # Format the number with the appropriate suffix
    if magnitude == 0:
        formatted_number = f"{int(number)}"
    else:
        formatted_number = f"{number:.1f}{suffixes[magnitude]}"

    return formatted_number


def generate_svg_code(new_text_1, new_text_2, new_color="#08C"):
    svg_code = '''<svg width="79.5" height="20" viewBox="0 0 795 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="releases: 41">
      <title>releases: 41</title>
      <linearGradient id="a" x2="0" y2="100%">
        <stop offset="0" stop-opacity=".1" stop-color="#EEE"/>
        <stop offset="1" stop-opacity=".1"/>
      </linearGradient>
      <mask id="m"><rect width="795" height="200" rx="30" fill="#FFF"/></mask>
      <g mask="url(#m)">
        <rect width="555" height="200" fill="#555"/>
        <rect width="240" height="200" fill="#08C" x="555"/>
        <rect width="795" height="200" fill="url(#a)"/>
      </g>
      <g aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,sans-serif" font-size="110">
        <text x="60" y="148" textLength="455" fill="#000" opacity="0.25">releases</text>
        <text x="50" y="138" textLength="455">releases</text>
        <text x="610" y="148" textLength="140" fill="#000" opacity="0.25">41</text>
        <text x="600" y="138" textLength="140">41</text>
      </g>
    </svg>'''

    def calculate_text_length(text):
        
        font_size = 110
        character_width = font_size * 0.6
        ss=character_width * len(text)
        return ss

    text_width_1 = calculate_text_length(new_text_1)
    text_width_2 = calculate_text_length(new_text_2)
    svg_code = svg_code.replace('releases', new_text_1)
    svg_code = svg_code.replace('41', new_text_2)
    svg_code = svg_code.replace('textLength="455"', f'textLength="{text_width_1}"')
    svg_code = svg_code.replace('textLength="140"', f'textLength="{text_width_2}"')
    svg_code = svg_code.replace('width="555"', f'width="{text_width_1 + 100}"')
    svg_code = svg_code.replace('width="240"', f'width="{text_width_2 + 100}"')
    svg_code = svg_code.replace('width="795"', f'width="{(text_width_1 + text_width_2) + 200}"')
    svg_code = svg_code.replace('width="79.5"', f'width="{((text_width_1 + text_width_2) + 200) / 10}"')
    svg_code = svg_code.replace('0 0 795 200', f'0 0 {((text_width_1 + text_width_2) + 200)} 200')
    svg_code = svg_code.replace('x="555"', f'x="{text_width_1 + 100}"')
    svg_code = svg_code.replace('x="610"', f'x="{text_width_1 + 135}"')
    svg_code = svg_code.replace('x="600"', f'x="{text_width_1 + 145}"')
    svg_code = svg_code.replace('#08C', new_color)
    return svg_code

def force_delete_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file: {file_path}. Error: {e}")
    
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
                print(f"Deleted empty directory: {dir_path}")
            except Exception as e:
                print(f"Failed to delete directory: {dir_path}. Error: {e}")

    try:
        os.rmdir(folder_path)
        print(f"Deleted root directory: {folder_path}")
    except Exception as e:
        print(f"Failed to delete root directory: {folder_path}. Error: {e}")

if __name__ == '__main__':
    all_var=format_table(main())
    with open('badges.md', 'w') as f:
        # Get current date and time in seconds since the epoch
        seconds_since_epoch = time.time()

        # Format the value as a date and time string
        date_time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(seconds_since_epoch))

        #   Print the value
        print(date_time_string)
        f.write(all_var)
        f.write("\n\nLast Update: "+date_time_string)

    print(all_var)
#}END.