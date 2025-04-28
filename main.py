import os
import sys

dir_in, dir_out, mx_depth = sys.argv[1], sys.argv[2], sys.argv[3]
mx_depth = int(mx_depth)
all_paths = os.walk(dir_in)
mx_depth -= 1
for i in all_paths:
    r, d, f = i
    path = r.replace(dir_in, '').split('/')
    step = 0
    if len(path) - mx_depth > 0:
        step = len(path) - mx_depth

    loc_path = str()
    for _ in path[step:]:
        loc_path += _
        loc_path += "/"
        if not os.path.isdir(f'{dir_out}/{loc_path}'):
            os.system(f"mkdir {dir_out}/{loc_path}")
    sep_path = "/".join(path)
    print(sep_path)
    step_sep_path = "/".join(path[step:])
    command = f'cp {dir_in}/{sep_path}/# {dir_out}/{step_sep_path}/'
    for j in f:
        os.system(command.replace('#', j))


