#!/usr/bin/env python
import sys
import subprocess
import yaml

def get_type(a):
    if isinstance(a, str):
        return 'str'
    elif isinstance(a, bool):
        return 'bool'
    elif isinstance(a, int):
        return 'int'
    elif isinstance(a, float):
        return 'float'
    elif isinstance(a, list):
        return 'list'
    else:
        import pdb; pdb.set_trace()

if __name__=="__main__":
    taskname = sys.argv[1]

    # why does this hang?
    # x = subprocess.run(['casa', '--nologger', '--log2term', '--nologfile', '-c', f'"help({taskname}); quit()"'],
    #                    capture_output=True)

    f = open(taskname + '.txt', 'r')

    # find just the relevant help string in the file
    fulltxt = f.readlines()
    for i, l in enumerate(fulltxt):
        if l.find('Arguments') > 0:
            l0 = i+1
        elif l.find('Returns') > 0:
            lf = i
            break

    # import pdb; pdb.set_trace()

    docs = fulltxt[l0:lf]
    x = {}
    for i, l in enumerate(docs):
        l = l.strip()[1:].strip()
        if len(l):
            # print(i, l)
            idx = l.find(':')
            if idx > -1:  # must be a keyword
                l0 = l[0:idx].strip()
                l1 = l[idx:].strip()[1:].strip()
                if 'Default Value' in l0:
                    try:
                        x[key]['default'] = eval(l1)
                    except:
                        x[key]['default'] = l1
                elif 'Allowed Values' in l0:
                    x[key]['choices'] = []
                else:  # must be a key
                    key = l0
                    x.setdefault(key, {})
                    x[key]['info'] = l1.strip()
            else:
                try:
                    x[key]['choices'].append(l)
                except:
                    print(f'Check on failure at {key}')



    with open(f'{taskname}.yaml', 'w') as out:
        yaml.dump(x, out, default_flow_style=False, sort_keys=False)





