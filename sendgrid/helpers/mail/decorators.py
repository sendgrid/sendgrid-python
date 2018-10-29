"""Contains decorators used in helper."""

import inspect
import wrapt


def accepts(*types, **kwtypes):
    """Decorator for verifying the type of method arguments."""
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        args_names = inspect.getargspec(wrapped)[0]
        if instance is not None:
            args_names = args_names[1:]

        for (arg_val, expected_type, arg_name) in zip(args, types, args_names):
            if not isinstance(arg_val, expected_type):
                raise TypeError(
                    "Argument '{}' should be of type {}, got: {}"
                    .format(arg_name, expected_type, type(arg_val))
                    )

        for kwarg in kwargs:
            if kwarg in kwtypes:
                arg_name = kwtypes[kwarg]
                actual_value = kwargs[kwarg]
                if not isinstance(actual_value, arg_name):
                    raise TypeError(
                        "Argument '{}' should be of type {}, got: {}"
                        .format(kwarg, arg_name, type(actual_value))
                        )

        return wrapped(*args, **kwargs)
    return wrapper
