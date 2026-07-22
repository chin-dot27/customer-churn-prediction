import json, os, sys, textwrap
from pathlib import Path
nb_path = os.path.join('Scripts', 'Customer churn prediction.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

globals_dict = {'__name__': '__main__', '__file__': nb_path}
print('Notebook loaded:', nb_path)
print('Current dir:', Path('.').resolve())
cell_num = 0
for cell in nb.get('cells', []):
    cell_num += 1
    if cell.get('cell_type') != 'code':
        continue
    source = textwrap.dedent(''.join(cell.get('source', [])))
    if not source.strip():
        continue
    print('\n--- Executing cell', cell_num, '---\n')
    try:
        exec(source, globals_dict)
    except ModuleNotFoundError as e:
        print('CELL', cell_num, 'SKIPPED (missing module):', repr(e))
        continue
    except Exception as e:
        print('CELL', cell_num, 'FAILED:', repr(e))
        raise

print('\nNotebook execution completed successfully.')
