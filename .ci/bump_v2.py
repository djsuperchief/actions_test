# Version 2 of the bump.
# This does not need to push to source....
import sys
import json
import os

path = os.path.dirname(os.path.realpath(__file__))

def open_ci():
    with open(f'{path}/ci_2.json') as json_data:
        ci_file = json.load(json_data)
        json_data.close()
        return ci_file
    
def bump_major(ci_file, version):
    if ci_file["version_config"]["major"] > int(version[0]):
        version[0] = int(version[0]) + 1
        print(f'{version[0]}.0.0')
    else:
        sys.stderr.write('ERROR: Major version must be more than the current repository semver.')
        sys.stdout.flush()
        exit(1)

def bump_minor(version):
    version[1] = int(version[1]) + 1
    print(f'{version[0]}.{version[1]}.0')

def bump_revision(version):
    version[2] = int(version[2]) + 1
    print(f'{version[0]}.{version[1]}.{version[2]}')

def main():
    version = sys.stdin.read().rstrip().split('.')
    ci_file = open_ci()

    match ci_file["version_config"]["bump"]:
        case 'major':
            bump_major(ci_file, version)
        case 'minor':
            bump_minor(version)
        case 'rev':
            bump_revision(version)
        case _:
            bump_revision(version)
    


if __name__ == '__main__':
    main()
