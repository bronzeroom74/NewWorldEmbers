#If you wish to modify this file, please ping @FatherAlduin in the Ashes dev server before making any changes
import os, sys, fnmatch, re
import time

startTime = time.time()

__version__ = 1.0

def check_basic_style(filepath):
    fixedErrors = 0

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.readlines()
        lineNum = 0
        openBraces = [0, 0]
        newContent = ""
        fixedErrors = 0
        for line in content:
            lineNum +=1
            equalSign = 0
            if not line.startswith("#"):
                if "{" in line:
                    hasComment = re.search(r'#.*[{}]+', line, re.M | re.I)
                    if not hasComment:
                        openBraces[0] += line.count('{')
                        closingBraces = line.count('{') - line.count(' {\n') - line.count(' { ')

                        if closingBraces > 0:
                            noSpaceleftOfBracket = re.search(r'(.*[^\s]+){(.*?\s?)', line,
                                                             re.M | re.I)

                            if noSpaceleftOfBracket:
                                line = re.sub(r'(.*[^\s]+){(.*?\s?)', r"\1 {\2", line)
                                fixedErrors += 1

                            noSpacerightOfBracket = re.search(r'(.*){([^\s]+?)', line,re.M | re.I)
                            if noSpacerightOfBracket:
                                line = re.sub(r'(.*){([^\s]+?)', r"\1{ \2", line)
                                fixedErrors += 1

                if "}" in line:
                    hasComment = re.search(r'#.*[{}]+', line, re.M | re.I)
                    if not hasComment:
                        openBraces[0] += -line.count('}')
                        openingingBraces = line.count('}') - line.count(' }\n') - line.count(' } ')

                        if openingingBraces > 0:

                            noSpaceleftOfBracket = re.search(r'(.*[^\s]+)}(.*?\n?)', line,re.M | re.I)
                            if noSpaceleftOfBracket:
                                line = re.sub(r'(.*[^\s]+)}(\s?)', r"\1 }\2", line)
                                fixedErrors += 1

                            noSpacerightOfBracket = re.search(r'(.*)}([^\s]+?)', line, re.M | re.I)
                            if noSpacerightOfBracket:
                                line = re.sub(r'(.*)}([^\s]+?)', r"\1} \2", line)
                                fixedErrors += 1

                if "=" in line:
                    equalSign = line.count('=') - line.count(' = ') + line.count('  =') + line.count('=  ')
                    if "  =" in line:
                        line = re.sub(r'  =', r" =", line)
                        equalSign = equalSign - line.count('  =')
                        fixedErrors += 1
                    if "=  " in line:
                        line = re.sub(r'=  ', r"= ", line)
                        equalSign = equalSign - line.count('=  ')
                        fixedErrors += 1
                    if equalSign != 0:
                        noSpaceLeftofEqualSign = re.search(r'(.*[^\s]+)=(.*)?', line, re.M | re.I)
                        if noSpaceLeftofEqualSign:
                            line = re.sub(r'(.*[^\s]+)=(.*)?', r"\1 =\2", line)
                            fixedErrors += 1

                        noSpaceRightofEqualSign = re.search(r'(.*)=([^\s]+.*)', line, re.M | re.I)
                        if noSpaceRightofEqualSign:
                            line = re.sub(r'(.*)=([^\s]+.*)?', r"\1= \2", line)
                            fixedErrors += 1



                if "    " in line:
                    line = re.sub(r'    ', r"\t", line)
                    fixedErrors += 1
            newContent +=line
    file.close()

    if fixedErrors != 0:
        with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(newContent)
        file.close()

    return fixedErrors


def main():
    print("Validating Basic Style - Secondary Check")

    files_list = []
    bad_count = 0

    scriptDir = os.path.realpath(__file__)
    rootDir = os.path.dirname(os.path.dirname(scriptDir))

    for root, dirnames, filenames in os.walk(rootDir + '/'+ 'common' + '/'):
        for filename in fnmatch.filter(filenames, '*.txt'):
            files_list.append(os.path.join(root, filename))

    for root, dirnames, filenames in os.walk(rootDir + '/'+ 'events' + '/'):
        for filename in fnmatch.filter(filenames, '*.txt'):
            files_list.append(os.path.join(root, filename))

    for root, dirnames, filenames in os.walk(rootDir + '/'+ 'history' + '/'):
        for filename in fnmatch.filter(filenames, '*.txt'):
            files_list.append(os.path.join(root, filename))

    for filename in files_list:
        bad_count = bad_count + check_basic_style(filename)

    print("Fixed " + str(bad_count) + " styling mistakes")
    print ('The script took {0} second!'.format(time.time() - startTime))


if __name__ == "__main__":
    sys.exit(main())
