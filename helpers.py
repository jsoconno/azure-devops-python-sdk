import inspect
import re


def to_dict_recursive(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict_recursive(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return to_dict_recursive(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [to_dict_recursive(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, to_dict_recursive(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


def flatten_dict(nested_dict, separator='.', prefix=''):
    return {prefix + separator + k if prefix else k: v
            for kk, vv in nested_dict.items()
            for k, v in flatten_dict(vv, separator, kk).items()
            } if isinstance(nested_dict, dict) else {prefix: nested_dict}


def get_methods(obj, hide_special_methods=True):
    try:
        methods = dir(obj)

        if hide_special_methods:
            methods = [
                method for method in methods if '__' not in method and not method.startswith('_')]
    except:
        None
    return methods


def get_arguments(obj, method):
    try:
        arguments = inspect.signature(getattr(obj, method)).parameters  # .args
        arguments = [str(v) for k, v in arguments.items()]
        # arguments = [arg for arg in arguments if 'self' not in arg]
    except:
        arguments = None
    return arguments


def create_docs(obj, client_name, output_markup=False):

    methods = get_methods(obj)
    docs = {}

    for method in methods:
        arguments = get_arguments(obj, method)
        parameters = {}
        imports = []

        try:
            content = getattr(obj, method).__doc__

            if content != None and "str(object='') -> str" not in content:
                lines = content.splitlines()

                content = [line.strip() for line in lines]
                title = content[0].replace('.', '')
                description = content[1]

                for line in content:

                    if ':param :class:' in line:
                        # parameters.append(line.replace(':param', '').strip())

                        # Create parameters dictionary
                        # :param :class:`<GitQueryCommitsCriteria> <azure.devops.v5_1.git.models.GitQueryCommitsCriteria>` search_criteria: Search options
                        search = re.search(
                            ':param :class:`(.*)` (.*): ?(.*)', line)

                        parameters[search.group(2)] = {
                            'type': 'class',
                            'description': search.group(3)
                        }

                        # Create import statement
                        search = re.search('<(.*)> <(.*)>', line)
                        model_name = search.group(1)
                        import_line = search.group(
                            2).replace(f'.{model_name}', '')
                        full_import_statement = f'from {import_line} import {model_name}'
                        imports.append(full_import_statement)

                    elif ':param' in line:
                        search = re.search(
                            ':param (\[?\{?\w*\}?\]?) (\w*): ?(.*)', line)

                        parameters[search.group(2)] = {
                            'type': search.group(1),
                            'description': search.group(3)
                        }

                    elif ':rtype:' in line:
                        return_type = line.replace(
                            ':rtype:', '').replace('`', '').strip()

                    else:
                        pass

                example_usage = f'connection.clients.{client_name}().{method}({", ".join(arguments)})'

                content = {
                    'description': description,
                    'parameters': parameters,
                    'return_type': return_type,
                    'imports': imports,
                    'example_usage': example_usage
                }

                docs[title] = content

        except Exception as e:
            print(e)
            print(line)

    if output_markup:
        markup = ''
        markup += f'## {client_name.replace("_", " ").title()}\n\n'

        for method, attributes in docs.items():
            markup += f'### {method}\n'
            markup += f'#### Description:\n'
            markup += f'{attributes["description"]}\n'
            markup += f'#### Parameters:\n'
            markup += f'| Name | Type | Description |\n'
            markup += f'| --- | --- | --- |\n'
            for parameter, details in attributes['parameters'].items():
                markup += f'| {parameter} | {details["type"]} | {details["description"]} |\n'
            markup += f'#### Return Type\n'
            markup += f'{attributes["return_type"]}\n'
            markup += f'#### Example Usage\n'
            markup += f'```\n'
            for i in attributes['imports']:
                markup += f'{i}\n'
            markup += f'\n'
            markup += f'{attributes["example_usage"]}\n'
            markup += f'```\n'

        docs = markup

    return docs
