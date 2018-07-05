import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Parser(object):

    def parse(filename):
        with open(filename) as f:
            params = {}
            constraints = []
            params_section = True
            last_key = None
            for line in f:
                if line == '\n' or line == '':
                    continue

                if line == '=constraints\n':
                    params_section = False
                    continue

                if params_section:
                    line = line.strip()
                    if line[0] == '=':
                        last_key = line[1:]
                        params[last_key] = []
                    else:
                        params[last_key].append(line)
                else:
                    matches = re.findall(r'(.+)[(](.+)[)] (!?=|>|<) (.+)[(](.+)[)]', line)
                    left_param, left_type, relation, right_param, right_type = matches[0]
                    constraints.append({
                        'left_param'  : left_param,
                        'left_type'   : left_type,
                        'relation'    : relation,
                        'right_param' : right_param,
                        'right_type'  : right_type
                    })

            print("\nparams:\n")
            pp.pprint(params)
            print("\nconstraints:\n")
            pp.pprint(constraints)
