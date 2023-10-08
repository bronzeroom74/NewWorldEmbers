#!/usr/bin/python
import sys
import argparse

########################################################
# Kszug's loc generator for idea files
#
# usage:
#   idea_loc_generator.py [-dh] input_file output_file
#
# optional arguments:
#   -d  
#      generate desc loc for every idea
#   -h
#      display help message
#########################################################

parser = argparse.ArgumentParser(description="Generates loc for idea files")
parser.add_argument("--desc", "-d", help="Generate desc loc", action="store_true")
parser.add_argument("input_file", type=str, help="Enter your input file")
parser.add_argument("output_file", type=str, help="Enter your output file")

args = parser.parse_args()

desc = args.desc 
input_file = args.input_file
output_file = args.output_file

def read_input_file(input_path):
    indent_level = 0
    ideas = []
    with open(input_path, "r", encoding="utf-8-sig") as f:
        input_lines = f.read().splitlines()

    for input_line in input_lines:
        if indent_level == 2 and "=" in input_line:
            split_line = input_line.split()
            ideas.append(split_line[0])
        indent_level += input_line.count("{")
        indent_level -= input_line.count("}")

    for x in ideas:
        print(x)

    return ideas

def read_output_file(output_path):
    with open(output_path, "r", encoding="utf-8-sig") as f:
        output_lines = f.read().splitlines()

    loc = []
    for output_line in output_lines:
        if output_line != "l_english:":
            split_line = output_line.split()
            loc.append(split_line[0][:-2])

    for x in loc:
        print(x)

    return loc

def write_output_file(output_path):
    f = open(output_path, "a", encoding="utf-8-sig")
    for x in ideas_in_file:
        if x not in loc_in_file:
            f.write(f"\n  {x}:0 \"WRITE ME\"")
            print(f"Added {x} to loc file")
        if desc and x+"_desc" not in loc_in_file:
            f.write(f"\n  {x}_desc:0 \"WRITE ME\"")
            print(f"Added {x}_desc to loc file")

print("Ideas:")
ideas_in_file = read_input_file(input_file)
print("Loc:")
loc_in_file = read_output_file(output_file)
print("Writing:")
write_output_file(output_file)

