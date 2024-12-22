# Blade to Flux converter

## Overview

This project is to help convert Laravel Blade templates using Bulma or Bootstrap to use Tailwind and Flux.  It uses LLM calls to convert the template syntax.

This project processes `.blade.php` template files in a specified directory using a specified AI model. The script utilizes the `pydantic_ai` package for AI model interaction, ensuring that the files are processed efficiently while tracking costs and time spent.

## Features

- Validates that the script is run in a `flux` branch.
- Processes `.blade.php` files with a specified AI model.
- Tracks processing costs and execution time.
- Allows for restarting from a specific file in the event of an interruption.

## Installation

### Prerequisites

Ensure the following tools and libraries are installed on your system:

- Python 3.8+
- Git
- Required Python packages listed in `requirements.txt`

### Steps

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the dependencies using [uv](https://docs.astral.sh/uv/):

   ```bash
   uv sync
   ```

## Usage

Run the script with the following options (**Note**: you must be in a branch with 'flux' in the name):

```bash
uv run main.py --directory <directory_path> [--model <model_name>] [--start-file <file_name>]
```

### Options

- `--directory`, `-d`: **(Required)** Path to the directory containing `.blade.php` files.
- `--model`, `-m`: Model name to be used for processing (default: `gpt-4o-mini`).
- `--start-file`, `-s`: File name to restart processing from (optional).

### Example

```bash
uv run main.py -d /Users/you/code/project/resources/templates
```

## Key Notes

- Ensure that the current Git branch is a `flux` branch before running the script.
- The script reads the system prompt from `system_prompt.txt`. Ensure this file is present and properly configured.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
