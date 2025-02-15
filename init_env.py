from typing import Dict, List, Optional

from django.core.management.utils import get_random_secret_key


def variable_handler(var: Dict) -> str:
    var_prompt: str = var["prompt"]
    var_value: Optional[str] = input(var_prompt) or var.get("default_value")
    allowed_values: Optional[List] = var.get("allowed_values")

    while True:
        if allowed_values and var_value not in allowed_values:
            print(  # noqa
                f"Value must be one of: {', '.join(allowed_values)}. Please try again."
            )
            var_value = input(var_prompt) or var.get("default_value")
        elif not var_value:
            print("Value cannot be empty. Please try again.")  # noqa
            var_value = input(var_prompt) or var.get("default_value")
        else:
            break

    return var_value


def main() -> None:
    env_variables: List[Dict] = [
        {
            "variable": "DEBUG",
            "prompt": "Enter the DEBUG (False/True) [False]: ",
            "default_value": "False",
            "allowed_values": ["True", "False"],
        },
        {"variable": "POSTGRES_DB", "prompt": "Enter the POSTGRES_DB: "},
        {"variable": "POSTGRES_USER", "prompt": "Enter the POSTGRES_USER: "},
        {"variable": "POSTGRES_PASSWORD", "prompt": "Enter the POSTGRES_PASSWORD: "},
        {
            "variable": "POSTGRES_HOST",
            "prompt": "Enter the POSTGRES_HOST (docker container name) [database]: ",
            "default_value": "database",
        },
        {
            "variable": "REDIS_LOCATION",
            "prompt": "Enter the REDIS_LOCATION (docker container name) [redis://redis:6379]: ",
            "default_value": "redis://redis:6379",
        },
        {"variable": "EMAIL_HOST_USER", "prompt": "Enter the EMAIL_HOST_USER: "},
        {
            "variable": "EMAIL_HOST_PASSWORD",
            "prompt": "Enter the EMAIL_HOST_PASSWORD: ",
        },
    ]

    print("Creating .env file...")  # noqa

    try:
        with open(".env", "w") as env_file:
            env_file.write(f"SECRET_KEY={get_random_secret_key()}\n")

            for var in env_variables:
                var_value: str = variable_handler(var)
                env_file.write(f"{var['variable']}={var_value}\n")

    except Exception as e:
        print(f"An error occurred while creating the .env file: {e}!")  # noqa
    except KeyboardInterrupt:
        print("File .env was not created! (^C)")  # noqa
    else:
        print("File .env was created successfully!")  # noqa


if __name__ == "__main__":
    main()
